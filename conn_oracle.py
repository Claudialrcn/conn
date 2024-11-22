import os

from dotenv import load_dotenv
import oracledb

load_dotenv()

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")

connection = oracledb.connect(user=username, password=password, host=hostname, sid=sid)

cursor = connection.cursor()

query = """
CREATE TABLE recipe (
        id INT PRIMARY KEY,
        Nombre VARCHAR(30)
    )
"""
# cursor.execute(query)

query = """
INSERT INTO recipe (id,Nombre)
VALUES (2, 'Cinamon roll')
"""
cursor.execute(query)


query = """
SELECT * FROM recipe
"""
iterador = cursor.execute(query)
for result in iterador:
    print(result)

connection.commit()

cursor.close()

connection.close()
