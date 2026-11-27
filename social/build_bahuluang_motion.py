"""Carousel bergerak "Dari SunaRi ke Bahuluang": 10 video MP4 1080x1350 (6 detik, loop).
Garis rute putus-putus menyambung di tepi tiap slide; perahu masuk dari kiri & keluar di kanan,
berangkat dari SunaRi (slide 1) dan berlabuh kembali di SunaRi (slide 10). Foto bergerak pelan (Ken Burns).
Run: python3 social/build_bahuluang_feed.py && python3 social/build_bahuluang_motion.py && node social/render_bahuluang_motion.js
-> social/bahuluang-motion/*.mp4"""
import pathlib
H = pathlib.Path(__file__).parent
html = (H / "bahuluang_feed.html").read_text()
Y = 1252  # garis rute = pengganti garis atas footer
CSS = """
body{background:#fff;margin:0}.t{margin:0!important}
.bt{border-top:none!important}
.fc .fg{bottom:160px!important}.fc .fl{bottom:140px!important;width:260px!important}
.rt{position:absolute;left:0;top:0;width:1080px;height:1350px;overflow:visible;pointer-events:none;z-index:5}
.ph img:first-child,.fc .bgf{will-change:transform}
"""
BOAT = """<g class="boat"><g class="bob">
  <path d="M-30 6 q-14 2 -26 -2 M-36 12 q-12 2 -22 -1" fill="none" stroke="{w}" stroke-width="2.4" stroke-linecap="round" opacity=".75"/>
  <path d="M-32 -6 L36 -6 L26 9 L-24 9 Z" fill="#5A3E31"/><path d="M-30 -3 L34 -3" stroke="#FF8A5C" stroke-width="3"/>
  <rect x="-14" y="-20" width="26" height="14" rx="2" fill="#FBF4EC" stroke="#5A3E31" stroke-width="2"/>
  <path d="M-4 -20 V-29" stroke="#5A3E31" stroke-width="2.4"/><path d="M-4 -29 L8 -26 L-4 -23 Z" fill="#FDB15D"/></g></g>"""
def svg(kind):
    light = kind == "cover"
    col = "#FBF4EC" if light else "#A0603E"
    x0 = 84 if kind == "cover" else 0
    x1 = 150 if kind == "end" else 1080
    s = f'<svg class="rt" data-kind="{kind}" viewBox="0 0 1080 1350"><path d="M{x0} {Y} H{x1}" stroke="{col}" stroke-width="3" stroke-dasharray="12 10" opacity="{.9 if light else .65}"/>'
    if kind in ("cover", "end"):
        px = x0 if kind == "cover" else x1
        s += f'<circle class="pulse" cx="{px}" cy="{Y}" r="10" fill="none" stroke="#FF8A5C" stroke-width="3"/><circle cx="{px}" cy="{Y}" r="9" fill="#FF8A5C" stroke="{"#FBF4EC" if light else "#fff"}" stroke-width="3"/>'
        lbl = "Berangkat dari SunaRi" if kind == "cover" else "Kembali ke SunaRi"
        ly, anc = (Y + 46, "start") if kind == "cover" else (Y + 36, "middle")
        lx = px - 6 if kind == "cover" else px
        s += f'<text x="{lx}" y="{ly}" text-anchor="{anc}" font-family="Montserrat" font-weight="700" font-size="16" letter-spacing="3" fill="{col if light else "#C0592C"}">{lbl.upper()}</text>'
    else:
        s += f'<circle class="pulse" cx="540" cy="{Y}" r="8" fill="none" stroke="#FF8A5C" stroke-width="2.5"/><circle cx="540" cy="{Y}" r="7" fill="#FF8A5C" stroke="#fff" stroke-width="2.5"/>'
    return s + BOAT.replace("{w}", "#FBF4EC" if light else "#7BA7B6") + "</svg>"
for i in range(1, 11):
    kind = "cover" if i == 1 else "end" if i == 10 else "mid"
    marker = f'id="bahuluang-{i:02d}">'
    html = html.replace(marker, marker + svg(kind), 1)
JS = """<script>
const T=6, Y=%d;
function ease(u){return u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2}
window.setT=function(t){
  const ph=t/T*2*Math.PI;
  document.querySelectorAll('.ph img:first-child,.fc .bgf').forEach(im=>im.style.transform=`scale(${1.045+0.035*Math.sin(ph)})`);
  document.querySelectorAll('.pulse').forEach(c=>{const u=(t%%1.5)/1.5;c.setAttribute('r',8+u*18);c.setAttribute('opacity',1-u)});
  document.querySelectorAll('.rt').forEach(s=>{
    const k=s.dataset.kind; let x;
    if(k==='cover'){x=84+(1080+120-84)*ease(Math.min(t/5,1));}
    else if(k==='end'){x=-70+(150-58+70)*ease(Math.min(t/3.2,1));}
    else{x=-70+(1080+140)*Math.min(t/5,1);}
    const b=s.querySelector('.boat'); b.setAttribute('transform',`translate(${x} ${Y-9}) scale(.85)`);
    s.querySelector('.bob').setAttribute('transform',`translate(0 ${2.2*Math.sin(t*2*Math.PI/1.5)}) rotate(${1.6*Math.sin(t*2*Math.PI/1.5+1)})`);
  });
};
</script>""" % (Y - 0)
html = html.replace("</style>", CSS + "</style>", 1).replace("</body>", JS + "</body>")
(H / "bahuluang_motion.html").write_text(html)
print("ok")
