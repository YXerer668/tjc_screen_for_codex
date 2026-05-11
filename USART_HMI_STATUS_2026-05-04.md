# USART HMI Status 2026-05-04

## Scope

This note records the current state of the local `usarthmi` toolchain, verified artifacts, and the exact gap that still blocks a true `scene -> TFT -> flash` workflow for the `TJC8048X543_011C` screen on `COM36`.

## Verified Working Pieces

### Serial runtime control

- `COM36 @ 9600` is the active screen link.
- Runtime drawing works on the real screen.
- The following have been visually verified on hardware:
  - page background color changes
  - temporary runtime button previews
  - scene-driven runtime preview push

### Scene authoring and preview

- Scene validation works for both JSON and YAML.
- Scene layout resolution works for:
  - `absolute`
  - `row`
  - `column`
  - `grid`
  - `stack`
  - `anchor`
- Local PNG preview rendering works.
- Current preview entrypoint:

```powershell
python -m usarthmi scene preview examples\menu_demo\scene.json --out .\preview_menu_demo.png
```

### HMI page rewriting

- The seed HMI container can be parsed safely.
- `0.pa` round-trips exactly for the current seed page.
- Rebuilt `.HMI` files preserve the original seed container addressing style.
- Scene build emits:
  - `output.hmi`
  - `preview.png`
  - `scene.normalized.json`
  - `manifest.json`

### Font toolchain

- The local `ZiLib` library is built successfully against `.NET Framework 4.8`.
- The local helper [ZiCli.exe](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tools/ZiCli/bin/Release/ZiCli.exe>) is built and runnable.
- Existing seed font [0.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/hmi_extract_v1/0.zi>) can be inspected.
- New `.zi` subset fonts can be generated from:
  - explicit text files
  - scene text
- `0.zi` replacement inside `.HMI` works.
- Multiple `.zi` files can now be packed into a TFT-style embedded font run.

## Important Artifacts

### Scene / HMI

- Seed HMI: [lcd_test.HMI](</D:/MySTM32/H723ZGT6/Program/ISP_Test/lcd_test.HMI>)
- Example scene preview: [preview_menu_demo.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/preview_menu_demo.png>)
- Current built scene HMI: [output.hmi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/build_menu_demo_v3/output.hmi>)
- Current built scene HMI with replaced font: [output_font.hmi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/build_menu_demo_v3/output_font.hmi>)
- Build manifest: [manifest.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/build_menu_demo_v3/manifest.json>)

### Fonts

- Extracted seed font: [0.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/hmi_extract_v1/0.zi>)
- Demo generated subset font: [build_font_demo.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/build_font_demo.zi>)
- Scene-derived subset font: [build_font_scene.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/build_font_scene.zi>)
- Packed TFT-style font run: [build_tft_font_run.bin](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/build_tft_font_run.bin>)
- Demo text source for font generation: [zi_chars_demo.txt](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tools/zi_chars_demo.txt>)

### Local tooling

- Font helper executable: [ZiCli.exe](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tools/ZiCli/bin/Release/ZiCli.exe>)
- Font helper source: [Program.cs](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tools/ZiCli/Program.cs>)
- Python font integration: [font_toolchain.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/font_toolchain.py>)
- Python TFT uploader: [tft_download.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_download.py>)
- Python TFT inspector: [tft_toolchain.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_toolchain.py>)
- Python TFT font packer: [tft_font_pack.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_font_pack.py>)
- Reference parsed TFT sample: [tft_reference_nextion43_18may.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tft_reference_nextion43_18may.json>)
- Experimental forced-conversion TFT, not flashed: [build_experimental_hsv_to_tjc8048x543.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/build_experimental_hsv_to_tjc8048x543.tft>)
- Official compiled target TFT, flashed and verified: [official_lcd_test_TJC8048X543_011_20260504.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/official_lcd_test_TJC8048X543_011_20260504.tft>)
- Official target TFT inspection: [official_lcd_test_TJC8048X543_011_20260504.inspect.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/official_lcd_test_TJC8048X543_011_20260504.inspect.json>)
- Extracted `USART HMI.exe` embedded PE files: [embedded_pe](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/embedded_pe>)
- XOR-decoded `ACTR.dll` container: [ACTR_xor09.bin](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/ACTR_xor09.bin>)
- Extracted `ACTR.dll` entries: [actr_entries](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/actr_entries>)

## Commands That Work Now

### Build local font helper

```powershell
python -m usarthmi font build-zicli
```

### Generate `.zi` from scene text

```powershell
python -m usarthmi font from-scene `
  --scene examples\menu_demo\scene.json `
  --out .\build_font_scene.zi `
  --font-file C:\Windows\Fonts\simsun.ttc `
  --name SimSun32scene `
  --height 32 `
  --font-size 32
```

### Replace `0.zi` in an HMI file

```powershell
python -m usarthmi font replace-hmi `
  --hmi .\build_menu_demo_v3\output.hmi `
  --zi .\build_font_scene.zi `
  --out .\build_menu_demo_v3\output_font.hmi
```

### Push a runtime scene preview to the real screen

```powershell
python -m usarthmi scene push-preview examples\menu_demo\scene.json --port COM36 --baud 9600 --page page0
```

### Inspect an existing TFT file

```powershell
python -m usarthmi --json tft inspect --file .\github_refs\Gaggiuino_35\Nextion_43\Nextion_43_18MAY2024_0_Deg.tft
```

### Upload the official compiled target TFT

```powershell
python -m usarthmi --json tft upload `
  --file .\official_lcd_test_TJC8048X543_011_20260504.tft `
  --port COM36 `
  --baud 9600 `
  --download-baud 921600 `
  --timeout-ms 8000
```

The uploader now mirrors the official open-source `TFTFileDownload` preparation sequence by default:

- sends `delay=2500`
- waits `1500ms`
- sends an empty command
- sends `whmi-wri filesize,baud,0`
- streams 4096-byte chunks and waits for `0x05` after each chunk

Use `--progress` to print progress to stderr. Use `--prepare-delay-ms 0` to disable the `delay=2500` preparation step.

### Analyze TFT upload chunks

```powershell
python -m usarthmi --json tft plan-upload `
  --file .\official_lcd_test_TJC8048X543_011_20260504.tft `
  --baseline .\official_lcd_test_TJC8048X543_011_20260504.tft `
  --download-baud 921600
```

For the known-good official TFT:

- file size: `11408156`
- upload chunks: `2786`
- theoretical serial-only minimum at `921600 8N1`: about `123.786s`
- all-`FF` chunks: `31`
- all-zero chunks: `16`
- comparing the file against itself reports `2786/2786` identical chunks

### Pack `.zi` files into a TFT-style font run

```powershell
python -m usarthmi --json tft pack-fonts `
  --font .\build_font_demo.zi `
  --font .\build_font_scene.zi `
  --out .\build_tft_font_run.bin
```

## What Is Not Finished Yet

- There is still no real `.tft` compiler in `usarthmi`.
- The serial upload command has now been exercised successfully with a known-good official `.tft` for this exact screen.
- The generated `.HMI` files are not yet equivalent to a fully official `USART HMI` build product.
- Static image resource packing into final `.HMI/.TFT` is still incomplete.
- The official `.tft` generated by `USART HMI` has been flashed and should persist after power cycle; what is still missing is a self-generated `.tft` from the `usarthmi` toolchain.
- The local `TFTTool` model database contains `TJC8048X543_011`, but the real screen handshake reports `TJC8048X543_011C`, so the suffix difference still needs to be explained or normalized before a fully confident generator/patcher path exists.
- Current `TFT` progress is strongest on the font segment; page/object/picture/resource sections are still not emitted by our own builder.
- A forced-converted same-resolution sample TFT was generated from `HSV Test.tft` to target `TJC8048X543_011`, but it was not flashed because the source content still reports `model_series=0` (T0), while `TJC8048X543` is X5 (`model_series=3`). It is useful as a header/checksum experiment, not as a safe screen payload.

## New Reverse Engineering Notes

- `ACTR.dll` is not a normal PE file. XORing the whole file with `0x09` reveals a 64-byte-record container.
- The decoded container includes these core entries:
  - `HMIFORM.dll`
  - `TFTEDIT.dll`
  - `TFTRUN.dll`
  - `Tcode.dll`
  - `hmitype.dll`
- The bundled `AppDllPass.dll` was extracted from `USART HMI.exe` and exports:
  - `AppDllPass_Decode`
  - `AppDllPass_Encode`
- Applying `AppDllPass_Decode` directly to the extracted entries does not yet produce normal PE headers, so there is at least one more loader/decode step.
- The real panel reports `mcu_code=10501` in `connect`.
- Official install file `3.cc` starts with little-endian code `10501`, and its payload size field matches `len(file)-8`. This strongly indicates `3.cc` is the matching static MCU/code block for the current panel family.
- The official wiki now provides `TFTFileDownload` binaries and C# source. Downloaded copies are kept locally:
  - [TFTFileDownload_0.zip](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/external/TFTFileDownload_0.zip>)
  - [TFTFileDownload_1.zip](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/external/TFTFileDownload_1.zip>)
  - [MainFrame.cs](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/external/TFTFileDownload_source/TFTFileDownLoad/TFTFileDownload/MainFrame.cs>)
