#!/usr/bin/python
import os;
import os.path;
import termcolor;

## Paths.
GIT_URL      = "git@github.com:N2OMatt/";
N2OMATT_PATH = "~/Documents/Projects/N2OMatt/";

# Repositiory - Directory Information.
REPOS = {
    "dots"               : N2OMATT_PATH,
    "DownloadRepos"      : N2OMATT_PATH,
    "lights-out"         : N2OMATT_PATH,
    "LinuxTidyAndClean"  : N2OMATT_PATH,
    "MyCerts"            : N2OMATT_PATH,
    "n2omatt.github.com" : N2OMATT_PATH,
    "ProjectEuler"       : N2OMATT_PATH,
};

# Download the repos...
for repo_name in sorted(REPOS.keys()):
    #Build the GIT url and the location of the repo.
    full_git_url   = os.path.join(GIT_URL, repo_name + ".git");
    full_repo_path = os.path.expanduser(os.path.join(REPOS[repo_name], repo_name));


    #Already have this repo in this computer.s
    if(os.path.isdir(full_repo_path)):
        print "[{}] is already downloaded....".format(termcolor.colored(repo_name, "blue"));
        continue;

    os.system("mkdir -p {}".format(full_repo_path));
    os.system("git clone {} {}".format(full_git_url, full_repo_path));
