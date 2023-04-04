import psycopg2

conn = psycopg2.connect(host="172.24.0.2", port = 5432, database="", user="postgres", password="secret")

cur = conn.cursor()

query = """
SELECT datname FROM pg_database
WHERE datistemplate = false;
"""
cur.execute(query)

db_version = cur.fetchone()
cur.close()

print(db_version)