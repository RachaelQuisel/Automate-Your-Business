import subprocess, pathlib
from PIL import Image
OUT = pathlib.Path(__file__).resolve().parent.parent  # the visuals/ folder
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{font-family:'Source Sans 3','Source Sans Pro',sans-serif;color:#202B33;background:#FBF8F3;position:relative;overflow:hidden}
.wrap{position:absolute;inset:0;padding:96px 96px 0 96px;display:flex;flex-direction:column}
.eyebrow{font-family:'Manrope';font-weight:700;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:#286575;margin-bottom:40px}
h1{font-family:'Manrope';font-weight:800;font-size:104px;line-height:1.02;letter-spacing:-.03em}
h2{font-family:'Manrope';font-weight:800;font-size:76px;line-height:1.06;letter-spacing:-.02em}
.sub{font-size:48px;line-height:1.3;color:#4D5B66;margin-top:44px}
.body{font-size:44px;line-height:1.38;color:#2c3a44;margin-top:44px}
.src{font-size:28px;line-height:1.4;color:#596874;margin-top:auto;margin-bottom:150px;border-left:6px solid #286575;padding-left:24px}
.foot{position:absolute;left:96px;right:96px;bottom:64px;display:flex;justify-content:space-between;align-items:center;font-family:'Manrope';font-weight:600;font-size:26px;color:#596874}
.dots{display:flex;gap:12px}.dots i{width:14px;height:14px;border-radius:50%;background:#CCD5DD;display:block}.dots i.on{background:#286575}
.bar{position:absolute;left:0;top:0;width:100%;height:18px;background:#286575}
.aqua{color:#286575}
.list{margin-top:48px;display:flex;flex-direction:column;gap:22px}
.row{display:flex;gap:28px;align-items:flex-start;background:#fff;border:2px solid #E2E8EE;border-radius:22px;padding:26px 32px}
.num{font-family:'Manrope';font-weight:800;font-size:44px;color:#286575;width:48px;flex:none}
.row b{font-family:'Manrope';font-weight:800;font-size:40px;display:block}
.row span{font-size:32px;color:#4D5B66;line-height:1.3}
.row.hl{background:#286575;border-color:#286575}.row.hl b,.row.hl span,.row.hl .num{color:#fff}
.tag{display:inline-block;margin-top:8px;font-family:'Manrope';font-weight:700;font-size:24px;background:#F3D9A4;color:#202B33;border-radius:999px;padding:6px 18px}
.grid .row{padding:22px 30px}.grid .row b{font-size:30px;width:250px;flex:none;color:#286575}.grid .row span{font-size:33px;color:#202B33}
.grid .row.hl span{color:#fff}
.cover{background:#1D4E5B;color:#fff}.cover .eyebrow{color:#F3D9A4}.cover .sub{color:#d5e3e7}.cover .foot{color:#bcd2d8}.cover .dots i{background:#3d6f7c}.cover .dots i.on{background:#F3D9A4}
.big{font-family:'Manrope';font-weight:800;font-size:96px;line-height:1.05;letter-spacing:-.02em}
.swipe{font-family:'Manrope';font-weight:700;font-size:30px;color:#F3D9A4}
.cta{margin-top:auto;margin-bottom:170px;background:#fff;border-radius:26px;padding:40px 44px;border:2px solid #E2E8EE}
.cta p{font-size:38px;line-height:1.35}.cta .flow{font-family:'Manrope';font-weight:700;font-size:30px;color:#286575;margin-top:18px}
"""
N=6
def dots(i): return '<div class="dots">'+''.join(f'<i class="{"on" if k==i else ""}"></i>' for k in range(1,N+1))+'</div>'
def foot(i, right=None):
    return f'<div class="foot"><span>Rachael Quisel · airbnbai.rent</span>{right or dots(i)}</div>'
slides = []
slides.append(('cover', f'''<div class="wrap"><div class="eyebrow">Notes from Lenny's Podcast</div>
<h1>Most automations skip one part.</h1><div class="sub">It's the part that matters most. Here's what a podcast episode taught me about building loops for my vacation rental.</div></div><svg style="position:absolute;left:96px;bottom:120px" width="888" height="560" viewBox="0 0 888 560"><circle cx="444" cy="330" r="185" fill="none" stroke="#3d6f7c" stroke-width="6" stroke-dasharray="14 12"/><circle cx="444" cy="145" r="22" fill="#3d7a8a"/><text x="444" y="103" text-anchor="middle" font-family="Manrope" font-weight="700" font-size="30" fill="#bcd2d8">Trigger</text><circle cx="620" cy="273" r="22" fill="#3d7a8a"/><text x="666" y="283" text-anchor="start" font-family="Manrope" font-weight="700" font-size="30" fill="#bcd2d8">Steps</text><circle cx="553" cy="480" r="22" fill="#3d7a8a"/><text x="599" y="490" text-anchor="start" font-family="Manrope" font-weight="700" font-size="30" fill="#bcd2d8">Decision</text><circle cx="335" cy="480" r="22" fill="#3d7a8a"/><text x="289" y="490" text-anchor="end" font-family="Manrope" font-weight="700" font-size="30" fill="#bcd2d8">Output</text><circle cx="268" cy="273" r="30" fill="#F3D9A4"/><text x="222" y="283" text-anchor="end" font-family="Manrope" font-weight="700" font-size="30" fill="#F3D9A4">Escape hatch</text></svg>
<div class="foot"><span>Rachael Quisel · airbnbai.rent</span><span class="swipe">Swipe →</span></div>'''))
slides.append(('', f'''<div class="bar"></div><div class="wrap"><div class="eyebrow">The idea</div>
<h2>Recurring work is turning into <span class="aqua">loops.</span></h2>
<div class="body">Anish Acharya (a16z) described AI agents taking a bug report through reproduction, a fix, review, deployment, and a customer email in about five minutes.</div>
<div class="body">Humans still own sales, strategy, exceptions, and deciding what's worth building.</div>
<div class="src">From my Snipd notes · Lenny's Podcast, "Why companies are becoming a series of loops" (paraphrased)</div></div>{foot(2)}'''))
slides.append(('', f'''<div class="bar"></div><div class="wrap"><div class="eyebrow">The detail I keep thinking about</div>
<div class="big">Kavak's AI agents <span class="aqua">call a human</span> when they get stuck.</div>
<div class="body">The human's coaching resolves the case and leaves a trace, so the agent is less likely to repeat the mistake.</div>
<div class="body"><b>Getting stuck is part of the design.</b></div>
<div class="src">Anecdote from the same episode (paraphrased from my Snipd notes)</div></div>{foot(3)}'''))
rows=[('1','Trigger','The event that starts it, not someone remembering'),('2','Steps','What happens, in order, every time'),('3','Decision','The one fork: one question, two answers'),('4','Output','What exists when it finishes')]
r=''.join(f'<div class="row"><div class="num">{n}</div><div><b>{t}</b><span>{d}</span></div></div>' for n,t,d in rows)
r+='<div class="row hl"><div class="num">5</div><div><b>Escape hatch</b><span>What happens when it gets stuck, and who it tells</span><br><span class="tag">The one most people skip</span></div></div>'
slides.append(('', f'''<div class="bar"></div><div class="wrap"><div class="eyebrow">The Loop Audit</div>
<h2>A loop has five parts.</h2><div class="list">{r}</div></div>{foot(4)}'''))
g=[('Trigger','A day someone is on the schedule'),('Steps','Gather assigned staff, contractor work, arrivals'),('Decision','Guest arriving? Name them, or "No guest checking in"'),('Output','One text, up to once a day')]
gr=''.join(f'<div class="row"><b>{t}</b><span>{d}</span></div>' for t,d in g)
gr+='<div class="row hl"><b style="color:#F3D9A4">Escape hatch</b><span>Still designing it. That\'s the honest answer.</span></div>'
slides.append(('', f'''<div class="bar"></div><div class="wrap"><div class="eyebrow">My test case</div>
<h2>The daily staff text at La&nbsp;Maison</h2><div class="list grid">{gr}</div>
<div class="body" style="font-size:36px;margin-top:36px">Running the audit showed me where this loop is most likely to break first.</div></div>{foot(5)}'''))
slides.append(('', f'''<div class="bar"></div><div class="wrap"><div class="eyebrow">The check</div>
<div class="big">Will a human find out when it fails?</div>
<div class="sub">If not, that's likely where the loop breaks first.</div>
<div class="cta"><p>Pick one recurring job in your business this week and map it.</p>
<div class="flow">Trigger → Steps → Decision → Output → Escape hatch</div></div></div>{foot(6)}'''))
pngs=[]
for i,(cls,html) in enumerate(slides,1):
    p=pathlib.Path(f'slide{i}.html'); p.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}">{html}</body></html>')
    out=OUT/f'loop-carousel-{i:02d}.png'
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=1',f'--window-size=1080,1350',f'--screenshot={out}',f'file://{p.resolve()}'],check=True,capture_output=True)
    pngs.append(out)
ims=[Image.open(x).convert('RGB') for x in pngs]
print([im.size for im in ims])
ims[0].save(OUT/'loop-carousel.pdf',save_all=True,append_images=ims[1:],resolution=144)
