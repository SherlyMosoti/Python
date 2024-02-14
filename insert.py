import sqlite3
conn = sqlite3.connect("test.db")


conn.execute("INSERT INTO EMPLOYEES  VALUES (31,'TERRY NYAKIO',26,480000.00);")
conn.execute("INSERT INTO EMPLOYEES  VALUES (32,'PURITY LIMO',28,580000.00);")
conn.execute("INSERT INTO EMPLOYEES  VALUES (33,'GLORIA CHEBET',32,680000.00);")
conn.execute("INSERT INTO EMPLOYEES  VALUES (34,'ALICIA GRACA',35,570000.00);")
conn.execute("INSERT INTO EMPLOYEES  VALUES (35,'BONIFACE MOBEGI',38,780000.00);")


conn.commit()
print("Records inserted successfully")
conn.close()