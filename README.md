# Build and Repair — updated for Space Engineers 1.210

The Nanobot Build and Repair System, built from the newest maintained code and
running on the current Space Engineers version (1.210 "Prosperity").

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
- **Nerfed build costs by default** (see [Block cost](#block-cost)).

`/nanobars version` shows the build number, so you can confirm which build a server
is running.

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

By default the blocks use the "nerfed" costs from SKO85's maintained version: about
10x the original components, plus Superconductors. For the original, cheaper Nanobot
costs, copy `Variants/OriginalResources/Data/CubeBlocks.sbc` over
`BuildAndRepair/Data/CubeBlocks.sbc`.

Changing costs doesn't break blocks that are already built: the game saves how far
each block is built as a percentage, so they stay complete. But grinding one down
refunds the new cost, so switching from cheap to nerfed hands out extra components
for any block built before the switch.

## Settings and commands

Server settings live in `ModSettings.xml` (created in the world's storage folder);
admins can use `/nanobars` chat commands. Full reference:
<https://sko85.github.io/SE-Mods/Build-and-Repair-System/>

## Credits

- Original mod: Dummy08 — Nanobot Build and Repair System
- Maintained version and the welding fix: SKO85 — <https://github.com/SKO85/SE-Mods>
