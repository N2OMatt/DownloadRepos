#!/bin/bash
##----------------------------------------------------------------------------##
## File      : download_n2omatt.sh                                            ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : September 06, 2017                                             ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - Copyright (c) 2017                                   ##
##                                                                            ##
## Description:                                                               ##
##   Clone all N2OMatt's public repos.                                        ##
##----------------------------------------------------------------------------##

ORGS="N2OMatt";
BASE_PATH="$HOME/Documents/Projects/";

for ORG in $ORGS; do
    ./github_repo_fetcher.py \
        --org=$ORG           \
        --output=$ORG.list;

    ./download_repos.py             \
        --org=AmazingCow            \
        --base-path=$BASE_PATH/$ORG \
        --repos-list=./$ORG.list;

    rm $ORG.list;
done;
