import tg_posts_parser as parser
import csv

with open("tg_ref_posts.csv", mode="w", encoding='utf-8') as w_file:
    names = ["id", "content", "post_date", "link", "ref_links", "whois_info"]
    file_writer = csv.DictWriter(w_file, delimiter=";",
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    data = open('wylsared.txt')

    data_lines = data.readlines()
    id = 0
    for line in data_lines:
        id += 1
        content = parser.get_post_text(line)
        post_date = parser.get_post_date(line)
        link = parser.get_post_link(line)
        ref_links = parser.get_post_ref_links(line)
        post_links = parser.get_all_post_links(line)
        host_owner = ""
        for post_link in post_links:
            host_owner = parser.get_host_owner(post_link)
        if len(ref_links) != 0:
            file_writer.writerow({"id": id, "content": content, "post_date": post_date, "link": link, "ref_links": ref_links, "whois_info": host_owner})
