# Third-Party Notices

This repository's own source code (everything except the bundled FFmpeg
binary described below) is licensed under the MIT License — see `LICENSE`.

This project bundles a redistributable build of **FFmpeg** so end users are
not required to install FFmpeg themselves. FFmpeg is **not** part of this
project's codebase: it is an independent, third-party program that this
application invokes as a separate process (via Python's `subprocess`) and
ships alongside the application's own files as a "mere aggregation," which
GPL Section 2 explicitly permits for independent works distributed together
on the same medium. Invoking FFmpeg's compiled binary as a separate process
does not make this project's own source code a derivative work of FFmpeg,
and does not change the license of the code in this repository.

## FFmpeg's license

FFmpeg's license depends entirely on how the specific binary was compiled —
it is not something this project chooses. This project's transcoding
pipeline uses `libx264` (`-c:v libx264`, `-tune animation`), a GPL-licensed
H.264 encoder. Any FFmpeg build that includes `libx264` must be compiled
with `--enable-gpl`, and FFmpeg's overall license then becomes the
**GNU General Public License, version 2 or later (GPL-2.0-or-later)** —
not LGPL, regardless of how the rest of FFmpeg is configured.

### Reference build (development / Linux)

The FFmpeg build used during development on Ubuntu reports:

- Version: `8.0.1-3ubuntu2`
- Configuration includes `--enable-gpl` and multiple GPL-licensed
  components: `--enable-libx264`, `--enable-libx265`, `--enable-libcdio`,
  `--enable-librubberband`, `--enable-libvidstab`, `--enable-libxvid`,
  `--enable-frei0r`
- `--enable-nonfree` is **not** present → this build is redistributable
- `--enable-version3` is **not** present → this build's license is
  **GPL v2 or later**, not GPL v3
- Full version/configuration banner: `ffmpeg -version`

### ⚠️ Windows binary bundled with releases — verify before every release

The binary actually shipped inside Windows releases is a **separate build**
(e.g. from gyan.dev or BtbN's ffmpeg-builds project) and may not share the
exact configuration of the Ubuntu reference build above. Before bundling
any FFmpeg binary for distribution:

1. Run `ffmpeg -version` against the *exact* binary being bundled.
2. Confirm `--enable-nonfree` is **absent**. A build compiled with
   `--enable-nonfree` (e.g. for `libfdk_aac`, certain hardware SDKs) is
   **not legally redistributable** and must not be shipped.
3. Note whether `--enable-version3` is present (→ GPL v3) or absent
   (→ GPL v2).
4. Fill in the table below, and add `licenses/FFmpeg-COPYING.GPLv3`
   alongside the GPLv2 file if the bundled build turns out to be GPL v3.

| Field | Value |
|---|---|
| Bundled FFmpeg version | `TODO` |
| Build source | `TODO — e.g. https://www.gyan.dev/ffmpeg/builds/ or https://github.com/BtbN/FFmpeg-Builds` |
| Build variant | `TODO — e.g. "full_build-shared"` |
| `--enable-nonfree` present? | `TODO` |
| `--enable-version3` present? | `TODO` |
| Resulting license | `TODO — GPL-2.0-or-later / GPL-3.0-or-later` |
| Corresponding source location | `TODO — link to the exact FFmpeg source tag/commit the build provider compiled from` |

## Obtaining FFmpeg's source code

In compliance with GPL Section 3, the complete corresponding source code for
the exact FFmpeg build distributed with this application is available at
the "Build source" / "Corresponding source" links in the table above, and/or
by written request to `TODO: add a contact email`, an offer valid for at
least three years from the date this software was distributed to you.

## License text

The full text of the license governing the bundled FFmpeg binary is included
in this repository at `licenses/FFmpeg-COPYING.GPLv2`. If a future release
bundles a GPL v3 build, add `licenses/FFmpeg-COPYING.GPLv3` alongside it and
reference both here.

## Copyright

FFmpeg is Copyright © the FFmpeg developers. See https://ffmpeg.org and
https://github.com/FFmpeg/FFmpeg for full authorship information.