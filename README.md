# D2R-Stash-Manager
A simple stash manager for Diablo 2 Remastered.

This script is a glorified file mover.
All it does is swaps shared stash files around based on what stash the user wants to use in-game.
It has no knowledge or ability to edit stashes or items directly.
All Move operations should be logged in case anything goes wrong.

__NOTE: Stashes should not be moved while D2R is running.__

D2R stores stash information in memory and will write to disk once closed.
This script has a rudimentary check to prevent users from accidentally moving stashes while D2R is running.
Yep, this is a pain in the butt, but that's the way it is.

As always, backup your save folder while adopting a new tool like this.

## Setup
1. Install [Python](https://www.python.org/) if you don't have it.
2. Create a `shared-stashes` folder within your D2R save directory.
    * This should be `C:\Users\<Name>\Saved Games\Diablo II Resurrected`.
    * Other subfolder names can be used, but must be provided via the `--stash-subdir` CLI option.

## How to Use
1. Run `python.exe d2r-stash-mgr.py` from a command line window.
2. Close D2R if it's running.
3. Select the stash you would like to activate by typing its number.
    * Selecting the same stash a 2nd time will restore the original stash when the script was run.
4. Start D2R and do whatever you need with the stash.
5. Go back to step 2 if you want to use another stash.
6. Close D2R.
7. Exit by typing `e`.
    * If a stash is selected, it will be moved back to its original place and the original stash will be restored for use in-game.

## Creating New Stashes
1. When your shared stash is empty, copy it into the `shared-stashes` subfolder.
    * The file should be named `SharedStashSoftCoreV2.d2i` within your D2R save directory.
    * It doesn't _have_ to be empty, but are ya really gonna dupe items? :)
    * You can create as many copies as you want to start a collection of stashes.
2. Restart the stash manager.
    * It has no ability to read new stashes while it's running.
