import tg_posts_parser as parser

data = open('wylsared.txt')

data_lines = data.readlines()
for line in data_lines:
    if len(parser.get_post_ref_links(line)) != 0:
        print(parser.get_post_ref_links(line))








