#!/usr/bin/env python3
import os
import sys

SKIP_DIRS = {'.git', '.idea', '__pycache__', '.venv', '.pytest_cache', '.claude'}


def list_files(root: str) -> list[str]:
    all_files = []
    sub_dirs = []

    try:
        with os.scandir(root) as it:
            entries = sorted(it, key=lambda e: e.name)
    except OSError as e:
        print(f'skipping {root}: {e.strerror}', file=sys.stderr)
        return all_files

    for entry in entries:
        if entry.is_dir(follow_symlinks=False):
            if entry.name not in SKIP_DIRS:
                sub_dirs.append(entry.path)
        else:
            all_files.append(entry.path)

    for sub_dir in sub_dirs:
        all_files += list_files(sub_dir)

    return all_files


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    for file in list_files(path):
        print(file)
