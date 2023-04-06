import psycopg2

conn = psycopg2.connect(host="172.26.0.2", port = 5432, database="root", user="postgres", password="secret1")

cur = conn.cursor()

query = """
SELECT datname FROM pg_database
WHERE datistemplate = false;
"""
cur.execute(query)

db_version = cur.fetchone()
cur.close()

print(db_version)