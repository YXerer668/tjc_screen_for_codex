from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from usarthmi.hmi_inspect import inspect_hmi
from usarthmi.tft_checksum import inspect_tft_checksum
from usarthmi.tft_patch import (
    _build_object_event_table,
    _build_page_event_table,
    patch_added_object_tft,
    patch_basic_tft,
)
from usarthmi.page_format import load_page_file, parse_page_data


CASE_ROOT = Path(r"C:\Users\SinYu\Desktop\case_for_codex")
EXTRACT_ROOT = (
    Path(__file__).resolve().parents[1]
    / "reverse_usarthmi"
    / "case_compare"
)


@unittest.skipUnless(CASE_ROOT.exists() and EXTRACT_ROOT.exists(), "local TJC case fixtures are not available")
class TftPatchTests(unittest.TestCase):
    def test_basic_patch_reproduces_known_cases_exactly(self) -> None:
        baseline_tft = CASE_ROOT / "case_00_baseline" / "lcd_test.tft"
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        for case_name in (
            "case_01_t0_text_hello",
            "case_02_t0_x_plus10",
            "case_03_b0_text_test",
        ):
            with self.subTest(case=case_name), tempfile.TemporaryDirectory() as temp_dir:
                out = Path(temp_dir) / f"{case_name}.tft"
                patch_basic_tft(
                    baseline_tft,
                    baseline_pa=baseline_pa,
                    target_pa=EXTRACT_ROOT / case_name / "extract" / "0.pa",
                    out_tft=out,
                )
                generated = out.read_bytes()
                official = (CASE_ROOT / case_name / "lcd_test.tft").read_bytes()
                self.assertEqual(generated, official)

    def test_added_object_patch_reproduces_known_cases_exactly(self) -> None:
        baseline_tft = CASE_ROOT / "case_00_baseline" / "lcd_test.tft"
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        for case_name in (
            "case_04_add_text",
            "case_05_add_button",
            "case_06_add_picture",
        ):
            with self.subTest(case=case_name), tempfile.TemporaryDirectory() as temp_dir:
                out = Path(temp_dir) / f"{case_name}.tft"
                patch_added_object_tft(
                    baseline_tft,
                    baseline_pa=baseline_pa,
                    target_pa=EXTRACT_ROOT / case_name / "extract" / "0.pa",
                    out_tft=out,
                )
                generated = out.read_bytes()
                official = (CASE_ROOT / case_name / "lcd_test.tft").read_bytes()
                self.assertEqual(generated, official)

    def test_added_object_patch_accepts_new_object_names(self) -> None:
        baseline_tft = CASE_ROOT / "case_00_baseline" / "lcd_test.tft"
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        target_pa = EXTRACT_ROOT / "case_04_add_text" / "extract" / "0.pa"
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            renamed_pa = temp / "renamed.pa"
            out = temp / "renamed.tft"
            page = load_page_file(target_pa)
            page.blocks[-1].set_string("objname", "note1")
            renamed_pa.write_bytes(page.serialize())

            patch_added_object_tft(
                baseline_tft,
                baseline_pa=baseline_pa,
                target_pa=renamed_pa,
                out_tft=out,
            )

            info = inspect_tft_checksum(out)
            self.assertTrue(info["valid"])

    def test_added_object_patch_accepts_multiple_new_objects(self) -> None:
        baseline_tft = CASE_ROOT / "case_00_baseline" / "lcd_test.tft"
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            target_pa = temp / "multi.pa"
            out = temp / "multi.tft"
            page = _build_multi_added_page()
            target_pa.write_bytes(page.serialize())

            result = patch_added_object_tft(
                baseline_tft,
                baseline_pa=baseline_pa,
                target_pa=target_pa,
                out_tft=out,
            ).to_dict()

            self.assertEqual(result["added_count"], 3)
            self.assertEqual([item["name"] for item in result["added_objects"]], ["note1", "btn1", "pic1"])
            info = inspect_tft_checksum(out)
            self.assertTrue(info["valid"])

    def test_added_object_patch_accepts_gbk_text(self) -> None:
        baseline_tft = CASE_ROOT / "case_00_baseline" / "lcd_test.tft"
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            target_pa = temp / "gbk_text.pa"
            out = temp / "gbk_text.tft"
            page = load_page_file(baseline_pa)
            text = load_page_file(EXTRACT_ROOT / "case_04_add_text" / "extract" / "0.pa").blocks[-1].clone()
            _configure_added_block(text, object_id=4, name="cn1", x=64, y=64, w=220, h=48)
            text.set_string("txt", "中文OK", encoding="gbk")
            text.set_int("txt_maxl", len("中文OK".encode("gbk")), width=2)
            page.blocks.append(text)
            target_pa.write_bytes(page.serialize())

            result = patch_added_object_tft(
                baseline_tft,
                baseline_pa=baseline_pa,
                target_pa=target_pa,
                out_tft=out,
            ).to_dict()

            self.assertEqual(result["added_count"], 1)
            info = inspect_tft_checksum(out)
            self.assertTrue(info["valid"])

    def test_event_table_builder_matches_empty_seed_events(self) -> None:
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        page = load_page_file(baseline_pa)

        self.assertEqual(
            _build_page_event_table(page.blocks[0]),
            bytes.fromhex(
                "00 00 00 00 04 00 00 00 64 6f 77 6e 00 00 00 00 "
                "02 00 00 00 75 70 00 00 00 00 06 00 00 00 75 6e "
                "6c 6f 61 64 00 00 00 00"
            ),
        )
        for block in page.blocks[1:]:
            with self.subTest(block=block.objname):
                self.assertEqual(
                    _build_object_event_table(block),
                    bytes.fromhex(
                        "00 00 00 00 04 00 00 00 64 6f 77 6e 00 00 00 00 "
                        "02 00 00 00 75 70 00 00 00 00"
                    ),
                )

    def test_event_table_builder_compiles_printh_up_event(self) -> None:
        source_pa = EXTRACT_ROOT / "case_05_add_button" / "extract" / "0.pa"
        page = load_page_file(source_pa)
        button = page.blocks[-1].clone()
        button.set_event("codesup-", ["printh 23 02 54 45"])

        event_data = _build_object_event_table(button)

        self.assertIn(b"\x04\x00\x00\x00down", event_data)
        self.assertIn(b"\x02\x00\x00\x00up", event_data)
        self.assertIn(b"\x0e\x00\x00\x00\x09\x0f\x0823 02 54 45", event_data)

    def test_page_event_table_builder_separates_load_and_loadend(self) -> None:
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        page = load_page_file(baseline_pa)
        page_block = page.blocks[0].clone()
        page_block.set_event("codesload-", ["printh 23 02 50 01"])
        page_block.set_event("codesloadend-", ["vis evtbtn,0"])

        event_data = _build_page_event_table(page_block)

        self.assertIn(b"\x0e\x00\x00\x00\x09\x0f\x0823 02 50 01", event_data)
        self.assertIn(b"\x03\x00\x00\x00\x09\x30\x08", event_data)
        self.assertIn(b"\x0b\x00\x00\x00\x09\x05\x04evtbtn,0", event_data)
        self.assertIn(b"\x04\x00\x00\x00down", event_data)

    def test_event_table_builder_accepts_rawhex_probe(self) -> None:
        source_pa = EXTRACT_ROOT / "case_05_add_button" / "extract" / "0.pa"
        page = load_page_file(source_pa)
        button = page.blocks[-1].clone()
        button.set_event("codesup-", ["rawhex 09 0a 08 32 33 20 30 32"])

        event_data = _build_object_event_table(button)

        self.assertIn(b"\x08\x00\x00\x00\x09\x0a\x0823 02", event_data)

    def test_checksum_matches_official_cases(self) -> None:
        for case_name in (
            "case_00_baseline",
            "case_01_t0_text_hello",
            "case_02_t0_x_plus10",
            "case_03_b0_text_test",
            "case_04_add_text",
            "case_05_add_button",
            "case_06_add_picture",
        ):
            with self.subTest(case=case_name):
                info = inspect_tft_checksum(CASE_ROOT / case_name / "lcd_test.tft")
                self.assertTrue(info["valid"])

    @unittest.skipUnless(
        all((CASE_ROOT / name / "lcd_test.HMI").exists() for name in (
            "case_17_slider",
            "case_18_gauge",
            "case_20_progress",
            "case_21_qrcode",
        )),
        "local extra-control fixtures are not available",
    )
    def test_added_object_patch_accepts_extra_visual_controls(self) -> None:
        baseline_tft = CASE_ROOT / "case_00_baseline" / "lcd_test.tft"
        baseline_pa = EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa"
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            target_pa = temp / "extra_visual.pa"
            out = temp / "extra_visual.tft"
            page = load_page_file(baseline_pa)

            slider = _load_case_last_block("case_17_slider")
            progress = _load_case_last_block("case_20_progress")
            gauge = _load_case_last_block("case_18_gauge")
            qr = _load_case_last_block("case_21_qrcode")
            _configure_added_block(slider, object_id=4, name="sld1", x=56, y=118, w=330, h=40)
            _configure_added_block(progress, object_id=5, name="bar1", x=56, y=206, w=330, h=30)
            _configure_added_block(gauge, object_id=6, name="gauge1", x=455, y=82, w=240, h=240)
            _configure_added_block(qr, object_id=7, name="qr1", x=560, y=290, w=150, h=150)
            page.blocks.extend([slider, progress, gauge, qr])
            target_pa.write_bytes(page.serialize())

            result = patch_added_object_tft(
                baseline_tft,
                baseline_pa=baseline_pa,
                target_pa=target_pa,
                out_tft=out,
            ).to_dict()

            self.assertEqual(result["added_count"], 4)
            self.assertEqual([item["type"] for item in result["added_objects"]], ["\x01", "j", "z", ":"])
            info = inspect_tft_checksum(out)
            self.assertTrue(info["valid"])

