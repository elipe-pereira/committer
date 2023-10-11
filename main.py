#!/usr/bin/python3
# coding: utf-8

from os import chdir
from os import system
from os.path import dirname
from os.path import realpath
from configparser import ConfigParser


class Main:
    def __init__(self):
        self.config_dir = dirname(realpath(__file__))
        self.title = ""
        self.path = ""
        self.remote = ""
        self.branch = ""

    def run(self):
        config = ConfigParser()
        config_file = self.config_dir + "/conf/committer.conf"
        config.read(config_file, "utf-8")
        sections = config.sections()

        for section in sections:
            self.title = config.get(section, 'title')
            self.path = config.get(section, 'path')
            self.remote = config.get(section, 'remote')
            self.branch = config.get(section, 'branch')
            chdir(self.path)
            system("git pull {0} {1}".format(self.remote, self.branch))
            system("git add .")
            system("git commit -m '{0}'".format(self.title))
            system("git push {0} {1}".format(self.remote, self.branch))
        else:
            if len(sections) == 0:
                print("Não há seções configuradas!")
            else:
                print("Fim da sincronização!")


if __name__ == "__main__":
    app = Main()
    app.run()
