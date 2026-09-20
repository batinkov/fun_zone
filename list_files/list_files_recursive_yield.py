#!/usr/bin/env python3
import os
import sys
from collections.abc import Iterator

SKIP_DIRS = {'.git', '.idea', '__pycache__', '.venv', '.pytest_cache', '.claude'}


def list_files(root: str) -> Iterator[str]:
    try:
        with os.scandir(root) as it:
            entries = sorted(it, key=lambda e: e.name)
    except OSError as e:
        print(f'skipping {root}: {e.strerror}', file=sys.stderr)
        return

    for entry in entries:
        if entry.is_dir(follow_symlinks=False):
            if entry.name not in SKIP_DIRS:
                yield from list_files(entry.path)
        else:
            yield entry.path


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    for file in list_files(path):
        print(file)
