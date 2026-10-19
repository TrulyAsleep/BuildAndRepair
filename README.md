# Build and Repair — updated for Space Engineers 1.210

The Nanobot Build and Repair System, built from the newest maintained code and
running on the current Space Engineers version (1.210 "Prosperity").

## Two versions

Both versions are the same mod. Only the block cost differs, and each one is
labelled everywhere a player looks:

| | Nerfed | Original Costs |
| --- | --- | --- |
| Folder | `BuildAndRepair/` | `BuildAndRepair-OriginalCosts/` |
| Block cost | About 10x the original parts, plus Superconductors | The original Nanobot recipe |
| Workshop thumbnail | Yellow **NERFED** band | Green **ORIGINAL** band |
| Block name in the G-menu | Build and Repair System (Nerfed) | Build and Repair System (Original) |
| Suggested Workshop title | Build and Repair (Nerfed) – SE 1.210 | Build and Repair (Original Costs) – SE 1.210 |

Use **one version per world, never both**: they define the same blocks and run the
same scripts, so together they conflict.

## What's in this build

- **Newest maintained code.** Based on SKO85's unreleased v2.5.6 development code
  (upstream commit `9ab62fe`, October 2026), which has about 95 bug fixes beyond their
  last Steam release (v2.5.5).
- **Fixes for an engine quirk v2.5.6 ran into.** In the current game, the engine's
  "will these items fit?" check always answers no for the mod's internal transport
  inventory, even though adding items to it works. v2.5.6 started relying on that
  check, which stalled two things:
  - Welding: blocks pulled components but never welded (fixed upstream by SKO85).
  - Collecting: blocks listed floating items to collect but never picked them up
    (fixed in this build, `261019.1`).

  Both now check free space directly and confirm the items arrived, so nothing is
  lost. SKO85's released v2.5.5 never used that check, so it isn't affected.

`/nanobars version` shows the build number, so you can confirm which build a server
is running.

## Install (single player / hosting from your game)

1. Copy **one** of the two folders into `%AppData%\SpaceEngineers\Mods\`, e.g.
   `%AppData%\SpaceEngineers\Mods\BuildAndRepair\Data\...`.
2. In Space Engineers: **Load Game** → select your world → **Edit Settings** → **Mods**.
3. **Remove any other Build and Repair mod** from the world.
4. Add the one you copied (it shows with a local/folder icon) and save.

Existing Build and Repair blocks stay in the world: both versions use the same block
IDs (`SELtdLargeNanobotBuildAndRepairSystem` / `SELtdSmallNanobotBuildAndRepairSystem`)
as the original mod and its reuploads.

## Publishing to the Workshop

Servers and the players joining them get mods from the Workshop. Each version is its
own Workshop item, and the file that ties a folder to its item is `modinfo.sbmi`,
which the game writes into the folder the first time you publish it.

- **Updating the Nerfed item you already published:** copy the contents of
  `BuildAndRepair/` over your existing `%AppData%\SpaceEngineers\Mods\BuildAndRepair\`
  folder, keeping the `modinfo.sbmi` that is already there, then **Publish**. That
  updates your existing item.
- **Publishing Original Costs for the first time:** copy `BuildAndRepair-OriginalCosts/`
  into the Mods folder and **Publish**. With no `modinfo.sbmi` it becomes a new item.
  Never copy the Nerfed folder's `modinfo.sbmi` into it: publishing would then
  overwrite your Nerfed item.

Then on each item's Workshop page:

1. Set visibility to **Unlisted** or **Public**. Not Friends-only or Private: players
   who can't download it can't join.
2. Under **Add/edit images & videos**, add the gallery images. The thumbnail is
   uploaded automatically from the folder's `thumb.jpg`.
   - Nerfed: `Workshop/1-updated.jpg`, `Workshop/2-features.jpg`, `Workshop/3-dropin.jpg`
   - Original Costs: `Workshop/OriginalCosts/1-updated.jpg`, plus the same
     `2-features.jpg` and `3-dropin.jpg`
3. Start each description with which version it is and a link to the other, e.g.
   *"This is the NERFED version (expensive to build). Prefer the original cheap
   recipe? Use Build and Repair (Original Costs) instead: [link]. Never use both."*

## Switching a world between versions

Remove one from the world's mod list (or the server's), add the other, and restart.

- Blocks stay, and each block's terminal settings carry over.
- Built blocks stay complete: the game saves how far each block is built as a
  percentage. But grinding one down refunds the new cost, so going from Original to
  Nerfed hands out extra components for blocks built before the switch.
- Server-wide `ModSettings.xml` tweaks don't carry over: that file lives in a world
  storage folder named after the mod's Workshop ID, so the other version starts from
  defaults. Copy your values over or set them with `/nanobars config`.

The same applies when moving a world over from an older Build and Repair mod.

## Settings and commands

Server settings live in `ModSettings.xml` (created in the world's storage folder);
admins can use `/nanobars` chat commands. Full reference:
<https://sko85.github.io/SE-Mods/Build-and-Repair-System/>

## For maintainers

- Make changes in `BuildAndRepair/`, then run `python3 tools/sync_original_costs.py`
  to copy them into `BuildAndRepair-OriginalCosts/`. Only that folder's
  `Data/CubeBlocks.sbc` and `thumb.jpg` are its own; the script never copies or
  deletes `modinfo.sbmi`.
- `Workshop/source/images.html` is the editable source for all Workshop images;
  re-render with `node render.cjs <output-dir>` (needs Playwright). Rajdhani font:
  SIL Open Font License.

## Credits

- Original mod: Dummy08 — Nanobot Build and Repair System
- Maintained version and the welding fix: SKO85 — <https://github.com/SKO85/SE-Mods>
