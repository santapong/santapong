#!/usr/bin/env python3
"""Build self-contained GitHub artwork, preserving the supplied logo pixels."""
import argparse
import base64
import hashlib
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGO = ROOT / 'assets/brand/draveniq-inside-the-coil.png'
LOGO_SHA256 = '4db41e57f2d752a92290aeb29687e0be196c1f591d447c7c151c734ffe2f9bf1'
NAVY, WHITE, AZURE, ICE, COBALT, CORAL = '#060A12', '#EDF3F5', '#168BEE', '#72D7FF', '#2052C8', '#ED8179'
THEMES = {
    'dark': dict(bg=NAVY, text=WHITE, muted='#A9BDD0', accent=ICE),
    'light': dict(bg=WHITE, text=NAVY, muted='#42566C', accent=COBALT),
}


def svg_open(width, height, title, description):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<defs><linearGradient id="blue" x1="0" y1="0" x2="1" y2=".35"><stop stop-color="{ICE}"/><stop offset=".5" stop-color="{AZURE}"/><stop offset="1" stop-color="{COBALT}"/></linearGradient>
<pattern id="grid" width="42" height="42" patternUnits="userSpaceOnUse"><path d="M42 0H0V42" fill="none" stroke="{ICE}" stroke-opacity=".065"/></pattern></defs>'''


def build_cover(theme, logo_data, *, mobile=False, animated=False):
    c = THEMES[theme]
    w, h = (800, 820) if mobile else (1600, 640)
    p = [svg_open(w, h, 'Santapong Sondhi / DraveNIQ',
        'Software, AI and robotics engineer from Thailand. Build with curiosity. Learn by making. Long-term ambition: embodied AGI and general-purpose humanoid robots. Original DraveNIQ dragon and wordmark.')]
    p.append(f'<rect width="{w}" height="{h}" rx="22" fill="{c["bg"]}"/>')
    if animated:
        p.append('''<style>
