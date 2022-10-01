import sqlite3
import pandas as pd

dbname = 'databases.db'
connection = sqlite3.connect(dbname)

# connection.close()
cur = connection.cursor()
theater_name = "TOHO CINEMAS HIBIYA"
sql = 'select * from theater1 where Screen_name=?'
cur.execute(sql, (theater_name,))
df = pd.DataFrame(cur.fetchall())

# df = pd.read_sql_query(
#     'select * from theater1 where Screen_name=theater_name,', connection)
# connection.close()
