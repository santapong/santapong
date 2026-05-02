<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=0d1117&height=1" width="100%"/>

<br/>

# Santapong Sondhi

**Software Engineer** · Ennovie Co., Ltd · Thailand

Designing AI agents, quantum systems, and production-grade platforms for jewelry manufacturing.

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/santapong-sondhi)
[![Gmail](https://img.shields.io/badge/Email-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:santapongsondhi@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/santapong)

</div>

---

### About

I work on the **Digital Platforms & Automation** team at Ennovie, a jewelry manufacturer in Thailand, where I design AI agents for operational workflows, production scheduling systems, and end-to-end data pipelines. Outside of work I operate a small Kubernetes home lab (3× Beelink EQ13) and study quantum computing toward an **MSc by 2027**.

My focus is shipping pragmatic systems: ones that hold up in production, integrate cleanly with existing infrastructure, and earn their complexity.

> *cheap + best = ship it · expensive + marginal = pass*

---

### Featured Projects

Click any project to expand its description, stack, and current status.

#### AI & Agents

<details>
<summary><b>Nexus</b> — Multi-agent platform with every department staffed by AI</summary>

<br/>

A distributed agent platform where each "department" is an autonomous AI worker communicating over Kafka. Agents share persistent memory, expose capabilities through MCP tools, and coordinate long-running workflows without a central orchestrator.

- **Stack:** Python · Kafka · MCP · Vector DB · Postgres
- **Highlights:** event-driven architecture, persistent agent memory, pluggable tool registry
- **Status:** Active development
- **Repo:** [santapong/Nexus](https://github.com/santapong/Nexus)

</details>

<details>
<summary><b>shopping-agent</b> — Conversational shopping over Google's Universal Commerce Protocol</summary>

<br/>

An AI shopping agent built on Google's Universal Commerce Protocol and Claude. It negotiates product discovery, comparison, and checkout flows through natural conversation while remaining vendor-agnostic.

- **Stack:** TypeScript · Claude · UCP · Next.js
- **Highlights:** vendor-neutral commerce abstraction, multi-turn negotiation, structured checkout
- **Repo:** [santapong/shopping-agent](https://github.com/santapong/shopping-agent)

</details>

<details>
<summary><b>capstone-project</b> — Agentic RAG for KMITL's Automation Engineering knowledge base</summary>

<br/>

A retrieval-augmented agent system that indexes coursework, lab notes, and reference material from KMITL's Automation Engineering program and answers domain questions with cited evidence.

- **Stack:** Python · LangChain · Vector DB · LLM
- **Highlights:** hierarchical retrieval, citation-aware responses, course-aware context
- **Repo:** [santapong/capstone-project](https://github.com/santapong/capstone-project)

</details>

<details>
<summary><b>Research</b> — Text · sketch · image → 3D CAD for jewelry manufacturing</summary>

<br/>

A generative pipeline that takes a designer's text prompt, hand sketch, or reference image and produces parametric 3D CAD models ready for the jewelry production floor.

- **Stack:** Python · Diffusion models · CAD kernels · GPU inference
- **Highlights:** multi-modal input, manufacturable geometry, designer-in-the-loop workflow
- **Repo:** [santapong/Research](https://github.com/santapong/Research)

</details>

<details>
<summary><b>School</b> — Lightweight LLM training toolkit for tool-calling</summary>

<br/>

A focused training toolkit for fine-tuning open-weight LLMs (Qwen, Llama, Mistral) on tool-calling tasks using LoRA and QLoRA. Designed for small teams who need reliable function-calling on commodity hardware.

- **Stack:** Python · PyTorch · Transformers · PEFT
- **Highlights:** LoRA/QLoRA recipes, tool-calling datasets, reproducible training configs
- **Repo:** [santapong/School](https://github.com/santapong/School)

</details>

#### Quantum Computing

<details>
<summary><b>TTQ</b> — Translating natural language into quantum circuits</summary>

<br/>

A seq2seq Transformer that translates plain-English problem descriptions into Qiskit circuits. The goal is to make quantum prototyping accessible without requiring deep gate-level expertise.

- **Stack:** Python · PyTorch · Qiskit · Transformer
- **Highlights:** custom NL → circuit dataset, gate-aware decoder, executable output
- **Repo:** [santapong/TTQ](https://github.com/santapong/TTQ)

</details>

<details>
<summary><b>CaaS-Q</b> — Quantum microservices for text embeddings in Hilbert space</summary>

<br/>

A microservices platform that embeds text into Hilbert spaces using parameterized circuits and ranks results by overlap fidelity. Explores whether quantum representations can outperform classical embeddings on similarity tasks.

- **Stack:** Python · Qiskit · FastAPI · Docker
- **Highlights:** parameterized circuit embeddings, fidelity-based ranking, REST API
- **Repo:** [santapong/CaaS-Q](https://github.com/santapong/CaaS-Q)

</details>

<details>
<summary><b>MedQCNN</b> — Hybrid quantum-classical CNN on Raspberry Pi 5 clusters</summary>

<br/>

A hybrid quantum-classical neural network targeting medical image classification. Runs on a cluster of Raspberry Pi 5 nodes to study edge-deployable quantum-inspired models.

- **Stack:** Python · PennyLane · PyTorch · Raspberry Pi 5
- **Highlights:** hybrid Q-C architecture, edge inference, medical imaging benchmarks
- **Repo:** [santapong/MedQCNN](https://github.com/santapong/MedQCNN)

</details>

<details>
<summary><b>QRS-project</b> — Web-based quantum circuit simulator</summary>

<br/>

A browser-based quantum circuit simulator built on an event-driven microservices backend. Lets users compose circuits visually and see real-time state evolution.

- **Stack:** TypeScript · React · Python · NATS/Kafka
- **Highlights:** real-time simulation, drag-and-drop circuit builder, multi-tenant backend
- **Repo:** [santapong/QRS-project](https://github.com/santapong/QRS-project)

</details>

<details>
<summary><b>Quantum-Daily</b> — Daily quantum katas in Rust, Mojo, and Python</summary>

<br/>

Short daily exercises that connect quantum theory to high-performance computing across three languages. A long-running discipline in keeping fundamentals sharp.

- **Stack:** Rust · Mojo · Python
- **Highlights:** cross-language katas, HPC-oriented implementations, theory ↔ practice bridge
- **Repo:** [santapong/Quantum-Daily](https://github.com/santapong/Quantum-Daily)

</details>

#### DevOps & Infrastructure

<details>
<summary><b>Cooker</b> — Visual graph-based CI/CD for OCI images and Kubernetes</summary>

<br/>

A graph-based CI/CD tool with a visual pipeline builder. Targets OCI image builds and Kubernetes deployments without YAML sprawl.

- **Stack:** Go · React · Kubernetes · OCI
- **Highlights:** node-graph pipelines, K8s-native deploys, no-YAML editing
- **Repo:** [santapong/Cooker](https://github.com/santapong/Cooker)

</details>

<details>
<summary><b>AI-OS</b> — Debian-based Linux distro for AI-agentic workloads</summary>

<br/>

A Debian-derived distribution preconfigured for running AI agents — GPU drivers, runtime stacks, agent frameworks, and observability tooling installed out of the box.

- **Stack:** Debian · Bash · Ansible · CUDA
- **Highlights:** opinionated agent runtime, preconfigured observability, reproducible images
- **Repo:** [santapong/AI-OS](https://github.com/santapong/AI-OS)

</details>

<details>
<summary><b>KeepSave</b> — Secure env variable storage and promotion for agents and teams</summary>

<br/>

A secrets and environment management service designed for AI agents and small dev teams. Handles secure storage, scoped access, and promotion across environments.

- **Stack:** Go · Postgres · Vault-style crypto
- **Highlights:** scoped secrets, environment promotion, agent-friendly API
- **Repo:** [santapong/KeepSave](https://github.com/santapong/KeepSave)

</details>

<details>
<summary><b>MCP-Pack</b> — A curated collection of MCP servers for developer utilities</summary>

<br/>

A growing collection of Model Context Protocol servers covering common developer needs — file ops, search, code intelligence, and more.

- **Stack:** TypeScript · Python · MCP
- **Highlights:** plug-and-play MCP servers, dev-tool focus, modular packaging
- **Repo:** [santapong/MCP-Pack](https://github.com/santapong/MCP-Pack)

</details>

<details>
<summary><b>Mr-Research</b> — Self-hosted web scraping and search</summary>

<br/>

A self-hosted alternative to commercial search APIs (Brave Search, Tavily). Combines targeted scraping, indexing, and ranking for research workflows.

- **Stack:** Python · Playwright · Elasticsearch
- **Highlights:** self-hosted, agent-friendly search, configurable crawlers
- **Repo:** [santapong/Mr-Research](https://github.com/santapong/Mr-Research)

</details>

#### Robotics & Hardware

<details>
<summary><b>Muninn</b> — Autonomous drone on Raspberry Pi Pico W</summary>

<br/>

An autonomous drone built around the Raspberry Pi Pico W. Currently flying on a PID baseline, with active migration to LQG control for better disturbance rejection.

- **Stack:** C/C++ · MicroPython · RPi Pico W · MAVLink
- **Highlights:** PID → LQG migration, low-cost flight controller, embedded estimation
- **Repo:** [santapong/Muninn](https://github.com/santapong/Muninn)

</details>

<details>
<summary><b>Trajectory</b> — RRT/RRT* pathing for CNC jewelry manufacturing</summary>

<br/>

Sampling-based motion planners (RRT and RRT*) tuned for CNC filing and polishing of jewelry parts. Reduces tool-path generation time on complex geometries.

- **Stack:** Python · NumPy · CAD/CAM
- **Highlights:** RRT/RRT* implementations, CNC-aware constraints, jewelry-specific tuning
- **Repo:** [santapong/Trajectory](https://github.com/santapong/Trajectory)

</details>

<details>
<summary><b>Drone-Simulation</b> — Browser-based drone training that deploys to real hardware</summary>

<br/>

A browser-based simulator for drone training. Models trained in simulation deploy to real drones via MAVLink and the DJI SDK.

- **Stack:** TypeScript · Three.js · MAVLink · DJI SDK
- **Highlights:** sim-to-real pipeline, in-browser training, MAVLink/DJI bridge
- **Repo:** [santapong/Drone-Simulation](https://github.com/santapong/Drone-Simulation)

</details>

<details>
<summary><b>watch</b> — Real-time object detection and tracking</summary>

<br/>

A real-time object detection and tracking pipeline using OpenCV and modern detector backbones. Tuned for low-latency inference on commodity hardware.

- **Stack:** Python · OpenCV · PyTorch
- **Highlights:** real-time tracking, configurable backbones, low-latency inference
- **Repo:** [santapong/watch](https://github.com/santapong/watch)

</details>

<details>
<summary><b>RFID_Project_2024</b> — RFID/barcode load monitoring with a Flask dashboard</summary>

<br/>

A Raspberry Pi system that reads RFID tags and barcodes for load/unload tracking, surfaced through a Flask dashboard.

- **Stack:** Python · Flask · Raspberry Pi · RFID/Barcode
- **Highlights:** real-time event capture, web dashboard, low-cost hardware
- **Repo:** [santapong/RFID_Project_2024](https://github.com/santapong/RFID_Project_2024)

</details>

#### Web & Applications

<details>
<summary><b>Aegis</b> — AI-driven financial OS</summary>

<br/>

A financial operations platform that uses AI to generate tasks automatically, forecast progress on Gantt timelines, and visualize cash flow.

- **Stack:** TypeScript · Next.js · Postgres · LLM
- **Highlights:** automated task generation, Gantt forecasting, cash-flow visualization
- **Repo:** [santapong/Aegis](https://github.com/santapong/Aegis)

</details>

<details>
<summary><b>Petroleum-tracking</b> — Bilingual (TH/EN) supply-chain tracking for petroleum</summary>

<br/>

End-to-end supply-chain tracking for petroleum logistics in Thailand. Bilingual (Thai/English) UI with role-aware dashboards.

- **Stack:** TypeScript · Next.js · Postgres
- **Highlights:** bilingual UX, full-chain visibility, role-based dashboards
- **Repo:** [santapong/Petroleum-tracking](https://github.com/santapong/Petroleum-tracking)

</details>

<details>
<summary><b>Rust-AI-Web-UI</b> — High-performance API for long-form narrative analysis</summary>

<br/>

A Rust-backed API for ingesting and analyzing long-form narratives with LLM integration. Designed for throughput on large documents.

- **Stack:** Rust · Axum · LLM
- **Highlights:** high-throughput ingestion, streaming analysis, LLM-aware chunking
- **Repo:** [santapong/Rust-AI-Web-UI](https://github.com/santapong/Rust-AI-Web-UI)

</details>

<details>
<summary><b>application-dashboard</b> — Production dashboard monorepo</summary>

<br/>

A professional dashboard monorepo containing the core application, testing suites, and deployment configurations as a single coherent unit.

- **Stack:** TypeScript · Turborepo · Next.js · CI/CD
- **Highlights:** monorepo layout, integrated test suites, deploy configs included
- **Repo:** [santapong/application-dashboard](https://github.com/santapong/application-dashboard)

</details>

<details>
<summary><b>resume-blog</b> — Medieval-themed portfolio with admin dashboard</summary>

<br/>

A portfolio site with a medieval visual theme, an admin dashboard, scroll-driven animations, and floating embers.

- **Stack:** TypeScript · Next.js · Tailwind · Framer Motion
- **Highlights:** custom theme, admin CMS, scroll animations
- **Repo:** [santapong/resume-blog](https://github.com/santapong/resume-blog)

</details>

---

### Tech

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![KQL](https://img.shields.io/badge/KQL-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Qiskit](https://img.shields.io/badge/Qiskit-6929C4?style=flat-square&logo=qiskit&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/K8s-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Raspberry Pi](https://img.shields.io/badge/RPi-A22846?style=flat-square&logo=raspberrypi&logoColor=white)
![Microsoft Fabric](https://img.shields.io/badge/Fabric-F35325?style=flat-square&logo=microsoft&logoColor=white)

</div>

---

### Education

**KMITL** — B.Eng. Mechatronics & Automation Engineering

**Next** — MSc Quantum Computing *(2027)*

---

### Stats

<div align="center">

<a href="https://github.com/santapong">
  <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=santapong&show_icons=true&hide_border=true&bg_color=00000000&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9&ring_color=58a6ff&include_all_commits=true&count_private=true" height="160" />
</a>
<a href="https://github.com/santapong">
  <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=santapong&layout=compact&hide_border=true&bg_color=00000000&title_color=58a6ff&text_color=c9d1d9&langs_count=8" height="160" />
</a>

<br/>

<img width="75%" src="https://github-readme-streak-stats.herokuapp.com/?user=santapong&background=00000000&ring=58a6ff&fire=58a6ff&currStreakLabel=58a6ff&sideLabels=c9d1d9&sideNums=c9d1d9&currStreakNum=c9d1d9&dates=484f58&stroke=30363d&hide_border=true" />

<br/><br/>

<img width="85%" src="https://github-readme-activity-graph.vercel.app/graph?username=santapong&bg_color=00000000&color=58a6ff&line=58a6ff&point=bc8cff&area_color=58a6ff&area=true&hide_border=true&custom_title=Contribution%20Graph" />

</div>

---

<div align="center">

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/santapong/santapong/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/santapong/santapong/output/github-contribution-grid-snake.svg" />
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/santapong/santapong/output/github-contribution-grid-snake.svg" />
  </picture>

</div>

<br/>

<div align="center">
  <sub>thanks for stopping by</sub>
</div>
