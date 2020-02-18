"""
HW04a
Author: Xinyi Ye
Date: 02/18/2020
"""
import urllib.request
import json


def find_re(s):
    """ find_re() function: input GitHub id, and get repository and commits number. """
    url_r = f"https://api.github.com/users/{s}/repos"
    l_data = []
    try:
        fp_r = urllib.request.urlopen(url_r)
    except ValueError:
        return(f"can't open {url_r}")
    else:
        data_r = json.load(fp_r)
        for r in data_r:
            l = []
            url_c = f"https://api.github.com/repos/{s}/{r['name']}/commits"
            try:
                fp_c = urllib.request.urlopen(url_c)
            except ValueError:
                return(f"can't open {url_c}")
            else:
                data_c = json.load(fp_c)
                l = [r['name'], len(data_c)]
                l_data. append(l)
        return l_data


if __name__ == "__main__":
    """ main() function:require input, and print output """
    try:
        id = input('please input GitHub ID:')
    except ValueError as e:
        print(e)
    else:
        for item in find_re(id):
            print(f"Repo: {item[0]}, Number of commits: {item[1]}")
