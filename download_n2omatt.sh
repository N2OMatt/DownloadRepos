#!/usr/bin/env sh
##~---------------------------------------------------------------------------##
##                        ____                       _   _                    ##
##                  _ __ |___ \ ___  _ __ ___   __ _| |_| |_                  ##
##                 | '_ \  __) / _ \| '_ ` _ \ / _` | __| __|                 ##
##                 | | | |/ __/ (_) | | | | | | (_| | |_| |_                  ##
##                 |_| |_|_____\___/|_| |_| |_|\__,_|\__|\__|                 ##
##                              www.n2omatt.com                               ##
##  File      : download_n2omatt.sh                                           ##
##  Project   : DownloadRepos                                                 ##
##  Date      : Sep 06, 2017                                                  ##
##  License   : GPLv3                                                         ##
##  Author    : n2omatt <n2omatt@amaizingcow.com                              ##
##  Copyright : n2omatt - 2017, 2018                                          ##
##                                                                            ##
##  Description :                                                             ##
##   Clone all N2OMatt's public repos.                                        ##
##---------------------------------------------------------------------------~##


##----------------------------------------------------------------------------##
## Github repos                                                               ##
##----------------------------------------------------------------------------##
ORGS="N2OMatt";
REAL_HOME=$(/usr/local/bin/user-real-home);
BASE_PATH="$REAL_HOME/Documents/Projects";

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

##----------------------------------------------------------------------------##
## Not a Bug                                                                  ##
##----------------------------------------------------------------------------##
git clone https://notabug.org/n2omatt/libreflix $BASE_PATH/$ORGS/libreflix
