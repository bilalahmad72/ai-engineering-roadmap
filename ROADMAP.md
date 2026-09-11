# 📖 Day-by-Day Roadmap

78 learning days · ~2 hours/day · 6 days/week · ≈13 weeks

_Generated from `data/curriculum/` — edit those files, not this one._

---

## Setup

`D01–D01` · roadmap ref `PHASE 0` · 0/1 done

> **Goal:** Machine ready: Python, venv, VS Code aur repo workflow.

### D01 — Python setup + syntax (Dart se mapping)

🟡 **Running** · 2h · ref `0.1`

**Objectives**

- Python 3 + venv + pip ka workflow samajhna
- Dart ke concepts ko Python me map karna (types, collections, classes)

**Tasks**

- [x] venv banao: python -m venv .venv, activate karo, pip install httpx
- [x] Ek cheatsheet likho: Dart List/Map/class/null-safety -> Python list/dict/class/Optional
- [ ] JSON parse + dump ka chhota script likho (json module)
- [ ] requirements.txt generate karo (pip freeze)

**Deliverable:** Dart-vs-Python cheatsheet note

**Notes:** [D01-python-setup.md](notes/daily/D01-python-setup.md), [TOOLING.md](notes/TOOLING.md)

---

## Python Core (scratch se)

`PY01–PY12` · roadmap ref `PHASE 0.1 — expanded` · 1/12 done

> **Goal:** Python zero se poori tarah — sirf itna jitna is safar me chahiye, lekin woh mazbooti se. Maqsad: kisi bhi maujooda Python file ko khol kar samajh lena.

### PY01 — Syntax, variables, types aur strings

✅ **Done** · 2h · ref `0.1`

**Objectives**

- Python ka syntax model (indentation, no semicolons, no braces)
- Types, type conversion aur f-strings

**Tasks**

- [x] Topic 1: variables, 5 types, type().__name__, format specs (:,.2f / :.6f / :.1%)
- [x] Topic 2: int/float/str/bool conversion, truthiness rule, isdigit vs float(), EAFP
- [x] Topic 3: string methods — strip/split/join/slicing, .env parsing, API key masking, validation
- [x] Topic 4: f-string deep dive — alignment tables, padding, {var=} debug shortcut

**Deliverable:** 4 practice files + PY01 note (concept + apna code + output)

**Notes:** [PY01-syntax-types.md](notes/daily/PY01-syntax-types.md), [ISSUES.md](notes/ISSUES.md)

### PY02 — Collections: list, tuple, dict, set

🟡 **Running** · 2h · ref `0.1`

**Objectives**

- Chaaron collections aur unka sahi istemal
- Indexing, slicing aur mutation

**Tasks**

- [x] list: append/extend/insert/remove/pop/sort/reverse + slicing [a:b:c]
- [x] dict: get/keys/values/items/update/pop + nested access
- [x] set: add/remove/union/intersection + duplicates hatana
- [ ] tuple: immutability, unpacking, swap; PRACTICE: exercises green karo

**Deliverable:** PY02 practice — sab tests green

**Notes:** [PY02-collections.md](notes/daily/PY02-collections.md)

### PY03 — Control flow: if, loops, comprehensions

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- Conditions aur loops Python ke tareeqe se
- Comprehensions — Python ka signature idiom

**Tasks**

- [ ] if/elif/else, truthy-falsy values, ternary, match statement
- [ ] for + range/enumerate/zip, while, break/continue/else
- [ ] List/dict/set comprehensions, nested aur conditional
- [ ] PRACTICE: exercises green karo

**Deliverable:** PY03 practice — sab tests green

### PY04 — Functions poori tarah

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- Parameters ki saari qismein
- Scope, closures aur lambda

**Tasks**

- [ ] positional, default, keyword-only, *args, **kwargs
- [ ] Multiple return values (tuple unpacking), type hints
- [ ] Scope: local/global, aur mutable default argument ka mashhoor bug
- [ ] lambda, map/filter vs comprehension; PRACTICE: exercises green karo

**Deliverable:** PY04 practice — sab tests green

### PY05 — Modules, imports aur project structure

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- Code ko multiple files me todna
- import system samajhna

**Tasks**

- [ ] import x / from x import y / as alias, aur circular import ka masla
- [ ] __name__ == '__main__' ka asal matlab
- [ ] Apna module + package (__init__.py) banao aur use karo
- [ ] pip, requirements.txt, aur standard project layout; PRACTICE: exercises

**Deliverable:** Multi-file package jo chalta ho

### PY06 — Files, paths, JSON aur environment

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- File I/O safely
- JSON aur .env — roz ka kaam

**Tasks**

- [ ] open() + with statement (context manager) + encoding='utf-8'
- [ ] pathlib: Path, /, exists, mkdir, glob, read_text
- [ ] json loads/dumps/load/dump + ensure_ascii + default=
- [ ] os.getenv + python-dotenv; PRACTICE: D01 ke EX5/EX6 bhi complete karo

**Deliverable:** PY06 practice + D01 exercises green

### PY07 — Errors aur exceptions

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- Traceback parhna
- Errors ko sahi tarah handle karna

**Tasks**

- [ ] try/except/else/finally, multiple except, exception hierarchy
- [ ] raise, custom exception class, exception chaining (raise ... from)
- [ ] Traceback ko neeche se upar parhna — asli line dhoondna
- [ ] Anti-pattern: bare except aur silent pass; PRACTICE: exercises

**Deliverable:** PY07 practice — sab tests green

