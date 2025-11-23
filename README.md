# TUYUL-FX-HYBRID v5.4.0 AGI Orchestrator

**Otak tengah TUYUL AGI** - Advanced AGI orchestrator with Fusion, Reflex, and Risk layers for intelligent decision-making, adaptive learning, and autonomous system management.

[![License](https://img.shields.io/badge/License-Apache%202.0%20Modified-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-green.svg)](https://fastapi.tiangolo.com)
[![Version](https://img.shields.io/badge/Version-5.4.0-orange.svg)](https://github.com/tjx578/TUYUL-KARTEL-FX-AGI-HYBRID)

## 🧠 Overview

TUYUL-FX-HYBRID adalah sistem AGI (Artificial General Intelligence) orchestrator yang menggabungkan tiga layer utama untuk pengambilan keputusan cerdas, pembelajaran adaptif, dan manajemen risiko otomatis.

### Core Layers

- **🔀 Fusion Layer**: Integrasi dan pemrosesan data dari multiple sources
- **⚡ Reflex Layer**: Pengambilan keputusan real-time dan adaptive learning
- **🛡️ Risk Layer**: Analisis dan mitigasi risiko otomatis

### Key Features

- ✅ **46 OpenAPI Endpoints** - RESTful API lengkap untuk semua fungsi AGI
- 🤖 **GPT Bridge** - Integrasi dengan OpenAI GPT models untuk NLP
- 📚 **Knowledge Vault Sync** - Auto-sync ke GitHub repository untuk knowledge base
- 📓 **Journal Vault Sync** - Logging otomatis decisions & reflections
- 🧠 **Adaptive Learning** - Continuous learning dari interactions
- 💭 **Semantic Reflection** - Analisis dan pembelajaran dari past decisions
- 📸 **Offline OCR** - Text extraction dari images dengan Tesseract
- 🔄 **GitHub Actions** - Auto-sync workflow untuk vault synchronization

## 🚀 Quick Start

### Prerequisites

- Python 3.9 atau lebih tinggi
- PostgreSQL (optional, untuk database persistence)
- Redis (optional, untuk caching)
- Tesseract OCR (optional, untuk OCR functionality)

### Installation

```bash
# Clone repository
git clone https://github.com/tjx578/TUYUL-KARTEL-FX-AGI-HYBRID.git
cd TUYUL-KARTEL-FX-AGI-HYBRID

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Configuration

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file dengan credentials Anda
nano .env
```

**Required Configuration:**
- `OPENAI_API_KEY`: OpenAI API key untuk GPT integration
- `GITHUB_TOKEN`: GitHub personal access token
- `GITHUB_KNOWLEDGE_VAULT_REPO`: Repository untuk knowledge storage
- `GITHUB_JOURNAL_VAULT_REPO`: Repository untuk journal/logs
- `SECRET_KEY`: Secret key untuk security (generate dengan: `openssl rand -hex 32`)

### Running the Application

```bash
# Run dengan uvicorn
python -m uvicorn src.tuyul_fx_hybrid.main:app --reload --host 0.0.0.0 --port 8000

# Atau langsung jalankan main.py
python src/tuyul_fx_hybrid/main.py
```

API akan tersedia di:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 📖 API Documentation

### System Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /status` - Comprehensive system status
- `GET /version` - API version
- `GET /config` - Public configuration

### Fusion Layer (5 endpoints)

- `POST /fusion/register-source` - Register data source
- `POST /fusion/fuse` - Fuse multiple data streams
- `POST /fusion/normalize` - Normalize data
- `GET /fusion/status` - Fusion layer status
- `GET /fusion/sources` - List data sources

### Reflex Layer (7 endpoints)

- `POST /reflex/decide` - Make decision
- `POST /reflex/add-rule` - Add reflex rule
- `POST /reflex/feedback` - Submit feedback
- `GET /reflex/status` - Reflex layer status
- `GET /reflex/rules` - List reflex rules
- `GET /reflex/patterns` - List learning patterns
- `GET /reflex/history` - Decision history

### Risk Layer (6 endpoints)

- `POST /risk/assess` - Assess risk
- `POST /risk/mitigation` - Add mitigation strategy
- `GET /risk/profile` - Risk profile
- `GET /risk/status` - Risk layer status
- `GET /risk/assessments` - List assessments
- `GET /risk/strategies` - List mitigation strategies

### GPT Bridge (6 endpoints)

- `POST /gpt/generate` - Generate GPT response
- `POST /gpt/analyze` - Analyze text
- `POST /gpt/search` - Semantic search
- `POST /gpt/insights` - Generate insights
- `POST /gpt/clear-history` - Clear conversation
- `GET /gpt/status` - GPT bridge status

### Adaptive Learning (5 endpoints)

- `POST /learning/experience` - Log experience
- `POST /learning/predict-reward` - Predict reward
- `POST /learning/suggest-action` - Suggest action
- `GET /learning/performance` - Performance trend
- `GET /learning/status` - Learning status

### Semantic Reflection (5 endpoints)

- `POST /reflection/reflect` - Reflect on decision
- `POST /reflection/insights` - Get insights
- `GET /reflection/effectiveness` - Reasoning effectiveness
- `GET /reflection/report` - Reflection report
- `GET /reflection/status` - Reflection status

### OCR Parser (5 endpoints)

- `POST /ocr/parse-image` - Parse image (base64)
- `POST /ocr/parse-batch` - Batch parse images
- `POST /ocr/extract-structured` - Extract structured data
- `GET /ocr/history` - OCR history
- `GET /ocr/status` - OCR status

### Knowledge Vault (7 endpoints)

- `POST /vault/knowledge/sync` - Sync knowledge
- `POST /vault/knowledge/pattern` - Sync pattern
- `POST /vault/knowledge/insight` - Sync insight
- `POST /vault/knowledge/read` - Read from vault
- `POST /vault/knowledge/list` - List files
- `GET /vault/knowledge/status` - Vault status
- `GET /vault/knowledge/history` - Sync history

### Journal Vault (6 endpoints)

- `POST /vault/journal/decision` - Sync decision
- `POST /vault/journal/reflection` - Sync reflection
- `POST /vault/journal/activity` - Sync activity
- `POST /vault/journal/read` - Read from vault
- `POST /vault/journal/list` - List files
- `GET /vault/journal/status` - Vault status

## 🔧 Architecture

```
┌─────────────────────────────────────────────────┐
│           TUYUL-FX-HYBRID v5.4.0                │
│              AGI Orchestrator                    │
└─────────────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
   ┌────▼────┐   ┌───▼────┐   ┌───▼────┐
   │ Fusion  │   │ Reflex │   │  Risk  │
   │  Layer  │   │ Layer  │   │ Layer  │
   └────┬────┘   └───┬────┘   └───┬────┘
        │            │            │
        └────────────┼────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
   ┌────▼────┐  ┌───▼────┐  ┌───▼────┐
   │   GPT   │  │Adaptive│  │Semantic│
   │ Bridge  │  │Learning│  │Reflect │
   └─────────┘  └────────┘  └────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
   ┌────▼────┐  ┌───▼────┐  ┌───▼────┐
   │   OCR   │  │Knowledge│ │Journal │
   │ Parser  │  │  Vault  │ │ Vault  │
   └─────────┘  └─────────┘ └────────┘
```

## 🧪 Testing

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=src/tuyul_fx_hybrid --cov-report=html

# Run specific test
pytest tests/unit/test_fusion_layer.py
```

## 📝 Usage Examples

### Example 1: Making a Decision

```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.post(
        "http://localhost:8000/reflex/decide",
        json={
            "context": {"market": "bullish", "risk_tolerance": "medium"},
            "options": [
                {"id": "buy", "priority": 0.8},
                {"id": "hold", "priority": 0.6},
                {"id": "sell", "priority": 0.3}
            ],
            "mode": "fast"
        }
    )
    decision = response.json()
    print(f"Decision: {decision['data']['action']}")
```

### Example 2: Risk Assessment

```python
response = await client.post(
    "http://localhost:8000/risk/assess",
    json={
        "action": {
            "id": "trade_action",
            "cost": 10000,
            "complexity": 0.7
        },
        "context": {
            "budget": 50000,
            "market_volatility": "high"
        }
    }
)
risk = response.json()
print(f"Risk Level: {risk['data']['risk_level']}")
```

### Example 3: OCR Parsing

```python
import base64

with open("document.png", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode()

response = await client.post(
    "http://localhost:8000/ocr/parse-image",
    json={
        "image_base64": image_base64,
        "source_id": "invoice_001"
    }
)
ocr_result = response.json()
print(f"Extracted Text: {ocr_result['data']['text']}")
```

## 🔄 Auto-Sync Workflow

GitHub Actions workflow otomatis sync ke vaults:
- **Schedule**: Setiap jam (configurable)
- **Triggers**: Push ke main/master branch
- **Sync Targets**: Knowledge Vault & Journal Vault

**Setup:**
1. Buat repositories untuk Knowledge dan Journal Vaults
2. Generate GitHub Personal Access Token dengan repo permissions
3. Tambahkan secrets ke repository:
   - `VAULT_SYNC_TOKEN`: GitHub token
   - `KNOWLEDGE_VAULT_REPO`: `org/knowledge-vault-repo`
   - `JOURNAL_VAULT_REPO`: `org/journal-vault-repo`

## 🤝 Contributing

Contributions welcome! Please:
1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

Apache License 2.0 Modified - See [LICENSE](LICENSE) file for details.

**Key Modifications:**
- Attribution required for production use
- Data privacy compliance mandatory
- Ethical use policy
- Research sharing encouraged

## 🙏 Acknowledgments

- OpenAI untuk GPT models
- FastAPI framework
- Tesseract OCR engine
- GitHub untuk version control dan Actions

## 📧 Contact

TUYUL KARTEL - [@tjx578](https://github.com/tjx578)

Project Link: [https://github.com/tjx578/TUYUL-KARTEL-FX-AGI-HYBRID](https://github.com/tjx578/TUYUL-KARTEL-FX-AGI-HYBRID)

---

**Built with ❤️ by TUYUL KARTEL**
