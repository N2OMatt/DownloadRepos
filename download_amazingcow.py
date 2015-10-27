#!/usr/bin/python
import os;
import os.path;

GIT_URL     = "https://github.com/AmazingCow/";
ENGINES_PATH = "~/Documents/Projects/AmazingCow/OpenSource/Engines/";
GAMES_PATH   = "~/Documents/Projects/AmazingCow/OpenSource/Games/";
LIBS_PATH    = "~/Documents/Projects/AmazingCow/OpenSource/Libs/";
TOOLS_PATH   = "~/Documents/Projects/AmazingCow/OpenSource/Tools/";

REPOS = { 
   #Engines.
    "ApplePy"          : ENGINES_PATH,
    "MonsterFramework" : ENGINES_PATH,
    #Games.
    "101_Games_To_Create" : GAMES_PATH,
    #Libs
    "ColorHelperCpp" : LIBS_PATH,
    "UIKitHelpers"   : LIBS_PATH,
    #Tools.
    "AmazingBuild"         : TOOLS_PATH,
    "COWTODO"              : TOOLS_PATH,
    "CppGuardChecker"      : TOOLS_PATH,
    "FrameMerger"          : TOOLS_PATH,
    "Gosh"                 : TOOLS_PATH,
    "ImageOrganizer"       : TOOLS_PATH,
    "LinuxUSBBootCreator"  : TOOLS_PATH,
    "PhotoShow"            : TOOLS_PATH,
    "SpriteSheetExtractor" : TOOLS_PATH,
    "Tasks"                : TOOLS_PATH,
};


for repo_name in sorted(REPOS.keys()):
    full_git_url   = os.path.join(GIT_URL, repo_name + ".git");
    full_repo_path = os.path.expanduser(os.path.join(REPOS[repo_name], repo_name));

    if(os.path.isdir(full_repo_path)):
        print "{} is already downloaded....".format(repo_name);
        continue;

    os.system("mkdir -p {}".format(full_repo_path));
    os.system("git clone {} {}".format(full_git_url, full_repo_path));