### PY08 — OOP: classes, dataclass, properties

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- Class banana aur use karna
- dataclass aur Pydantic ka farq

**Tasks**

- [ ] __init__, self, instance vs class attributes, methods
- [ ] __str__/__repr__/__eq__, @property, @staticmethod, @classmethod
- [ ] Inheritance + super(), aur composition kab behtar hai
- [ ] @dataclass; Pydantic ka taaruf (validation ke liye); PRACTICE: exercises

**Deliverable:** PY08 practice — sab tests green

### PY09 — Iterators aur generators (streaming ki bunyad)

⬜ **Pending** · 2h · ref `0.1 / 1.2`

**Objectives**

- yield kya karta hai
- Lazy evaluation — LLM streaming isi par chalti hai

**Tasks**

- [ ] Iterable vs iterator, for loop andar se kaise chalta hai
- [ ] yield se generator function, generator expression ( ) vs [ ]
- [ ] Memory ka farq: badi file line-by-line vs poori list me
- [ ] Generator se ek fake token stream banao; PRACTICE: exercises

**Deliverable:** Generator-based fake LLM stream

### PY10 — Async Python (asyncio)

⬜ **Pending** · 2h · ref `0.1 / 0.2`

**Objectives**

- async/await Python me — Dart se farq
- Concurrent calls

**Tasks**

- [ ] async def, await, coroutine vs Future, asyncio.run
- [ ] asyncio.gather (Dart Future.wait) se parallel calls
- [ ] async for, async with, aur async generator (streaming ke liye)
- [ ] Blocking code async ko kaise tabah karta hai; PRACTICE: exercises

**Deliverable:** PY10 practice — concurrent async script

### PY11 — Typing, stdlib aur Pythonic idioms

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- Type hints theek se
- Woh stdlib jo roz chahiye

**Tasks**

- [ ] typing: list[str], dict[str, Any], Optional, Union (|), Literal, TypedDict
- [ ] datetime + timezone, uuid, logging (print ki jagah)
- [ ] enumerate/zip/any/all/sorted(key=)/max(key=) patterns
- [ ] PEP 8 + Ruff se apna purana code saaf karo; PRACTICE: exercises

**Deliverable:** PY11 practice + Ruff-clean code

### PY12 — Doosron ka Python code parhna (asli imtihan)

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- Anjaan codebase khol kar samajhna
- Debugger se code ka behaviour dekhna

**Tasks**

- [ ] Is repo ka scripts/track.py line-by-line parho aur uska flow likho
- [ ] VS Code debugger: breakpoint, F5, F10, F11, variables panel
- [ ] track.py me ek chhota feature khud add karo (e.g. 'streak' count)
- [ ] Ek open-source Python repo kholo aur uska entry point dhoondo

**Deliverable:** track.py me apna feature + code-reading note

---

## API Foundations (Python me)

`D02–D04` · roadmap ref `PHASE 0.1 / 0.2` · 0/3 done

> **Goal:** Python core ko asli kaam par lagana: async HTTP, FastAPI, aur SSE streaming - LLM APIs se pehle ka aakhri padao.

### D02 — Python async + HTTP client

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- async/await Python me (Dart Future/async se compare)
- httpx se REST calls aur error handling

**Tasks**

- [ ] asyncio.run + async def se 3 concurrent HTTP calls karo
- [ ] httpx.AsyncClient use karke ek public API hit karo
- [ ] Timeout aur exception handling add karo
- [ ] Dart Future.wait vs asyncio.gather ka comparison note karo

**Deliverable:** async_http_demo.py

### D03 — FastAPI basics + .env secrets

⬜ **Pending** · 2h · ref `0.1`

**Objectives**

- FastAPI se chhota backend service khada karna
- API keys ko .env me safely rakhna

**Tasks**

- [ ] pip install fastapi uvicorn python-dotenv
- [ ] GET /health aur POST /echo endpoints banao (Pydantic model ke saath)
- [ ] .env + os.getenv se dummy key load karo, .gitignore me .env daalo
- [ ] uvicorn --reload se run karke curl se test karo

**Deliverable:** Chalta hua FastAPI hello-service

### D04 — API refresher: streaming, retries, rate limits

⬜ **Pending** · 2h · ref `0.2`

**Objectives**

- SSE (Server-Sent Events) kya hai aur LLM streaming me kyun zaroori hai
- Exponential backoff aur rate limit handling

**Tasks**

- [ ] FastAPI me StreamingResponse se SSE endpoint banao jo 1 word/second bheje
- [ ] Us endpoint ko Python client se stream karke consume karo
- [ ] Exponential backoff retry helper likho (429/5xx par)
- [ ] Auth types note karo: API key vs Bearer vs OAuth

**Deliverable:** sse_demo (server + client) + retry helper

---

## LLM Fundamentals + API Integration

`D05–D14` · roadmap ref `PHASE 1` · 0/10 done

> **Goal:** LLM APIs ko confidently call karna: streaming, structured output, tools, cost control.

### D05 — Tokens, tokenization aur context window

⬜ **Pending** · 2h · ref `1.1`

**Objectives**

- Token kya hai aur cost/limits tokens me kyun measure hote hain
- Context window ka app design par asar

**Tasks**

- [ ] tiktoken (ya Anthropic count_tokens) se apne sample texts ke tokens ginno
- [ ] Urdu/Roman Urdu vs English text ka token count compare karo
- [ ] 3 models ke context windows aur per-1M pricing ka table banao
- [ ] Note karo: lambi chat history ka cost par kya asar padta hai

**Deliverable:** Token/cost comparison table

