import psycopg2

con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="qwerty007",
    host="127.0.0.1",
    port="5432"
)

cur = con.cursor()

cur.execute('''
INSERT INTO tg_posts (text, date, link, ref_links, whois_info) values ()
''')

con.commit()
con.close()
