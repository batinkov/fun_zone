#!/usr/bin/env python3
import os
import sys
from collections import deque

SKIP_DIRS = {'.git', '.idea', '__pycache__', '.venv', '.pytest_cache'}


def list_files(root):
    dirs = deque([root])
    all_files = []

    while dirs:
        current = dirs.popleft()

        # try/with don't create a scope, so 'entries' is visible below.
        # sorted() copies the entries into a list before 'with' closes the iterator.
        # The 'continue' guarantees 'entries' is set whenever the loop below runs.
        try:
            with os.scandir(current) as it:
                entries = sorted(it, key=lambda e: e.name)
        except OSError as e:
            print(f'skipping {current}: {e.strerror}', file=sys.stderr)
            continue

        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                if entry.name not in SKIP_DIRS:
                    dirs.append(entry.path)
            else:
                all_files.append(entry.path)

    return all_files


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    for file in list_files(path):
        print(file)
