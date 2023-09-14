import psycopg2
import yacman

from collections.abc import Mapping
from psycopg2 import OperationalError, sql
from psycopg2.errors import UniqueViolation


class SeqColConf(yacman.YAMLConfigManager):
    def __init__(
        self,
        entries={},
        filepath=None,
        yamldata=None,
        writable=False,
        wait_max=60,
        skip_read_lock=False,
    ):
        super(SeqColConf, self).__init__(entries, filepath, yamldata, writable)


# Use like:
# pgdb = RDBDict(...)       # Open connection
# pgdb["key"] = "value"     # Insert item
# pgdb["key"]               # Retrieve item
# pgdb.close()              # Close connection


class RDBDict(Mapping):
    """
    A Relational DataBase Dict.

    Simple database connection manager object that allows us to use a
    PostgresQL database as a simple key-value store to back Python
    dict-style access to database items.
    """

    def __init__(self, db_name, db_user, db_password, db_host, db_port, db_table):
        self.db_table = db_table
        self.db_name = db_name
        self.db_user = db_user
        self.db_host = db_host
        self.db_port = db_port
        self.connection = self.create_connection(
            db_name, db_user, db_password, db_host, db_port
        )
        self.connection.autocommit = True

    def __repr__(self):
        return (
            "RDBD object\n"
            + "db_table: {}\n".format(self.db_table)
            + "db_name: {}\n".format(self.db_name)
            + "db_user: {}\n".format(self.db_user)
            + "db_host: {}\n".format(self.db_host)
            + "db_port: {}\n".format(self.db_port)
        )

    def init_table(self):
        # Wrap statements to prevent SQL injection attacks
        stmt = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS {table}(
            key TEXT PRIMARY KEY, 
            value TEXT);
        """
        ).format(table=sql.Identifier(self.db_table))
        return self.execute_query(stmt, params=None)

    def insert(self, key, value):
        stmt = sql.SQL(
            """
            INSERT INTO {table}(key, value)
            VALUES (%(key)s, %(value)s);
        """
        ).format(table=sql.Identifier(self.db_table))
        params = {"key": key, "value": value}
        return self.execute_query(stmt, params)

    def update(self, key, value):
        stmt = sql.SQL(
            """
            UPDATE {table} SET value=%(value)s WHERE key=%(key)s
        """
        ).format(table=sql.Identifier(self.db_table))
        params = {"key": key, "value": value}
        return self.execute_query(stmt, params)

    def __getitem__(self, key):
        # This little hack makes this work with `in`;
        # e.g.: for x in rdbdict, which is now disabled, instead of infinite.
        if isinstance(key, int):
            raise IndexError
        stmt = sql.SQL(
            """
            SELECT value FROM {table} WHERE key=%(key)s
        """
        ).format(table=sql.Identifier(self.db_table))
        params = {"key": key}
        res = self.execute_read_query(stmt, params)
        if not res:
            print("Not found: {}".format(key))
        return res

    def __setitem__(self, key, value):
        try:
            return self.insert(key, value)
        except UniqueViolation as e:
            print("Updating existing value for {}".format(key))
            return self.update(key, value)

    def __delitem__(self, key):
        stmt = sql.SQL(
            """
            DELETE FROM {table} WHERE key=%(key)s
        """
        ).format(table=sql.Identifier(self.db_table))
        params = {"key": key}
        res = self.execute_query(stmt, params)
        return res

    def create_connection(self, db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print("Error: {e}".format(e=str(e)))
        return connection

    def execute_read_query(self, query, params=None):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                print("Not found for key: {}".format(query))
                print("Result: {}".format(str(result)))
                print("Query: {}".format(str(query)))
                return None
        except OperationalError as e:
            print("Error: {e}".format(e=str(e)))
            raise Exception
            return None
        except TypeError as e:
            print("TypeError: {e}, item: {q}".format(e=str(e), q=query))
            raise Exception
            return None

    def execute_multi_query(self, query, params=None):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except OperationalError as e:
            print("Error: {e}".format(e=str(e)))
            raise Exception
            return None
        except TypeError as e:
            print("TypeError: {e}, item: {q}".format(e=str(e), q=query))
            raise Exception
            return None

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            return cursor.execute(query, params)
            print("Query executed successfully")
        except OperationalError as e:
            print("Error: {e}".format(e=str(e)))

    def close(self):
        print("Closing connection")
        return self.connection.close()

    def __del__(self):
        self.close()

    def __len__(self):
        stmt = sql.SQL(
            """
            SELECT COUNT(*) FROM {table}
        """
        ).format(table=sql.Identifier(self.db_table))
        res = self.execute_read_query(stmt)
        return res

    def __iter__(self):
        self._current_idx = 0
        return self

    def __next__(self):
        stmt = sql.SQL(
            """
            SELECT key,value FROM {table} LIMIT 1 OFFSET %(idx)s
        """
        ).format(table=sql.Identifier(self.db_table))
        res = self.execute_read_query(stmt, {"idx": self._current_idx})
        self._current_idx += 1
        if not res:
            print("Not found: {}".format(self._current_idx))
            raise StopIteration
        return res


# We don't need the full SeqColClient,
# which also has loading capability, and requires pyfaidx, which requires
# biopython, which requires numpy, which is huge and can't compile the in
# default fastapi container.
# So, I had written the below class which provides retrieve only.
# HOWEVER, switching from alpine to slim allows install of numpy;
# This inflates the container size from 262Mb to 350Mb; perhaps that's worth paying.
# So I can avoid duplicating this and just use the full SeqColClient from seqcol
# class SeqColClient(refget.RefGetClient):
#     def retrieve(self, druid, reclimit=None, raw=False):
#         try:
#             return super(SeqColClient, self).retrieve(druid, reclimit, raw)
#         except henge.NotFoundException as e:
#             _LOGGER.debug(e)
#             try:
#                 return self.refget(druid)
#             except Exception as e:
#                 _LOGGER.debug(e)
#                 raise e
#                 return henge.NotFoundException("{} not found in database, or in refget.".format(druid))
