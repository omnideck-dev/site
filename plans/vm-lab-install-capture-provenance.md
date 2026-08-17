# Desktop install screenshot provenance

The public site assets under `static/images/install/` are unedited copies of screenshots produced by the deployed omnideck release lab at `/mnt/data/VMs/omnideck-release-lab`.

Release under test: [`omnideck v0.1.0-beta.8`](https://github.com/omnideck-dev/omnideck/releases/tag/v0.1.0-beta.8) at source commit `647e25e7f673`.

## Desktop icon

`static/images/omnideck-app-icon.svg` is an exact copy of `desktop/src-tauri/icons/source.svg` from the Desktop repository.

- SHA-256: `b80f504fff59de38b8836575fd056566579cc2874f2de5873b3dd7f37865986c`

## macOS ARM64

### Native Desktop qualification

- Lab run: `20260815T230446Z-1418934`
- Target: physical Apple Silicon host, application-clean `runtime-ready` baseline
- Result: passed the package smoke, first-run setup, recovery, restart, host-boundary, and DMG lifecycle journeys
- Public DMG SHA-256: `f19a954c72bac68809950b3298b80ecc1b86d9d8803e6d2c0ce633bd2c128b8a`
- Site asset:
  - `macos-first-launch.png` — `ba49f7b110f28d6d8a7d92475d1891d5dfae593dafa9a807453428516bc11de0`
  - `macos-setup-complete.png` — `7d215a9d0220a109779d3aa2c88ddb297ba65045e4e70a21a99d610dda92a62e`

### Quarantined download and Gatekeeper journey

- Lab run: `20260815T230916Z-macos-install`
- Target: physical Apple Silicon host running macOS 15.3.1
- Result: passed the DMG, Applications, Privacy & Security, and administrator-approval journey
- Input: `/Users/larry/Downloads/omnideck_0.1.0-beta.8_aarch64.dmg`
- Download SHA-256: `f19a954c72bac68809950b3298b80ecc1b86d9d8803e6d2c0ce633bd2c128b8a`
- Download quarantine record: `0083;6a7f9eda;Safari;84EC876F-4BE8-4A2F-A645-AF0E54642D10`
- Site assets:
  - `macos-dmg-install.png` — `e56720f0eac138c61e17589766a009b645befdb8d5929026f9837b4b8ceb86b5`
  - `macos-privacy-security.png` — `36dfb2aa438181c1d78cd7d73d4debe606a33779665a6351c7d1488de71b63e9`
  - `macos-security-approval.png` — `d315914fcaefe2d70ae75c9efa4f9c7babc48dbcab7ca49062bc8fbf0389c395`

The already-installed product app was backed up before reproducing the first-open quarantine state. After capture it was restored to its original executable SHA-256 (`094b4b051f1fd7c86959fd072db466e7afcebab1e370e2f0a24cf689d300e4a0`) and original quarantine record (`01c3;6a7f9eda;Safari;84EC876F-4BE8-4A2F-A645-AF0E54642D10`). The temporary capture copy and system-created screenshot files were removed before the lease ended.

## Windows 11 x86-64

- Lab run: `20260815T232730Z-1437406`
- Target: disposable Windows 11 25H2 VM, clean baseline
- Result: passed SmartScreen, NSIS install, UAC, Windows-feature recovery, restart, RunOnce resume, ready state, recovery, and reinstall
- Public EXE SHA-256: `c497334d0dd094deb68fcfe576f8b188f272d8f831f193f9844bd51e95f697a4`
- Site assets:
  - `windows-smartscreen-warning.png` — `4260cd8ea61f428046db7a27478ff50da4d0471901ed282707313ea1785382ec`
  - `windows-smartscreen-run-anyway.png` — `aab1c7b50d63d33bf3e4cc79505ef32b0a6732c684488a8c753e4b1cacd5dfe9`
  - `windows-installer.png` — `9fe63534afcebf92619adf88495c7fa03e121e87dc2192b203d80b159066d054`
  - `windows-uac.png` — `42aea709582d98cb47be96bdcbdd74de066ff48669f6359fd2e079d51dc0cfa6`
  - `windows-restart-required.png` — `915b71f3a8fdb55de04b584324a843574e43c8dcb9078d149786b4622f8a2a05`
  - `windows-setup-resume.png` — `eed0f392d796abbf092ded6154b56ee3abf90e2424aa4a88ecf0a14e48e8fc3e`
  - `windows-setup-complete.png` — `e1e8d03c27319b968c6e523e41127dfa5d28183067cee404dcf96735e29daabe`

The Windows test harness stages the exact release bytes under `candidate-setup.exe`, which is visible after expanding SmartScreen details. The public download retains its release filename.

## Ubuntu AppImage x86-64

- Lab run: `20260815T033122Z-704266`
- Target: disposable Ubuntu 24.04 VM, clean baseline
- First-run installation journey: passed
- Overall run: failed later at the unrelated native zoom bridge check
- Public AppImage SHA-256: `2e08e598e5fbd778d58ab39468a9e92f085dd60a82505ed3569d8b1ee38b0eae`
- Site assets:
  - `linux-first-launch.png` — `9f788f0f160b9d009f40e7bbdcfc6e2b80595abbadf69e019eef091320fa3b81`
  - `linux-runtime-setup.png` — `97e9ef3181054943782e4cd9cae883ff3b186c25ed0deb72dfaeca6f1a7625e5`
  - `linux-setup-complete.png` — `2feead76e24007107720bde2df1876873644df6f58830264a266cec8c7bd172f`

The Linux ready screen was recaptured from the exact release AppImage in lab run `20260816T200910Z-2317305`. The controller paused before the app opened the workbench so the ready state remained visible for the console screenshot. The capture-only qualification was then stopped, and the lab reset the disposable Ubuntu VM to its clean snapshot.
