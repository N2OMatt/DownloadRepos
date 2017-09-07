#!/usr/bin/python
##----------------------------------------------------------------------------##
## File      : github_repo_fetcher.py                                         ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : September 05, 2017 (Happy Birthday Daddy)                      ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - Copyright (c) 2017                                   ##
##                                                                            ##
## Description:                                                               ##
##   Download and save the list of repositories from GitHub in                ##
##   the format that download_repos.py expects.                               ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
## Python
import json;
import os.path;
import os;
import sys;
import urllib;
## Project
import helpers;


################################################################################
## Constants                                                                  ##
################################################################################
BASE_URL = "https://api.github.com/users/{ORGANIZATION_NAME}/repos"


################################################################################
## Helper Functions                                                           ##
################################################################################
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

def save_repos_list(repos, filename):
    out_file = open(filename, "w");
    for info in repos:
        line = "{0} , {1}\n".format(info["name"], info["url"]);
        out_file.write(line);
    out_file.close();


################################################################################
## Script                                                                     ##
################################################################################
def main():
    ## Get options...
    options = helpers.getoptions_init(["org=", "output="]);

    ## Init...
    org_name = helpers.getoptions_getarg(options, "org");
    output   = helpers.getoptions_getarg(options, "output");

    ## Check...
    org_name = helpers.check_and_clean("org",    org_name);
    output   = helpers.check_and_clean("output", output  );

    ## Fetch the repos and save to list.
    repos = fetch_list_repos(org_name);
    save_repos_list(repos, output);

if __name__ == '__main__':
    try:
        main();
    except Exception as e:
        import pdb;
        pdb.set_trace();
        raise e
