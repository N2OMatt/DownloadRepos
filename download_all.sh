#!/usr/bin/env bash
##----------------------------------------------------------------------------##
## File      : download_all.sh                                                ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : September 05, 2017 (Happy Birthday Daddy)                      ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - 2017, 2018                                           ##
##                                                                            ##
## Description:                                                               ##
##                                                                            ##
##----------------------------------------------------------------------------##

## Get all the downloaders and execute them.
for ITEM in $(ls *.sh); do
    echo $0 | grep $ITEM > /dev/null && echo "Same file ($ITEM) - Skipping" && continue;
    ./$ITEM
done;
