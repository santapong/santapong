<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 🖥️  SANTAPONG — GitHub Profile README v3.1                    -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<!-- ▓▓▓ MINIMAL ANIMATED HEADER ▓▓▓ -->
<svg width="840" height="240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#111820"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#58a6ff">
        <animate attributeName="stop-color" values="#58a6ff;#bc8cff;#58a6ff" dur="10s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#bc8cff">
        <animate attributeName="stop-color" values="#bc8cff;#58a6ff;#bc8cff" dur="10s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="840" height="240" fill="url(#bg)" rx="16"/>

  <!-- ═══ Ambient orbs — soft, slow, out of focus ═══ -->
  <circle cx="140" cy="120" r="80" fill="#58a6ff" opacity="0.03">
    <animate attributeName="r" values="80;95;80" dur="8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.03;0.05;0.03" dur="8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="120" r="90" fill="#bc8cff" opacity="0.03">
    <animate attributeName="r" values="90;75;90" dur="9s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.03;0.05;0.03" dur="9s" repeatCount="indefinite"/>
  </circle>
  <circle cx="420" cy="200" r="60" fill="#3fb950" opacity="0.02">
    <animate attributeName="r" values="60;70;60" dur="7s" repeatCount="indefinite"/>
  </circle>

  <!-- ═══ Minimal floating dots — like dust in sunlight ═══ -->
  <circle cx="180" cy="60" r="1.5" fill="#58a6ff" opacity="0.25">
    <animate attributeName="cy" values="60;50;60" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.25;0.08;0.25" dur="6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="660" cy="55" r="1" fill="#bc8cff" opacity="0.2">
    <animate attributeName="cy" values="55;48;55" dur="7s" repeatCount="indefinite"/>
  </circle>
  <circle cx="350" cy="190" r="1.2" fill="#58a6ff" opacity="0.15">
    <animate attributeName="cy" values="190;183;190" dur="8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="530" cy="185" r="1" fill="#bc8cff" opacity="0.18">
    <animate attributeName="cy" values="185;178;185" dur="5.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="90" cy="170" r="0.8" fill="#3fb950" opacity="0.15">
    <animate attributeName="cy" values="170;164;170" dur="9s" repeatCount="indefinite"/>
  </circle>
  <circle cx="750" cy="175" r="1.2" fill="#3fb950" opacity="0.12">
    <animate attributeName="cy" values="175;168;175" dur="6.5s" repeatCount="indefinite"/>
  </circle>

  <!-- ═══ Name ═══ -->
  <text x="420" y="88" text-anchor="middle" font-family="'Segoe UI','Helvetica Neue',sans-serif" font-size="48" font-weight="300" fill="#e6edf3" letter-spacing="8" opacity="0.95">
    santapong
  </text>

  <!-- ═══ Accent line — breathing ═══ -->
  <rect x="370" y="105" width="100" height="2" rx="1" fill="url(#accent)" opacity="0.6">
    <animate attributeName="width" values="100;60;100" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="x" values="370;390;370" dur="6s" repeatCount="indefinite"/>
  </rect>

  <!-- ═══ Subtitle ═══ -->
  <text x="420" y="140" text-anchor="middle" font-family="'Courier New',monospace" font-size="12" fill="#8b949e" letter-spacing="3" opacity="0.7">
    software engineer  ·  automation  ·  quantum
  </text>

  <!-- ═══ Status line — understated ═══ -->
  <text x="420" y="190" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#484f58">
    thailand  ·  building things quietly  ·  ☕
  </text>

  <!-- ═══ Subtle border — single pixel, barely there ═══ -->
  <rect x="0.5" y="0.5" width="839" height="239" rx="16" fill="none" stroke="#21262d" stroke-width="1"/>
</svg>

<br/>

<!-- Social badges -->
[![Profile Views](https://komarev.com/ghpvc/?username=santapong&color=58a6ff&style=flat-square&label=visitors)](https://github.com/santapong)
&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/linkedin-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_LINKEDIN)
&nbsp;&nbsp;
[![Email](https://img.shields.io/badge/email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:your-email@example.com)
&nbsp;&nbsp;
[![YouTube](https://img.shields.io/badge/youtube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/@YOUR_CHANNEL)

</div>

<!-- ═══════════════ DIVIDER ═══════════════ -->
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
 ║     output    = coffee × (1 - sleep)        ║
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

<!-- ═══════════════ ANIMATED FOOTER ═══════════════ -->
<div align="center">
<svg width="840" height="60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ftBg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a0e17"/>
      <stop offset="50%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#0a0e17"/>
    </linearGradient>
    <linearGradient id="ftLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#58a6ff" stop-opacity="0">
        <animate attributeName="stop-opacity" values="0;0.3;0" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#bc8cff" stop-opacity="0.3">
        <animate attributeName="stop-opacity" values="0.3;0;0.3" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#58a6ff" stop-opacity="0">
        <animate attributeName="stop-opacity" values="0;0.3;0" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
  </defs>
  <rect width="840" height="60" fill="url(#ftBg)" rx="12"/>
  <rect x="0.5" y="0.5" width="839" height="59" rx="12" fill="none" stroke="#21262d" stroke-width="0.5"/>
  <line x1="80" y1="2" x2="760" y2="2" stroke="url(#ftLine)" stroke-width="1"/>
  <text x="420" y="28" text-anchor="middle" font-family="'Segoe UI','Helvetica Neue',sans-serif" font-size="12" fill="#484f58" letter-spacing="2">
    thanks for stopping by
  </text>
  <text x="420" y="48" text-anchor="middle" font-family="'Courier New',monospace" font-size="11" fill="#8b949e">
    ☕ · built quietly from thailand
  </text>
</svg>
</div>
