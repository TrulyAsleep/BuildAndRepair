#!/usr/bin/env python3
"""Rebuild BuildAndRepair-OriginalCosts from BuildAndRepair.

The Original Costs mod is the main mod with a different Data/CubeBlocks.sbc
(original component costs, "(Original)" block names) and its own thumb.jpg.
Everything else is copied from the main mod, so run this after every change to
BuildAndRepair/ and commit both folders together:

    python3 tools/sync_original_costs.py

modinfo.sbmi is never copied or deleted: it is the file Space Engineers writes
when you publish, and it points at one specific Workshop item. Copying the main
mod's into this folder would make publishing the Original Costs mod overwrite
the main Workshop item.
"""
import filecmp
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = os.path.join(ROOT, "BuildAndRepair")
VARIANT = os.path.join(ROOT, "BuildAndRepair-OriginalCosts")

# Files that belong to the variant itself (paths relative to the mod folder).
VARIANT_OWNED = {os.path.join("Data", "CubeBlocks.sbc"), "thumb.jpg"}
NEVER_TOUCH = {"modinfo.sbmi"}


def mod_files(folder):
    for dirpath, _, filenames in os.walk(folder):
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), folder)
            if rel in VARIANT_OWNED or os.path.basename(rel) in NEVER_TOUCH:
                continue
            yield rel


def main():
    for rel in VARIANT_OWNED:
        if not os.path.isfile(os.path.join(VARIANT, rel)):
            sys.exit("missing variant file: BuildAndRepair-OriginalCosts/" + rel.replace(os.sep, "/"))

    main_files = set(mod_files(MAIN))
    copied = removed = 0
    for rel in sorted(main_files):
        src, dst = os.path.join(MAIN, rel), os.path.join(VARIANT, rel)
        if os.path.isfile(dst) and filecmp.cmp(src, dst, shallow=False):
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1

    for rel in sorted(set(mod_files(VARIANT)) - main_files):
        os.remove(os.path.join(VARIANT, rel))
        removed += 1
    for dirpath, _, _ in os.walk(VARIANT, topdown=False):
        if dirpath != VARIANT and not os.listdir(dirpath):
            os.rmdir(dirpath)

    print("BuildAndRepair-OriginalCosts: %d copied, %d removed" % (copied, removed))


if __name__ == "__main__":
    main()