### D06 — Sampling params + message roles

⬜ **Pending** · 2h · ref `1.1`

**Objectives**

- temperature, top_p, max_tokens, stop sequences ka practical asar
- system / user / assistant roles ka sahi istemal

**Tasks**

- [ ] Ek hi prompt ko temperature 0 / 0.7 / 1.2 par chalao, outputs compare karo
- [ ] max_tokens chhota rakh kar dekho response kaise cut hota hai (stop_reason)
- [ ] System prompt badal kar tone/persona change karke dekho
- [ ] Findings notes me likho

**Deliverable:** params_experiment.py + observations

### D07 — Model landscape + multimodal

⬜ **Pending** · 2h · ref `1.1`

**Objectives**

- GPT / Claude / Gemini / Llama / Mistral ka comparison
- Kaunsa model kis kaam ke liye (cheap vs smart)

**Tasks**

- [ ] Har family ka latest model + pricing + context window note karo
- [ ] Multimodal (text+image+audio) support ka comparison banao
- [ ] Model selection cheatsheet: task -> recommended model
- [ ] Open-source vs API tradeoffs 5 points me likho

**Deliverable:** Model selection cheatsheet

### D08 — OpenAI API hands-on

⬜ **Pending** · 2h · ref `1.2`

**Objectives**

- Chat completions end-to-end
- Errors, retries, timeouts handle karna

**Tasks**

- [ ] openai SDK install + first chat completion
- [ ] Multi-turn conversation loop banao (history maintain karke)
- [ ] Rate limit / invalid key / timeout errors deliberately trigger karke handle karo
- [ ] Usage object se token count log karo

**Deliverable:** openai_chat.py (multi-turn CLI chat)

### D09 — Anthropic Messages API hands-on

⬜ **Pending** · 2h · ref `1.2`

**Objectives**

- Claude Messages API ka shape
- System prompt, stop_reason, prompt caching

**Tasks**

- [ ] anthropic SDK se first message call
- [ ] System prompt alag param me dena (OpenAI se farq note karo)
- [ ] Prompt caching try karo aur cost difference dekho
- [ ] OpenAI vs Anthropic request/response diff table banao

**Deliverable:** claude_chat.py + API diff table

### D10 — Streaming responses (SSE) code me

⬜ **Pending** · 2h · ref `1.2`

**Objectives**

- Dono providers se streaming
- Chunk parsing aur partial updates

**Tasks**

- [ ] OpenAI stream=True se token-by-token print karo
- [ ] Anthropic streaming events (content_block_delta) handle karo
- [ ] Streaming ke doraan error/disconnect handle karo
- [ ] FastAPI me /chat/stream proxy endpoint banao jo aage stream kare

**Deliverable:** Streaming proxy endpoint (Phase 4B ki base)

### D11 — Structured outputs / JSON mode

⬜ **Pending** · 2h · ref `1.3`

**Objectives**

- Model se reliable JSON nikalna
- Pydantic se validate karna

**Tasks**

- [ ] Pydantic model define karo (e.g. Invoice, Recipe)
- [ ] OpenAI structured outputs / response_format se JSON lo
- [ ] Claude me tool-schema trick se JSON lo
- [ ] Invalid JSON par retry/repair logic likho

**Deliverable:** structured_extract.py

### D12 — Function calling / tool use - pehla taste

⬜ **Pending** · 2h · ref `1.2 / 3.1`

**Objectives**

- Tool definition ka structure
- Tool result wapas model ko dena

**Tasks**

- [ ] Ek get_weather (mock) tool define karo JSON schema ke saath
- [ ] Model ka tool_use response parse karke tool chalao
- [ ] Result wapas bhej kar final answer lo
- [ ] Yehi cheez dono providers me karke syntax farq note karo

**Deliverable:** first_tool_call.py

### D13 — Prompt engineering core

⬜ **Pending** · 2h · ref `1.3`

**Objectives**

- Zero-shot, few-shot, CoT, role prompting
- Prompt templates + variables

**Tasks**

- [ ] Ek classification task lo aur zero-shot vs few-shot accuracy compare karo
- [ ] Chain-of-thought add karke reasoning task improve karo
- [ ] Prompt template class banao (variables inject karne ke liye)
- [ ] Output format control: XML tags vs JSON vs markdown

**Deliverable:** prompts/ folder with templates

### D14 — Prompt injection, versioning + Phase 1 mini-project

⬜ **Pending** · 2h · ref `1.3 / 5.1`

**Objectives**

- Injection risk samajhna aur mitigate karna
- Prompt A/B testing + cost control

**Tasks**

- [ ] Apne hi prompt par injection attack try karo, phir mitigation lagao
- [ ] 2 prompt versions ka same input par A/B comparison script likho
- [ ] Cheap model + expensive model routing logic add karo
- [ ] MINI-PROJECT: CLI assistant - streaming + tool call + structured output, sab ek jagah

**Deliverable:** Phase 1 mini-project: CLI AI assistant

---

## Flutter + AI Integration (Client)

`D15–D20` · roadmap ref `PHASE 4.1 / 4.2` · 0/6 done

> **Goal:** Apni asli taqat: Flutter me streaming AI chat, vision, voice aur state management. Phase 1 ke saath parallel bhi chala sakte ho.

### D15 — Flutter se LLM backend call (Dio setup)

⬜ **Pending** · 2h · ref `4.1`

**Objectives**

- Flutter app ko apne FastAPI proxy se jorna
- Request/response models banana

**Tasks**

