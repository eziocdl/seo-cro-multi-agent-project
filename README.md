# 🔍 AI SEO Audit Team

> **Multi-Agent System for Professional SEO, CRO, and GEO Analysis**

[![Deploy on Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=flat&logo=render)](https://render.com)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Professional system that uses **4 specialized agents** powered by Google Gemini to perform in-depth website analysis, providing strategic reports with objective scores and actionable recommendations.

---

## 🎯 Features

### ✨ Multi-Dimensional Analysis

- **🔍 SEO Health** - Complete search engine optimization audit
  - On-Page SEO (tags, meta data, headings)
  - Technical SEO (HTTPS, mobile-friendly, performance)
  - Content Quality (structure, keywords, density)
  - Core Web Vitals (speed, responsiveness)

- **📊 CRO Analysis** - Conversion rate and usability analysis
  - CTA Effectiveness
  - Form Optimization
  - Trust & Credibility
  - Page Experience
  - Mobile Readiness

- **🌐 GEO Optimization** - AI Search Engines preparation
  - Structured Data (Schema.org)
  - Compatibility with ChatGPT, Bard, Perplexity
  - Content optimization for LLMs

### 🚀 Advanced Technology

- **4 Specialized Agents** working in sequential pipeline
- **Real Web Scraping** with BeautifulSoup (verifiable data)
- **Objective Scoring System** (0-100) based on real metrics
- **Professional Markdown Reports** ready to export
- **Responsive Web Interface** with real-time visualization

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (SPA)                           │
│                   HTML5 + CSS3 + Vanilla JS                     │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP POST /invoke
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FLASK API BACKEND                           │
│                  (Python 3.11 + Gunicorn)                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐      ┌────────────────┐                      │
│  │ Web Scraper  │─────▶│ Scoring System │                      │
│  │ (Real Data)  │      │  (0-100 Score) │                      │
│  └──────────────┘      └────────────────┘                      │
│         │                       │                               │
│         └───────────┬───────────┘                               │
│                     ▼                                           │
│         ┌───────────────────────┐                               │
│         │   4 AGENTS PIPELINE   │                               │
│         │  (Google Gemini API)  │                               │
│         └───────────┬───────────┘                               │
│                     │                                           │
│    ┌────────────────┼────────────────┬────────────────┐        │
│    ▼                ▼                ▼                ▼        │
│ ┌──────┐      ┌─────────┐      ┌─────────┐      ┌──────────┐  │
│ │Agent1│      │ Agent 2 │      │ Agent 3 │      │ Agent 4  │  │
│ │Page  │─────▶│  SERP   │─────▶│   CRO   │─────▶│Strategic │  │
│ │Audit │      │Analyst  │      │Analyst  │      │ Advisor  │  │
│ └──────┘      └─────────┘      └─────────┘      └──────────┘  │
│    │              │                 │                 │        │
│    └──────────────┴─────────────────┴─────────────────┘        │
│                           ▼                                     │
│              ┌────────────────────────┐                         │
│              │  MARKDOWN REPORT       │                         │
│              │  (Strategic Analysis)  │                         │
│              └────────────────────────┘                         │
└─────────────────────────────────────────────────────────────────┘
```

### 🔄 Agent Pipeline

1. **Agent 1: Page Auditor**
   - Analyzes on-page elements (title, meta, headings)
   - Extracts primary and secondary keywords
   - Identifies technical SEO issues

2. **Agent 2: SERP Analyst**
   - Simulates competitive SERP analysis
   - Identifies content opportunities
   - Maps competitor strategies

3. **Agent 3: CRO Analyst**
   - Evaluates usability and user experience
   - Identifies conversion barriers
   - Proposes UX/UI improvements

4. **Agent 4: Strategic Advisor**
   - Consolidates analysis from previous 3 agents
   - Generates complete strategic report in PT-BR
   - Prioritizes recommendations by impact/effort

---

## 📊 Scoring System

### Calculation Methodology

All scores are calculated from **real data** extracted from the website:

#### 🔍 SEO Score (0-100)

| Component | Weight | Criteria |
|-----------|--------|----------|
| **On-Page SEO** | 25 pts | Title tag (50-60 chars), Meta description (150-160 chars), Unique H1 |
| **Technical SEO** | 25 pts | HTTPS, Mobile-friendly, Canonical tags |
| **Content Quality** | 25 pts | Word count (>300), Alt text in images, Keyword density |
| **Performance** | 25 pts | Load time (<3s), Structured data, Link quality |

#### 📊 CRO Score (0-100)

| Component | Weight | Criteria |
|-----------|--------|----------|
| **CTA Effectiveness** | 20 pts | Presence, positioning, clarity |
| **Form Optimization** | 20 pts | Simplicity, validation, feedback |
| **Trust & Credibility** | 20 pts | Testimonials, social proof, security |
| **Page Experience** | 20 pts | Navigation, visual hierarchy, consistency |
| **Mobile Readiness** | 20 pts | Responsiveness, touch targets, viewport |

#### 🌐 GEO Score (0-100)

| Component | Weight | Criteria |
|-----------|--------|----------|
| **Structured Data** | 50 pts | Schema.org implementation, relevant types |
| **AI-Friendly Content** | 30 pts | Clear formatting, FAQs, semantic context |
| **Metadata Quality** | 20 pts | Open Graph, Twitter Cards, JSON-LD |

### 📈 Score Classification

```
80-100 → Excellent  ✅ Optimized website
60-79  → Good       👍 Minor improvements needed
40-59  → Fair       ⚠️  Requires optimization
0-39   → Critical   🚨 Urgent action required
```

---

## 🛠️ Tech Stack

### Backend

- **Python 3.11** - Main language
- **Flask 3.0** - Minimalist web framework
- **Gunicorn 21.2** - WSGI server for production
- **Google Gemini 1.5 Flash** - LLM for processing
- **BeautifulSoup 4.12** - Web scraping with native parser
- **Pydantic 2.9** - Structured data validation
- **Python-dotenv 1.0** - Environment variable management

### Frontend

- **HTML5 + CSS3** - Responsive interface
- **Vanilla JavaScript** - Client-side logic (no frameworks)
- **Marked.js** - Markdown rendering
- **Fetch API** - Asynchronous communication

### DevOps & Deploy

- **Render.com** - Cloud hosting (free tier)
- **Git/GitHub** - Version control
- **Gunicorn (gthread worker)** - Optimized for async I/O

---

## 📁 Project Structure

```
ai_seo_audit_team/
├── 🔧 Core Application
│   ├── app.py                      # Flask API (main)
│   ├── agent.py                    # 4-agent pipeline
│   ├── web_scraper.py              # Real website scraping
│   ├── scoring_system.py           # 0-100 score calculation
│   └── __init__.py                 # Package initialization
│
├── 🎨 Frontend
│   └── public/
│       ├── index.html              # Main interface
│       ├── script.js               # Client logic
│       └── style.css               # Responsive styles
│
├── ⚙️ Configuration
│   ├── requirements.txt            # Python dependencies
│   ├── runtime.txt                 # Python version (3.11.0)
│   ├── Procfile                    # Render/Heroku config
│   ├── render.yaml                 # Render blueprint
│   └── .env.example                # Environment variables template
│
├── 🚀 Deploy Scripts
│   ├── render-build.sh             # Build script
│   └── start-server.sh             # Startup script
│
└── 📚 Documentation
    └── README.md                   # This file
```

**Total:** ~1,900 lines of Python code | ~28KB frontend

---

## 🚀 Installation and Usage

### 📋 Prerequisites

- Python 3.11 or higher
- Google AI Studio account (for API Key)
- Git

### 🔧 Local Installation

#### 1. Clone the repository

```bash
git clone https://github.com/eziocdl/seo-cro-multi-agent-project.git
cd ai_seo_audit_team
```

#### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your Google API Key:

```env
GOOGLE_API_KEY=AIzaSy...your_key_here
```

**Get API Key:** https://aistudio.google.com/app/apikey

#### 5. Start the server

```bash
python app.py
```

#### 6. Access the application

Open in browser:
```
http://localhost:8000
```

---

## 🌐 Production Deploy

### Deploy on Render.com (Free)

**Estimated time:** 5 minutes

1. **Fork/Clone** this repository on GitHub

2. Access **[Render.com](https://render.com)** and login

3. Click **"New +"** → **"Web Service"**

4. Connect your GitHub repository

5. **Configure:**

```yaml
Name: ai-seo-audit-team
Region: Oregon (US West)
Branch: main
Runtime: Python 3

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app --bind 0.0.0.0:$PORT --timeout 180 --workers 1 --threads 2 --worker-class gthread

Instance Type: Free
```

6. **Add Environment Variable:**

```
Key: GOOGLE_API_KEY
Value: your_key_here
```

7. Click **"Create Web Service"**

8. Wait ~3 minutes

9. ✅ **Done!** Your URL will be available

---

## 🎮 How to Use

### Web Interface

1. **Access the application** (local or deployed)
2. **Enter the URL** of the website you want to analyze
3. **Click "Analyze Website"**
4. **Wait 1-2 minutes** (4-agent pipeline processing)
5. **View the complete report** with:
   - SEO, CRO, GEO scores (0-100)
   - Detailed analysis of each component
   - Prioritized strategic recommendations
   - 30-day implementation roadmap

### REST API

#### Endpoint: Health Check

```bash
GET /health

# Response
{
  "status": "healthy",
  "service": "AI SEO Audit Team API",
  "version": "1.0.0"
}
```

#### Endpoint: Website Analysis

```bash
POST /invoke
Content-Type: application/json

{
  "message": "https://example.com"
}

# Response
{
  "output": "# Strategic Digital Audit Report\n\n..."
}
```

---

## 📊 Report Example

The system generates Markdown reports with professional structure:

```markdown
# Strategic Digital Audit Report

> Analysis performed on: 11/20/2025 at 01:46:26 PM

**Analyzed URL:** https://example.com

---

## Digital Performance Index

╔══════════════════════════════════════════════════════╗
║  OVERALL SCORE: 78/100 - Good                       ║
╠══════════════════════════════════════════════════════╣
║  SEO Health:        85/100  ████████▌░              ║
║  CRO Readiness:     72/100  ███████▏░░             ║
║  GEO Optimization:  65/100  ██████▌░░░             ║
╚══════════════════════════════════════════════════════╝

## Executive Summary
[...]

## 1. SEO Audit
[...]

## 2. Competitive Analysis - SERP Intelligence
[...]

## 3. CRO Audit
[...]

## 4. GEO Optimization
[...]

## Prioritized Strategic Recommendations
[...]

## Implementation Roadmap (30 Days)
[...]
```

---

## ⚙️ Advanced Configuration

### Environment Variables

```env
# Required
GOOGLE_API_KEY=AIzaSy...     # Google AI Studio API Key

# Optional
FLASK_ENV=production          # production | development
PORT=8000                     # Server port (default: 8000)
```

### Agent Customization

Edit `app.py` to adjust:
- Agent instructions
- Gemini model (gemini-1.5-flash, gemini-pro, etc)
- Prompts and output formatting

### Scoring Customization

Edit `scoring_system.py` to adjust:
- Component weights (constants at top)
- Scoring criteria
- Classification thresholds

---

## 🐛 Troubleshooting

### Problem: "GOOGLE_API_KEY not found"

**Solution:**
```bash
# Check if .env exists
cat .env

# Configure the variable
echo "GOOGLE_API_KEY=your_key" >> .env
```

### Problem: "Bad Gateway" on Render

**Solution:**
```bash
# In Render Dashboard → Settings → Start Command
# Paste exactly:
gunicorn app:app --bind 0.0.0.0:$PORT --timeout 180 --workers 1 --threads 2 --worker-class gthread
```

### Problem: "429 Quota Exceeded"

**Cause:** Free tier request limit from Gemini (15 req/min)

**Solution:** Wait 1 minute or upgrade API key

---

## 🗺️ Roadmap

### ✅ Version 1.0 (Current)

- [x] 4-agent specialized pipeline
- [x] Real web scraping with BeautifulSoup
- [x] Objective scoring system (0-100)
- [x] Markdown reports
- [x] Responsive web interface
- [x] Free deploy on Render

### 🚧 Version 1.1 (Next)

- [ ] Professional PDF generation
- [ ] Google Search Console integration
- [ ] Backlink analysis
- [ ] Historical score comparison
- [ ] Report caching

### 🔮 Version 2.0 (Future)

- [ ] Multi-site dashboard
- [ ] User authentication
- [ ] Public API with rate limiting
- [ ] Word/Excel export
- [ ] SEO tools integration (Ahrefs, SEMrush)

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the project
2. Create a branch: `git checkout -b feature/new-feature`
3. Commit: `git commit -m 'feat: add feature X'`
4. Push: `git push origin feature/new-feature`
5. Open a Pull Request

### Code Standards

- **Python:** PEP 8
- **Commits:** Conventional Commits
- **Docstrings:** Google Style

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Ezio Lima

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👤 Author

**Ezio Lima**

- GitHub: [@eziocdl](https://github.com/eziocdl)
- LinkedIn: [Ezio Lima](https://www.linkedin.com/in/ezio-lima)
- Portfolio: https://eziolima.dev

---

## 🙏 Acknowledgments

- Google AI for providing the Gemini API
- Render.com for free hosting
- Flask and BeautifulSoup communities
- All contributors to this project

---

## 📞 Support

### Resources

- 🐛 [Report Issues](https://github.com/eziocdl/seo-cro-multi-agent-project/issues)
- 💬 [Discussions](https://github.com/eziocdl/seo-cro-multi-agent-project/discussions)

### Useful Links

- 🔗 **Live Demo:** https://seo-cro-multi-agent-project.onrender.com
- 📚 **Google AI Studio:** https://aistudio.google.com
- 🎨 **Render Dashboard:** https://dashboard.render.com

---

<div align="center">

**⭐ If this project was helpful, consider giving it a star on GitHub! ⭐**

Developed with dedication by [Ezio Lima](https://github.com/eziocdl)

[⬆ Back to top](#-ai-seo-audit-team)

</div>
