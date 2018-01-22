#!/usr/bin/env python
##----------------------------------------------------------------------------##
## File      : download_repos.py                                              ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : Jul 22, 2017                                                   ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - 2017, 2018                                           ##
##                                                                            ##
## Description:                                                               ##
##   Given a list of repositories in a file download all the repos            ##
##   into a correct directories in the filesystem.                            ##
##                                                                            ##
##   The list is expected to be:                                              ##
##     Name_Of_The_Foler : https://url_of_repo.git                            ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
## Python
import os.path;
import os;
import pdb;
## Project
import helpers;


################################################################################
## Helper Functions                                                           ##
################################################################################
## Helper functions ##
def make_dir(base_path):
    fullname = os.path.abspath(
        os.path.expanduser(
            base_path
        )
    );

    if(os.path.isdir(fullname) == False):
        print "Creating directory: ({0})".format(fullname);
        os.system("mkdir -p {0}".format(fullname));

    return fullname;

def parse_repos_list(filename):
    lines     = open(os.path.abspath(filename)).readlines();
    info_list = [];

    for line in lines:
        name, url = line.split(",");
        info = {
            "name" : name.strip().replace("\n",""),
            "url"  : url.strip ().replace("\n","")
        };
        info_list.append(info);

    return info_list;

def clone_repos(repos_list, repos_dir):
    for repo in repos_list:
        repo_name     = repo["name"];
        repo_url      = repo["url" ];
        repo_full_dir = os.path.join(repos_dir, repo_name);

        print "Clonning repo ({0}) in ({1})".format(repo_name, repos_dir);
        if(os.path.isdir(repo_full_dir)):
            print "Repo already cloned...";
            continue;

        ## Create the Respository directory.
        os.makedirs(repo_full_dir);

        ## Go to it to perform the git commands.
        old_cwd = os.getcwd();
        os.chdir(repo_full_dir);

        ## Git commands...        
        cmd_clone    = "git clone {0} .".format(repo_url);
        cmd_sub_init = "git submodule update --init --recursive";

        full_cmd = "{CMD_CLONE} && {CMD_SUB_INIT}".format(            
            CMD_CLONE   = cmd_clone,
            CMD_SUB_INIT= cmd_sub_init
        );

        os.system(full_cmd);

        ## Restore the cwd...
        os.chdir(old_cwd);

################################################################################
## Script                                                                     ##
################################################################################
def main():
    ## Get options...
    options = helpers.getoptions_init([
        "org=",
        "base-path=",
        "repos-list=",
    ]);

    ## Init...
    org_name   = helpers.getoptions_getarg(options, "org"       );
    base_path  = helpers.getoptions_getarg(options, "base-path" );
    repos_list = helpers.getoptions_getarg(options, "repos-list");

    ## Check...
    org_name   = helpers.check_and_clean("org",        org_name  );
    base_path  = helpers.check_and_clean("base-path",  base_path );
    repos_list = helpers.check_and_clean("repos-list", repos_list);

    ## Create the base directory, parse the repos list
    ## and start clonning the repositories.
    repos_dir  = make_dir(base_path);
    repos_info = parse_repos_list(repos_list);
    clone_repos(repos_info, repos_dir);


if __name__ == '__main__':
    try:
        main();
    except Exception as e:
        pdb.set_trace();
        raise e

