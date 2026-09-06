# Flutter Developer → AI/GenAI Engineer Roadmap
**For:** Bilal Ahmad | Senior Flutter Developer → Flutter + AI Integration Specialist
**Goal:** Learn the concepts, then build gigs/services on Upwork & Fiverr
**Target path:** LLM Application Engineer → Generative AI Engineer → AI Agent Engineer

---

## PHASE 0 — Foundations (skip what you already know, confirm the rest)

### 0.1 Python Basics (needed even though you're a Dart/Flutter dev)
- Python syntax, virtual environments (venv), pip
- Working with JSON, requests library, async/await in Python
- FastAPI or Flask basics (to build small AI backend services)
- Reading/writing `.env` files for API keys (security basics)

### 0.2 API & Networking Refresher (you already know this from Dio/REST — just confirm)
- REST API structure, HTTP methods, status codes
- Authentication: API keys, Bearer tokens, OAuth basics
- Streaming responses (Server-Sent Events / chunked responses) — critical for LLM streaming
- WebSockets basics (used in real-time AI chat apps)
- Rate limiting & retry logic (exponential backoff)

---

## PHASE 1 — LLM Fundamentals (Core Knowledge)

### 1.1 What LLMs Actually Are (conceptual, no math needed)
- Tokens & tokenization (why cost/limits are measured in tokens)
- Context window (what it means, why it limits app design)
- Temperature, top_p, max_tokens, stop sequences
- System prompt vs user prompt vs assistant message roles
- Chat completion vs text completion models
- Multimodal models (text+image+audio input/output)
- Model families overview: GPT (OpenAI), Claude (Anthropic), Gemini (Google), Llama/open-source, Mistral

### 1.2 LLM API Integration (hands-on, most important for you)
- OpenAI API: chat completions, function calling, structured outputs, vision, embeddings, Assistants API
- Anthropic Claude API: Messages API, tool use, extended thinking, prompt caching
- Google Gemini API basics
- Streaming responses in code (SSE handling)
- Error handling: rate limits, token limits, timeouts, retries
- Cost management: token counting, choosing cheaper models for sub-tasks

### 1.3 Prompt Engineering (small but essential concepts)
- Zero-shot vs few-shot prompting
- Chain-of-thought prompting
- Role prompting (system prompt design)
- Prompt templates & variables
- Output formatting control (JSON mode, XML tags, structured outputs)
- Prompt injection risks & basic mitigation
- Prompt versioning/testing (A/B comparing prompts)

---

## PHASE 2 — RAG (Retrieval-Augmented Generation) — HIGH PRIORITY

### 2.1 Core RAG Concepts
- What RAG is and why it's needed (LLM doesn't "know" your private data)
- Chunking strategies (fixed-size, semantic, recursive chunking)
- Embeddings — what they are (vector representation of text meaning)
- Embedding models (OpenAI text-embedding-3, Google, open-source options like sentence-transformers)
- Similarity search (cosine similarity, dot product) — conceptual only
- Retrieval pipeline: query → embed → search → retrieve → inject into prompt → generate

### 2.2 Vector Databases (you already know Postgres — huge advantage)
- **pgvector** (Postgres extension) — since you already use Postgres/Supabase
- Supabase Vector (built on pgvector) — directly usable with your existing stack
- Pinecone (managed vector DB, popular in industry)
- Chroma, Weaviate, Qdrant (alternatives, good to know exist)
- Indexing strategies (HNSW, IVFFlat) — just conceptual awareness

### 2.3 Building a Full RAG Pipeline (project-based learning)
- Document loading & parsing (PDF, docx, txt, web pages)
- Chunking + metadata tagging
- Embedding generation + storage in vector DB
- Query pipeline with re-ranking (basic)
- Hybrid search (keyword + vector search combined)
- Citation/source attribution in responses

---

## PHASE 3 — AI Agents & Tool Use — HIGH PRIORITY (you're already close via MCP/Claude skills)

### 3.1 Function Calling / Tool Use
- What "function calling" means to an LLM (structured tool definitions)
- Defining tool schemas (JSON schema for parameters)
- Multi-step tool calling (LLM decides which tool, when)
- Parallel vs sequential tool calls

### 3.2 Agent Concepts
- What an "AI agent" actually is (LLM + tools + loop + memory)
- ReAct pattern (Reason + Act loop)
- Agent memory: short-term (conversation) vs long-term (vector DB/persistent storage)
- Planning & task decomposition (breaking a big goal into steps)
- Multi-agent systems (orchestrator + sub-agents) — conceptual
- Guardrails & validation (stopping agents from doing something wrong)
- Human-in-the-loop patterns (approval steps before agent takes action)

### 3.3 MCP (Model Context Protocol) — you already use this daily!
- What MCP is and why it exists (standardized tool/connector protocol)
- MCP servers vs MCP clients
- Building a simple custom MCP server (you already understand this from Claude skills usage)
- This is a genuine strength already — just formalize the understanding