- The open-source `TFTFileDownload` implementation does not contain a sparse/incremental protocol. It uses the same public protocol:
  - optional scan/connect
  - `delay=2500`
  - empty command
  - `whmi-wri filesize,baud,0`
  - 4096-byte chunks
  - wait for single-byte `0x05` after command and each chunk
- The public wiki page [HMI download protocol](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/hmi_download_protocol.html>) also documents only full-stream `whmi-wri`.
- Therefore the official editor's "same part not downloaded/written" behavior is not exposed by the public TFT downloader source. It is likely either:
  - inside the closed `USART HMI` editor download path, or
  - inside the screen bootloader/flash layer as "receive full stream but skip flash erase/write for unchanged blocks".

## Flash Verification 2026-05-04

- Official output path supplied by user:
  - `C:\Users\SinYu\AppData\Roaming\USART HMI\work\a-20265415630280\output\lcd_test.tft`
- The official TFT inspected as:
  - `model=TJC8048X543_011`
  - `model_series=3`
  - `lcd_resolution_x=800`
  - `lcd_resolution_y=480`
  - `editor_version=tjc-1.67.6`
  - `file_size=11408156`
- The file was uploaded successfully over `COM36`:
  - initial baud: `9600`
  - download baud: `921600`
  - chunks sent: `2786`
- Post-flash serial verification passed:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get dim` returned `100`
  - `get t0.txt` returned `nihao`
  - `get b0.txt` returned `ceshi`
  - `get p0.pic` returned `0`

## Chinese / English Font Baseline 2026-05-05

- Added a practical 800x480 `page0` font baseline under:
  - [ui_cn_en_32](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/font_baselines/ui_cn_en_32>)
- The verified scene contains:
  - `主菜单  UI FONT 32`
  - `开始  设置  系统  返回`
  - `状态: 正常  温度: 36.5C`
  - `确认 / 取消 / 保存 / 运行`
  - `中文英文混排 OK 123 ABC xyz`
- `ZiCli` now has `--full-codepage`, exposed through:
  - `python -m usarthmi font generate-zi --full-codepage`
- A sparse GB2312 subset font was tested first:
  - [UiCNEN32GB.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/font_baselines/ui_cn_en_32/UiCNEN32GB.zi>)
  - size about `29.6KB`
  - result: loaded by the panel, but Chinese rendered as repeated wrong glyphs
  - conclusion: GB2312 subset mode is not a safe baseline on this panel yet
- The working baseline is full GB2312:
  - [UiCNEN32GBFull.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/font_baselines/ui_cn_en_32/UiCNEN32GBFull.zi>)
  - `8273` characters
  - `.zi` payload about `2.1MB`
  - font height `32`
  - codepage `gb2312`
- The flashed TFT is:
  - [output_gb2312_full.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/font_baselines/ui_cn_en_32/build_gb2312_full/output_gb2312_full.tft>)
- Upload verification:
  - `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11414492`
  - chunks sent `2787`
  - elapsed about `209s`
- Serial verification after flashing:
  - `sendme` returned page `0`
  - `get title.font` returned `0`
  - `get title.txt` raw bytes were `D6 F7 B2 CB B5 A5 20 20 55 49 20 46 4F 4E 54 20 33 32`
  - protocol parser now decodes `0x70` string returns as `gbk`, so JSON `value` shows `主菜单  UI FONT 32`
- Visual verification:
  - [ui_cn_en_32_gb2312_full_cam1.jpg](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/font_baselines/ui_cn_en_32/captures/ui_cn_en_32_gb2312_full_cam1.jpg>)
- Added `.zi`-backed preview rendering:
  - new parser/renderer: [zi_font.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/zi_font.py>)
  - `hmi preview-pa`, `hmi preview`, and `scene preview` accept `--font 0=path\to\font.zi`
  - `hmi preview` also auto-loads embedded `N.zi` entries from the HMI container
  - generated local preview: [preview_zi_font.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/font_baselines/ui_cn_en_32/preview_zi_font.png>)
  - generated scene preview: [scene_preview_zi_font.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/font_baselines/ui_cn_en_32/scene_preview_zi_font.png>)

## TFT Object Tail Reverse Probe 2026-05-04

- Added a repeatable CLI probe:
  - `python -m usarthmi --json tft reverse-tail --file official_lcd_test_TJC8048X543_011_20260504.tft --hmi-pa hmi_extract_current\0.pa --context-bytes 32`
- The current evidence JSON is saved at:
  - [official_lcd_test_tft_tail_reverse.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/official_lcd_test_tft_tail_reverse.json>)
- The official TFT object region is:
  - start `0xAE0000`
  - end `0xAE10DE`
  - size `0x10DE`
- The parsed `.HMI` `0.pa` objects align uniquely with the compiled TFT object records:
  - `page0`: header `0xAE01EB`, body `0xAE0207`, coords `0xAE0213`, value offset `0x20`, record length `0x40`
  - `t0`: header `0xAE022B`, body `0xAE0247`, coords `0xAE0253`, value offset `0x60`, record length `0x54`, text `nihao` at `0xAE0313`
  - `b0`: header `0xAE027F`, body `0xAE029B`, coords `0xAE02A7`, value offset `0xB4`, record length `0x54`, text `ceshi` at `0xAE031F`
  - `p0`: header `0xAE02D3`, body `0xAE02EF`, coords `0xAE02FB`, value offset `0x108`, record length `0x40`
- In each object record:
  - `coord_offset - 0x0C` is the body start.
  - `body_start - 0x1C` is the object header.
  - header byte 0 matches the HMI object type (`y/t/b/p`).
  - header byte 1 matches the HMI object id.
  - body dword 0 matches the compiled object value offset.
- A u32 value-offset table matching all four body dword-0 values exists at `0xAE01DB`:
  - `0x20, 0x60, 0xB4, 0x108`
- Text objects currently share a compiled text-pointer bias:
  - bias `0x1CB`
  - `t0` body `+0x2C` stores pointer `0x148`; `0x148 + 0x1CB = 0x313`, which is `nihao`
  - `b0` body `+0x30` stores pointer `0x154`; `0x154 + 0x1CB = 0x31F`, which is `ceshi`
- Resource matching from the extracted `.HMI` directory shows:
  - `0.i` is embedded byte-for-byte in the official TFT at `0x80F14`
  - `0.zi` is embedded byte-for-byte in the official TFT at `0x81BD6`
  - `Program.s`, `0.pa`, and `0.is` are not embedded as raw files
- Static resource matching from the installed `USART HMI` directory shows:
  - `input.bin` is embedded byte-for-byte at `0x20090`
  - `3.cc` is embedded byte-for-byte at `0x24532`
  - `cdx.dll` is embedded byte-for-byte at `0x7F4DA`
- These sections are contiguous:
  - `0x20000..0x20090`: 0x90-byte resource directory/header
  - `0x20090..0x24532`: `input.bin`
  - `0x24532..0x7F4DA`: `3.cc`
  - `0x7F4DA..0x80F14`: `cdx.dll`
  - `0x80F14..0x81BD6`: HMI `0.i`
  - `0x81BD6..0xACF82A`: HMI `0.zi`
  - `0xACF82A..0xAE0000`: zero padding/alignment before the object tail
- The 0x90-byte resource directory stores relative offsets from `0x20000`:
  - word 0/1: `input.bin` offset `0x90`, size `0x44A2`
  - word 3/4: `3.cc` offset `0x4532`, size `0x5AFA8`
  - word 6/7: `cdx.dll` offset `0x5F4DA`, size `0x1A3A`
  - word 21/22: `0.i` offset `0x60F14`, size `0xCC2`
  - word 24/25: `0.zi` offset `0x61BD6`, size `0xA4DC54`
- This means first-pass picture and font transfer can likely reuse the HMI resource blobs directly, while page/object data must be compiled into the object tail format.
- This is now the strongest known path toward a TFT writer/patcher: generate or patch the object tail from `.pa` semantics, then handle picture/font/resource tables separately.

## Case Diff Reverse Probe 2026-05-04

- User-provided one-variable official compiler samples are stored under:
  - `C:\Users\SinYu\Desktop\case_for_codex`
- Added a repeatable comparison CLI:
  - `python -m usarthmi --json tft compare-cases --case-root "C:\Users\SinYu\Desktop\case_for_codex" --out reverse_usarthmi\case_compare --install-dir "C:\Program Files (x86)\USART HMI"`
- The summary is saved at:
  - [summary.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/case_compare/summary.json>)
- `case_01_t0_text_hello`:
  - same file size as baseline
  - changes only `0xAE0313..` string pool text plus the final 4-byte word
- `case_02_t0_x_plus10`:
  - same file size as baseline
  - changes `t0` primary coordinates at relative `0x253`
  - also changes mirrored/render coordinates at relative `0x11A0`
  - changes the final 4-byte word
- `case_03_b0_text_test`:
  - same file size as baseline
  - changes `b0` string pool text plus the final 4-byte word
- The compiled tail must be considered `unknown_objects_address..EOF`, not only `unknown_objects_address..pictures_address` from TFTTool:
  - baseline tail size `0x131C`, while TFTTool `pictures_address` cuts at `0x10DE`
  - the post-`pictures_address` section contains mirrored coordinates/render metadata and the final 4-byte word
- Coordinate matches are now two-per-object:
  - baseline `page0`: `0x213`, `0x1116`
  - baseline `t0`: `0x253`, `0x11A0`
  - baseline `b0`: `0x2A7`, `0x122A`
  - baseline `p0`: `0x2FB`, `0x12B4`
- Adding one object changes the value-offset table:
  - 4-object baseline: `0x20, 0x60, 0xB4, 0x108`
  - 5-object cases: `0x24, 0x64, 0xB8, 0x10C, 0x148`
- Adding duplicate text does not deduplicate the string pool:
  - `case_04_add_text` stores `nihao`, `ceshi`, `nihao`
  - `case_05_add_button` stores `nihao`, `ceshi`, `ceshi`
- Text pointer bias remains stable in 5-object cases:
  - bias `0x1EB`
  - `t0` pointer body `+0x2C`
  - `b0/b1` pointer body `+0x30`
- Final 4-byte checksum is now decoded:
  - implemented in [tft_checksum.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_checksum.py>)
  - X5 / model series 3 uses the TFTTool word-based CRC variant
  - the checksum is then XORed with bytes `0x03`, `0x2E`, and `0x3C` from the TFT header/body
  - verified against all 7 user-provided official TFT samples

## Experimental TFT Writer V0 2026-05-04

- Added a conservative same-layout TFT patcher:
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - CLI: `python -m usarthmi --json tft patch-basic --baseline-tft <official-baseline.tft> --baseline-pa <baseline-0.pa> --target-pa <target-0.pa> --out <candidate.tft>`
- Current V0 scope:
  - object count/type/order must be unchanged
  - patches all matching coordinate sequences in the compiled tail
  - patches fixed-size text slots using `txt_maxl + 2` bytes
  - recomputes the final 4-byte TFT checksum by default
- Validation against user-provided official cases:
  - `case_01_t0_text_hello`: generated TFT equals official target byte-for-byte
  - `case_02_t0_x_plus10`: generated TFT equals official target byte-for-byte
  - `case_03_b0_text_test`: generated TFT equals official target byte-for-byte
- Added regression test:
  - [test_tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_tft_patch.py>)
- This proves the currently reversed fields are sufficient to generate real same-layout TFT content. The next blocker is no longer checksum; it is generating new-object tails rather than only patching same-layout files.

## Live Flash Verification: nihao -> buhao 2026-05-04

- Built a same-layout patched target:
  - target `.pa`: [0_buhao.pa](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_buhao_patch/0_buhao.pa>)
  - generated `.tft`: [lcd_test_buhao.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_buhao_patch/lcd_test_buhao.tft>)
- Patch summary:
  - file size `11408156`
  - changed `t0.txt` from `nihao` to `buhao`
  - checksum recomputed to `0x7F034D2F`
  - compared with baseline: only string bytes and final checksum differ
- Uploaded to the real screen:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11408156`
  - chunks sent `2786`
  - elapsed `207.359s`
