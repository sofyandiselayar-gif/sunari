"""Bersihkan screenshot Google Maps: hapus UI aplikasi, pin, label & skala; logo "Google Maps" & watermark © Google TETAP dipertahankan (atribusi wajib).
Run: python3 assets/maps/bahuluang/bersihkan_peta.py -> assets/maps/bahuluang/peta-N.png (720x950)"""
import cv2, numpy as np, pathlib
H = pathlib.Path(__file__).parent
TOP, BOT = 200, 1150                      # buang kolom cari, chip, dan panel bawah
BTN = [("c", 657, 268, 42), ("r", 598, 908, 692, 1002), ("r", 598, 1028, 692, 1122)]   # tombol lapisan, lokasi, rute
M = {
 1: [("c", 258, 527, 28), ("t", 284, 512, 365, 543), ("c", 292, 563, 10), ("t", 262, 624, 380, 660), ("t", 240, 656, 322, 684), ("c", 326, 703, 11),
     ("c", 361, 710, 26), ("c", 264, 778, 18), ("p", [(196, 752), (262, 766), (262, 790), (204, 800)]), ("c", 209, 741, 11), ("t", 190, 742, 284, 1092),
     ("c", 300, 928, 11), ("c", 298, 950, 11), ("t", 296, 938, 372, 966), ("c", 308, 1021, 27), ("c", 266, 1077, 11)],
 2: [("c", 383, 303, 27), ("c", 364, 418, 27), ("c", 418, 773, 27), ("t", 506, 414, 590, 442), ("t", 316, 562, 444, 590), ("t", 496, 690, 562, 718),
     ("t", 90, 636, 190, 980), ("c", 207, 1052, 27)],
 3: [("t", 238, 200, 336, 480), ("t", 136, 672, 304, 728), ("c", 328, 695, 28), ("t", 112, 855, 244, 890), ("c", 272, 868, 28)],
 4: [],
 5: [("t", 76, 826, 280, 860), ("c", 305, 840, 28), ("r", 436, 1050, 580, 1104)],
 6: [("r", 450, 1050, 580, 1104)],
 7: [("t", 260, 720, 394, 752), ("c", 420, 732, 28), ("c", 657, 373, 40)],
}
def clone(im, sm):
    """Isi area bertopeng dengan tekstur tetangga (geser sumber, pilih yang paling menyatu), tepi dihaluskan."""
    ys, xs = np.nonzero(sm); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    h, w = y1 - y0, x1 - x0; ring = cv2.dilate(sm, np.ones((9, 9), np.uint8)) & ~sm
    wide = cv2.dilate(sm, np.ones((31, 31), np.uint8)) & ~sm
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(float)
    hp = np.abs(gray - cv2.GaussianBlur(gray, (0, 0), 3))
    if hp[wide > 0].mean() < 6:                       # area polos (laut) -> isi halus
        return cv2.inpaint(im, cv2.dilate(sm, np.ones((5, 5), np.uint8)), 9, cv2.INPAINT_TELEA)
    best = None
    for dx, dy in [(-1.3, 0), (1.3, 0), (0, -1.3), (0, 1.3), (-1.3, -1.3), (1.3, 1.3), (-1.3, 1.3), (1.3, -1.3), (-2.4, 0), (0, -2.4), (0, 2.4)]:
        ox, oy = int(dx * w), int(dy * h)
        if not (0 <= x0 + ox and x1 + ox <= im.shape[1] and 0 <= y0 + oy and y1 + oy <= im.shape[0]): continue
        if (ALL[y0 + oy:y1 + oy, x0 + ox:x1 + ox] > 0).any(): continue
        sh = np.roll(np.roll(im, -oy, 0), -ox, 1)
        err = np.abs(sh[ring > 0].astype(int) - im[ring > 0].astype(int)).mean()
        if best is None or err < best[0]: best = (err, sh)
    if best is None: return cv2.inpaint(im, sm, 9, cv2.INPAINT_TELEA)
    a = cv2.GaussianBlur(cv2.dilate(sm, np.ones((7, 7), np.uint8)).astype(float) / 255, (0, 0), 3)[..., None]
    return (best[1] * a + im * (1 - a)).astype(np.uint8)
for n, shapes in M.items():
    im = cv2.imread(str(H / f"src/peta-{n}-asli.jpg"))
    mk = np.zeros(im.shape[:2], np.uint8)
    ALL = np.zeros(im.shape[:2], np.uint8)
    for s in shapes + BTN:
        if s[0] == "c": cv2.circle(ALL, (s[1], s[2]), s[3] + 4, 255, -1)
        elif s[0] in "rt": cv2.rectangle(ALL, (s[1] - 4, s[2] - 4), (s[3] + 4, s[4] + 4), 255, -1)
        else: cv2.fillPoly(ALL, [np.array(s[1])], 255)
    for s in shapes + BTN:
        if s[0] in "cr":
            sm = np.zeros(im.shape[:2], np.uint8)
            if s[0] == "c": cv2.circle(sm, (s[1], s[2]), s[3] + 3, 255, -1)
            else: cv2.rectangle(sm, (s[1] - 3, s[2] - 3), (s[3] + 3, s[4] + 3), 255, -1)
            im = clone(im, sm); continue
        if s[0] == "c": cv2.circle(mk, (s[1], s[2]), s[3], 255, -1)
        elif s[0] == "r": cv2.rectangle(mk, (s[1], s[2]), (s[3], s[4]), 255, -1)
        elif s[0] == "t":
            x0, y0, x1, y1 = s[1:]; roi = im[y0:y1, x0:x1].astype(int)
            txt = ((roi.min(axis=2) > 205).astype(np.uint8) * 255)
            mk[y0:y1, x0:x1] |= cv2.dilate(txt, np.ones((7, 7), np.uint8))
        else: cv2.fillPoly(mk, [np.array(s[1])], 255)
    mk = cv2.dilate(mk, np.ones((5, 5), np.uint8))
    out = cv2.inpaint(im, mk, 9, cv2.INPAINT_TELEA)
    cv2.imwrite(str(H / f"peta-{n}.png"), out[TOP:BOT])
    cv2.imwrite(str(H / f"src/mask-{n}.png"), mk[TOP:BOT])
print("ok")
