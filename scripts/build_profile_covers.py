#!/usr/bin/env python3
"""Build the profile's self-contained animated and still SVG headers."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    'dark': dict(bg='#0d1117', text='#f1f4f8', muted='#a5adba', line='#303844', panel='#151c26', accent='#c6b3f2', grid='#a7b1c2'),
    'light': dict(bg='#f5f7fa', text='#1f2937', muted='#586779', line='#d6dee8', panel='#ffffff', accent='#65509b', grid='#6b7a90'),
}
LINES = [
    'Building toward intelligent humanoid robots.',
    'Exploring embodied AI and robot learning.',
    'Making ideas real, one system at a time.',
]
STILL = 'Building toward embodied AGI and humanoid robots.'
PROJECTS = [
    ('RLM', 'ROBOT EXPERIMENTS', 1040, 57, '#6fc6a4'),
    ('RoboLLM', 'PERCEPTION & CONTROL', 1300, 57, '#65aef0'),
    ('Cooker', 'SOFTWARE DELIVERY', 1040, 224, '#ecaa70'),
    ('KeepSave', 'SECRETS & ACCESS', 1300, 224, '#b09ae4'),
]


def build(theme: str, animated: bool) -> str:
    c = THEMES[theme]
    motion_description = ('The headline types through three statements; reduced motion shows the complete ambition instead.' if animated else 'This is the complete still-text version of the banner.')
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="380" viewBox="0 0 1600 380" role="img" aria-labelledby="title desc">
<title id="title">Santapong Sondhi — building toward embodied AGI and humanoid robots</title>
<desc id="desc">Software, AI and robotics engineer. Long-term ambition: embodied AGI and general-purpose humanoid robots. Current projects: RLM, RoboLLM, Cooker and KeepSave. {motion_description}</desc>
<defs>
<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{c['grid']}" opacity=".09"/></pattern>''']
    if animated:
        for i in range(len(LINES)):
            parts.append(f'<clipPath id="line-{i}" clipPathUnits="userSpaceOnUse"><rect class="reveal phase-{i}" x="76" y="207" width="0" height="46"/></clipPath>')
    parts.append('</defs>')
    if animated:
        parts.append('''<style>
/* Complete, still text is the default if motion is reduced or CSS is unavailable. */
@media (prefers-reduced-motion: no-preference) {
  .motion { display: inline; }
  .still { display: none; }
  .reveal { animation: type-cycle 18s steps(48, end) infinite; }
  .phase-1 { animation-delay: 6s; }
  .phase-2 { animation-delay: 12s; }
}
@keyframes type-cycle {
  0%, 1% { width: 0; }
  14%, 26% { width: 800px; }
  32%, 100% { width: 0; }
}
</style>''')
    parts.append(f'''<rect width="1600" height="380" rx="16" fill="{c['bg']}"/>
<rect width="1600" height="380" rx="16" fill="url(#dots)"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="76" y="65" fill="{c['muted']}" font-size="17" letter-spacing="3">SOFTWARE / AI / ROBOTICS</text>
<text x="72" y="149" fill="{c['text']}" font-size="78" font-weight="700" letter-spacing="-2">Santapong Sondhi</text>
<text x="76" y="188" fill="{c['muted']}" font-size="21">Engineer. Builder. Exploring what intelligence can become.</text>
</g>
<g font-family="Consolas, Liberation Mono, monospace" font-size="26" fill="{c['accent']}">
<text class="still" x="76" y="239">{escape(STILL)}</text>''')
    if animated:
        parts.append('<g class="motion" display="none">')
        for i, line in enumerate(LINES):
            parts.append(f'<text x="76" y="239" clip-path="url(#line-{i})">{escape(line)}</text>')
        parts.append('</g>')
    parts.append(f'''</g>
<path d="M76 279H154" stroke="{c['accent']}" stroke-width="3"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="76" y="323" fill="{c['muted']}" font-size="17" letter-spacing="1">NORTH STAR: EMBODIED AGI + HUMANOID ROBOTICS</text>
<text x="1039" y="35" fill="{c['muted']}" font-size="13" letter-spacing="2">WHAT I'M BUILDING TODAY</text>
</g>
<g fill="none" stroke="{c['line']}" stroke-width="2"><path d="M1138 116H1398V265H1138Z"/><path d="M1138 116L1398 265M1398 116L1138 265" stroke-dasharray="5 8"/></g>''')
    for name, label, x, y, accent in PROJECTS:
        parts.append(f'''<g transform="translate({x} {y})"><rect width="216" height="112" rx="12" fill="{c['panel']}" stroke="{c['line']}"/><rect x="18" y="21" width="7" height="7" rx="2" fill="{accent}"/><g font-family="Arial, Helvetica, sans-serif"><text x="18" y="66" fill="{c['text']}" font-size="31" font-weight="700">{name}</text><text x="18" y="91" fill="{c['muted']}" font-size="11" letter-spacing="1.15">{escape(label)}</text></g></g>''')
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    for theme in THEMES:
        for animated in (True, False):
            suffix = '' if animated else '-static'
            (ROOT / f'assets/profile-cover-{theme}{suffix}.svg').write_text(build(theme, animated))
