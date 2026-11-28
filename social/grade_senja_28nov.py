"""Color grading foto senja 28 Nov 2026 (senja/85-99) untuk carousel cerita "Senja Hari Ini · 28 Nov".
Memakai look yang sama dengan grade_senja_cerita.py. Run: python3 social/grade_senja_28nov.py"""
from grade_senja_cerita import grade
JOBS = {"85-dua-tamu-bingkai-pohon-tirai.jpg": .45, "97-gazebo-tirai-pantulan-matahari.jpg": .7,
        "96-kayak-pulau-awan.jpg": .8, "92-kamboja-bingkai-matahari-tamu.jpg": .6, "91-tamu-memotret-matahari.jpg": .5,
        "88-matahari-terbenam-langit-merah.jpg": .35, "87-tamu-berhijab-tepi-pantai.jpg": .5,
        "99-pelayan-nampan-senja.jpg": .45, "98-kayak-langit-merah.jpg": .4}
if __name__ == "__main__":
    for f, s in JOBS.items(): print(grade("senja/" + f, s))