- [ ] Naya Flutter project banao (clean architecture scaffold)
- [ ] Dio client + interceptor setup (logging, error mapping)
- [ ] D10 wale /chat/stream backend ka non-streaming version call karo
- [ ] Response ko model class me parse karke screen par dikhao

**Deliverable:** Flutter app jo backend se AI reply le raha hai

### D16 — Streaming Flutter me (SSE + typewriter UI)

⬜ **Pending** · 2h · ref `4.1`

**Objectives**

- Dio ResponseType.stream se SSE consume karna
- Token-by-token UI update

**Tasks**

- [ ] Dio se stream response lo aur utf8 decode + line split karo
- [ ] SSE data: lines parse karke Stream<String> banao
- [ ] Typewriter effect widget banao jo chunks append kare
- [ ] Stream cancel / dispose sahi se handle karo

**Deliverable:** Streaming text widget

### D17 — Chat UI patterns + markdown rendering

⬜ **Pending** · 2h · ref `4.1`

**Objectives**

- Message bubbles, loading, error states
- AI response me markdown/code blocks render karna

**Tasks**

- [ ] Message model (role, content, status, timestamp) banao
- [ ] Bubble widgets + auto-scroll to bottom
- [ ] flutter_markdown se response render karo (code block styling ke saath)
- [ ] Empty / loading / error / retry states design karo

**Deliverable:** Reusable chat UI package/folder

### D18 — Streaming state Riverpod/BLoC ke saath

⬜ **Pending** · 2h · ref `4.2`

**Objectives**

- Streaming ke 4 states manage karna
- Cancellation aur long-running operations

**Tasks**

- [ ] State define karo: idle / streaming / complete / error
- [ ] Riverpod StreamProvider (ya BLoC) se stream ko state me convert karo
- [ ] Stop button se generation cancel karo (CancelToken)
- [ ] Rebuild optimization: sirf message bubble rebuild ho, poori list nahi

**Deliverable:** Chat state notifier/bloc

### D19 — Vision + voice integration

⬜ **Pending** · 2h · ref `4.1`

**Objectives**

- Image ko vision model par bhejna
- Speech-to-text aur text-to-speech basics

**Tasks**

- [ ] image_picker se image lo, base64 karke backend par bhejo
- [ ] Backend se vision model (Claude/GPT/Gemini vision) call karao
- [ ] speech_to_text package se voice input lo
- [ ] flutter_tts se AI response bulwao

**Deliverable:** Multimodal chat screen

### D20 — Caching + on-device ML Kit + Phase checkpoint

⬜ **Pending** · 2h · ref `4.1 / 4.2`

**Objectives**

- Same query par dobara API call na ho
- On-device AI ka scope samajhna

**Tasks**

- [ ] Response cache (Hive/sqflite) + cache key strategy
- [ ] Google ML Kit se text recognition (OCR) try karo
- [ ] OCR text ko LLM ko bhej kar summarize karao
- [ ] CHECKPOINT: streaming + markdown + vision + cache wala working demo app

**Deliverable:** Phase 4A checkpoint app

---

## RAG (Retrieval-Augmented Generation)

`D21–D34` · roadmap ref `PHASE 2` · 0/14 done

> **Goal:** Private data par LLM chalana - chunking se le kar pgvector, hybrid search aur citations tak. Tumhara Postgres/Supabase background yahan shortcut hai.

### D21 — RAG kya hai aur kyun (architecture overview)

⬜ **Pending** · 2h · ref `2.1`

**Objectives**

- RAG ki zaroorat samajhna (LLM tumhara private data nahi jaanta)
- Naive RAG pipeline ka end-to-end naksha

**Tasks**

- [ ] Pipeline diagram banao: ingest -> chunk -> embed -> store -> retrieve -> prompt -> generate
- [ ] RAG vs fine-tuning vs long-context ka comparison likho
- [ ] Kaunse client problems RAG se hal hote hain, 5 examples likho (Fiverr gig ideas)
- [ ] Ek chhoti hardcoded 'fake RAG' banao: text ko prompt me daal kar sawal pucho

**Deliverable:** RAG architecture note + fake-RAG script

### D22 — Embeddings conceptually

⬜ **Pending** · 2h · ref `2.1`

**Objectives**

- Embedding kya hai (text ka meaning vector)
- Embedding models ka comparison

**Tasks**

- [ ] Embedding vs token ka farq clear karo notes me
- [ ] OpenAI text-embedding-3-small/large, Gemini, sentence-transformers compare karo
- [ ] Dimensions, cost, aur quality ka tradeoff note karo
- [ ] Decide karo default embedding model kaunsa use karoge aur kyun

**Deliverable:** Embedding model decision note

### D23 — Embeddings generate + similarity hand se

⬜ **Pending** · 2h · ref `2.1`

**Objectives**

- Actual embeddings banana
- Cosine similarity khud calculate karna

**Tasks**

- [ ] 10 sentences ke embeddings generate karo
- [ ] numpy se cosine similarity matrix banao
- [ ] Dekho kaunse sentences semantically qareeb aaye
- [ ] Ek 'search' function likho: query -> top 3 similar sentences

**Deliverable:** similarity_demo.py

### D24 — Chunking strategies

⬜ **Pending** · 2h · ref `2.1 / 2.3`

**Objectives**

- Fixed, recursive aur semantic chunking
- Chunk size + overlap ka retrieval quality par asar

**Tasks**

- [ ] Ek lambi document lo aur 3 tareeqon se chunk karo
- [ ] Chunk size 256 vs 512 vs 1024 par retrieval quality compare karo
- [ ] Overlap add karke dekho context kaise behtar hota hai
- [ ] Har chunk ke saath metadata attach karo (source, page, section)