### 3.4 Agent Frameworks (pick ONE to start, don't learn all)
- LangChain / LangGraph (most popular, steep learning curve)
- LlamaIndex (RAG-focused, good if RAG is your main use case)
- CrewAI (multi-agent, simpler mental model)
- Or: raw/no-framework approach (just API + custom loop) — good for understanding fundamentals first

---

## PHASE 4 — Flutter + AI Integration (YOUR SPECIALTY — where you win)

### 4.1 Flutter-Specific AI Integration Patterns
- Calling LLM APIs from Dio (streaming response handling in Flutter)
- Displaying streaming text (typewriter effect UI pattern)
- Chat UI patterns (message bubbles, loading states, markdown rendering in chat)
- flutter_markdown or similar packages for rendering AI responses
- Voice input/output integration (speech-to-text, text-to-speech packages)
- Image picker + vision API integration (send image to GPT-4V/Claude vision/Gemini)
- On-device AI: Google ML Kit (text recognition, object detection, translation)
- On-device small models (TensorFlow Lite / Core ML basics — optional, advanced)

### 4.2 State Management for AI Features (you already know this — just apply it)
- Managing streaming state with Riverpod/BLoC (loading, streaming, error, complete states)
- Handling long-running AI operations (background tasks, cancellation tokens)
- Caching AI responses (avoid re-calling API for same query)
- Optimistic UI patterns for AI chat (you already do this — reuse the pattern)

### 4.3 Backend Architecture for AI Flutter Apps
- Why you should NEVER call LLM APIs directly from Flutter client (API key security)
- Building a thin backend proxy (Firebase Functions, Supabase Edge Functions, or FastAPI)
- Supabase Edge Functions (Deno/TypeScript) — good fit since you already use Supabase
- Firebase Cloud Functions + Vertex AI / Gemini integration
- Storing conversation history in Postgres/Supabase (schema design for chat apps)
- User-level rate limiting & usage tracking (important for cost control)

---

## PHASE 5 — Production, Cost & Reliability Concerns

### 5.1 Cost Management
- Token counting before sending requests
- Choosing the right model per task (cheap model for simple tasks, expensive for complex)
- Caching strategies (prompt caching, response caching)
- Setting usage limits per user

### 5.2 Evaluation & Testing (lightweight version, not full eval engineering)
- How to test if a prompt/RAG pipeline "works" (basic eval sets)
- Hallucination awareness — how to reduce it (grounding, citations)
- Logging AI interactions for debugging

### 5.3 Security Basics
- Prompt injection awareness (someone tricking your AI feature)
- Never exposing API keys client-side
- Content moderation (basic filtering of harmful inputs/outputs, especially important for public apps)
- PII handling awareness (don't send sensitive user data unnecessarily to third-party APIs)

---

## PHASE 6 — Portfolio & Positioning (after Phases 1-4 are solid)

### 6.1 Build 2-3 Portfolio Projects
1. **AI Chat App in Flutter** — streaming chat UI + backend proxy + conversation history in Supabase
2. **RAG-powered Document Q&A App** — upload PDF → chunk/embed → ask questions → get cited answers (Flutter frontend + Supabase pgvector backend)
3. **Simple AI Agent Demo** — an agent that automates a real task (e.g., your own content pipeline: input topic → agent researches → drafts → formats — tie this to your existing skills work)

### 6.2 Case Study Write-ups
- Document the "before/after" and technical decisions for each project
- Screenshots + short video demos (you already have video production skills — use them)

### 6.3 Upwork/Fiverr Positioning (once learning is done)
- Profile headline: "Flutter Developer | AI Integration Specialist (LLM, RAG, AI Agents)"
- Service packages: AI chatbot integration, RAG document search feature, AI agent automation for existing apps
- Pricing calibration based on the earlier market research ($20-35/hr to start, scale up with portfolio)

---

## Suggested Learning Order (Priority Sequence)

1. Phase 0 (quick refresher, 3-5 days)
2. Phase 1 — LLM Fundamentals + API integration (1-2 weeks)
3. Phase 4.1 & 4.2 — Start integrating into Flutter immediately (parallel with Phase 1, don't wait)
4. Phase 2 — RAG + pgvector/Supabase (2-3 weeks) — your Postgres background makes this fast
5. Phase 3 — Agents & Tool Use (2-3 weeks) — you're already halfway here via MCP/Claude skills usage
6. Phase 5 — Production concerns (learn as-you-go while building projects, not as separate study block)
7. Phase 6 — Portfolio + Fiverr/Upwork positioning

**Total realistic timeline: 8-12 weeks** of consistent part-time learning (given your existing dev background, this is faster than a typical beginner path).

---

## Notes
- You do NOT need deep math, PyTorch, model training, or fine-tuning for this path — that's traditional ML Engineer/Researcher territory, not required for LLM Application/Agent Engineer roles.
- Your existing Postgres + Supabase experience is a genuine shortcut for the RAG phase — most learners have to learn vector DBs from scratch.
- Your daily use of Claude Code, Cursor, Antigravity, and Claude skills already IS agent/tool-use experience — Phase 3 will feel like formalizing what you're already doing, not learning from zero.