- Post-flash serial verification:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get t0.txt` returned `buhao`
  - `get dim` returned `100`
- This is the first confirmed live-screen proof that a non-official `usarthmi` generated TFT patch can be flashed and run.

## Milestone: First Non-Official TFT Patch Accepted By Screen

- Status: achieved.
- Scope proven:
  - parse official baseline HMI/TFT
  - modify page text through a generated target `0.pa`
  - patch compiled TFT text slots
  - recompute final TFT checksum
  - upload through public `whmi-wri`
  - verify runtime state over serial
- Practical meaning:
  - `usarthmi` can now generate a valid same-layout TFT patch without calling the official GUI compiler.
  - Same-layout edits such as text and coordinates are no longer only theoretical reverse-engineering results; they have been accepted by the real `TJC8048X543_011C` panel.

## Next Target: Full New-Object Object Tail Generation

- New blocker:
  - Generate the complete compiled object tail for added widgets instead of only patching existing same-layout objects.
- Immediate fixtures:
  - `case_04_add_text`
  - `case_05_add_button`
  - `case_06_add_picture`
- Required object-tail pieces to synthesize:
  - event token area growth for the extra object
  - object count and offset table changes
  - primary object records for `t1/b1/p1`
  - string pool growth with duplicate text preserved
  - value-offset table update
  - mirrored/render metadata section after TFTTool `pictures_address`
  - final TFT checksum recomputation
- Target acceptance for the next phase:
  - Generate `case_04_add_text`, `case_05_add_button`, and `case_06_add_picture` from baseline plus target `.pa`.
  - Match the official TFT outputs byte-for-byte.
  - Then flash one added-object TFT to the real screen and verify over serial.

## Current Gap

The remaining blocker is not runtime serial drawing, not font generation, and not `0.zi` replacement.

The blocker is:

`scene/HMI/font state` can be created locally, but it still cannot be compiled into a final `TFT` payload that is known-good for `TJC8048X543_011C`, then flashed and verified on the real panel.

## Recommended Next Step

Continue reverse engineering toward one of these:

1. Build a real `TFT` emitter inside `usarthmi`.
2. Or derive a reusable bridge from a known-good official `.tft` layout and patch it safely.

Until that step is complete, all screen changes remain either:
- runtime-only, or
- local `.HMI` source artifacts not yet proven as flashable screen firmware.

## Milestone: One-Object Add TFT Tail Generation 2026-05-04

- Status: achieved for the current seed and one added `t/b/p` object.
- Implemented:
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - [cli.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/cli.py>)
  - [test_tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_tft_patch.py>)
- New CLI:
  - `python -m usarthmi --json tft patch-add-object --baseline-tft <baseline.tft> --baseline-pa <baseline 0.pa> --target-pa <target 0.pa> --out <out.tft>`
- Proven byte-for-byte against official fixtures:
  - `case_04_add_text`
  - `case_05_add_button`
  - `case_06_add_picture`
- Reverse facts now encoded:
  - event token area grows by one extra down/up event block sequence
  - object hash/index list is regenerated and sorted by recovered object hash
  - primary object block is rebuilt with value-offset table, records, text pointers, and duplicate text slots
  - `attr/usercode` section is rebuilt as `0x24` header plus per-object 24-byte property records
  - mirror section is rebuilt as 16-byte header plus fixed `0x8A` per-object records
  - encrypted Header2 fields, Header1/Header2 CRCs, and final TFT checksum are recomputed
- Command-line verification:
  - generated [case_04_add_text.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/patch_add_object/case_04_add_text.tft>)
  - SHA256 matched the official `case_04_add_text/lcd_test.tft`
  - checksum verified as valid: `0xEA1A9568`
- Current limitation:
  - This is still a current-seed V1 path.
  - It supports adding exactly one object whose type is `t`, `b`, or `p`.
  - Object-name hashes were the next blocker at this point; the algorithm was solved in the later section below.

## Live Flash Verification: Added `t1` Object 2026-05-04

- Flashed generated file:
  - [case_04_add_text.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/patch_add_object/case_04_add_text.tft>)
- Upload result:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11409408`
  - chunks sent `2786`
  - elapsed `208.079s`
  - log: [case_04_upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/patch_add_object/case_04_upload_result.json>)
- Post-flash serial verification:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get t1.txt` returned `nihao`
  - `get t1.x` returned `355`
- Meaning:
  - Added-object tail generation is accepted by the real screen.
  - The new object is not only visible in the binary; it is present in the runtime object table and queryable over serial.

## Reverse Fact: Object Name Hash Algorithm 2026-05-04

- Status: solved and encoded.
- Implemented:
  - [object_hash.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/object_hash.py>)
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - [test_object_hash.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_object_hash.py>)
- Algorithm:
  - encode the page/object name as ASCII
  - right-pad with `00` to 14 bytes
  - run the same non-reflected Nextion/TJC CRC32 variant used by TFTTool `NextionChecksum`
- Known values now generated by formula, no hardcoded fixture map:
  - `page0 -> 0xAC967926`
  - `t0 -> 0xC02992D9`
  - `b0 -> 0xCE1A7436`
  - `p0 -> 0x56156502`
  - `t1 -> 0xB64689A1`
  - `b1 -> 0xB8756F4E`
  - `p1 -> 0x207A7E7A`
- Evidence:
  - The earlier clue `t0^t1 == b0^b1 == p0^p1 == 0x766F1B78` matches the CRC contribution after padding to 14 bytes.
  - Local TJC `case_04_add_text` hash/index block is reconstructed and found in the official TFT.
  - Public `Gaggiuino_35/Nextion_43` HMI/TFT pair reconstructs all 20 page hash/index blocks from `.pa` object names and IDs.
- New CLI:
  - `python -m usarthmi --json tft hash-name t1`
- Test result:
  - `python -m pytest tests\test_object_hash.py -q` -> 4 passed
  - `python -m pytest tests\test_tft_patch.py -q` -> 4 passed
  - `python -m pytest -q` -> 32 passed
- Practical impact:
  - Added-object TFT generation is no longer limited to recovered names `t1/b1/p1`.
  - Arbitrary ASCII object names up to 14 bytes can now be placed into the compiled object hash/index list.
  - A regression test renames the added object to `note1` and verifies the generated TFT checksum remains valid.

## Live Flash Verification: Arbitrary Object Name `note1` 2026-05-04

- Status: achieved on the real `COM36` panel.
- Generated artifacts:
  - target page: [0_note1.pa](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_note1_patch/0_note1.pa>)
  - generated TFT: [lcd_test_note1.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_note1_patch/lcd_test_note1.tft>)
  - patch/checksum record: [patch_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_note1_patch/patch_result.json>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_note1_patch/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_note1_patch/verify_after_upload.json>)
- Build facts:
  - added object name: `note1`
  - type: `t`
  - object id: `4`
  - generated hash: `0x2611D5E4`
  - TFT checksum valid: `0xDAEFBDE3`
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11409408`
  - chunks sent `2786`
  - elapsed `207.656s`