/* All content and logo stay still. The decorative line draws once, then rests. */
@media (prefers-reduced-motion: no-preference) {
 .trace { animation: draw 3.6s ease-out 1 both; }
}
@keyframes draw { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
</style>''')
    if mobile:
        p.append(f'''<g font-family="Arial, Helvetica, sans-serif">
<text x="48" y="63" fill="{c['accent']}" font-size="20" letter-spacing="3">ENGINEER / BUILDER / EXPLORER</text>
<text x="44" y="140" fill="{c['text']}" font-size="62" font-weight="700" letter-spacing="-2">Santapong Sondhi</text>
<text x="48" y="235" fill="{c['text']}" font-size="58" font-weight="700" letter-spacing="-2">Build with curiosity.</text>
<text x="48" y="305" fill="{c['accent']}" font-size="58" font-weight="700" letter-spacing="-2">Learn by making.</text></g>
<rect x="48" y="346" width="704" height="307" rx="16" fill="{NAVY}"/>
<image x="170" y="349" width="460" height="306.6667" preserveAspectRatio="xMidYMid meet" xlink:href="{logo_data}"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="48" y="710" fill="{c['muted']}" font-size="26">Software, AI &amp; robotics · Thailand</text>
<text x="48" y="765" fill="{c['accent']}" font-size="22">Toward embodied AI &amp; humanoid robotics</text></g>
<path d="M48 796H752" fill="none" stroke="url(#blue)" stroke-width="3"/>''')
    else:
        p.append(f'''<rect x="1030" y="32" width="538" height="576" rx="16" fill="{NAVY}" stroke="#1C3048"/>
<image x="1034" y="50" width="530" height="353.3333" preserveAspectRatio="xMidYMid meet" xlink:href="{logo_data}"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="72" y="73" fill="{c['accent']}" font-size="20" letter-spacing="3.4">ENGINEER / BUILDER / EXPLORER</text>
<text x="65" y="174" fill="{c['text']}" font-size="89" font-weight="700" letter-spacing="-3">Santapong Sondhi</text>
<text x="72" y="295" fill="{c['text']}" font-size="72" font-weight="700" letter-spacing="-2.5">Build with curiosity.</text>
<text x="72" y="383" fill="{c['accent']}" font-size="72" font-weight="700" letter-spacing="-2.5">Learn by making.</text>
<text x="74" y="442" fill="{c['muted']}" font-size="27">Software, AI &amp; robotics · Thailand</text>
<text x="74" y="559" fill="{c['muted']}" font-size="19" letter-spacing="1.4">EMBODIED AI / ROBOT LEARNING / DEVELOPER TOOLS</text>
<circle cx="1080" cy="452" r="5" fill="{CORAL}"/>
<text x="1100" y="458" fill="{ICE}" font-size="16" letter-spacing="2.4">MY NORTH STAR</text>
<text x="1075" y="512" fill="{WHITE}" font-size="31" font-weight="700">Intelligence that can</text>
<text x="1075" y="554" fill="{WHITE}" font-size="31" font-weight="700">learn, adapt &amp; act.</text></g>
<path class="trace" d="M74 493H951" pathLength="1" stroke-dasharray="1" fill="none" stroke="url(#blue)" stroke-width="3"/>''')
    p.append('</svg>')
    return '\n'.join(p) + '\n'


PROJECTS = [
    ('rlm', '01', 'RESEARCH / PRIVATE', 'RLM', 'Make robot experiments repeatable.', 'EPISODES / POLICIES / EVALUATION',
     '''<path d="M1040 111C1110 35 1295 37 1350 112M1381 163C1455 247 1350 315 1275 292M1187 290C1080 318 1018 252 1052 187" stroke-dasharray="9 10"/>
<rect x="1030" y="92" width="150" height="88" rx="13"/><rect x="1292" y="92" width="150" height="88" rx="13"/><rect x="1162" y="235" width="150" height="88" rx="13"/>
<path d="M1056 119H1153M1056 136H1125M1056 153H1140M1320 136H1414M1193 275L1216 294L1259 259"/>
<circle cx="1330" cy="136" r="6" fill="#ED8179"/><circle cx="1367" cy="136" r="6" fill="#72D7FF"/><circle cx="1404" cy="136" r="6" fill="#72D7FF"/>'''),
    ('robollm', '02', 'RESEARCH / ROBOTICS WORKBENCH', 'RoboLLM', 'Connect perception, language & action.', 'ROS 2 / MUJOCO / VISION-LANGUAGE-ACTION',
     '''<path d="M1065 307H1420M1180 299V264L1110 203L1202 101L1298 168L1352 154M1349 143L1381 154L1385 181M1355 170L1371 194" stroke-width="10"/>
<circle cx="1110" cy="203" r="18" fill="#060A12"/><circle cx="1202" cy="101" r="18" fill="#060A12"/><circle cx="1298" cy="168" r="13" fill="#060A12"/>
<rect x="1014" y="83" width="94" height="61" rx="11"/><circle cx="1048" cy="114" r="15"/><path d="M1108 103L1132 93V137L1108 127M1352 243L1395 219L1438 243V287L1395 312L1352 287ZM1352 243L1395 268L1438 243M1395 268V312"/>
<path d="M1225 54H1370M1240 39H1385" opacity=".25"/>'''),
    ('cooker', '03', 'ENGINEERING / DEVELOPER TOOLS', 'Cooker', 'Turn source code into running systems.', 'BUILD / REVIEW / DEPLOY',
     '''<path d="M1027 187H1450" stroke-dasharray="8 9"/>
<rect x="1014" y="140" width="98" height="96" rx="15"/><rect x="1188" y="140" width="98" height="96" rx="15"/><rect x="1362" y="140" width="98" height="96" rx="15"/>
<path d="M1047 170L1033 187L1047 204M1079 170L1093 187L1079 204M1070 165L1057 210M1215 187L1230 202L1260 171M1390 183L1411 171L1432 183V210L1411 222L1390 210ZM1390 183L1411 195L1432 183M1411 195V222"/>
<path d="M1237 139V91H1411V139" opacity=".45"/><circle cx="1237" cy="91" r="5" fill="#ED8179"/>
<path d="M1063 261V284H1411V261" opacity=".25"/>'''),
    ('keepsave', '04', 'ENGINEERING / DEVELOPER TOOLS', 'KeepSave', 'Keep access deliberate. Keep secrets safe.', 'VAULT / IDENTITY / RECOVERY',
     '''<rect x="1080" y="65" width="205" height="245" rx="27"/><rect x="1097" y="83" width="171" height="209" rx="18" opacity=".35"/>
<circle cx="1182" cy="177" r="42"/><path d="M1182 166V196" stroke-width="11"/><circle cx="1182" cy="161" r="9" fill="#72D7FF"/>
<path d="M1285 121H1340V90H1373M1285 188H1373M1285 254H1340V286H1373" opacity=".55"/>
<g stroke="#ED8179"><rect x="1373" y="68" width="53" height="45" rx="9"/><rect x="1373" y="166" width="53" height="45" rx="9"/><rect x="1373" y="264" width="53" height="45" rx="9"/>
<path d="M1386 90L1396 99L1413 80M1386 188L1396 197L1413 178M1386 286L1396 295L1413 276"/></g>'''),
]


def build_project(item):
    slug, number, category, name, tagline, topics, drawing = item
    p = [svg_open(1600, 360, f'{name} / {tagline}', 'Original conceptual project illustration, not a product screenshot or experimental result.'),
         f'<rect width="1600" height="360" rx="18" fill="{NAVY}"/>',
         '<path d="M968 0H1600V360H968Z" fill="url(#grid)"/>',
         '<path d="M960 44V316" stroke="#24364A"/>',
         f'<g fill="none" stroke="{ICE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{drawing}</g>',
         f'''<g font-family="Arial, Helvetica, sans-serif">
<text x="64" y="61" fill="{CORAL}" font-size="20" letter-spacing="2">{number}</text>
<text x="111" y="61" fill="#A9BDD0" font-size="18" letter-spacing="2.2">{escape(category)}</text>
<text x="59" y="157" fill="{WHITE}" font-size="82" font-weight="700" letter-spacing="-2.5">{name}</text>
<text x="64" y="218" fill="{ICE}" font-size="33">{escape(tagline)}</text>
<text x="64" y="300" fill="#A9BDD0" font-size="19" letter-spacing="1.3">{escape(topics)}</text></g>
<path d="M64 335H1536" stroke="url(#blue)" stroke-width="2" opacity=".65"/>
</svg>''']
    return '\n'.join(p) + '\n'


def outputs():
    logo = LOGO.read_bytes()
    if hashlib.sha256(logo).hexdigest() != LOGO_SHA256:
        raise SystemExit('Supplied logo differs from the reviewed source; reconcile before generating.')
    data = 'data:image/png;base64,' + base64.b64encode(logo).decode('ascii')
    for theme in THEMES:
        yield f'assets/profile-cover-{theme}.svg', build_cover(theme, data, animated=True)
        yield f'assets/profile-cover-{theme}-static.svg', build_cover(theme, data)
        yield f'assets/profile-cover-mobile-{theme}.svg', build_cover(theme, data, mobile=True)
    for item in PROJECTS:
        yield f'assets/projects/{item[0]}.svg', build_project(item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify generated files without writing.')
    args = parser.parse_args()
    for name, content in outputs():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise SystemExit(f'Out of date: {name}')
        else:
            path.write_text(content)
        print(('Checked ' if args.check else 'Built ') + name)
