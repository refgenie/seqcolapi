
# main()

# Some testing/developing notes:
# Run like: export POSTGRES_PASSWORD=`pass aws/rds_postgres`; python3 main.py

# import importlib
# importlib.reload(scconf)

# mydict = SqliteDict('/home/nsheff/code/refget/docs_jupyter/my_db.sqlite', autocommit=True)
# rgc = refget.RefGetClient("https://refget.herokuapp.com/sequence/", mydict)
#2262e7f00a684c9f061eb33a3cdd32e13ff67642e69c8c96

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




["25ccf153f9ac4876a631270b6bb23328f8e5fed08087a9f5","7ea134e2ee93733d2a0aa66150d9b4540ad7fafe5782715b","9cb12355bb8bf4acabfb401392c47e3b55a71802c5a79c98"]


Some examples:
http://localhost:8000/seqcol/2262e7f00a684c9f061eb33a3cdd32e13ff67642e69c8c96/0
http://localhost:8000/seqcol/2262e7f00a684c9f061eb33a3cdd32e13ff67642e69c8c96/1
http://localhost:8000/seqcol/2262e7f00a684c9f061eb33a3cdd32e13ff67642e69c8c96

http://localhost:8000/seqcol/53b74be8b295b733fdfafbd7d2a22b1686733740de7fdc59

http://localhost:8000/seqcol/7ea134e2ee93733d2a0aa66150d9b4540ad7fafe5782715b

http://localhost:8000/seqcol/0e6a942e25005983bf54622997ec90cbf34b1c7dce597636
http://localhost:8000/seqcol/61966c86d7c3bb28fff946c52eefff0b


http://localhost:8000/refget/6681ac2f62509cfc220d78751b8dc524

https://www.ebi.ac.uk/ena/cram/sequence/112a8b1df94ef0498a0bfe2d2ea5cc23




http://localhost:8000/refget/112a8b1df94ef0498a0bfe2d2ea5cc23
