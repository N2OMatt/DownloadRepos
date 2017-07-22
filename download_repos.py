#!/usr/bin/python
##----------------------------------------------------------------------------##
## File      : download_repos.py                                              ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : Jul 22, 2017                                                   ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - Copyright (c) 2017                                   ##
##                                                                            ##
## Description:                                                               ##
##                                                                            ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
import os;
import os.path;
import urllib;
import json;
import sys;

#Sometimes I don't have termcolor.
try:
    from termcolor import colored;
except ImportError, e:
    def colored(msg, color):
        return msg;


## Paths.
BASE_URL  = "https://api.github.com/users/{ORGANIZATION_NAME}/repos"
BASE_PATH = os.path.expanduser("~/Documents/Projects/AmazingCow");


ORGANIZATION_NAMES = [
    "AmazingCow-Game-Core",
    "AmazingCow-Game-Framework",
    "AmazingCow-Game-Tool",
    "AmazingCow-Game",
    "AmazingCow-Libs",
    "AmazingCow-Tools",
    "AmazingCow-Imidiar",
    "AmazingCow",
];


################################################################################
## Helper Functions                                                           ##
################################################################################
## Helper functions ##
def make_dir(name, base_path):
    fullname = os.path.join(base_path, name);
    if(os.path.isdir(fullname) == False):
        print "Creating directory: ({0})".format(fullname);
        os.system("mkdir -p {0}".format(fullname));

    return fullname;

def fetch_list_repos(organization_name):
    url      = BASE_URL.format(ORGANIZATION_NAME=organization_name);
    response = urllib.urlopen(url);
    data     = json.loads(response.read());


    print "Fetching repos for: ({0})".format(organization_name);
    repos = [];
    for info in data:
        repos.append({
          "url"  : info["clone_url"],
          "name" : info["name"]
        });

    return repos;

def clone_repos(repos_info, repos_dir):
    for repo_info in repos_info:
        print "Clonning repo ({0}) in ({1})".format(repo_info["name"], repos_dir);

        repo_full_dir = os.path.join(repos_dir, repo_info["name"]);

        if(os.path.isdir(repo_full_dir)):
            print "Repo already cloned...";
            continue;

        ## Commands...
        mkdir    = "mkdir -p {0}".format(repo_full_dir);
        cd       = "cd {0}".format(repo_full_dir);
        clone    = "git clone {0} .".format(repo_info["url"]);
        sub_init = "git submodule update --init --recursive";

        full_cmd = "{0} && {1} && {2} && {3}".format(
            mkdir,
            cd,
            clone,
            sub_init
        );
        os.system(full_cmd);


################################################################################
## Script                                                                     ##
################################################################################
def main():
    org_name  = sys.argv[1];
    base_path = sys.argv[2];

    repos_dir  = make_dir(org_name, base_path);
    repos_info = fetch_list_repos(org_name);
    clone_repos(repos_info, repos_dir);


if __name__ == '__main__':
    main();
