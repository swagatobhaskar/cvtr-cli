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
H.264 encoder, so any FFmpeg build used here must be compiled with
`--enable-gpl` and its overall license is GPL, not LGPL. The GPL *version*
(v2 vs v3) depends on which other components are compiled in.

## Windows binary bundled with releases (the one actually shipped)

The Windows binary bundled with releases is a `gyan.dev` "essentials"
build. Its reported configuration:

- Version: `9.0.2-essentials_build-www.gyan.dev`
- `--enable-gpl` is present, with GPL-licensed components enabled:
  `libx264`, `libx265`, `libxvid`, `libvidstab`, `librubberband`
- `--enable-nonfree` is **absent** → this build is redistributable
- `--enable-version3` **is present** — required because this build also
  enables `libopencore-amrnb`, `libopencore-amrwb`, and `libvo-amrwbenc`
  (Apache License 2.0 codecs, incompatible with GPLv2 but compatible with
  GPLv3), and `gmp` (LGPLv3+ in current versions)

**Resulting license: GNU General Public License, version 3 or later
(GPL-3.0-or-later).** This is the license that actually governs the FFmpeg
binary distributed with this application — not GPLv2.

| Field | Value |
|---|---|
| Bundled FFmpeg version | `9.0.2-essentials_build-www.gyan.dev` |
| Build source | https://www.gyan.dev/ffmpeg/builds/ |
| Build variant | `essentials_build` |
| `--enable-nonfree` present? | No |
| `--enable-version3` present? | Yes |
| Resulting license | GPL-3.0-or-later |
| Corresponding source location | https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip |
<!-- `TODO — gyan.dev publishes build scripts/patches; link the specific ones matching this version, or point to the matching upstream FFmpeg git tag/commit plus gyan.dev's build config` | -->

Re-run `ffmpeg -version` against the exact binary before every release and
update this table if the build, provider, or enabled components change —
a future switch to a different build (or a different gyan.dev/BtbN variant)
could change the license, the redistributability, or both.

### Reference only: Linux development environment

The `ffmpeg` used locally during development on Ubuntu (package
`8.0.1-3ubuntu2`) is a *different, separately-built* binary — GPL v2 or
later, since it does not enable the Apache-2.0 AMR codecs that force
`--enable-version3`. This build is **not** distributed to end users, so it
does not itself create a distribution obligation; it's noted here only for
completeness, since a future Linux release of this application would need
its own version of this check against whatever binary is actually shipped.

## Obtaining FFmpeg's source code

In compliance with GPLv3 Section 6, the complete corresponding source code
for the exact FFmpeg build distributed with this application must be made
available — either by including it, linking to it, or a written offer valid
for at least three years. Fill in "Corresponding source location" above
and/or a contact for source requests (`bhaskarswagato@gmail.com`) before
shipping a release that bundles this binary.

## License text

The full text of the license governing the bundled Windows FFmpeg binary is
included in this repository at `licenses/FFmpeg-COPYING.GPLv3` — that's the
operative one for what's actually shipped. `licenses/FFmpeg-COPYING.GPLv2`
is kept for reference against the Linux development build described above,
but does not apply to the distributed application unless a future Linux
release ships a GPLv2-only ffmpeg build.

## Copyright

FFmpeg is Copyright © the FFmpeg developers. See https://ffmpeg.org and
https://github.com/FFmpeg/FFmpeg for full authorship information.
