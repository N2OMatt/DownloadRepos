#!/usr/bin/env bash
##----------------------------------------------------------------------------##
## File      : download_amazingcow.sh                                         ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : September 06, 2017                                             ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - 2017, 2018                                           ##
##                                                                            ##
## Description:                                                               ##
##   Clone all public AmazingCow's repos.                                     ##
##----------------------------------------------------------------------------##

ORGS="AmazingCow-Apps           \
      AmazingCow-Game-Core      \
      AmazingCow-Game-Framework \
      AmazingCow-Game-Tool      \
      AmazingCow-Game           \
      AmazingCow-Libs           \
      AmazingCow-Tools          \
      AmazingCow-Imidiar        \
      AmazingCow-Services       \
      AmazingCow-UnixLike       \
      AmazingCow";

BASE_PATH="$HOME/Documents/Projects/AmazingCow"

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
