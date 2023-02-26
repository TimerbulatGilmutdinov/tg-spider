import tg_posts_parser as parser

data = open('wylsared.txt')

links_list = []

data_lines = data.readlines()
for line in data_lines:
    print(parser.get_post_link(line))
    post_links = parser.get_all_post_links(line)
    for post_link in post_links:
        print(parser.get_host_owner(post_link))







