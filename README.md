# D2R-Stash-Manager
A simple stash manager for Diablo 2 Remastered.

This script is a glorified file mover.
All it does is swaps shared stash files around based on what stash the user wants to use in-game.
It has no knowledge or ability to edit stashes or items directly.
All Move operations should be logged in case anything goes wrong.

__NOTE: Stashes should not be moved while D2R is running.__
D2R stores stash information in memory and will write to disk once closed.
The script has a rudimentary check to prevent users from accidentally moving stashes while D2R is running.

## Setup
1. Install [Python](https://www.python.org/) if you don't have it.
2. Create a `shared-stashes` folder within your D2R save directory.
    * This should be `C:\Users\<Name>\Saved Games\Diablo II Resurrected`.
    * Other subfolder names can be used, but must be provided via the `--stash-subdir` CLI option.

## How to Use
1. Run `python.exe d2r-stash-mgr.py` from a command line window.
2. Select the stash you would like to activate by typing its number.
    * Once you are done with that stash, select another by entering a different number.
    * Selecting the same stash a 2nd time will restore the original stash when the script was run.
3. Exit by typing `e`.
    * If a stash is selected, it will be moved back to its original place and the original stash will be restored for use in-game.
