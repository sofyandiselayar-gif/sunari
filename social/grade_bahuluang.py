"""Color grading tema SunaRi untuk foto feed "Sehari ke Bahuluang" -> assets/photos/graded/. Foto asli tidak diubah.
Memakai resep yang sama dengan grade_photos.py (WB hangat, highlight keemasan, bayangan Driftwood Deep, fade lembut).
Run: python3 social/grade_bahuluang.py"""
import pathlib, re
H = pathlib.Path(__file__).parent
exec((H / "grade_photos.py").read_text().split("JOBS =")[0])
src = (H / "build_bahuluang_feed20.py").read_text()
photos = re.findall(r'\(\s*(B|P) \+ "([^"]+)"', src)
S = {"senja/21-siluet-tamu-tepi-pantai.jpg": 0.5}          # foto senja sudah hangat
for pre, f in photos:
    rel = ("bahuluang/" if pre == "B" else "") + f.replace("__", "/")
    grade(rel, rel.replace("/", "__"), S.get(rel, 0.8)); print("graded", rel)
