import json
import subprocess
import re

import final_link_resolver

# cmd = '''snscrape --jsonl --since 2022-01-01 telegram-channel wylsared > wylsared.txt'''
# args_list = cmd.split(" ")
# process = subprocess.run(args_list, shell=True)

utm_pattern = r'https:\/\/\S+\.\S+\/\?utm_source=\S+'

data = open('wylsared.txt')


def get_all_links():
    links_list = []

    data_lines = data.readlines()
    for line in data_lines:
        json_map = json.loads(line)
        links = json_map["outlinks"]
        if links and json_map["content"] is not None:
            for link in links:
                links_list.append(link)

    return links_list


def get_all_domains(links_list):
    domains_list = []
    for link in links_list:
        domains_list.append(final_link_resolver.get_domain_of_ref(link))
    return domains_list


def get_post_link(line):
    json_map = json.loads(line)
    post_link = json_map["url"]
    return post_link


def get_post_date(line):
    json_map = json.loads(line)
    date = json_map["date"]
    return date


def get_post_text(line):
    json_map = json.loads(line)
    content = json_map["content"]
    return content


def get_all_post_links(line):
    links_list = []
    json_map = json.loads(line)
    links = json_map["outlinks"]
    for link in links:
        links_list.append(link)
    return links_list


def get_post_ref_links(line):
    links_list = []

    json_map = json.loads(line)
    links = json_map["outlinks"]
    if links and json_map["content"] is not None:
        for link in links:
            links_list.append(link)

    ref_links = []

    for link in links_list:
        matches = re.findall(utm_pattern, link)
        if len(matches) != 0:
            ref_links.append(matches)
    return ref_links
