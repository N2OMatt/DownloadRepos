#!/usr/bin/python
import os;
import os.path;

GIT_URL      = "https://github.com/n2omatt/";
N2OMATT_PATH = "~/Documents/Projects/N2OMatt/";

REPOS = { 
    "DownloadRepos"     : N2OMATT_PATH,
    "LinuxTidyAndClean" : N2OMATT_PATH,
    "dots"              : N2OMATT_PATH,
    "lights-out"        : N2OMATT_PATH,
    "ProjectEuler"      : N2OMATT_PATH,
    "Study"             : N2OMATT_PATH
};


for repo_name in sorted(REPOS.keys()):
    full_git_url   = os.path.join(GIT_URL, repo_name + ".git");
    full_repo_path = os.path.expanduser(os.path.join(REPOS[repo_name], repo_name));

    if(os.path.isdir(full_repo_path)):
        print "{} is already downloaded....".format(repo_name);
        continue;

    os.system("mkdir -p {}".format(full_repo_path));
    os.system("git clone {} {}".format(full_git_url, full_repo_path));