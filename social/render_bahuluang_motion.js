// Render carousel bergerak ke MP4 (1080x1350, 30 fps, 6 detik loop). Usage: node social/render_bahuluang_motion.js [01,02,...]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs'); const { spawn } = require('child_process');
const FPS = 30, T = 6, only = process.argv[2] ? process.argv[2].split(',') : null;
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'bahuluang-motion'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'bahuluang_motion.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const ids = await p.$$eval('.t', ts => ts.map(t => t.id));
  for (const id of ids) {
    if (only && !only.includes(id.slice(-2))) continue;
    await p.evaluate(id => document.querySelectorAll('.t').forEach(t => t.style.display = t.id === id ? 'block' : 'none'), id);
    const file = path.join(out, id + '.mp4');
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-r', String(FPS), '-i', '-',
      '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
      '-c:a', 'aac', '-movflags', '+faststart', file]);
    for (let f = 0; f < FPS * T; f++) {
      await p.evaluate(t => window.setT(t), f / FPS);
      const buf = await p.screenshot({ type: 'jpeg', quality: 95, clip: { x: 0, y: 0, width: 1080, height: 1350 } });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r)); console.log('saved', id);
  }
  await b.close();
})();
