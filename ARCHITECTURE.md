# TUYUL-FX-HYBRID Architecture

## Overview

TUYUL-FX-HYBRID is a modular AGI orchestrator built with FastAPI, featuring three core layers (Fusion, Reflex, Risk) and multiple supporting modules.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Application                       │
│                     (46 Endpoints)                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┐
    │                 │                 │
┌───▼───┐        ┌────▼────┐      ┌────▼────┐
│Fusion │        │ Reflex  │      │  Risk   │
│Layer  │        │ Layer   │      │  Layer  │
└───┬───┘        └────┬────┘      └────┬────┘
    │                 │                 │
    │    ┌────────────┼────────────┐    │
    │    │            │            │    │
    └────►   Modules Layer         ◄────┘
         │                         │
    ┌────┴────┬────────┬──────────┴─────┐
    │         │        │                 │
┌───▼───┐ ┌──▼──┐ ┌───▼────┐     ┌─────▼──────┐
│  GPT  │ │ OCR │ │Adaptive│     │  Semantic  │
│Bridge │ │Parse│ │Learning│     │ Reflection │
└───┬───┘ └─────┘ └───┬────┘     └─────┬──────┘
    │                 │                 │
    └─────────────────┼─────────────────┘
                      │
         ┌────────────┼────────────┐
         │                         │
    ┌────▼────────┐       ┌───────▼────────┐
    │  Knowledge  │       │    Journal     │
    │    Vault    │       │     Vault      │
    │  (GitHub)   │       │   (GitHub)     │
    └─────────────┘       └────────────────┘
```

## Core Components

### 1. Fusion Layer (`layers/fusion.py`)

**Purpose**: Multi-source data integration and normalization

**Key Features**:
- Data source registration
- Multi-stream data fusion
- Feature extraction
- Data normalization (OCR, API, Database)

**Endpoints**: 5
- Register source
- Fuse data
- Normalize data
- Get status
- List sources

### 2. Reflex Layer (`layers/reflex.py`)

**Purpose**: Real-time decision making and adaptive responses

**Key Features**:
- Fast and deliberate decision modes
- Reflex rules engine
- Learning from feedback
- Pattern recognition
- Performance tracking

**Endpoints**: 7
- Make decision
- Add reflex rule
- Submit feedback
- Get status
- List rules
- List patterns
- Decision history

### 3. Risk Layer (`layers/risk.py`)

**Purpose**: Risk assessment and mitigation

**Key Features**:
- Multi-dimensional risk assessment (Financial, Operational, Strategic, Technical)
- Risk level determination
- Mitigation strategy management
- Risk profiling

**Endpoints**: 6
- Assess risk
- Add mitigation strategy
- Get risk profile
- Get status
- List assessments
- List strategies

## Supporting Modules

### 4. GPT Bridge (`modules/gpt_bridge.py`)

**Purpose**: OpenAI GPT integration for NLP

**Features**:
- Text generation
- Text analysis (sentiment, entities, summary)
- Semantic search
- Insight generation
- Conversation history

**Endpoints**: 6

### 5. Adaptive Learning (`modules/adaptive_learning.py`)

**Purpose**: Continuous learning from experiences

**Features**:
- Experience logging (state-action-reward)
- Reward prediction
- Action suggestion
- Performance trend analysis
- Knowledge base building
- Pattern detection

**Endpoints**: 5

### 6. Semantic Reflection (`modules/semantic_reflection.py`)

**Purpose**: Analysis and learning from past decisions

**Features**:
- Decision quality analysis
- Lesson extraction
- Insight accumulation
- Reasoning pattern tracking
- Effectiveness analysis

**Endpoints**: 5

### 7. OCR Parser (`modules/ocr_parser.py`)

**Purpose**: Offline text extraction from images

**Features**:
- Image-to-text conversion (Tesseract)
- Batch processing
- Structured data extraction (invoices, receipts, documents)
- Feed history tracking

**Endpoints**: 5

### 8. Vault Sync (`modules/vault_sync.py`)

**Purpose**: GitHub-based knowledge and journal storage

**Components**:
- **Knowledge Vault**: Stores learned knowledge, patterns, insights
- **Journal Vault**: Stores decisions, reflections, activities

**Features**:
- Automatic GitHub sync
- Read/Write operations
- File listing
- Sync history tracking

**Endpoints**: 13 (7 Knowledge + 6 Journal)

## Data Flow

### Decision Making Flow

```
1. Request → Reflex Layer
2. Reflex → Risk Assessment
3. Risk → Return assessment
4. Reflex → Apply rules/patterns
5. Reflex → Make decision
6. Decision → Log to Journal Vault
7. Response → Client
```

### Learning Flow

```
1. Experience → Adaptive Learning
2. Learning → Update knowledge base
3. Learning → Detect patterns
4. Pattern → Store in Knowledge Vault
5. Feedback → Semantic Reflection
6. Reflection → Extract lessons
7. Lessons → Update insights
8. Insights → Store in Knowledge Vault
```

### Data Integration Flow

```
1. Multiple sources → Fusion Layer
2. Fusion → Normalize data
3. Fusion → Extract features
4. Fusion → Fuse streams
5. Fused data → Downstream layers
```

## Configuration

### Environment Variables

See `.env.example` for all configuration options:

- **API**: Host, port, version, debug mode
- **GPT**: API key, model, parameters
- **GitHub**: Token, vault repositories
- **Database**: PostgreSQL connection
- **Redis**: Cache connection
- **OCR**: Tesseract path, languages
- **Learning**: Learning rate, batch size, epochs
- **Security**: Secret key, algorithm, token expiration
- **Logging**: Level, file path

## Security

### Authentication & Authorization

- JWT token-based authentication (ready for implementation)
- Secret key for token signing
- Configurable token expiration

### Data Privacy

- No sensitive data logged
- API keys stored in environment variables
- GitHub tokens with minimal required permissions

### Error Handling

- Graceful error handling
- Detailed logging
- User-friendly error messages

## Scalability

### Horizontal Scaling

- Stateless API design
- External state in Redis/PostgreSQL
- Multiple worker processes supported

### Caching

- Redis for frequently accessed data
- In-memory caching for hot paths
- Configurable TTLs

### Performance

- Async/await throughout
- Efficient batch processing
- Minimal I/O blocking

## Testing Strategy

### Unit Tests

- Test individual components
- Mock external dependencies
- Fast execution

### Integration Tests

- Test component interactions
- Use test databases
- End-to-end scenarios

### API Tests

- Test all endpoints
- Validate responses
- Check error handling

## Deployment

### Development

```bash
make run
```

### Production

```bash
make run-prod
```

With Docker:
```bash
docker build -t tuyul-fx-hybrid .
docker run -p 8000:8000 --env-file .env tuyul-fx-hybrid
```

### Monitoring

- Health check endpoint: `/health`
- System status endpoint: `/status`
- Component-specific status endpoints
- Logging to file and stdout

## Future Enhancements

1. **Database Persistence**: Full PostgreSQL integration
2. **Authentication**: JWT implementation
3. **Rate Limiting**: API rate limiting
4. **WebSocket**: Real-time updates
5. **Model Training**: On-device ML model training
6. **Distributed Processing**: Celery task queue
7. **Metrics**: Prometheus/Grafana integration
8. **Advanced OCR**: Multi-language, handwriting recognition
9. **Plugin System**: Extensible module architecture
10. **GraphQL API**: Alternative to REST
