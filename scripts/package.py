"""Build and check the self-contained plugin archive using only Python's stdlib."""

import hashlib
import json
import struct
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "humanizer-zh"
SOURCE_SHA256 = "95627fd4437d886f98032ccc62d79136e6310f1fc04e354bb86431795ff206df"
FILES = ("plugin.json", "LICENSE", "assets/icon.png", "skills/humanizer-zh/SKILL.md")


def main():
    manifest = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["name"] == PLUGIN.name
    interface = manifest["extensions"]["com.openai"]["interface"]
    assert interface["displayName"] == "讲人话"
    assert len(interface["shortDescription"]) <= 30
    assert "apps" not in manifest and "apps" not in manifest["extensions"]["com.openai"]
    archive = ROOT / "dist" / f"{PLUGIN.name}-{manifest['version']}.zip"
    archive.parent.mkdir(exist_ok=True)
    assert {p.relative_to(PLUGIN).as_posix() for p in PLUGIN.rglob("*") if p.is_file()} == set(FILES)
    with ZipFile(archive, "w", ZIP_DEFLATED) as package:
        for relative in FILES:
            path = PLUGIN / relative
            assert not path.is_symlink()
            package.write(path, f"{PLUGIN.name}/{relative}")
    with ZipFile(archive) as package:
        assert package.testzip() is None
        assert set(package.namelist()) == {f"{PLUGIN.name}/{p}" for p in FILES}
        assert hashlib.sha256(package.read(f"{PLUGIN.name}/skills/humanizer-zh/SKILL.md")).hexdigest() == SOURCE_SHA256
        assert b"MIT License" in package.read(f"{PLUGIN.name}/LICENSE")
        for key in ("logo", "composerIcon"):
            icon = package.read(f"{PLUGIN.name}/{interface[key].removeprefix('./')}")
            assert icon[:8] == b"\x89PNG\r\n\x1a\n"
            width, height = struct.unpack(">II", icon[16:24])
            assert 256 <= width == height <= 4096 and len(icon) <= 5 * 1024 * 1024
    print(f"检查通过：{archive}")


if __name__ == "__main__":
    main()