**Deliverable:** chunking.py + comparison notes

### D25 — Document loading & parsing

⬜ **Pending** · 2h · ref `2.3`

**Objectives**

- PDF/docx/html/txt se clean text nikalna
- Parsing ke real-world masail

**Tasks**

- [ ] pypdf ya pdfplumber se PDF text extract karo
- [ ] python-docx aur BeautifulSoup se docx/html handle karo
- [ ] Tables, headers/footers, aur scanned PDFs ke masail note karo
- [ ] Ek unified loader function banao jo file type detect kare

**Deliverable:** loaders.py

### D26 — pgvector setup (Supabase/Postgres)

⬜ **Pending** · 2h · ref `2.2`

**Objectives**

- pgvector extension enable karna
- Documents + chunks ka schema design

**Tasks**

- [ ] Supabase project me vector extension enable karo
- [ ] Tables banao: documents, chunks (embedding vector(1536), metadata jsonb)
- [ ] RLS policies socho (user apna hi data dekhe)
- [ ] Foreign keys + cascade delete set karo

**Deliverable:** SQL migration file

### D27 — Embeddings store + similarity query

⬜ **Pending** · 2h · ref `2.2`

**Objectives**

- pgvector me insert aur search
- SQL me distance operators

**Tasks**

- [ ] Chunks + embeddings ko batch insert karo
- [ ] <=> (cosine) operator se nearest neighbours query likho
- [ ] Ek Postgres function match_chunks(query_embedding, k) banao
- [ ] Python se function call karke results verify karo

**Deliverable:** Working vector search query

### D28 — Indexing: HNSW vs IVFFlat

⬜ **Pending** · 2h · ref `2.2`

**Objectives**

- Index ke bagair search kyun slow hai
- Do index types ka tradeoff

**Tasks**

- [ ] Bina index ke 10k rows par query time measure karo
- [ ] IVFFlat index banao aur time dobara measure karo
- [ ] HNSW index banao aur compare karo (build time vs query time vs recall)
- [ ] Decision note: kis situation me kaunsa index

**Deliverable:** Index benchmark note

### D29 — Full retrieval pipeline

⬜ **Pending** · 2h · ref `2.3`

**Objectives**

- query -> embed -> search -> context assemble
- Top-k tuning

**Tasks**

- [ ] End-to-end retrieve() function likho
- [ ] Top-k=3 vs 5 vs 10 ka answer quality par asar dekho
- [ ] Context length budget manage karo (token limit ke andar)
- [ ] Duplicate/overlapping chunks filter karo

**Deliverable:** retriever.py

### D30 — Prompt assembly + citations

⬜ **Pending** · 2h · ref `2.3`

**Objectives**

- Retrieved context ko prompt me sahi tarah daalna
- Source attribution dena

**Tasks**

- [ ] RAG prompt template banao (context XML tags me)
- [ ] Model ko chunk IDs cite karne par majboor karo
- [ ] Citations ko source metadata se resolve karke show karo
- [ ] Jab context me jawab na ho to 'nahi pata' kehne wala instruction test karo

**Deliverable:** rag_answer.py with citations

### D31 — Hybrid search (keyword + vector)

⬜ **Pending** · 2h · ref `2.3`

**Objectives**

- Pure vector search kahan fail hota hai
- Full-text + vector ko combine karna

**Tasks**

- [ ] Postgres tsvector full-text search set karo
- [ ] Aisi queries dhoondo jahan keyword search jeete (names, IDs, exact terms)
- [ ] Reciprocal Rank Fusion (RRF) se dono results merge karo
- [ ] Pure vector vs hybrid ka side-by-side comparison

**Deliverable:** hybrid_search.py

### D32 — Re-ranking basics

⬜ **Pending** · 2h · ref `2.3`

**Objectives**

- Re-ranker kya karta hai
- Retrieve-then-rerank pattern

**Tasks**

- [ ] Top-20 retrieve karke LLM se top-5 rerank karao
- [ ] Cohere rerank / cross-encoder option explore karo
- [ ] Latency vs quality tradeoff measure karo
- [ ] Decide karo kab reranking worth hai

**Deliverable:** reranker.py

### D33 — Metadata filtering + multi-tenant RAG

⬜ **Pending** · 2h · ref `2.3 / 5.3`

**Objectives**

- Per-user document isolation
- Filtered vector search

**Tasks**

- [ ] user_id se filtered vector search karo (WHERE + vector order)
- [ ] Date range / document type filters add karo
- [ ] RLS policies test karo (dusre user ka data leak na ho)
- [ ] Multi-tenant schema ke pitfalls note karo

**Deliverable:** Filtered + secure retrieval

### D34 — RAG evaluation + Phase 2 mini-project

⬜ **Pending** · 2h · ref `2.3 / 5.2`

**Objectives**

- RAG kaam kar raha hai ya nahi, kaise pata karein
- Common failure modes

**Tasks**

- [ ] 20 question/answer ka eval set banao apne documents se
- [ ] Retrieval hit-rate aur answer correctness manually score karo
- [ ] Failure modes note karo: bad chunking, missing context, hallucination
- [ ] MINI-PROJECT: PDF upload -> ingest -> question -> cited answer (FastAPI se)

**Deliverable:** Phase 2 mini-project: Document Q&A API

---

## AI Agents & Tool Use

`D35–D48` · roadmap ref `PHASE 3` · 0/14 done