def _build_multi_added_page():
    baseline = load_page_file(EXTRACT_ROOT / "case_00_baseline" / "extract" / "0.pa")
    text = load_page_file(EXTRACT_ROOT / "case_04_add_text" / "extract" / "0.pa").blocks[-1].clone()
    button = load_page_file(EXTRACT_ROOT / "case_05_add_button" / "extract" / "0.pa").blocks[-1].clone()
    picture = load_page_file(EXTRACT_ROOT / "case_06_add_picture" / "extract" / "0.pa").blocks[-1].clone()

    _configure_added_block(text, object_id=4, name="note1", x=355, y=321, w=100, h=31)
    text.set_string("txt", "note1")
    _configure_added_block(button, object_id=5, name="btn1", x=192, y=310, w=100, h=50)
    button.set_string("txt", "BTN1")
    _configure_added_block(picture, object_id=6, name="pic1", x=579, y=346, w=92, h=92)

    baseline.blocks = [*baseline.blocks, text, button, picture]
    return baseline


def _load_case_last_block(case_name: str):
    hmi_path = CASE_ROOT / case_name / "lcd_test.HMI"
    inspection = inspect_hmi(hmi_path)
    raw = hmi_path.read_bytes()
    entry = next(item for item in inspection.entries if item.name == "0.pa")
    return parse_page_data(raw[entry.data_offset : entry.data_offset + entry.length]).blocks[-1].clone()


def _configure_added_block(block, *, object_id: int, name: str, x: int, y: int, w: int, h: int) -> None:
    block.set_int("id", object_id, width=1)
    block.set_string("objname", name)
    block.set_int("x", x, width=2)
    block.set_int("y", y, width=2)
    block.set_int("w", w, width=2)
    block.set_int("h", h, width=2)
    block.set_int("endx", x + w - 1, width=2)
    block.set_int("endy", y + h - 1, width=2)


if __name__ == "__main__":
    unittest.main()
