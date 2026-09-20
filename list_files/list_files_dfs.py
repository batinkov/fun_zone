#!/usr/bin/env python3
import os
import sys

SKIP_DIRS = {'.git', '.idea', '__pycache__', '.venv', '.pytest_cache'}


def list_files(root: str) -> list[str]:
    all_files = []
    stack = [root]

    while stack:
        current = stack.pop()

        try:
            with os.scandir(current) as it:
                entities = sorted(it, key=lambda e: e.name)
        except OSError as e:
            print(f'skipping {current}: {e.strerror}', file=sys.stderr)
            continue

        for entity in entities:
            if entity.is_dir(follow_symlinks=False):
                if entity.name not in SKIP_DIRS:
                    stack.append(entity.path)
            else:
                all_files.append(entity.path)

    return all_files


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    for file in list_files(path):
        print(file)