> **Goal:** Agent = LLM + tools + loop + memory. MCP tum already daily use karte ho - yahan usay formalize karna hai.

### D35 — Agent actually kya hai

⬜ **Pending** · 2h · ref `3.2`

**Objectives**

- Agent vs chatbot vs workflow ka farq
- Loop, tools, memory, termination

**Tasks**

- [ ] Agent ki definition apne lafzon me likho: LLM + tools + loop + memory
- [ ] Claude Code khud kaise agent hai, uska breakdown likho
- [ ] 3 real use cases likho jo tum Fiverr par bech sakte ho
- [ ] Agent loop ka pseudocode likho (stop condition ke saath)

**Deliverable:** Agent concepts note

### D36 — Tool schemas deep dive

⬜ **Pending** · 2h · ref `3.1`

**Objectives**

- Accha tool schema kaise likhein
- Description hi asli prompt hai

**Tasks**

- [ ] 5 tools ke JSON schemas likho (search, read_file, send_email, db_query, calculator)
- [ ] Required vs optional params, enums, nested objects use karo
- [ ] Buri vs achi tool description ka A/B test karo
- [ ] Dekho model galat schema par kaise fail hota hai

**Deliverable:** tools/ schema library

### D37 — Raw agent loop (bina framework)

⬜ **Pending** · 2h · ref `3.2 / 3.4`

**Objectives**

- Poora agent loop khud likhna
- Fundamentals framework se pehle

**Tasks**

- [ ] while loop: call model -> agar tool_use hai to chalao -> result wapas -> repeat
- [ ] Max iterations limit lagao (infinite loop se bachne ke liye)
- [ ] Conversation history properly maintain karo
- [ ] Har step log karo taake debugging aasan ho

**Deliverable:** agent.py (raw loop, ~100 lines)

### D38 — Multi-step aur parallel tool calls

⬜ **Pending** · 2h · ref `3.1`

**Objectives**

- Ek turn me multiple tools
- Sequential vs parallel execution

**Tasks**

- [ ] Aisa task do jisme 3 tools chahiye (multi-step chain)
- [ ] Parallel tool calls handle karo (asyncio.gather)
- [ ] Tool failure handle karo (error result wapas model ko do)
- [ ] Tool call sequence visualize/log karo

**Deliverable:** Multi-tool agent

### D39 — ReAct pattern

⬜ **Pending** · 2h · ref `3.2`

**Objectives**

- Reason + Act loop
- Thinking traces ka faida

**Tasks**

- [ ] ReAct prompt likho: Thought -> Action -> Observation
- [ ] Apne raw agent ko ReAct style me convert karo
- [ ] Extended thinking / reasoning models se compare karo
- [ ] Note: kab ReAct zaroori hai aur kab overkill

**Deliverable:** react_agent.py

### D40 — Short-term memory + context management

⬜ **Pending** · 2h · ref `3.2 / 5.1`

**Objectives**

- Conversation history ko context window me fit rakhna
- Summarization aur trimming

**Tasks**

- [ ] Sliding window trimming implement karo
- [ ] Purani history ka summary bana kar replace karo
- [ ] Token budget tracker banao
- [ ] Long conversation par test karo, cost measure karo

**Deliverable:** memory/short_term.py

### D41 — Long-term memory (vector DB)

⬜ **Pending** · 2h · ref `3.2`

**Objectives**

- Persistent memory RAG ke through
- Kya yaad rakhna hai aur kya nahi

**Tasks**

- [ ] Phase 2 wala pgvector reuse karke memory store banao
- [ ] Agent ko save_memory aur recall_memory tools do
- [ ] Facts extract karke store karo (poori chat nahi)
- [ ] Nayi session me recall test karo

**Deliverable:** memory/long_term.py

### D42 — Planning & task decomposition

⬜ **Pending** · 2h · ref `3.2`

**Objectives**

- Bara goal chhote steps me todna
- Plan-then-execute pattern

**Tasks**

- [ ] Planner prompt banao jo task ko steps me tode
- [ ] Steps ko execute karke progress track karo
- [ ] Re-planning add karo jab koi step fail ho
- [ ] Single-agent vs orchestrator+subagents ka concept note karo

**Deliverable:** planner_agent.py

### D43 — Guardrails & validation

⬜ **Pending** · 2h · ref `3.2`

**Objectives**

- Agent ko galat kaam se rokna
- Input/output validation layers

**Tasks**

- [ ] Tool-level permission checks lagao (kaunsa tool kis condition me chale)
- [ ] Output validation: schema + business rules
- [ ] Destructive actions ke liye allowlist/denylist
- [ ] Deliberately galat instruction de kar guardrail test karo

**Deliverable:** guardrails.py

### D44 — Human-in-the-loop approvals

⬜ **Pending** · 2h · ref `3.2`

**Objectives**

- Approval step se pehle rukna
- Resumable agent state

**Tasks**

- [ ] Risky tools ko 'requires_approval' mark karo
- [ ] Agent ko pause karke approval maango, phir resume karo
- [ ] Agent state serialize/deserialize karo (DB me save)
- [ ] Claude Code ka permission prompt pattern study karke note karo

**Deliverable:** Approval-gated agent

### D45 — MCP concepts

⬜ **Pending** · 2h · ref `3.3`

**Objectives**

- MCP kyun exist karta hai
- Server vs client, transports

**Tasks**

- [ ] MCP spec ka overview parho (tools, resources, prompts)
- [ ] stdio vs HTTP/SSE transport ka farq note karo
- [ ] Apne installed MCP servers ki list banao aur unke tools inspect karo
- [ ] MCP vs plain function calling: kab kya use karein

