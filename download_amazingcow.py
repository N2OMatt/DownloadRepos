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
    "AmazingCow",
];



## Helper functions ##
def make_dir(name):
    fullname = os.path.join(BASE_PATH, name);
    if(os.path.isdir(fullname) == False):
        print "Creating directory: ({})".format(fullname);
        os.system("mkdir -p {}".format(fullname));

    return fullname;

def fetch_list_repos(organization_name):
    url      = BASE_URL.format(ORGANIZATION_NAME=organization_name);
    response = urllib.urlopen(url);
    data     = json.loads(response.read());


    print "Fetching repos for: ({})".format(organization_name);
    repos = [];
    for info in data:
        repos.append(
            { "url"  : info["clone_url"],
              "name" : info["name"]
            });

    return repos;

def clone_repos(repos_info, repos_dir):
    for repo_info in repos_info:
        print "Clonning repo ({}) in ({})".format(repo_info["name"], repos_dir);

        repo_full_dir = os.path.join(repos_dir, repo_info["name"]);

        if(os.path.isdir(repo_full_dir)):
            print "Repo already cloned...";
            return;

        os.system("git clone {} {}".format(repo_info["url"], repo_full_dir));


for organization_name in ORGANIZATION_NAMES:
    repos_dir  = make_dir(organization_name);
    repos_info = fetch_list_repos(organization_name);
    clone_repos(repos_info, repos_dir);

    print "----"

#

    # print a["clone_url"];
# print response.read();
# # Download the repos...
# for repo_name in sorted(REPOS.keys()):
#     #Build the GIT url and the location of the repo.
#     full_git_url   = os.path.join(GIT_URL, repo_name + ".git");
#     full_repo_path = os.path.expanduser(os.path.join(REPOS[repo_name], repo_name));

#     #Already have this repo in this computer
#     if(os.path.isdir(full_repo_path)):
#         print "[{}] is already downloaded....".format(termcolor.colored(repo_name, "blue"));
#         continue;

#     os.system("mkdir -p {}".format(full_repo_path));
#     os.system("git clone {} {}".format(full_git_url, full_repo_path));
