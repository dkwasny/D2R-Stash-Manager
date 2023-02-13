# D2R-Stash-Manager
A simple stash manager for Diablo 2 Remastered.

This script is a glorified file mover.
All it does is swap shared stash files around based on what stash the user wants to use in-game.
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
3. Download [d2r-stash-mgr.py](https://raw.githubusercontent.com/dkwasny/D2R-Stash-Manager/main/d2r-stash-mgr.py) to a folder of your choosing.
   * Use `Ctrl-S` to save the file.
4. [Create some starter stashes](#creating-new-stashes) if you don't have some already.

## How to Use
1. Open a command line or terminal window.
2. Navigate to the directory containing `d2r-stash-mgr.py`.
3. Run `python.exe d2r-stash-mgr.py`.
4. Close D2R if it's running.
5. Select the stash you would like to activate by typing its number.
    * Selecting the same stash a 2nd time will restore the original stash from when the script was first run.
6. Start D2R and do whatever you need with the stash.
7. Go back to step 4 if you want to use another stash.
8. Close D2R.
9. Exit by typing `e`.
    * If a stash is still selected at exit, the script will move it back to its original place and the original stash will be restored for use in-game.

## Creating New Stashes
1. When your shared stash is empty, copy it into the `shared-stashes` subfolder.
    * The file should be named `SharedStashSoftCoreV2.d2i` within your D2R save directory.
    * It doesn't _have_ to be empty, but are ya really gonna dupe items? :)
    * The new stash can be named however you want.
    * You can create as many copies as you want to start a collection of stashes.
    * The [GoMule](https://sourceforge.net/projects/gomule/files/gomule/R0.44/) folks have some empty stashes for use as well.
2. Restart the stash manager.
    * There's no ability to read new stashes while the script is running.
    
## Troubleshooting
* If the script crashes for whatever reason, you will need to manually rename your stashes back to their original state.
* The last active stash will be named `SharedStashSoftCoreV2.d2i` and the original stash will be named `_tmp_.d2i`.
