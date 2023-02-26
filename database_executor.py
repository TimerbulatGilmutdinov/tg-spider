import psycopg2
import tg_posts_parser as parser

con = psycopg2.connect(
    database="data_mining",
    user="postgres",
    password="qwerty007",
    host="localhost",
)

cur = con.cursor()

data = open('wylsared.txt')

links_list = []

data_lines = data.readlines()
for line in data_lines:
    content = parser.get_post_text(line)
    post_date = parser.get_post_date(line)
    link = parser.get_post_link(line)
    ref_links = parser.get_post_ref_links(line)
    post_links = parser.get_all_post_links(line)
    host_owner = ""

    for post_link in post_links:
        host_owner = parser.get_host_owner(post_link)
    print('starting insert')
    cur.execute('''
    INSERT INTO tg_posts (content, post_date, link, ref_links, whois_info) values (%s, %s, %s, %s, %s)
    ''', (content, post_date, link, ref_links, host_owner))
    print('inserted')

con.commit()
con.close()
