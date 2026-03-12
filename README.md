<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 🖥️  SANTAPONG OS v3.0 — GitHub Profile README                 -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<!-- ▓▓▓ ANIMATED SVG BOOT HEADER ▓▓▓ -->
<svg width="840" height="280" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0e17"/>
      <stop offset="50%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#0a0e17"/>
    </linearGradient>
    <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00ff41">
        <animate attributeName="stop-color" values="#00ff41;#58a6ff;#bc8cff;#f778ba;#00ff41" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="33%" stop-color="#58a6ff">
        <animate attributeName="stop-color" values="#58a6ff;#bc8cff;#f778ba;#00ff41;#58a6ff" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="66%" stop-color="#bc8cff">
        <animate attributeName="stop-color" values="#bc8cff;#f778ba;#00ff41;#58a6ff;#bc8cff" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#f778ba">
        <animate attributeName="stop-color" values="#f778ba;#00ff41;#58a6ff;#bc8cff;#f778ba" dur="8s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <linearGradient id="scanLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00ff41" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00ff41" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#00ff41" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="borderGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00ff41" stop-opacity="0.6">
        <animate attributeName="stop-opacity" values="0.6;0.2;0.6" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#58a6ff" stop-opacity="0.4">
        <animate attributeName="stop-opacity" values="0.4;0.7;0.4" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#bc8cff" stop-opacity="0.6">
        <animate attributeName="stop-opacity" values="0.6;0.2;0.6" dur="3s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <!-- Glow filter -->
    <filter id="glow">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Dot pattern -->
    <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.5" fill="#00ff41" opacity="0.08"/>
    </pattern>
    <!-- Particle -->
    <circle id="p" r="1.2" fill="#00ff41" opacity="0.5"/>
  </defs>

  <!-- Background -->
  <rect width="840" height="280" fill="url(#bgGrad)" rx="16"/>
  <!-- Animated border -->
  <rect x="1" y="1" width="838" height="278" rx="15" fill="none" stroke="url(#borderGlow)" stroke-width="1.5"/>
  <!-- Dot overlay -->
  <rect width="840" height="280" fill="url(#dots)" rx="16"/>

  <!-- Grid lines -->
  <g opacity="0.03" stroke="#58a6ff" stroke-width="0.5">
    <line x1="0" y1="56" x2="840" y2="56"/><line x1="0" y1="112" x2="840" y2="112"/>
    <line x1="0" y1="168" x2="840" y2="168"/><line x1="0" y1="224" x2="840" y2="224"/>
    <line x1="168" y1="0" x2="168" y2="280"/><line x1="336" y1="0" x2="336" y2="280"/>
    <line x1="504" y1="0" x2="504" y2="280"/><line x1="672" y1="0" x2="672" y2="280"/>
  </g>

  <!-- ══ Quantum circuit LEFT ══ -->
  <g opacity="0.12" stroke="#58a6ff" fill="none" stroke-width="1">
    <line x1="25" y1="55" x2="25" y2="155"/>
    <line x1="55" y1="55" x2="55" y2="155"/>
    <line x1="85" y1="55" x2="85" y2="155"/>
    <!-- H gate -->
    <rect x="17" y="70" width="16" height="16" rx="2"/>
    <text x="25" y="82" text-anchor="middle" fill="#58a6ff" font-size="9" font-family="monospace">H</text>
    <!-- CNOT -->
    <circle cx="55" cy="78" r="5"/><circle cx="55" cy="78" r="1.5" fill="#58a6ff"/>
    <line x1="55" y1="78" x2="85" y2="78"/>
    <circle cx="85" cy="78" r="6"/><line x1="85" y1="72" x2="85" y2="84"/><line x1="79" y1="78" x2="91" y2="78"/>
    <!-- Z gate -->
    <rect x="17" y="105" width="16" height="16" rx="2"/>
    <text x="25" y="117" text-anchor="middle" fill="#58a6ff" font-size="9" font-family="monospace">Z</text>
    <!-- Measurement -->
    <rect x="47" y="105" width="16" height="16" rx="2"/>
    <path d="M50,117 Q55,109 60,117" stroke-width="0.8"/>
    <!-- T gate -->
    <rect x="77" y="105" width="16" height="16" rx="2"/>
    <text x="85" y="117" text-anchor="middle" fill="#58a6ff" font-size="9" font-family="monospace">T</text>
    <!-- Ket labels -->
    <text x="10" y="80" fill="#58a6ff" font-size="8" font-family="monospace" opacity="0.6">|0⟩</text>
    <text x="10" y="115" fill="#58a6ff" font-size="8" font-family="monospace" opacity="0.6">|1⟩</text>
  </g>

  <!-- ══ Quantum circuit RIGHT ══ -->
  <g opacity="0.12" stroke="#bc8cff" fill="none" stroke-width="1">
    <line x1="755" y1="55" x2="755" y2="155"/>
    <line x1="785" y1="55" x2="785" y2="155"/>
    <line x1="815" y1="55" x2="815" y2="155"/>
    <!-- X gate -->
    <rect x="747" y="70" width="16" height="16" rx="2"/>
    <text x="755" y="82" text-anchor="middle" fill="#bc8cff" font-size="9" font-family="monospace">X</text>
    <!-- Swap -->
    <line x1="780" y1="73" x2="790" y2="83"/><line x1="790" y1="73" x2="780" y2="83"/>
    <line x1="810" y1="73" x2="820" y2="83"/><line x1="820" y1="73" x2="810" y2="83"/>
    <line x1="785" y1="78" x2="815" y2="78" stroke-dasharray="2,2"/>
    <!-- RY gate -->
    <rect x="747" y="105" width="16" height="16" rx="2"/>
    <text x="755" y="117" text-anchor="middle" fill="#bc8cff" font-size="8" font-family="monospace">Ry</text>
    <!-- CNOT -->
    <circle cx="785" cy="113" r="5"/><circle cx="785" cy="113" r="1.5" fill="#bc8cff"/>
    <line x1="785" y1="113" x2="815" y2="113"/>
    <circle cx="815" cy="113" r="6"/><line x1="815" y1="107" x2="815" y2="119"/><line x1="809" y1="113" x2="821" y2="113"/>
    <!-- Ket labels -->
    <text x="822" y="80" fill="#bc8cff" font-size="8" font-family="monospace" opacity="0.6">⟨0|</text>
    <text x="822" y="115" fill="#bc8cff" font-size="8" font-family="monospace" opacity="0.6">⟨ψ|</text>
  </g>

  <!-- Floating particles -->
  <use href="#p" x="130" y="40"><animate attributeName="y" values="40;28;40" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.5;0.15;0.5" dur="4s" repeatCount="indefinite"/></use>
  <use href="#p" x="710" y="50"><animate attributeName="y" values="50;62;50" dur="3.2s" repeatCount="indefinite"/></use>
  <use href="#p" x="220" y="210"><animate attributeName="y" values="210;198;210" dur="5s" repeatCount="indefinite"/></use>
  <use href="#p" x="620" y="220"><animate attributeName="y" values="220;230;220" dur="3.8s" repeatCount="indefinite"/></use>
  <use href="#p" x="350" y="35"><animate attributeName="y" values="35;25;35" dur="4.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.3;0.6;0.3" dur="4.5s" repeatCount="indefinite"/></use>
  <use href="#p" x="490" y="42"><animate attributeName="y" values="42;34;42" dur="3.6s" repeatCount="indefinite"/></use>
  <use href="#p" x="160" y="170"><animate attributeName="y" values="170;160;170" dur="4.2s" repeatCount="indefinite"/></use>
  <use href="#p" x="680" y="165"><animate attributeName="y" values="165;175;165" dur="3.9s" repeatCount="indefinite"/></use>

  <!-- ══ BOOT SEQUENCE TEXT ══ -->
  <text x="420" y="42" text-anchor="middle" font-family="'Courier New',monospace" font-size="10" fill="#8b949e" opacity="0.5">
    [BOOT] loading modules... ████████████████████ OK
  </text>

  <!-- Main name -->
  <text x="420" y="98" text-anchor="middle" font-family="'Courier New',monospace" font-size="52" font-weight="bold" fill="url(#nameGrad)" filter="url(#glow)" letter-spacing="6">
    SANTAPONG
  </text>

  <!-- Subtitle -->
  <text x="420" y="132" text-anchor="middle" font-family="'Courier New',monospace" font-size="13" fill="#c9d1d9" letter-spacing="2">
    SOFTWARE ENGINEER  ·  AUTOMATION ARCHITECT  ·  QUANTUM EXPLORER
  </text>
  <!-- Blinking cursor -->
  <rect x="652" y="120" width="8" height="14" fill="#00ff41" filter="url(#softGlow)">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>

  <!-- Separator line -->
  <line x1="200" y1="155" x2="640" y2="155" stroke="#30363d" stroke-width="0.5"/>

  <!-- Location / status tags -->
  <g font-family="'Courier New',monospace" font-size="11">
    <rect x="185" y="168" width="100" height="22" rx="4" fill="#161b22" stroke="#30363d" stroke-width="0.5"/>
    <text x="235" y="183" text-anchor="middle" fill="#8b949e">📍 Thailand</text>

    <rect x="300" y="168" width="110" height="22" rx="4" fill="#161b22" stroke="#30363d" stroke-width="0.5"/>
    <text x="355" y="183" text-anchor="middle" fill="#3fb950">⚡ Online</text>

    <rect x="425" y="168" width="90" height="22" rx="4" fill="#161b22" stroke="#30363d" stroke-width="0.5"/>
    <text x="470" y="183" text-anchor="middle" fill="#8b949e">☕ ×  ∞</text>

    <rect x="530" y="168" width="125" height="22" rx="4" fill="#161b22" stroke="#30363d" stroke-width="0.5"/>
    <text x="593" y="183" text-anchor="middle" fill="#58a6ff">🛠️ Building</text>
  </g>

  <!-- Scan line -->
  <rect width="840" height="3" fill="url(#scanLine)">
    <animate attributeName="y" from="-3" to="280" dur="5s" repeatCount="indefinite"/>
  </rect>

  <!-- Bottom waveform decoration -->
  <g opacity="0.08" stroke="#00ff41" stroke-width="1" fill="none">
    <path d="M0,250 Q105,240 210,250 T420,250 T630,250 T840,250">
      <animate attributeName="d" values="M0,250 Q105,240 210,250 T420,250 T630,250 T840,250;M0,250 Q105,260 210,250 T420,250 T630,250 T840,250;M0,250 Q105,240 210,250 T420,250 T630,250 T840,250" dur="4s" repeatCount="indefinite"/>
    </path>
    <path d="M0,255 Q105,265 210,255 T420,255 T630,255 T840,255">
      <animate attributeName="d" values="M0,255 Q105,265 210,255 T420,255 T630,255 T840,255;M0,255 Q105,245 210,255 T420,255 T630,255 T840,255;M0,255 Q105,265 210,255 T420,255 T630,255 T840,255" dur="3.5s" repeatCount="indefinite"/>
    </path>
  </g>
