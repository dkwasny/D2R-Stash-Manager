import argparse
from pathlib import Path
import subprocess


D2R_SAVE_DIR = Path.home() / 'Saved Games' / 'Diablo II Resurrected'
DEFAULT_STASH_SUBDIR = 'shared-stashes'
ACTIVE_STASH_NAME = 'SharedStashSoftCoreV2'
TMP_STASH_NAME = '_tmp_'
STASH_SUFFIX = '.d2i'
FORCE_EXIT_VALUE = '_forceexit_'
EXIT_VALUES = {'e', 'E', FORCE_EXIT_VALUE}
D2R_EXECUTABLE = 'D2R.exe'


def print_sep():
    print('----------')

def check_dir(path, name):
    if not path.exists():
        raise Exception(f'{name} path does not exist: {path}')
    if not path.is_dir():
        raise Exception(f'{name} path is not a directory: {path}')

def print_stashes(stashes, active_idx):
    print_sep()
    for i in range(len(stashes)):
        if active_idx is not None and i == active_idx:
            cursor = '-->'
        else:
            cursor = '   '
        print(f'{cursor} {i}: {stashes[i].stem}')
    print_sep()

def move_and_log(src, dest):
    print(f'Move {src} to {dest}')
    src.rename(dest)

def swap_stashes(old_path, new_path):
    move_and_log(active_stash_path, old_path)
    move_and_log(new_path, active_stash_path)

def is_d2r_running():
    output = subprocess.check_output(
        ['tasklist', '/fi', f'imagename eq {D2R_EXECUTABLE}'],
        text=True
    ).strip()
    return output != 'INFO: No tasks are running which match the specified criteria.'


# Arg parsing
parser = argparse.ArgumentParser(
    description='D2R Stash Manager',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    '--stash-subdir',
    dest='stash_subdir',
    help='Stash Subdirectory (within D2R Save Directory)',
    default=DEFAULT_STASH_SUBDIR
)

args = parser.parse_args()

stash_dir = D2R_SAVE_DIR / args.stash_subdir

print(f'Save Dir = {D2R_SAVE_DIR}')
print(f'Stash Dir = {stash_dir}')

# Get relevant dirs
check_dir(D2R_SAVE_DIR, 'D2R save')
check_dir(stash_dir, 'Stash')

active_stash_path = D2R_SAVE_DIR / f'{ACTIVE_STASH_NAME}{STASH_SUFFIX}'
if not active_stash_path.is_file():
    raise Exception(f'Starting stash not found: {active_stash_path}')

tmp_stash_path = D2R_SAVE_DIR / f'{TMP_STASH_NAME}{STASH_SUFFIX}'
if tmp_stash_path.exists():
    raise Exception(f'Tmp stash found: {tmp_stash_path}')

# Read stash filenames
stashes = [x for x in stash_dir.iterdir() if x.suffix == STASH_SUFFIX]
stashes.sort()
if not stashes:
    raise Exception(f'No stashes found in dir: {stash_dir}')

active_stash_idx = -1
print_stashes(stashes, active_stash_idx)

# Main loop
running = True
while running:
    val = input('Select Stash (e to exit): ')
    if is_d2r_running() and val != FORCE_EXIT_VALUE:
        print('D2R may be running!  Please exit D2R if it is open.')
        print(f'If this message is showing in error, type "{FORCE_EXIT_VALUE}" (dangerous if D2R is running)')
        continue

    if val in EXIT_VALUES:
        running = False
        continue

    if not val.isdigit():
        print(f'Input is not a number: {val}')
        continue
    
    input_val = int(val)

    if input_val < 0 or input_val > len(stashes) - 1:
        print(f'Input is not a valid index: {val}')
        continue

    if input_val == active_stash_idx:
        # Revert back to starting stash
        old_stash_path = stashes[active_stash_idx]
        new_stash_path = tmp_stash_path
        active_stash_idx = -1
    else:
        # Activate selected stash
        if active_stash_idx == -1:
            old_stash_path = tmp_stash_path
        else:
            old_stash_path = stashes[active_stash_idx]

        active_stash_idx = input_val
        new_stash_path = stashes[active_stash_idx]

    swap_stashes(old_stash_path, new_stash_path)

    print_stashes(stashes, active_stash_idx)

if active_stash_idx != -1:
    # If a stash is active on exit, revert back to starting stash
    old_stash_path = stashes[active_stash_idx]
    swap_stashes(old_stash_path, tmp_stash_path)
    