**Deliverable:** MCP concepts note

### D46 — Custom MCP server banao

⬜ **Pending** · 2h · ref `3.3`

**Objectives**

- Apna MCP server likhna
- Tools expose karna

**Tasks**

- [ ] MCP Python (ya TypeScript) SDK install karo
- [ ] 3 tools wala server banao (koi real kaam - e.g. is roadmap repo ka progress read/update)
- [ ] Local me test karo MCP inspector se
- [ ] Error handling + input validation add karo

**Deliverable:** Custom MCP server

### D47 — MCP server ko client se jorna

⬜ **Pending** · 2h · ref `3.3`

**Objectives**

- Real client me integrate karna
- Debugging

**Tasks**

- [ ] Apna server Claude Code / Claude Desktop me register karo
- [ ] Asli tasks par tools chala kar test karo
- [ ] Logs dekh kar issues debug karo
- [ ] Server ka README + usage docs likho

**Deliverable:** Working MCP integration + docs

### D48 — Framework chuno + Phase 3 mini-project

⬜ **Pending** · 2h · ref `3.4`

**Objectives**

- LangGraph / LlamaIndex / CrewAI ka comparison
- Ek chuno, apna agent port karo

**Tasks**

- [ ] Teeno ka comparison table banao (learning curve, use case, community)
- [ ] Ek framework choose karo aur reason likho
- [ ] D37 wale raw agent ko us framework me port karo
- [ ] MINI-PROJECT: real task automate karne wala agent (research -> draft -> format)

**Deliverable:** Phase 3 mini-project: working agent

---

## Backend Architecture for AI Flutter Apps

`D49–D52` · roadmap ref `PHASE 4.3` · 0/4 done

> **Goal:** Production-safe backend: API keys kabhi client me nahi, history Postgres me, usage control ke saath.

### D49 — Proxy architecture + key security

⬜ **Pending** · 2h · ref `4.3 / 5.3`

**Objectives**

- Client se direct LLM call kyun kabhi nahi
- Thin proxy ka design

**Tasks**

- [ ] Demo karo: Flutter APK se hardcoded key kaise nikal sakti hai
- [ ] Proxy architecture diagram banao (Flutter -> Auth -> Proxy -> LLM)
- [ ] Auth strategy decide karo (Supabase JWT verify)
- [ ] 3 options compare karo: Supabase Edge Functions vs Firebase Functions vs FastAPI

**Deliverable:** Backend architecture decision doc

### D50 — Supabase Edge Function LLM proxy

⬜ **Pending** · 2h · ref `4.3`

**Objectives**

- Deno Edge Function me LLM call
- Streaming pass-through

**Tasks**

- [ ] Supabase CLI setup + edge function scaffold
- [ ] Environment secrets me API key rakho
- [ ] LLM response ko client tak stream karo (ReadableStream)
- [ ] Flutter app se end-to-end streaming test karo

**Deliverable:** Deployed edge function proxy

### D51 — Conversation history schema

⬜ **Pending** · 2h · ref `4.3`

**Objectives**

- Chat data model Postgres me
- Efficient queries

**Tasks**

- [ ] Tables: conversations, messages (role, content, tokens, model, created_at)
- [ ] RLS policies: user apni hi conversations dekhe
- [ ] Pagination query likho (cursor based)
- [ ] Flutter side history load + infinite scroll

**Deliverable:** Chat schema + migrations

### D52 — Rate limiting + usage tracking

⬜ **Pending** · 2h · ref `4.3 / 5.1`

**Objectives**

- Per-user cost control
- Abuse se bachna

**Tasks**

- [ ] usage table: user_id, date, tokens_in, tokens_out, cost
- [ ] Har request ke baad usage record karo
- [ ] Daily/monthly limit enforce karo (limit cross par 429)
- [ ] Flutter me 'limit reached' UI state handle karo

**Deliverable:** Usage tracking + limits

---

## Production, Cost & Reliability

`D53–D56` · roadmap ref `PHASE 5` · 0/4 done

> **Goal:** Jo cheezein client project ko professional banati hain: cost, evals, logging, security.

### D53 — Cost management

⬜ **Pending** · 2h · ref `5.1`

**Objectives**

- Request se pehle cost estimate
- Model routing aur caching

**Tasks**

- [ ] Pre-flight token counting + cost estimator function likho
- [ ] Router banao: simple task -> chhota model, complex -> bara model
- [ ] Prompt caching + response caching lagao
- [ ] Ek week ka projected cost calculate karo apne demo app ke liye

**Deliverable:** cost_utils.py + routing logic

### D54 — Evaluation basics

⬜ **Pending** · 2h · ref `5.2`

**Objectives**

- Prompt/RAG kaam kar raha hai ya nahi, measure karna
- Regression testing

**Tasks**

- [ ] 20 cases ka eval set banao (input + expected behaviour)
- [ ] Automated eval runner likho (LLM-as-judge ya rule based)
- [ ] Prompt change karke score ka farq dekho
- [ ] CI style script: prompt change par evals chalein

**Deliverable:** evals/ folder + runner

### D55 — Hallucination + logging/observability

⬜ **Pending** · 2h · ref `5.2`

**Objectives**

- Hallucination kam karna
- Debugging ke liye proper logs

**Tasks**

- [ ] Grounding + citations + 'nahi pata' instruction se hallucination kam karo
- [ ] Structured logging: prompt, model, tokens, latency, cost, trace_id
- [ ] Ek simple trace viewer banao (ya Langfuse/Helicone try karo)
- [ ] Deliberately hallucination trigger karke detection test karo