</svg>

<br/>

<!-- Social badges row -->
[![Profile Views](https://komarev.com/ghpvc/?username=santapong&color=00ff41&style=flat-square&label=VISITORS)](https://github.com/santapong)
&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN)
&nbsp;&nbsp;
[![Email](https://img.shields.io/badge/EMAIL-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:your-email@example.com)
&nbsp;&nbsp;
[![YouTube](https://img.shields.io/badge/YOUTUBE-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/@YOUR_CHANNEL)

</div>

<!-- ═══════════════ ANIMATED DIVIDER ═══════════════ -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0e17,30:161b22,70:161b22,100:0a0e17&height=1"/>

<br/>

<!-- ═══════════════ TWO-COLUMN: INIT + STATUS ═══════════════ -->
<table>
<tr>
<td width="55%" valign="top">

### ⚡ `> ./init.py`

```python
class Santapong:
    """
    Turning caffeine into production systems
    since approximately forever.
    """
    
    def __init__(self):
        self.name       = "Santapong"
        self.role       = "Software Engineer"
        self.company    = "Ennovie"
        self.industry   = "Jewelry Manufacturing 💎"
        self.team       = "Digital Platforms & Automation"
        self.base       = "Thailand 🇹🇭"
        
    @property
    def education(self):
        return {
            "beng":   "KMITL — Mechatronics & Automation",
            "next":   "MSc Quantum Computing (2027)",
            "always": "curiosity-driven self-study",
        }
        
    @property
    def philosophy(self):
        return """
        cheap  + best     → ship it 🚀
        costly + marginal → hard pass ✋
        if it works, ships fast, costs less:
            that's the architecture.
        """

    def daily_loop(self):
        while self.coffee > 0:
            self.build_agents()
            self.automate_manufacturing()
            self.break_kubernetes()
            self.fix_kubernetes()      # ← usually here
            self.coffee -= 1
```

</td>
<td width="45%" valign="top">

### 📡 `> systemctl status`

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SANTAPONG OS v3.0                  ┃
┃  ════════════════════════════════   ┃
┃                                     ┃
┃  ◉ PROCESS: agentic-ai             ┃
┃    ██████████████░░░░░░  70%       ┃
┃    → MCP servers · LangChain       ┃
┃                                     ┃
┃  ◉ PROCESS: icpa-scheduler         ┃
┃    ████████████████░░░░  80%       ┃
┃    → production scheduling          ┃
┃                                     ┃
┃  ◉ PROCESS: quantum-prep           ┃
┃    ██████░░░░░░░░░░░░░░  30%       ┃
┃    → Qiskit · DisCoCat · QNLP     ┃
┃                                     ┃
┃  ◉ PROCESS: k8s-homelab            ┃
┃    ████████████████████  100%  ✓   ┃
┃    → 3× EQ13 · Dokploy            ┃
┃                                     ┃
┃  ◉ SYSTEM FUEL                      ┃
┃    ☕☕☕☕☕☕☕░░░░░░░  70%       ┃
┃                                     ┃
┃  ┌──────────────────────────────┐  ┃
┃  │  uptime: too long            │  ┃
┃  │  load:   yes                 │  ┃
┃  │  mood:   building things     │  ┃
┃  └──────────────────────────────┘  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

</td>
</tr>
</table>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0e17,30:161b22,70:161b22,100:0a0e17&height=1"/>

<br/>

### 🗺️ `> ls -la ~/active-quests/`

<table>
<tr>
<td width="50%">

<details open>
<summary>🤖 <code>MAIN QUEST</code> — <b>Agentic AI</b></summary>
<br/>

> **"Company as a Service"** — autonomous agents handling ops end-to-end

```
 ┌──────────────────────────────────────────┐
 │                ARCHITECTURE              │
 │                                          │
 │   ┌──────┐    ┌────────┐    ┌────────┐  │
 │   │ User │───▸│  n8n   │───▸│ Python │  │
 │   └──────┘    └───┬────┘    └───┬────┘  │
 │                   │             │        │
 │              ┌────▾────┐  ┌────▾─────┐  │
 │              │   LLM   │◂─│LangChain │  │
 │              └────┬────┘  └──────────┘  │
 │                   │                      │
 │         ┌─────────▾──────────┐           │
 │         │    MCP Servers     │           │
 │         │  ┌─────┐ ┌─────┐  │           │
 │         │  │ DB  │ │ API │  │           │
 │         │  └─────┘ └─────┘  │           │
 │         └────────────────────┘           │
 │                                          │
 │  STATUS: 🟢 Active    PRIORITY: ★★★★★  │
 └──────────────────────────────────────────┘
```

*Teaching robots to file paperwork so I don't have to.*

</details>

</td>
<td width="50%">

<details open>
<summary>📐 <code>MAIN QUEST</code> — <b>ICPA Scheduler</b></summary>
<br/>

> Production scheduling engine for jewelry manufacturing

```
 ┌──────────────────────────────────────────┐
 │              SCHEDULING ENGINE           │
 │                                          │
 │   ┌────────────────────────────────┐     │
 │   │      Sales Orders (input)     │     │
 │   └──────────────┬─────────────────┘     │
 │                  │                       │
 │        ┌─────────▾──────────┐            │
 │        │   Forward Pass     │            │
 │        │   ┌─────────────┐  │            │
 │        │   │ PRO Groups  │  │            │
 │        │   │ + Affinity  │  │            │
 │        │   └─────────────┘  │            │
 │        └─────────┬──────────┘            │
 │                  │                       │
 │        ┌─────────▾──────────┐            │
 │        │  Backward Pass     │            │
 │        │  + Line Locking    │            │
 │        └────────────────────┘            │
 │                                          │
 │  STATUS: 🟢 Active    PRIORITY: ★★★★★  │
 └──────────────────────────────────────────┘
```

*Global Left Shift algorithm, but make it jewelry.*

</details>

</td>
</tr>
<tr>
<td width="50%">

<details>
<summary>💰 <code>SIDE QUEST</code> — <b>Money Manager</b></summary>
<br/>

> Personal finance tracker — because spreadsheets have limits

```
 ┌──────────────────────────────────────────┐
 │                                          │
 │   ┌──────────┐      ┌────────┐          │
 │   │ Next.js  │─────▸│ Prisma │          │
 │   │  (UI)    │      │ (ORM)  │          │
 │   └──────────┘      └───┬────┘          │
 │                         │               │
 │                    ┌────▾──────┐         │
 │                    │PostgreSQL │         │
 │                    └───────────┘         │
 │                                          │
 │  STATUS: 🟡 In Progress                 │
 └──────────────────────────────────────────┘
```

*My bank account needed an API layer.*

</details>

</td>
<td width="50%">

<details>
<summary>🏠 <code>ENDLESS MODE</code> — <b>Home Lab</b></summary>
<br/>

> 3 tiny PCs in a closet running production workloads

```
 ┌──────────────────────────────────────────┐
 │           CLOSET INFRASTRUCTURE          │
 │                                          │
 │  ┌────────┐ ┌────────┐ ┌────────┐       │
 │  │ EQ13-1 │ │ EQ13-2 │ │ EQ13-3 │       │
 │  │ worker │ │ worker │ │  ctrl  │       │
 │  └───┬────┘ └───┬────┘ └───┬────┘       │
 │      └──────────┼──────────┘             │
 │            ┌────▾────┐                   │
 │            │   K8s   │                   │
 │            │ cluster │                   │
 │            └────┬────┘                   │
 │            ┌────▾────┐                   │
 │            │ Dokploy │                   │
 │            └─────────┘                   │
 │                                          │
 │  STATUS: 🟢 Running   UPTIME: 99.7%    │
 └──────────────────────────────────────────┘
```

*It's not hoarding if it's containers.*

</details>

</td>
</tr>
<tr>
<td colspan="2">

<details>
<summary>🔬 <code>NEW GAME+</code> — <b>Quantum Computing Prep</b> &nbsp; &nbsp; <i>MSc target: 2027</i></summary>
<br/>

> Understanding reality at the smallest scale, then making it useful.

```
 ┌──────────────────────────────────────────────────────────────────────────┐
 │                         QUANTUM RESEARCH TREE                           │
 │                                                                          │
 │   ┌──────────────┐     ┌──────────────┐     ┌──────────────────────┐    │
 │   │ Linear Alg.  │     │    Qiskit    │     │  Category Theory     │    │
 │   │ foundations   │     │  circuits    │     │  monoidal cats       │    │
 │   └──────┬───────┘     └──────┬───────┘     └──────────┬───────────┘    │
 │          │                    │                        │                │
 │          └────────────┬───────┘                        │                │
 │                  ┌────▾─────┐                          │                │
 │                  │ Quantum  │                          │                │
 │                  │ Mech.    │                          │                │
 │                  └────┬─────┘                          │                │
 │                       └──────────────┬─────────────────┘                │
 │                                 ┌────▾─────┐                            │
 │                                 │ DisCoCat │                            │
 │                                 └────┬─────┘                            │
 │                           ┌──────────▾──────────┐                       │
 │                           │  QNLP / lambeq      │                       │
 │                           │  DisCoPy toolkit     │                       │
 │                           └─────────────────────┘                       │
 │                                                                          │
 │   STATUS: 🔵 Studying                  TARGET: MSc 2027                 │
 └──────────────────────────────────────────────────────────────────────────┘
```

*Schrödinger's grad student — simultaneously applying and not applying.*

</details>

</td>
</tr>
</table>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0e17,30:161b22,70:161b22,100:0a0e17&height=1"/>

<br/>

### ⚔️ `> skill-tree --render --animated`

<!-- ANIMATED SVG SKILL BARS -->
<table>
<tr>
<td width="50%" valign="top">

<h4>🎯 Core Combat</h4>

<p><code>Python</code> <sup>main weapon</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="py" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#3776AB"/><stop offset="100%" stop-color="#FFD43B"/></linearGradient></defs><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="96%" height="10" rx="5" fill="url(#py)"><animate attributeName="width" from="0%" to="96%" dur="1.5s" fill="freeze"/></rect><text x="93%" y="8" font-size="7" fill="#0d1117" font-family="monospace" font-weight="bold">96%</text></svg>

<p><code>TypeScript</code> <sup>rising fast</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="88%" height="10" rx="5" fill="#3178C6"><animate attributeName="width" from="0%" to="88%" dur="1.5s" fill="freeze"/></rect><text x="85%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">88%</text></svg>

<p><code>SQL / KQL</code> <sup>data whisperer</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="80%" height="10" rx="5" fill="#58a6ff"><animate attributeName="width" from="0%" to="80%" dur="1.5s" fill="freeze"/></rect><text x="77%" y="8" font-size="7" fill="#0d1117" font-family="monospace" font-weight="bold">80%</text></svg>

<p><code>Power Platform</code> <sup>enterprise glue</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="72%" height="10" rx="5" fill="#742774"><animate attributeName="width" from="0%" to="72%" dur="1.5s" fill="freeze"/></rect><text x="69%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">72%</text></svg>

<h4>🧠 AI & Data</h4>

<p><code>LangChain / MCP</code> <sup>agent architect</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="80%" height="10" rx="5" fill="#1C8C3C"><animate attributeName="width" from="0%" to="80%" dur="1.5s" fill="freeze"/></rect><text x="77%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">80%</text></svg>

<p><code>pandas</code> <sup>old reliable</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="96%" height="10" rx="5" fill="#150458"><animate attributeName="width" from="0%" to="96%" dur="1.5s" fill="freeze"/></rect><text x="93%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">96%</text></svg>

<p><code>Microsoft Fabric</code> <sup>data lakehouse</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="72%" height="10" rx="5" fill="#F35325"><animate attributeName="width" from="0%" to="72%" dur="1.5s" fill="freeze"/></rect><text x="69%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">72%</text></svg>

</td>
<td width="50%" valign="top">

<h4>🏗️ Infrastructure</h4>

<p><code>Docker</code> <sup>second nature</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="96%" height="10" rx="5" fill="#2496ED"><animate attributeName="width" from="0%" to="96%" dur="1.5s" fill="freeze"/></rect><text x="93%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">96%</text></svg>

<p><code>Kubernetes</code> <sup>closet cluster</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="72%" height="10" rx="5" fill="#326CE5"><animate attributeName="width" from="0%" to="72%" dur="1.5s" fill="freeze"/></rect><text x="69%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">72%</text></svg>

<p><code>GitHub Actions</code> <sup>CI/CD wizard</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="80%" height="10" rx="5" fill="#2088FF"><animate attributeName="width" from="0%" to="80%" dur="1.5s" fill="freeze"/></rect><text x="77%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">80%</text></svg>

<p><code>Linux</code> <sup>home sweet home</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="96%" height="10" rx="5" fill="#FCC624"><animate attributeName="width" from="0%" to="96%" dur="1.5s" fill="freeze"/></rect><text x="93%" y="8" font-size="7" fill="#0d1117" font-family="monospace" font-weight="bold">96%</text></svg>

<h4>🌀 Exploring <sup>allocating skill points...</sup></h4>

<p><code>Qiskit</code> <sup>quantum baby steps</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="qi" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#6929C4"/><stop offset="100%" stop-color="#bc8cff"><animate attributeName="stop-color" values="#bc8cff;#6929C4;#bc8cff" dur="3s" repeatCount="indefinite"/></stop></linearGradient></defs><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="32%" height="10" rx="5" fill="url(#qi)"><animate attributeName="width" from="0%" to="32%" dur="1.5s" fill="freeze"/></rect><text x="29%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">32%</text></svg>

<p><code>Category Theory</code> <sup>brain melting (fun)</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="24%" height="10" rx="5" fill="#bc8cff"><animate attributeName="width" from="0%" to="24%" dur="1.5s" fill="freeze"/></rect><text x="21%" y="8" font-size="7" fill="#0d1117" font-family="monospace" font-weight="bold">24%</text></svg>

<p><code>QNLP / DisCoCat</code> <sup>yes, there's a cat 🐱</sup></p>
<svg width="100%" height="10" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="qn" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#f778ba"/><stop offset="100%" stop-color="#bc8cff"><animate attributeName="stop-color" values="#bc8cff;#f778ba;#bc8cff" dur="4s" repeatCount="indefinite"/></stop></linearGradient></defs><rect width="100%" height="10" rx="5" fill="#161b22"/><rect width="16%" height="10" rx="5" fill="url(#qn)"><animate attributeName="width" from="0%" to="16%" dur="1.5s" fill="freeze"/></rect><text x="12%" y="8" font-size="7" fill="#fff" font-family="monospace" font-weight="bold">16%</text></svg>

</td>
</tr>
</table>

<br/>

<details>
<summary>🛠️ <b>Full tech inventory</b> &nbsp; <i>(click to expand)</i></summary>
<br/>

<div align="center">

| | |
|:---|:---|
| **Languages** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white) ![KQL](https://img.shields.io/badge/KQL-0078D4?style=flat-square&logo=microsoftazure&logoColor=white) |
| **AI & Data** | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) ![Fabric](https://img.shields.io/badge/Fabric-F35325?style=flat-square&logo=microsoft&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white) |
| **Platform** | ![Power Apps](https://img.shields.io/badge/Power_Apps-742774?style=flat-square&logo=powerapps&logoColor=white) ![Dataverse](https://img.shields.io/badge/Dataverse-0B556A?style=flat-square&logo=microsoft&logoColor=white) ![BC](https://img.shields.io/badge/Business_Central-0078D4?style=flat-square&logo=dynamics365&logoColor=white) |
| **Infra** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![K8s](https://img.shields.io/badge/K8s-326CE5?style=flat-square&logo=kubernetes&logoColor=white) ![GH Actions](https://img.shields.io/badge/Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) |
| **Frontend** | ![Next.js](https://img.shields.io/badge/Next.js-000?style=flat-square&logo=next.js&logoColor=white) ![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black) ![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white) |
| **Quantum** | ![Qiskit](https://img.shields.io/badge/Qiskit-6929C4?style=flat-square&logo=qiskit&logoColor=white) ![DisCoPy](https://img.shields.io/badge/DisCoPy-ff6b6b?style=flat-square) ![lambeq](https://img.shields.io/badge/lambeq-bc8cff?style=flat-square) |

</div>

</details>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0e17,30:161b22,70:161b22,100:0a0e17&height=1"/>

<br/>

### 📜 `> git log --oneline --graph --education`

```
* a3f7e2b (HEAD -> life/next) 🎯 feat: Master's in Quantum Computing [2027]
|         Focus: QNLP · DisCoCat · Quantum Circuits
|         Status: Preparing...
|
* 7c1d5f9 (life/current) 📖 chore: self-study quantum + category theory [2025]
|         Stack: Qiskit · lambeq · DisCoPy · linear algebra
|         Status: In progress
|
* 0b2e5f1 (tag: v1.0) 🎓 feat: B.Eng. Mechatronics & Automation [2019]
|         Institution: KMITL (King Mongkut's)
|         Status: Completed ✓
|
* initial commit 🌱
```

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0e17,30:161b22,70:161b22,100:0a0e17&height=1"/>

<br/>

### 🖥️ `> neofetch --ascii`

```
                            ╭─ santapong@earth ────────────────────────────────╮
              .--.          │                                                   │
             |o_o |         │  OS       Thailand 64-bit (caffeinated edition)   │
             |:_/ |         │  Uptime   too long, send help                    │
            //   \ \        │  Shell    bash + zsh (can't commit to one)       │
           (|     | )       │  Editor   VS Code (fight me)                     │
          /'\_   _/`\       │  Nodes    3× Beelink EQ13 (closet datacenter)   │
          \___)=(___/       │  CPU      Coffee-powered neural network          │
                            │  GPU      Imagination.exe                        │
                            │  RAM      Mostly occupied by K8s pods            │
                            │  Theme    [████████] dark mode, obviously        │
                            │  Music    lo-fi beats to kubectl by              │
                            │                                                   │
                            ╰───────────────────────────────────────────────────╯
```

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0e17,30:161b22,70:161b22,100:0a0e17&height=1"/>

<br/>

### 📊 `> htop --github`

<div align="center">

<!-- Trophies -->
<img src="https://github-profile-trophy.vercel.app/?username=santapong&theme=algolia&no-bg=true&no-frame=true&column=7&margin-w=10" width="100%"/>

<br/><br/>

<a href="https://github.com/santapong">
  <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=santapong&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00ff41&icon_color=58a6ff&text_color=c9d1d9&ring_color=00ff41&include_all_commits=true&count_private=true" height="180" />
</a>
<a href="https://github.com/santapong">
  <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=santapong&layout=compact&hide_border=true&bg_color=0d1117&title_color=00ff41&text_color=c9d1d9&langs_count=8" height="180" />
</a>

<br/><br/>

<img width="90%" src="https://github-readme-streak-stats.herokuapp.com/?user=santapong&background=0d1117&ring=00ff41&fire=58a6ff&currStreakLabel=00ff41&sideLabels=c9d1d9&sideNums=c9d1d9&currStreakNum=c9d1d9&dates=8b949e&stroke=30363d&hide_border=true" />

<br/><br/>

<img width="95%" src="https://github-readme-activity-graph.vercel.app/graph?username=santapong&bg_color=0d1117&color=00ff41&line=58a6ff&point=bc8cff&area_color=00ff41&area=true&hide_border=true&custom_title=📡%20Contribution%20Signal" />

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0e17,30:161b22,70:161b22,100:0a0e17&height=1"/>

<br/>

<!-- ═══════════════ EASTER EGGS ═══════════════ -->

<details>
<summary>🥚 &nbsp; <i>there's something here... should you click it?</i></summary>
<br/>

<div align="center">

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║   🏆  ACHIEVEMENT UNLOCKED                  ║
 ║                                              ║
 ║   ▸ Title:   "CURIOUS VISITOR"              ║
 ║   ▸ Rarity:  Common                         ║
 ║   ▸ Reward:  A free quantum state           ║
 ║                                              ║
 ║        |ψ⟩ = α|0⟩ + β|1⟩                   ║
 ║                                              ║
 ║   It's both here and not here.              ║
 ║   Much like my weekend plans.               ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

</div>

<details>
<summary>🥚🥚 &nbsp; <i>OK but what if you keep going?</i></summary>
<br/>

<div align="center">

```
 ╔══════════════════════════════════════════════╗
 ║                                              ║
 ║   🏆🏆  RARE ACHIEVEMENT                    ║
 ║                                              ║
 ║   ▸ Title:   "WON'T STOP CLICKING"         ║
 ║   ▸ Rarity:  Uncommon                       ║
 ║   ▸ Reward:  My production formulas         ║
 ║                                              ║
 ║     output    = mass coffee × (1 - sleep)     ║
 ║     bugs      = 1 / (tests_written + 1)     ║
 ║     deadlines = ∞ × optimism                ║
 ║                                              ║
 ╚══════════════════════════════════════════════╝
```

</div>

<details>
<summary>🥚🥚🥚 &nbsp; <i>you're not seriously going to—</i></summary>
<br/>

<div align="center">

<!-- ANIMATED SECRET BADGE -->
<svg width="440" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="eggGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00ff41">
        <animate attributeName="stop-color" values="#00ff41;#58a6ff;#bc8cff;#f778ba;#00ff41" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#bc8cff">
        <animate attributeName="stop-color" values="#bc8cff;#f778ba;#00ff41;#58a6ff;#bc8cff" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <filter id="eggGlow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="440" height="200" fill="#0a0e17" rx="16" stroke="url(#eggGrad)" stroke-width="2"/>
  <text x="220" y="40" text-anchor="middle" font-family="monospace" font-size="15" fill="url(#eggGrad)" filter="url(#eggGlow)">🏆🏆🏆 LEGENDARY ACHIEVEMENT</text>
  <text x="220" y="70" text-anchor="middle" font-family="monospace" font-size="12" fill="#c9d1d9">"THE UNSTOPPABLE EXPLORER"</text>
  <line x1="120" y1="82" x2="320" y2="82" stroke="#30363d" stroke-width="0.5"/>
  <text x="220" y="108" text-anchor="middle" font-family="monospace" font-size="11" fill="#8b949e">You are hereby inducted into</text>
  <text x="220" y="130" text-anchor="middle" font-family="monospace" font-size="13" fill="url(#eggGrad)" filter="url(#eggGlow)">☕ The Secret Order of the Coffee Bean ☕</text>
  <text x="220" y="158" text-anchor="middle" font-family="monospace" font-size="10" fill="#8b949e">Member #∞ · Clearance: Maximum Curiosity</text>
  <text x="220" y="182" text-anchor="middle" font-family="monospace" font-size="10" fill="#3fb950">
    That's it. No more. Go build something. 🚀
  </text>
  <!-- Floating sparkles -->
  <circle cx="60" cy="100" r="2" fill="#00ff41" opacity="0.4">
    <animate attributeName="cy" values="100;90;100" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.4;0.1;0.4" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="380" cy="80" r="1.5" fill="#bc8cff" opacity="0.4">
    <animate attributeName="cy" values="80;70;80" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="400" cy="150" r="1" fill="#58a6ff" opacity="0.3">
    <animate attributeName="cy" values="150;142;150" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="40" cy="160" r="1.5" fill="#f778ba" opacity="0.3">
    <animate attributeName="cy" values="160;152;160" dur="2.2s" repeatCount="indefinite"/>
  </circle>
</svg>

</div>

</details>
</details>
</details>

<br/>

<!-- ═══════════════ SNAKE ═══════════════ -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/santapong/santapong/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/santapong/santapong/output/github-contribution-grid-snake.svg" />
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/santapong/santapong/output/github-contribution-grid-snake.svg" />
  </picture>
</div>

<br/>

<!-- ═══════════════ ANIMATED SVG FOOTER ═══════════════ -->
<div align="center">
<svg width="840" height="70" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a0e17"/>
      <stop offset="50%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#0a0e17"/>
    </linearGradient>
    <linearGradient id="footLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00ff41" stop-opacity="0"/>
      <stop offset="50%" stop-color="#58a6ff" stop-opacity="0.5">
        <animate attributeName="offset" values="0.2;0.5;0.8;0.5;0.2" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#bc8cff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="840" height="70" fill="url(#footBg)" rx="12"/>
  <line x1="40" y1="1" x2="800" y2="1" stroke="url(#footLine)" stroke-width="1"/>
  <!-- Waveform -->
  <g opacity="0.12" stroke="#00ff41" fill="none" stroke-width="1">
    <path d="M30,35 Q130,25 230,35 T430,35 T630,35 T830,35">
      <animate attributeName="d" values="M30,35 Q130,25 230,35 T430,35 T630,35 T830,35;M30,35 Q130,45 230,35 T430,35 T630,35 T830,35;M30,35 Q130,25 230,35 T430,35 T630,35 T830,35" dur="4s" repeatCount="indefinite"/>
    </path>
    <path d="M30,40 Q130,50 230,40 T430,40 T630,40 T830,40">
      <animate attributeName="d" values="M30,40 Q130,50 230,40 T430,40 T630,40 T830,40;M30,40 Q130,30 230,40 T430,40 T630,40 T830,40;M30,40 Q130,50 230,40 T430,40 T630,40 T830,40" dur="3.5s" repeatCount="indefinite"/>
    </path>
  </g>
  <text x="420" y="30" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#8b949e">
    visitor.count++  ·  thanks for stopping by
  </text>
  <text x="420" y="50" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#00ff41">
    connection.close() ☕
  </text>
</svg>
</div>
