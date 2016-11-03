#!/usr/bin/python

## Imports ##
import os;
import os.path;
import urllib;
import json;

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
    "AmazingCow-One-Game-Per-Week",
    "AmazingCow",
];



## Helper functions ##
def make_dir(name):
    fullname = os.path.join(BASE_PATH, name);
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
        repos.append(
            { "url"  : info["clone_url"],
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

        os.system("git clone {0} {1}".format(repo_info["url"], repo_full_dir));


for organization_name in ORGANIZATION_NAMES:
     repos_dir  = make_dir(organization_name);
     repos_info = fetch_list_repos(organization_name);
     clone_repos(repos_info, repos_dir);

     print "----"