- Post-flash serial verification:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get note1.txt` returned `note1`
  - `get note1.x` returned `355`
  - `get note1.id` returned `4`
  - `get t1.txt` returned `0x1A invalid_reference`
- Meaning:
  - The recovered object-name hash algorithm is not only byte-matching fixtures; it is accepted by the real screen runtime.
  - The compiled object lookup table now works for a new arbitrary object name, not just fixture-derived names.

## Preview Milestone: HMI/PA Page Preview 2026-05-04

- Status: implemented.
- Implemented:
  - [preview.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/preview.py>)
  - [cli.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/cli.py>)
  - [test_scene_layout.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_scene_layout.py>)
- New CLI:
  - `python -m usarthmi --json hmi preview --hmi <file.HMI> --out preview.png`
  - `python -m usarthmi --json hmi preview-pa --pa <0.pa> --assets-dir <extract_dir> --out preview.png`
- Rendered preview artifacts:
  - [preview_note1_with_assets.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_note1_patch/preview_note1_with_assets.png>)
  - [preview_seed_hmi_with_assets.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_note1_patch/preview_seed_hmi_with_assets.png>)
- Supported in this first preview pass:
  - page background from `bco`
  - absolute coordinates from `.pa`
  - text objects
  - button objects
  - picture objects
  - number-like objects
  - yellow object-name labels similar to the official editor
  - embedded `*.i` / `*.is` JPEG/PNG picture resources from HMI/extract directories
- Current limitation:
  - This is a practical visual preview, not a pixel-perfect official renderer.
  - Font metrics and some advanced widget styles are approximate.

## Milestone: Multiple Appended Objects In One TFT 2026-05-04

- Status: achieved and live-flashed.
- Implemented:
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - [cli.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/cli.py>)
  - [test_tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_tft_patch.py>)
- New behavior:
  - `patch-add-object` now accepts one or more appended `t/b/p` objects.
  - Existing baseline objects must still remain unchanged and first in the target page.
  - Target object names and IDs are validated as unique.
  - Object IDs are validated to fit the one-byte compiled record field.
- Generated artifacts:
  - target page: [0_multi.pa](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_multi_patch/0_multi.pa>)
  - preview: [preview_multi.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_multi_patch/preview_multi.png>)
  - generated TFT: [lcd_test_multi.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_multi_patch/lcd_test_multi.tft>)
  - patch/checksum record: [patch_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_multi_patch/patch_result.json>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_multi_patch/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_multi_patch/verify_after_upload.json>)
- Build facts:
  - object count: `7`
  - added objects: `note1` (`t`, id `4`), `btn1` (`b`, id `5`), `pic1` (`p`, id `6`)
  - file size: `11411592`
  - TFT checksum valid: `0x62C3E6A1`
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11411592`
  - chunks sent `2787`
  - elapsed `208.468s`
- Post-flash serial verification:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get note1.txt` returned `note1`
  - `get note1.id` returned `4`
  - `get note1.x` returned `355`
  - `get btn1.txt` returned `BTN1`
  - `get btn1.id` returned `5`
  - `get btn1.x` returned `192`
  - `get pic1.pic` returned `0`
  - `get pic1.id` returned `6`
  - `get pic1.x` returned `579`
- Meaning:
  - The object-tail generator now handles multiple appended compiled records, user/attribute records, mirror records, and hash entries in one build.
  - This enables the next step: generating richer menu pages from scene/HMI authoring instead of one-off object fixtures.

## Milestone: Scene Builder Routed To Multi-Object TFT Generator 2026-05-04

- Status: implemented and live-flashed.
- Implemented:
  - [editor.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/editor.py>)
  - [cli.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/cli.py>)
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>)
- New CLI path:
  - `python -m usarthmi --json tft build --scene reverse_usarthmi\live_scene_build\scene_multi.json --seed D:\MySTM32\H723ZGT6\Program\ISP_Test\lcd_test.HMI --baseline-tft C:\Users\SinYu\Desktop\case_for_codex\case_00_baseline\lcd_test.tft --out reverse_usarthmi\live_scene_build`
- Generated artifacts:
  - scene: [scene_multi.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/scene_multi.json>)
  - normalized scene: [scene.normalized.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/scene.normalized.json>)
  - target page: [target_0.pa](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/target_0.pa>)
  - preview: [preview_target_pa.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/preview_target_pa.png>)
  - generated HMI: [output.hmi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/output.hmi>)
  - generated TFT: [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/output.tft>)
  - manifest: [manifest.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/manifest.json>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_scene_build/verify_after_upload.json>)
- Build facts:
  - object count: `7`
  - added objects: `note1` (`t`, id `4`), `btn1` (`b`, id `5`), `pic1` (`p`, id `6`)
  - file size: `11411584`
  - TFT checksum valid: `0x7734E28E`
  - object-tail padding is inserted before the final TFT checksum when the scene-generated tail is not naturally 4-byte aligned.
- Validation facts:
  - `python -m pytest tests\test_editor_tft_build.py -q` -> 2 passed
  - `python -m pytest tests\test_tft_patch.py -q` -> 5 passed, 13 subtests passed
  - `python -m pytest -q` -> 36 passed, 20 subtests passed
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11411584`
  - chunks sent `2787`
  - elapsed `207.422s`
- Post-flash serial verification:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get note1.txt` returned `note1`
  - `get note1.id` returned `4`
  - `get btn1.txt` returned `BTN1`
  - `get btn1.id` returned `5`
  - `get pic1.pic` returned `0`
  - `get pic1.id` returned `6`
- Current boundary:
  - Scene-to-TFT supports appended `text/button/image` objects for the current seed layout.
  - Image widgets may reference picture IDs already present in the seed, such as `pic=0`.
  - Packing brand-new image resources into TFT is still rejected explicitly instead of producing a fake or broken file.

## Reverse Sample: Imported JPG Resource 2026-05-04

- Status: sample captured and initial layout recovered.
- User-provided case folders:
  - source JPG: [case_07_image_source_png_jpg](</C:/Users/SinYu/Desktop/case_for_codex/case_07_image_source_png_jpg>)
  - official HMI: [case_08_hmi_with_imported_image](</C:/Users/SinYu/Desktop/case_for_codex/case_08_hmi_with_imported_image>)
  - official TFT: [case_09_tft_with_imported_image](</C:/Users/SinYu/Desktop/case_for_codex/case_09_tft_with_imported_image>)
  - compare workspace: [case_11_image_resource_compare_work](</C:/Users/SinYu/Desktop/case_for_codex/case_11_image_resource_compare_work>)
- Generated compare artifacts:
  - HMI extract: [hmi_extract](</C:/Users/SinYu/Desktop/case_for_codex/case_11_image_resource_compare_work/hmi_extract>)
  - preview: [preview_hmi_with_imported_image.png](</C:/Users/SinYu/Desktop/case_for_codex/case_11_image_resource_compare_work/preview_hmi_with_imported_image.png>)
  - notes: [README_image_resource_findings.md](</C:/Users/SinYu/Desktop/case_for_codex/case_11_image_resource_compare_work/README_image_resource_findings.md>)
  - probes: [image_resource_probe.json](</C:/Users/SinYu/Desktop/case_for_codex/case_11_image_resource_compare_work/image_resource_probe.json>), [embedded_jpeg_probe.json](</C:/Users/SinYu/Desktop/case_for_codex/case_11_image_resource_compare_work/embedded_jpeg_probe.json>)
- HMI facts:
  - new entries: `1.is` (`73406` bytes) and `1.i` (`106378` bytes)
  - `1.is` is a 27-byte resource header followed by the original JPG exactly
  - `1.i` is a 44-byte compiled-resource header followed by a recompressed/padded JPG
  - `0.pa` adds object `p1`, `pic=1`, box `162,87,489,342`
- TFT facts:
  - official image TFT size: `11540132`
  - baseline TFT size: `11408156`
  - delta: `131976`
  - `pic=1` JPEG payload is at TFT offset `0x81C02`, size `106334`, dimensions `496x352`
  - the TFT payload exactly matches `1.i` after its 44-byte header, not the original JPG from `1.is`
- Layout hypothesis:
  - TFT picture resource section begins with one 24-byte index record per picture
  - each picture then has a 20-byte image block header followed by the JPEG payload
  - compiled width/height are padded to multiples of 16

## Milestone: Independent TFT Picture Resource Packer 2026-05-04

- Status: implemented and live-flashed.
- Implemented:
  - [tft_images.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_images.py>)
  - [editor.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/editor.py>)
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>)
- New behavior:
  - Scene `image` widgets with `resources.asset` are assigned new sequential TFT `pic` ids after seed resources.
  - PNG/JPG inputs are padded to 16-pixel boundaries and JPEG-encoded into the TFT picture resource section.
  - Historical note: this first implementation expanded the resource area and moved the object section.
  - This was later proven different from official USART HMI output; see the 2026-05-05 fixed-region picture packer milestone below.
  - Header1 file size/resource size/resource CRC/header CRC, Header2 shifted addresses/header CRC, and final TFT checksum were recomputed.
  - The resulting resource-expanded TFT was used as the seed for the existing appended-object tail generator.
- Generated artifacts:
  - scene: [scene_image.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_pack/scene_image.json>)
  - resource seed TFT: [resource_seed.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_pack/resource_seed.tft>)
  - output TFT: [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_pack/output.tft>)
  - manifest: [manifest.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_pack/manifest.json>)
  - preview: [preview_target_pa.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_pack/preview_target_pa.png>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_pack/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_pack/verify_after_upload.json>)
- Build facts:
  - source image: `489x342`
  - compiled image: `496x352`
  - assigned picture id: `1`
  - added object: `photo1` (`p`, id `4`, `pic=1`, box `162,87,489,342`)
  - output TFT size: `11540132`
  - object start shifted from `0xAE0000` to `0xB00000`; this is now a superseded behavior, not the official-compatible path.
  - new JPEG payload offset: `0x81C02`
  - TFT checksum valid: `0x464E199A`
- Validation facts:
  - `python -m pytest tests\test_editor_tft_build.py -q` -> 3 passed
  - `python -m pytest tests\test_tft_patch.py -q` -> 5 passed, 13 subtests passed
  - `python -m pytest -q` -> 37 passed, 20 subtests passed
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11540132`
  - chunks sent `2818`
  - elapsed `209.016s`