**Deliverable:** Logging layer + hallucination notes

### D56 — Security: injection, moderation, PII

⬜ **Pending** · 2h · ref `5.3`

**Objectives**

- Prompt injection se bachna
- Content moderation + PII handling

**Tasks**

- [ ] Apne RAG/agent par injection attacks try karo (document me hidden instructions)
- [ ] Mitigation: untrusted content ko data ke tor par treat karna, tags me wrap karna
- [ ] Moderation API se harmful input/output filter karo
- [ ] PII detection/redaction add karo third-party API bhejne se pehle

**Deliverable:** Security checklist + mitigations

---

## Portfolio & Positioning

`D57–D66` · roadmap ref `PHASE 6` · 0/10 done

> **Goal:** 3 portfolio projects + case studies + Upwork/Fiverr launch. Yahi se paisa aata hai.

### D57 — Project 1: AI Chat App - backend

⬜ **Pending** · 2h · ref `6.1`

**Objectives**

- Scope lock karna
- Backend + DB ready

**Tasks**

- [ ] Feature list finalize karo (scope creep se bacho)
- [ ] Edge function proxy + chat schema deploy karo
- [ ] Auth flow set karo
- [ ] API contract document karo

**Deliverable:** Project 1 backend live

### D58 — Project 1: Flutter streaming chat UI

⬜ **Pending** · 2h · ref `6.1`

**Objectives**

- Phase 4A ke widgets reuse
- Polished UX

**Tasks**

- [ ] Chat screen + streaming + markdown integrate karo
- [ ] Conversation list + new chat + delete
- [ ] Loading/error/empty states polish karo
- [ ] Dark mode + responsive check

**Deliverable:** Project 1 app working

### D59 — Project 1: history, polish, deploy

⬜ **Pending** · 2h · ref `6.1 / 6.2`

**Objectives**

- Production ready banana
- Demo ready banana

**Tasks**

- [ ] History persistence + pagination
- [ ] Usage limits + error handling
- [ ] Build release APK / web deploy
- [ ] Screenshots + 60 second demo video record karo

**Deliverable:** Project 1 shipped + demo

### D60 — Project 2: RAG Doc Q&A - ingestion

⬜ **Pending** · 2h · ref `6.1`

**Objectives**

- PDF upload -> chunks -> embeddings
- Supabase storage + pgvector

**Tasks**

- [ ] File upload endpoint + Supabase storage
- [ ] Background ingestion job (parse -> chunk -> embed -> store)
- [ ] Ingestion status tracking (pending/processing/ready/failed)
- [ ] Bare documents par test karo

**Deliverable:** Ingestion pipeline live

### D61 — Project 2: retrieval + citations API

⬜ **Pending** · 2h · ref `6.1`

**Objectives**

- Hybrid search + cited answers
- Streaming answers

**Tasks**

- [ ] Ask endpoint: hybrid retrieve -> rerank -> answer with citations
- [ ] Answer streaming karo
- [ ] Per-user document isolation verify karo
- [ ] Eval set par quality check karo

**Deliverable:** Q&A API with citations

### D62 — Project 2: Flutter frontend + demo

⬜ **Pending** · 2h · ref `6.1 / 6.2`

**Objectives**

- Upload + ask UI
- Citations dikhana

**Tasks**

- [ ] File picker + upload progress + ingestion status UI
- [ ] Q&A screen with streaming answer
- [ ] Citation chips jo source chunk kholein
- [ ] Screenshots + demo video

**Deliverable:** Project 2 shipped + demo

### D63 — Project 3: AI Agent demo - build

⬜ **Pending** · 2h · ref `6.1`

**Objectives**

- Real task automate karna
- Apne content pipeline se tie karna

**Tasks**

- [ ] Agent scope: topic -> research -> draft -> format output
- [ ] Tools define + agent loop wire karo
- [ ] Guardrails + approval step add karo
- [ ] 3 real topics par chala kar output quality dekho

**Deliverable:** Agent v1 working

### D64 — Project 3: MCP integration + finish

⬜ **Pending** · 2h · ref `6.1 / 6.2`

**Objectives**

- Apna MCP server plug karna
- Presentable banana

**Tasks**

- [ ] D46 wala MCP server agent ke saath integrate karo
- [ ] Simple UI ya CLI polish karo
- [ ] README + architecture diagram
- [ ] Demo video record karo

**Deliverable:** Project 3 shipped + demo

### D65 — Case study write-ups

⬜ **Pending** · 2h · ref `6.2`

**Objectives**

- Technical decisions document karna
- Client-facing language me likhna

**Tasks**

- [ ] Har project ka case study: problem -> approach -> tech decisions -> result
- [ ] Before/after aur metrics (latency, cost per query) daalo
- [ ] Screenshots + video embed karo
- [ ] GitHub repos public + README polish karo

**Deliverable:** 3 case studies published

### D66 — Upwork/Fiverr launch

⬜ **Pending** · 2h · ref `6.3`

**Objectives**

- Profile positioning
- Service packages + pricing

**Tasks**

- [ ] Headline: Flutter Developer | AI Integration Specialist (LLM, RAG, AI Agents)
- [ ] 3 gig packages banao: AI chatbot integration, RAG document search, AI agent automation
- [ ] Pricing set karo ($20-35/hr start, portfolio ke saath scale)
- [ ] Pehli 10 proposals bhejo / gigs publish karo

**Deliverable:** Live profile + gigs

