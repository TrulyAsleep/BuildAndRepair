# Build and Repair — updated for Space Engineers 1.210

The Nanobot Build and Repair System, updated to work on the current Space Engineers
build (1.210 "Prosperity", after 1.209 "Economy 2").

## What was broken

Since the latest game updates, Build and Repair blocks stop welding completely. They
pick a target and pull components out of cargo, but nothing ever gets built (with
auto-push on, the components just bounce back and forth between the block and your
containers).

The cause is an engine change: the mod moves components through an internal
"transport" inventory, and the current game build refuses every item added to an
inventory created the way the old code created it. Every Build and Repair version
based on the original code is affected.

This build fixes it: the transport inventory is created with an explicit mass limit,
and every hand-off checks real free space and confirms the items actually arrived,
returning anything that didn't so no components are lost.

It is based on SKO85's maintained source (v2.5.6 development code, upstream commit
`9ab62fe`, October 2026), which also includes about 95 bug fixes since the last Steam
release (v2.5.5).

## Install (single player / hosting from your game)

1. Copy the `BuildAndRepair` folder into `%AppData%\SpaceEngineers\Mods\`
   so you end up with `%AppData%\SpaceEngineers\Mods\BuildAndRepair\Data\...`.
2. In Space Engineers: **Load Game** → select your world → **Edit Settings** → **Mods**.
3. **Remove the old, outdated Build and Repair mod** from the world. Do not run both;
   two copies of the same block script conflict.
4. Add **BuildAndRepair** (it shows with a local/folder icon) and save.

Your existing Build and Repair blocks stay in the world: this version uses the same
block IDs (`SELtdLargeNanobotBuildAndRepairSystem` / `SELtdSmallNanobotBuildAndRepairSystem`)
as the original mod and its reuploads.

### Dedicated servers

Servers and the players joining them get mods from the Workshop, so publish it first:

1. Install it locally as above, then in the game's **Mods** screen select
   **BuildAndRepair** and click **Publish**.
2. Set the Workshop item's visibility to **Unlisted** or **Public**. Not Friends-only
   or Private: players who can't download it can't join.
3. In the server's mod list, remove the old Build and Repair mod and add the new
   Workshop ID, then restart the server.

Each block's terminal settings carry over (same storage key as the original mod).
Server-wide `ModSettings.xml` tweaks do not: that file lives in a world storage folder
named after the mod's Workshop ID, so the new ID starts from defaults. Copy your old
values over or set them with `/nanobars config` if you had changed any.

## Workshop images

- `BuildAndRepair/thumb.jpg` is the Workshop preview image. The game uploads it
  automatically when you publish.
- `Workshop/*.jpg` are gallery images for the Workshop page. After publishing, add
  them on the item's page under **Add/edit images & videos**.
- `Workshop/source/` holds the editable source (`images.html`); re-render with
  `node render.cjs` (needs Playwright). Rajdhani font: SIL Open Font License.

## Block cost

By default the blocks use the original Nanobot build costs. To use the more expensive
"nerfed" costs instead (10x components plus Superconductors), copy
`Variants/Nerfed/Data/CubeBlocks.sbc` over `BuildAndRepair/Data/CubeBlocks.sbc`.
Changing costs on an existing world can make already-built blocks show as
incomplete, so pick one and stick with it.

## Settings and commands

Server settings live in `ModSettings.xml` (created in the world's storage folder);
admins can use `/nanobars` chat commands. Full reference:
<https://sko85.github.io/SE-Mods/Build-and-Repair-System/>

## Credits

- Original mod: Dummy08 — Nanobot Build and Repair System
- Maintained version and the 1.210 fix: SKO85 — <https://github.com/SKO85/SE-Mods>