- Post-flash serial verification:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get photo1.pic` returned `1`
  - `get photo1.id` returned `4`
  - `get photo1.x` returned `162`
  - `get photo1.w` returned `489`
  - `get photo1.h` returned `342`
- Current boundary:
  - New image resources are proven for appended picture/image objects.
  - Generated `output.hmi` does not yet contain the added `*.i/*.is` HMI resource entries.
  - New image-button support was added in the next milestone below; it still needs official fixture comparison.

## Milestone: Inferred Multi-State Image Button TFT Path 2026-05-04

- Status: implemented and live-flashed as an inferred path.
- Implemented:
  - [editor.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/editor.py>)
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - [tft_images.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_images.py>)
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>)
- Inference:
  - Button `sta=1` exposes the two compiled background slots as `bco/bco2`.
  - Button image mode likely uses the same two compiled slots with `sta=2`.
  - The authoring layer maps `normal -> pic`, `pressed -> pic2`, but the live runtime currently reads those two compiled slots back as `bco/bco2`.
- Generated artifacts:
  - scene: [scene_image_button.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/scene_image_button.json>)
  - resource seed TFT: [resource_seed.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/resource_seed.tft>)
  - output TFT: [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/output.tft>)
  - preview: [preview.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/preview.png>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/verify_after_upload.json>)
  - attribute sweep: [verify_attrs_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/verify_attrs_after_upload.json>)
- Build facts:
  - added object: `playbtn` (`b`, id `4`, box `320,330,160,96`)
  - packed normal image: picture id `1`, source `play.png`
  - packed pressed image: picture id `2`, source `play_pressed.png`
  - output TFT size: `11540500`
  - TFT checksum valid: `0xF9CDB181`
- Validation facts:
  - `python -m pytest tests\test_editor_tft_build.py -q` -> 4 passed
  - `python -m pytest tests\test_tft_patch.py -q` -> 5 passed, 13 subtests passed
  - `python -m pytest -q` -> 39 passed, 20 subtests passed
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11540500`
  - chunks sent `2818`
  - elapsed `213.579s`
- Post-flash serial verification:
  - `connect` returned `TJC8048X543_011C`
  - `sendme` returned page `0`
  - `get playbtn.id` returned `4`
  - `get playbtn.sta` returned `2`
  - `get playbtn.x` returned `320`
  - `get playbtn.w` returned `160`
  - `get playbtn.h` returned `96`
  - `get playbtn.txt` returned `PLAY`
  - `get playbtn.bco` returned `1`
  - `get playbtn.bco2` returned `2`
  - `get playbtn.pic`, `get playbtn.pic2`, `get playbtn.picc`, and `get playbtn.picc2` returned `0x1A`
  - `click playbtn down/up` sent successfully with no error response
- Current boundary:
  - The screen runtime accepts the generated object and two packed image IDs.
  - Manual visual confirmation is still needed to decide whether this is fully correct for the pressed-state image.
  - An official image-button fixture should still be captured later to verify the exact HMI/TFT byte layout.

## Milestone: Clean Seed Objects Mode 2026-05-04

- Status: implemented and live-flashed.
- Purpose:
  - The current TFT writer still keeps the seed page's original `t0/b0/p0` records for compatibility.
  - `project.clean_seed_objects=true` moves those seed objects offscreen instead of deleting them, so the generated scene is visually clean while the current seed-based tail compiler remains safe.
- Implemented:
  - [editor.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/editor.py>)
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>)
  - [scene_image_button.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack/scene_image_button.json>)
- Generated artifacts:
  - clean build directory: [live_image_button_pack_clean](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack_clean>)
  - output TFT: [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack_clean/output.tft>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack_clean/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_button_pack_clean/verify_after_upload.json>)
- Build facts:
  - output TFT size: `11540500`
  - TFT checksum valid: `0x366E46B0`
  - old seed objects are retained but moved to `x=832,y=512,w=1,h=1`
  - `playbtn` remains at `x=320,y=330,w=160,h=96`
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11540500`
  - chunks sent `2818`
  - elapsed `213.672s`
- Post-flash serial verification:
  - `sendme` returned page `0`
  - `get t0.x/y/w/h` returned `832/512/1/1`
  - `get b0.x/y/w/h` returned `832/512/1/1`
  - `get p0.x/y/w/h` returned `832/512/1/1`
  - `get playbtn.x/y/w/h` returned `320/330/160/96`
  - `get playbtn.sta` returned `2`
  - `get playbtn.bco` returned `1`
  - `get playbtn.bco2` returned `2`
- Current boundary:
  - This is a safe visual clean mode, not true object deletion.
  - A later full-page compiler should support deleting seed objects entirely.

## Milestone: Custom TFT Font Replacement 2026-05-04

- Status: implemented and live-flashed.
- Implemented:
  - [tft_fonts.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_fonts.py>)
  - [cli.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/cli.py>)
  - [test_tft_fonts.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_tft_fonts.py>)
- New CLI:
  - `python -m usarthmi --json tft patch-font --baseline-tft <input.tft> --font <custom.zi> --out <output.tft>`
- Safe strategy:
  - Locate the first embedded `.zi` magic inside the TFT resource area.
  - Replace it in place with a same-or-smaller generated `.zi`.
  - Zero-fill the remaining old font span.
  - Preserve TFT file size and all Header2 section addresses.
  - Recompute resource CRC, Header1 CRC, and final TFT checksum.
- Generated artifacts:
  - scene: [scene_custom_font.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_custom_font/scene_custom_font.json>)
  - generated font: [Hupo48ASCII.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_custom_font/Hupo48ASCII.zi>)
  - base build: [build_base](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_custom_font/build_base>)
  - final TFT: [output_custom_font.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_custom_font/output_custom_font.tft>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_custom_font/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_custom_font/verify_after_upload.json>)
- Font facts:
  - source font file: `C:\Windows\Fonts\STHUPO.TTF`
  - generated `.zi` name: `Hupo48ASCII`
  - codepage: `utf-8`
  - char height: `48`
  - char count: `95`
  - generated `.zi` size: `14681`
  - replaced TFT font span: `0x84429..0xAD207D`, old span `10804308`
- Build facts:
  - visible text object: `fontmsg`, text `FONT TEST 123`, font `0`
  - image button remains `playbtn`
  - clean seed objects remain offscreen
  - final TFT size: `11541756`
  - final TFT checksum valid: `0x9AFAC92B`
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11541756`
  - chunks sent `2818`
  - elapsed `214.343s`
- Post-flash serial verification:
  - `sendme` returned page `0`
  - `get fontmsg.id` returned `4`
  - `get fontmsg.txt` returned `FONT TEST 123`
  - `get fontmsg.x/y/w/h` returned `120/96/560/88`
  - `get fontmsg.font` returned `0`
  - `get playbtn.id` returned `5`
  - `get playbtn.sta` returned `2`
  - `get playbtn.bco/bco2` returned `1/2`
  - `get t0.x`, `get b0.x`, and `get p0.x` returned `832`, confirming clean mode remains active.
- Current boundary:
  - Serial object lookup validated the custom-font TFT structure, but the photographed panel did not visibly show `FONT TEST 123`; only the `PLAY` button and a small black artifact were visible.
  - The custom `.zi` replacement path is therefore not visually proven yet.
  - Follow-up diagnosis should separate text-object compilation from `.zi` resource compatibility.
  - Larger font resources still need the resource-shifting path.
  - The current TFT text compiler still emits ASCII text bytes; Chinese text in TFT string pools remains a separate follow-up.

## Milestone: Original-Font Text Object Diagnostic 2026-05-04

- Status: implemented and live-flashed.
- Purpose:
  - Verify the generated text object itself using the stock embedded font, before changing the `.zi` resource.
  - Avoid confusing text object record bugs with custom font rendering bugs.
- Implemented:
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>) now patches text-object primary record metadata for `t` objects.
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>) now verifies generated text records keep `style=1` and `txt_maxl=13` for `FONT TEST 123`.
- Text record fields now patched for `t` objects:
  - `sta`
  - `style`
  - `borderc`
  - `font`
  - solid/image background slot
  - `pco`
  - `xcen`
  - `ycen`
  - `pw`
  - `txt_maxl`
- Important note:
  - The byte that looked like `borderw` is intentionally left as the official template value; exact official TFT reproduction showed that USART HMI 1.67.6 leaves it zero in the primary record.
- Generated artifacts:
  - scene: [scene_original_font_text.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_original_font_text/scene_original_font_text.json>)
  - build directory: [live_original_font_text/build](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_original_font_text/build>)
  - preview: [preview.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_original_font_text/build/preview.png>)
  - output TFT: [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_original_font_text/build/output.tft>)
  - upload record: [upload_result.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_original_font_text/build/upload_result.json>)
  - runtime verification: [verify_after_upload.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_original_font_text/build/verify_after_upload.json>)
- Build facts:
  - `fontmsg` uses stock font id `0`.
  - `fontmsg` is at `x=80,y=70,w=640,h=120`.
  - `fontmsg.txt` is `FONT TEST 123`.
  - `fontmsg.bco` is `65504`, a yellow diagnostic background.
  - output TFT size: `11541756`
  - TFT checksum valid: `0x11B0BBBB`
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11541756`
  - chunks sent `2818`
  - elapsed `212.922s`
- Post-flash serial verification:
  - `sendme` returned page `0`
  - `get fontmsg.txt` returned `FONT TEST 123`
  - `get fontmsg.txt_maxl` returned `13`
  - `get fontmsg.bco` returned `65504`
  - `get fontmsg.pco` returned `0`
  - `get fontmsg.style` returned `1`
  - `get fontmsg.font` returned `0`
  - `get fontmsg.x/y` returned `80/70`
  - `get playbtn.bco/bco2` returned `1/2`

## Milestone: Official Cases 12-15 Text/Image References 2026-05-05

- Status: captured and analyzed.
- User supplied official USART HMI GUI outputs under:
  - [case_12_text_yellow_font0](</C:/Users/SinYu/Desktop/case_for_codex/case_12_text_yellow_font0>)
  - [case_13_image_button_only](</C:/Users/SinYu/Desktop/case_for_codex/case_13_image_button_only>)
  - [case_14_text_plus_image_button](</C:/Users/SinYu/Desktop/case_for_codex/case_14_text_plus_image_button>)
  - [case_15_text_after_import_images](</C:/Users/SinYu/Desktop/case_for_codex/case_15_text_after_import_images>)
- Visual facts from official screenshots:
  - `case_12` displays yellow `fontmsg` text with `newtxt`.
  - `case_13` displays the two-state `playbtn`.
  - `case_14` displays both `fontmsg` and `playbtn` together.
- Parsed `.pa` facts:
  - Official `fontmsg` uses `style=0`, not `style=1`.
  - Official `fontmsg` keeps `txt_maxl=10`.
  - Official `fontmsg.txt` is `newtxt`.
  - Official `fontmsg.bco=65504`, `pco=0`, `font=0`.
  - Official `playbtn` uses `sta=2`, `style=4`, `pic=1`, `pic2=2`.
- Compiler fix:
  - [editor.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/editor.py>) now prefers the current seed page's own `t0`/`b0` as text/button prototypes instead of keyboard template widgets.
  - Short text now preserves the seed/default `txt_maxl=10` instead of shrinking it to the exact text length.
- Verification:
  - A scene containing only `fontmsg` with `newtxt` now builds an `output.tft` that is byte-for-byte identical to official `case_12` `lcd_test.tft`.
  - Test added in [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>).
  - Validation command passed: `7 passed, 13 subtests passed`.
- New resource-pack insight:
  - Official image cases keep `unknown_objects_address=0xAE0000`.
  - Official image cases keep Header1 `ressource_files_size=11272192`.
  - Official image import shifts `fonts_address` from `0xACF82A` to `0xAD164B`.
  - Our earlier image packer moved the object section to `0xB00000`; this is now known to be the wrong direction for matching official output.

## Milestone: Fixed-Region Picture Packer + Live PLAY/newtxt Flash 2026-05-05

- Status: implemented, tested, and live-flashed.
- Core correction:
  - [tft_images.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_images.py>) no longer expands the TFT resource section for new pictures.
  - Header1 `ressource_files_size` remains fixed at `0xAC0000`.
  - Header2 `unknown_objects_address` remains fixed at `0xAE0000`.
  - New picture bytes are inserted inside the fixed resource area and consume trailing `00/FF` padding before the object section.
  - If a picture would overwrite non-padding resource bytes, the packer errors instead of silently corrupting fonts or code.
- Image-size behavior:
  - Default JPEG quality is now `85`, close to the official PLAY image block sizes and smaller than the earlier `95` default.
  - If fixed resource padding is insufficient, the packer lowers JPEG quality and then downscales proportionally as a safety fallback.
  - The large cat/photo test image now fits the fixed resource budget without moving the object section.
- Regression tests:
  - `test_scene_build_packs_new_picture_resource` now asserts `new_object_start == old_object_start`.
  - `test_scene_build_packs_image_button_states` now asserts `new_object_start == old_object_start`.
  - Full relevant command passed: `python -m pytest tests\test_editor_tft_build.py tests\test_tft_patch.py tests\test_tft_fonts.py tests\test_tft_download.py -q`
  - Result: `16 passed, 13 subtests passed`.
- Generated live sample:
  - scene: [scene.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_fixed_image_text/scene.json>)
  - output TFT: [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_fixed_image_text/build/output.tft>)
  - preview: [preview.png](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_fixed_image_text/preview.png>)
  - camera capture after flash: [after_upload.jpg](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_fixed_image_text/camera/after_upload.jpg>)
- Build facts:
  - `playbtn` is an image-style button at `x=320,y=300,w=160,h=96`.
  - `playbtn.txt` is `PLAY`.
  - `fontmsg` is a yellow stock-font text object at `x=80,y=70,w=640,h=120`.
  - `fontmsg.txt` is `newtxt`.
  - packed picture ids: normal `1`, pressed `2`.
  - `inserted_bytes=7433`, `trimmed_resource_tail_bytes=7433`.
  - final TFT checksum valid: `0x65A47AE0`.
- Upload facts:
  - port `COM36`
  - initial baud `9600`
  - download baud `921600`
  - bytes sent `11410688`
  - chunks sent `2786`
  - elapsed `210.156s`
- Post-flash verification:
  - camera showed the expected yellow text area and blue PLAY button area.
  - `sendme` returned page `0`.
  - `get fontmsg.txt` returned `newtxt`.
  - `get playbtn.txt` returned `PLAY`.
  - `click playbtn,1` sent successfully with no error response.
  - `get playbtn.pic` returned `1A`; this looks like a screen-side unreadable/invalid runtime property for the image slot, not an object lookup failure.
- Current boundary:
  - Text and image-button objects are live and queryable by name.
  - Picture resources now follow the official fixed-object-start layout.
  - Exact byte-for-byte reproduction of official `case_14` is not claimed yet; our JPEG encoder output differs slightly from the official editor's image blocks.

## Milestone: Official Image-Button Object Tail Layout Matched 2026-05-05

- Status: implemented and regression-tested.
- Official fixtures used:
  - [case_13_image_button_only](</C:/Users/SinYu/Desktop/case_for_codex/case_13_image_button_only>)
  - [case_14_text_plus_image_button](</C:/Users/SinYu/Desktop/case_for_codex/case_14_text_plus_image_button>)
- Recovered image-button layout rules:
  - Full-image buttons use `sta=2`, with `pic` as normal state and `pic2` as pressed state.
  - When any full-image button exists, the object-tail prefix switches to an image-button variant.
  - The image-button prefix inserts fixed bytes `92 48 C9 76` at offset `0x86` and adjusts two internal length/offset fields by `+4`.
  - Page event layout gains one extra empty event block before the normal event sequence.
  - Mirror records expand from `0x8A` to `0x8C` bytes.
  - Mirror/user records use the official full-image-button slot layout, including the recovered `pic/pic2` user-record metadata.
  - Image-button tail padding before the final checksum word is `FF FF`, not `00 00`.
- Implemented in:
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>)
- Verification:
  - Generated `case13`-equivalent TFT now has official size `11409424`, object region `0x153E`, compiled tail `0x1810`.
  - Generated `case14`-equivalent TFT now has official size `11410680`, object region `0x199A`, compiled tail `0x1CF8`.
  - From `unknown_objects_address` to the final 4-byte TFT checksum word, generated `case13/case14` tails are byte-for-byte identical to official outputs.
  - Full test suite passed: `44 passed, 22 subtests passed`.

## Milestone: Official PLAY Picture Encoder Matched 2026-05-05

- Status: implemented and regression-tested.
- Recovered picture encoder parameters:
  - JPEG `quality=96`
  - JPEG `subsampling=2` / 4:2:0
  - JFIF density/DPI `96x96`
  - `optimize=False`
  - `progressive=False`
  - 16-pixel aligned black padding remains correct.
- Header/resource correction:
  - Header2 field at offset `0x30`, labeled `pages_count` by TFTTool, is updated to `(picture_region_end & 0xFFFF)` after packing picture resources.
  - Header2 field at offset `0x34`, labeled `pictures_count` by TFTTool, increases by `+4` for the recovered full-image-button object-tail layout.
- Implemented in:
  - [tft_images.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_images.py>)
  - [tft_patch.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_patch.py>)
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>)
- Verification:
  - Compiled `1.i` / `2.i` JPEG payloads for the PLAY normal/pressed images now match official case image payloads byte-for-byte.
  - Scene-generated `case13` TFT now matches official [case_13_image_button_only/lcd_test.tft](</C:/Users/SinYu/Desktop/case_for_codex/case_13_image_button_only/lcd_test.tft>) byte-for-byte.
  - Scene-generated `case14` TFT now matches official [case_14_text_plus_image_button/lcd_test.tft](</C:/Users/SinYu/Desktop/case_for_codex/case_14_text_plus_image_button/lcd_test.tft>) byte-for-byte.
  - Full test suite passed again: `44 passed, 22 subtests passed`.

## Milestone: HMI Picture Resource Writeback 2026-05-05

- Status: implemented and regression-tested.
- Core behavior:
  - `build_scene` now assigns picture IDs before HMI writing, even when only `output.hmi` is requested.
  - The HMI writer rebuilds the container directory instead of patching only one entry in-place.
  - Existing seed resources are preserved.
  - `0.pa` is rewritten with the generated page/object table.
  - Referenced image assets are added as resource pairs:
    - `N.i`: official-style JPEG screen resource entry.
    - `N.is`: official-style source image entry containing the original `png` / `jpg` bytes.
- Implemented in:
  - [editor.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/editor.py>)
  - [tft_images.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_images.py>)
  - [test_editor_tft_build.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_editor_tft_build.py>)
- Verification:
  - Scene-generated `output.hmi` for the PLAY image-button fixture contains `1.is`, `2.is`, `1.i`, and `2.i`.
  - Generated `1.is`, `2.is`, `1.i`, and `2.i` match the official [case_14_text_plus_image_button](</C:/Users/SinYu/Desktop/case_for_codex/case_14_text_plus_image_button>) extracted resources byte-for-byte.
  - Full test suite passed: `45 passed, 22 subtests passed`.
- Remaining boundary:
  - This proves HMI resource payload writeback for the current single-page PLAY image-button fixtures.
  - The generated HMI container is structurally valid and inspectable, but broad official-editor round-trip editing still needs more fixtures and manual open/save checks.

## Milestone: Picture Source Edge Cases Hardened 2026-05-05

- Status: implemented and regression-tested.
- Core behavior:
  - PNG/JPG picture loading now applies EXIF orientation before compiling.
  - Transparent PNGs are flattened onto a black RGB background before TFT JPEG encoding, matching the current no-alpha screen resource path.
  - JPG/JPEG source resources in HMI `.is` entries keep the original source payload and use the normalized `jpg` tag.
  - Non-16-aligned images are still stored as 16-pixel padded JPEG dimensions while keeping logical width/height in the resource records.
  - Large/high-entropy images can reduce JPEG quality and then scale down until they fit a caller-provided fixed resource budget.
  - The legacy Pillow `getdata()` warning in RGB565 asset normalization was removed by switching to byte iteration.
- Implemented in:
  - [tft_images.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/tft_images.py>)
  - [editor.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/usarthmi/editor.py>)
  - [test_tft_images.py](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/tests/test_tft_images.py>)
- Verification:
  - Added source-independent tests for transparent PNG flattening, JPG `.is` source payload/tag preservation, 16-pixel padding, and shrink-to-budget behavior.
  - Full test suite passed: `48 passed, 22 subtests passed`.
- Remaining boundary:
  - These are local synthetic edge cases; more official-editor fixtures are still useful for unusual PNG compression modes, palette/transparency combinations, and real-world large photos.

## Milestone: Mixed JPG/PNG/Image-Button Live Stress Scene 2026-05-05

- Status: implemented, flashed, and visually checked.
- Scene/artifacts:
  - [scene.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_stress/scene.json>)
  - [output.hmi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_stress/build/output.hmi>)
  - [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_stress/build/output.tft>)
  - [after_upload_sorted_resources_cam1.jpg](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_image_stress/captures/after_upload_sorted_resources_cam1.jpg>)
- What this scene covers:
  - generated JPG picture resource (`photo1.pic=2`)
  - generated transparent PNG picture resource (`badge1.pic=1`)
  - two-state image button (`playbtn.sta=2`, normal/pressed resources `3/4`)
  - generated text objects (`title`, `valtxt`, `subtxt`)
  - cleaned seed objects moved offscreen
- Bug found:
  - The first flashed build displayed the transparent PNG in `photo1` and the JPG in `badge1`, even though serial reads returned `photo1.pic=2` and `badge1.pic=1`.
  - Root cause: TFT picture records were emitted in asset insertion order. The live panel appears to resolve picture resources by resource table order, not only by the record's embedded `picture_id` field.
- Fix:
  - `pack_picture_resources_into_tft` now sorts new picture resources by `picture_id` before writing the TFT picture table.
  - Added a regression test that declares assets out of order and verifies the TFT picture table is ordered as `0,1,2`.
- Verification:
  - Full suite passed after the fix: `49 passed, 22 subtests passed`.
  - Rebuilt and re-uploaded the fixed TFT to `COM36`.
  - Serial readback after upload:
    - `sendme -> 0`
    - `get photo1.pic -> 2`
    - `get badge1.pic -> 1`
    - `get playbtn.sta -> 2`
    - `get title.txt -> IMG STRESS OK`
    - `get subtxt.txt -> jpg + transparent png + image button`
  - Camera capture confirmed the visual order: JPG card on the left, transparent PNG badge in the middle, PLAY button on the right.
- Remaining boundary:
  - `number` widgets are still not supported by the TFT tail compiler; attempting to include `n0` correctly failed with `type '4'`, so the live stress scene used a text-based value display (`valtxt`) instead.

## Milestone: Custom Font Recognition Confirmed 2026-05-05

- Status: implemented, flashed, and visually confirmed.
- Scene/artifacts:
  - [scene.json](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_font_recognition/scene.json>)
  - [Impact56ASCII_ordered.zi](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_font_recognition/Impact56ASCII_ordered.zi>)
  - [output_impact_ordered.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_font_recognition/build_impact_ordered/output_impact_ordered.tft>)
  - [font_stock_cam1.jpg](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_font_recognition/captures/font_stock_cam1.jpg>)
  - [font_impact_ordered_cam1.jpg](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_font_recognition/captures/font_impact_ordered_cam1.jpg>)
- What was tested:
  - Stock font test scene with three large text objects was flashed first for a visual baseline.
  - `Impact56ASCII.zi` using UTF-8/codepage `0x18` was generated and patched into the TFT; the panel loaded the new glyph shapes, but text rendered mostly as repeated `F`.
  - `Impact56ASCII_codepage_ascii.zi` using ASCII/codepage `0x01` was generated and patched; the panel loaded the glyph shapes, but characters were still scrambled.
  - Root cause was found in `tools/ZiCli/Program.cs`: glyphs were collected in a `HashSet`, so the generated `.zi` glyph order was not codepage order.
- Fix:
  - `ZiCli` now stores requested codepoints as integers and emits glyphs ordered by `CodePage.CodePoints`, with any extra codepoints appended sorted numerically.
  - This makes ASCII `.zi` glyph order match the panel's codepage-index lookup.
- Verification:
  - Rebuilt `ZiCli`.
  - Generated `Impact56ASCII_ordered.zi`: codepage `ascii`, version `5`, height `56`, 95 characters, size `18464` bytes.
  - Patched it into [build_stock/output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_font_recognition/build_stock/output.tft>) with `tft patch-font`.
  - Uploaded [output_impact_ordered.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/live_font_recognition/build_impact_ordered/output_impact_ordered.tft>) to `COM36`.
  - Serial readback after upload:
    - `sendme -> 0`
    - `get fonta.txt -> FONT TEST 123`
    - `get fonta.font -> 0`
    - `get fontb.txt -> WIDE III 888`
    - `get fontc.txt -> IMPACT FONT CHECK`
  - Camera capture confirmed correct text and visually different Impact-style glyphs on the real panel.
  - Full Python test suite passed: `49 passed, 22 subtests passed`.
- Current conclusion:
  - The panel recognizes our custom font resource when the `.zi` is codepage-ordered.
  - Ordered ASCII small fonts are now a working baseline path.
- Remaining boundary:
  - Small GB2312/Chinese baseline fonts still need the same live verification.
  - The current safe TFT font patch still replaces only the first embedded `.zi` in-place and requires the replacement to fit inside the original font span.

## Probe: Event/Logic Bytecode Still Not Scheduled 2026-05-05

- Status: partially implemented, live-probed, not solved yet.
- Implemented pieces:
  - Page `codesloadend-` is now preserved in parsed `.pa` files and accepted by scene validation.
  - The minimal event compiler now emits `vis obj,state` as `09 05 04 + ASCII payload`.
  - Page event blocks can include the official `09 30 08` load/loadend separator observed in external Nextion TFT samples.
  - Regression tests cover `loadend`, `vis`, `printh`, `click`, and `rawhex` event block construction.
- Live probe:
  - Built [output.tft](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/event_logic_probe/build_load_probe_current/output.tft>) with page `load` code:
    - `printh 23 02 50 02`
    - `vis evtbtn,0`
  - Uploaded it to `COM36`; upload completed successfully:
    - size `11409472`
    - sent `11409472`
    - elapsed `210.391s`
  - Serial read immediately after boot and after `page 0` returned no `23 02 50 02` signature.
  - Runtime sanity check still worked: `get evtbtn.x -> 300`.
  - Camera capture [build_load_probe_current_cam.jpg](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/event_logic_probe/build_load_probe_current_cam.jpg>) showed `EVENT TEST` was still visible, so the compiled `vis evtbtn,0` did not execute.
- Current conclusion:
  - The command opcode itself is not the problem; runtime `vis evtbtn,0` hides the object correctly.
  - The object exists and is addressable; serial `get evtbtn.x` works.
  - The compiled event byte blocks are present in the TFT object tail, but the panel does not schedule them.
  - The missing piece is likely an additional event entry/index/flag outside the obvious event byte stream, or a TJC-specific event directory not yet regenerated.
- Official loader probe:
  - Added [RunOfficialInit.cs](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/tools/RunOfficialInit.cs>) to try listing official dynamically loaded assemblies; direct invocation currently hits `StackOverflowException`.
  - Updated [DecodeAppDllPass.cs](</C:/Users/SinYu/Documents/Codex/2026-05-03/files-mentioned-by-the-user-delay/reverse_usarthmi/tools/DecodeAppDllPass.cs>) so `AppDllPass_Decode` receives a fourth key-buffer pointer instead of null.
  - Simple key modes (`zero`, `ff`, `magic`) still did not decode `ACTR.dll` into a valid PE, so the official compiler internals are not opened yet.
- Verification:
  - Focused tests passed after the event compiler changes: `20 passed, 16 subtests passed`.
- Next best evidence needed:
  - A true official TJC 1.67.6 TFT compiled from the same seed with one simple event such as page-load `printh 23 02 50 02` or button-down `vis evtbtn,0`.
  - With that fixture, the remaining event scheduling fields should be diffable instead of guessed.

## Finding: Offline TJC Wiki Integrated As Fixture Source 2026-05-07

- Source received from the user:
  - `C:\Users\SinYu\Desktop\tjcwiki`
- High-value pages found:
  - `advanced\hmi_download_protocol.html`
  - `advanced\download_protocol\python_code.html`
  - `start\ide_introduce\ide_introduce8.html`
  - `widgets\Page.html`
- Download protocol conclusion:
  - The public protocol is still full-stream only:
    - optional active-parse exit + `connect`
    - `whmi-wri filesize,baud,0`
    - switch to forced download baud
    - wait for single-byte `0x05`
    - stream every TFT byte in 4096-byte chunks
    - wait for single-byte `0x05` after each chunk
  - The official public Python downloader source was saved locally under:
    - `external\tjcwiki_download_protocol\official_tftdownloader.py`
  - That source also contains no sparse/differential write command. The editor's "same part not downloaded/written" behavior is not exposed in the public downloader.
- Official HMI samples downloaded as ignored local fixtures:
  - `external\tjcwiki_samples\command_printh.HMI`
  - `external\tjcwiki_samples\command_vis.HMI`
  - `external\tjcwiki_samples\command_click.HMI`
  - `external\tjcwiki_samples\command_page.HMI`
  - `external\tjcwiki_samples\command_sendme.HMI`
- Tooling improvement:
  - `inspect-hmi` now reports structured `0.pa` block summaries in addition to raw string runs:
    - object/page `objname`
    - `type_code`
    - useful numeric fields such as `id/x/y/w/h/pic/font/bco/pco`
    - grouped event scripts parsed from `codesload-*`, `codesloadend-*`, `codesdown-*`, `codesup-*`, `codesunload-*`, and `codestimer-*`
  - `page_format` now decodes event tokens with ASCII/UTF-8/GBK fallback and serializes non-ASCII event comments with GBK when needed.
- Official sample evidence extracted:
  - `command_vis.HMI`:
    - `b0.codesdown-1 -> vis t0,0`
    - `b1.codesdown-1 -> vis t0,1`
  - `command_printh.HMI`:
    - `b0.codesdown-3 -> //printh ... printh ff ff ff`
    - `b1.codesdown-3 -> //printh ... printh 0d 0a`
  - `command_click.HMI`:
    - `page0.codesload-2 -> //用click去触发触摸热区,类似于调用函数 | click getTime,1`
    - `tm0.codestimer-2 -> //用click去触发触摸热区,类似于调用函数 | click getTime,1`
    - `getTime.codesdown-29 -> RTC copy and weekday if/else script`
- Updated conclusion:
  - The HMI event field names and event text structure match our authoring layer.
  - The live failure is therefore more likely in the TFT-side event registration/scheduling table, not in HMI event text naming.
  - The next best fixture is still an official TJC 1.67.6 TFT compiled from a tiny event-bearing HMI for the same model/seed; the wiki samples help parse source-side events, but they do not provide compiled TFT output.
- Verification:
  - Full Python test suite passed after the parser changes: `59 passed, 25 subtests passed`.

## Finding: Official Cases 17-21 Added 2026-05-11

- Source received from the user:
  - `C:\Users\SinYu\Desktop\case_for_codex\case_17_slider`
  - `C:\Users\SinYu\Desktop\case_for_codex\case_18_gauge`
  - `C:\Users\SinYu\Desktop\case_for_codex\case_19_timer`
  - `C:\Users\SinYu\Desktop\case_for_codex\case_20_progress`
  - `C:\Users\SinYu\Desktop\case_for_codex\case_21_qrcode`
- Each case contains:
  - `lcd_test.HMI`
  - `lcd_test.tft`
  - `screenshot.png`
- Visual contact sheet generated at:
  - `reverse_usarthmi\case17_21_contact.png`
- Structured compare output generated at:
  - `reverse_usarthmi\case17_21_compare_cleanbaseline\summary.json`
  - `reverse_usarthmi\case17_21_compare_cleanbaseline\case_*\reverse_tail.json`
  - Note: `C:\Users\SinYu\Desktop\case_for_codex\case_00_baseline\lcd_test.HMI` was later found to be dirty/mismatched against its TFT, so the clean compare uses `D:\MySTM32\H723ZGT6\Program\ISP_Test\lcd_test.HMI` plus `official_lcd_test_TJC8048X543_011_20260504.tft` as the baseline.
- New HMI object facts:
  - `case_17_slider`: `slider1`, type code `0x01`, fields include `mode/psta/wid/hig/dis/pic/picc/bco/pic1/picc1/bco1/pic2/pco/val/maxval/minval/ch`, events include `codesslide-0`.
  - `case_18_gauge`: `gauge1`, type code `z`, fields include `sta/pic/picc/bco/pco/pco2/val/format/up/down/left/hig/wid/vvs0/vvs1/vvs2`.
  - `case_19_timer`: `tm0`, type code `3`, fields include `tim/en`, event `codestimer-0`.
  - `case_20_progress`: `bar1`, type code `j`, fields include `sta/dez/val/dis/bco/bpic/pco/ppic`.
  - `case_21_qrcode`: `qr1`, type code `:`, fields include `sta/dis/bco/pco/pic/txt/txt_maxl`.
- TFT reverse summary:
  - Existing reverse logic can locate compiled object records for slider, gauge, progress, and QR code.
  - Timer has no normal coordinate/object body match because it is a non-visual object; it needs separate handling in any future compiled-object model.
  - QR code text pointer follows the same pointer+bias pattern as text-like objects (`body+0x28`, bias `0x1EF` in this fixture).
- Tooling updates from these cases:
  - `page_format.EVENT_PREFIXES` now includes `codesslide-`.
  - Scene event validation and HMI event writing now accept `slide` and `timer`.
  - `inspect-hmi` summaries now expose additional fields used by slider/gauge/timer/progress/QR objects.
- Verification:
  - Focused tests passed: `13 passed`.
  - Full Python test suite passed after these updates: `60 passed, 25 subtests passed`.
