#!/usr/bin/python
##----------------------------------------------------------------------------##
## File      : download_amazingcow.py                                         ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : 2015                                                           ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - Copyright (c) 2015, 2017                             ##
##                                                                            ##
## Description:                                                               ##
##                                                                            ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
import os;


################################################################################
## Constants                                                                  ##
################################################################################
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
## Script                                                                     ##
################################################################################
def main():
    for org_name in ORGANIZATION_NAMES:
        cmd = "./download_repos.py {0} {1}".format(
            org_name, BASE_PATH
        );
        os.system(cmd);

if __name__ == '__main__':
    main()
