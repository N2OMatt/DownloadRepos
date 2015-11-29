#!/usr/bin/python
import os;
import os.path;
import termcolor;

## Paths.
GIT_URL           = "https://github.com/AmazingCow/";
ENGINES_PATH      = "~/Documents/Projects/AmazingCow/OpenSource/Engines/";
GAMES_PATH        = "~/Documents/Projects/AmazingCow/OpenSource/Games/";
GAMES_GAME_PATH   = "~/Documents/Projects/AmazingCow/OpenSource/Games/Game/";
GAMES_CORE_PATH   = "~/Documents/Projects/AmazingCow/OpenSource/Games/Core/";
LIBS_PATH         = "~/Documents/Projects/AmazingCow/OpenSource/Libs/";
TOOLS_PATH        = "~/Documents/Projects/AmazingCow/OpenSource/Tools/";

# Repositiory - Directory Information.
REPOS = {
    #Engines.
    "MonsterFramework" : ENGINES_PATH,
    #Games.
    "101_Games_To_Create" : GAMES_PATH,
    #Games - Core
    "Core_Genius"       : GAMES_CORE_PATH,
    "Core_LightsOff"    : GAMES_CORE_PATH,
    "Core_Mastermind"   : GAMES_CORE_PATH,
    "Core_Minesweeper"  : GAMES_CORE_PATH,
    "Core_PegSolitaire" : GAMES_CORE_PATH,
    "Core_Snake"        : GAMES_CORE_PATH,
    "CoreCoord"         : GAMES_CORE_PATH,
    #Games - Game
    "Game_Snake" : GAMES_GAME_PATH,
    "Game_Taz"   : GAMES_GAME_PATH,
    #Libs
    "ColorHelperCpp" : LIBS_PATH,
    "Termcolor_cpp"  : LIBS_PATH,
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
