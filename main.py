#!/usr/bin/python3
# coding: utf-8

import os
import configparser

config_dir = os.path.dirname(os.path.realpath(__file__))
title = ""
path = ""


def main():
    config = configparser.ConfigParser()
    config_file = config_dir + "/conf/committer.conf"
    config.read(config_file, "utf-8")
    sections = config.sections()

    for section in sections:
        title = config.get(section, 'title')
        path = config.get(section, 'path')
        remote = config.get(section, 'remote')
        branch = config.get(section, 'branch')
        os.chdir(path)
        os.system("git pull {0} {1}".format(remote, branch))
        os.system("git add .")
        os.system("git commit -m '{0}'".format(title))
        os.system("git push {0} {1}".format(remote, branch))
    else:
        if len(sections) == 0:
            print("Não há seções configuradas!")
        else:
            print("Fim da sincronização!")


if __name__ == "__main__":
    main()
