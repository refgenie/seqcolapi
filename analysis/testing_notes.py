# main()

# Some testing/developing notes:
# Run like: export POSTGRES_PASSWORD=`pass aws/rds_postgres`; python3 main.py

# import importlib
# importlib.reload(scconf)

# mydict = SqliteDict('/home/nsheff/code/refget/docs_jupyter/my_db.sqlite', autocommit=True)
# rgc = refget.RefGetClient("https://refget.herokuapp.com/sequence/", mydict)
# 2262e7f00a684c9f061eb33a3cdd32e13ff67642e69c8c96

# print(pgdb)
# pgdb.table
# pgdb["test"]
# pgdb["test"] = "123"
# pgdb["test2"] = "234"
# pgdb["test2"]


# pgdb.init_table()
# pgdb.connection

# pgdb.close()

# x = pgdb.execute_read_query("SELECT value FROM seqcol WHERE key='test' LIMIT 1")

# cursor = pgdb.connection.cursor()
# cursor.execute("SELECT value FROM seqcol WHERE key='test' LIMIT 1")
# cursor.fetchone()[0]


# sc.insert("GATTACA", "sequence")
# import seqcol
# sc = seqcol.SeqColClient(database=pgdb, schemas=["/home/nsheff/code/seqcol/seqcol/schemas/RawSeqCol.yaml"])

# fa_file = "/home/nsheff/code/seqcol/demo_fasta/demo.fa.gz"
# content = sc.load_fasta2(fa_file)
# content
