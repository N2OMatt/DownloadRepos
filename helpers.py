##----------------------------------------------------------------------------##
## File      : helpers.py                                                     ##
## Project   : DownloadRepos                                                  ##
## Author    : n2omatt <n2omatt@amazingcow.com>                               ##
## Date      : September 06, 2017                                             ##
## License   : GPLv3                                                          ##
## Copyright : N2OMatt - Copyright (c) 2017                                   ##
##                                                                            ##
## Description:                                                               ##
##   Just some helpers...                                                     ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
import sys;
import getopt;

################################################################################
## Error                                                                      ##
################################################################################
def error(msg):
    print("[FATAL] {0}".format(msg));
    exit(1);


################################################################################
## Sanity Checks                                                              ##
################################################################################
def check_and_clean(name, arg):
    if(arg is None):
        error("{0} is required.".format(name));

    arg = arg.strip();
    if(len(arg) == 0):
        error("{0} cannot be empty.".format(name));

    return arg;


################################################################################
## getopt                                                                     ##
################################################################################
def getoptions_init(flags_list):
    try:
        cmd_options = getopt.gnu_getopt(
            sys.argv[1:],
            "",
            flags_list
        );
        return cmd_options;
    except Exception as e:
        raise e;

def getoptions_getarg(options, name):
    for opt, arg in options[0]:
        if(name in opt):
            return arg;
    return None;
