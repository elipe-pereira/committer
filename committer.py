#!/usr/bin/python3
# Committer - Faz o commit das pastas configuradas

import os
import sys
import configparser

config_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
title = ""
path = ""

def main():
    config = configparser.ConfigParser()
    config_file = config_dir + "/etc/committer/committer.conf"
    config.read(config_dir + "/etc/committer/committer.conf")
    sections = config.sections()

    if len(section) == 0:
        print("Não Há seções configuradas")
        sys.exit()
    else:
        for section in sections:
            title = config.get(section, 'title')
            path = config.get(section, 'path')
            branch = config.get(section, 'branch')
            os.chdir(path)
            os.system("git pull")
            os.system("git add .")
            os.system("git commit -m '{0}'".format(title))
            os.system("git push origin {0}".format(branch))
        
main()
