# RAG (Retrieval-Augmented Generation)

> Private data par LLM chalana - chunking se le kar pgvector, hybrid search aur citations tak. Tumhara Postgres/Supabase background yahan shortcut hai.

`D21–D34` · roadmap ref `PHASE 2` · **0/14 days** `░░░░░░░░░░░░░░░░` 0%

Poore safar ka board: [README](../../README.md) · Live dashboard: [dashboard](https://bilalahmad72.github.io/ai-engineering-roadmap/)

---

## Is phase ke din

| Day | Topic | Status | Tasks | Notes |
|---|---|---|---|---|
| [`D21`](#d21) | RAG kya hai aur kyun (architecture overview) | ⬜ | 0/4 | — |
| [`D22`](#d22) | Embeddings conceptually | ⬜ | 0/4 | — |
| [`D23`](#d23) | Embeddings generate + similarity hand se | ⬜ | 0/4 | — |
| [`D24`](#d24) | Chunking strategies | ⬜ | 0/4 | — |
| [`D25`](#d25) | Document loading & parsing | ⬜ | 0/4 | — |
| [`D26`](#d26) | pgvector setup (Supabase/Postgres) | ⬜ | 0/4 | — |
| [`D27`](#d27) | Embeddings store + similarity query | ⬜ | 0/4 | — |
| [`D28`](#d28) | Indexing: HNSW vs IVFFlat | ⬜ | 0/4 | — |
| [`D29`](#d29) | Full retrieval pipeline | ⬜ | 0/4 | — |
| [`D30`](#d30) | Prompt assembly + citations | ⬜ | 0/4 | — |
| [`D31`](#d31) | Hybrid search (keyword + vector) | ⬜ | 0/4 | — |
| [`D32`](#d32) | Re-ranking basics | ⬜ | 0/4 | — |
| [`D33`](#d33) | Metadata filtering + multi-tenant RAG | ⬜ | 0/4 | — |
| [`D34`](#d34) | RAG evaluation + Phase 2 mini-project | ⬜ | 0/4 | — |

---

## D21

### RAG kya hai aur kyun (architecture overview)

⬜ **Pending** · 2h

**Objectives**

- RAG ki zaroorat samajhna (LLM tumhara private data nahi jaanta)
- Naive RAG pipeline ka end-to-end naksha

**Tasks**

- [ ] Pipeline diagram banao: ingest -> chunk -> embed -> store -> retrieve -> prompt -> generate
- [ ] RAG vs fine-tuning vs long-context ka comparison likho
- [ ] Kaunse client problems RAG se hal hote hain, 5 examples likho (Fiverr gig ideas)
- [ ] Ek chhoti hardcoded 'fake RAG' banao: text ko prompt me daal kar sawal pucho

**Deliverable:** RAG architecture note + fake-RAG script

---

## D22

### Embeddings conceptually

⬜ **Pending** · 2h

**Objectives**

- Embedding kya hai (text ka meaning vector)
- Embedding models ka comparison

**Tasks**

- [ ] Embedding vs token ka farq clear karo notes me
- [ ] OpenAI text-embedding-3-small/large, Gemini, sentence-transformers compare karo
- [ ] Dimensions, cost, aur quality ka tradeoff note karo
- [ ] Decide karo default embedding model kaunsa use karoge aur kyun

**Deliverable:** Embedding model decision note

---

## D23

### Embeddings generate + similarity hand se

⬜ **Pending** · 2h

**Objectives**

- Actual embeddings banana
- Cosine similarity khud calculate karna

**Tasks**

- [ ] 10 sentences ke embeddings generate karo
- [ ] numpy se cosine similarity matrix banao
- [ ] Dekho kaunse sentences semantically qareeb aaye
- [ ] Ek 'search' function likho: query -> top 3 similar sentences

**Deliverable:** similarity_demo.py

---

## D24

### Chunking strategies

⬜ **Pending** · 2h

**Objectives**

- Fixed, recursive aur semantic chunking
- Chunk size + overlap ka retrieval quality par asar

**Tasks**

- [ ] Ek lambi document lo aur 3 tareeqon se chunk karo
- [ ] Chunk size 256 vs 512 vs 1024 par retrieval quality compare karo
- [ ] Overlap add karke dekho context kaise behtar hota hai
- [ ] Har chunk ke saath metadata attach karo (source, page, section)

**Deliverable:** chunking.py + comparison notes

---

## D25

### Document loading & parsing

⬜ **Pending** · 2h

**Objectives**

- PDF/docx/html/txt se clean text nikalna
- Parsing ke real-world masail

**Tasks**

- [ ] pypdf ya pdfplumber se PDF text extract karo
- [ ] python-docx aur BeautifulSoup se docx/html handle karo
- [ ] Tables, headers/footers, aur scanned PDFs ke masail note karo
- [ ] Ek unified loader function banao jo file type detect kare

**Deliverable:** loaders.py

---

## D26

### pgvector setup (Supabase/Postgres)

⬜ **Pending** · 2h

**Objectives**

- pgvector extension enable karna
- Documents + chunks ka schema design

**Tasks**

- [ ] Supabase project me vector extension enable karo
- [ ] Tables banao: documents, chunks (embedding vector(1536), metadata jsonb)
- [ ] RLS policies socho (user apna hi data dekhe)
- [ ] Foreign keys + cascade delete set karo

**Deliverable:** SQL migration file

---

## D27

### Embeddings store + similarity query

⬜ **Pending** · 2h

**Objectives**

- pgvector me insert aur search
- SQL me distance operators

**Tasks**

- [ ] Chunks + embeddings ko batch insert karo
- [ ] <=> (cosine) operator se nearest neighbours query likho
- [ ] Ek Postgres function match_chunks(query_embedding, k) banao
- [ ] Python se function call karke results verify karo

**Deliverable:** Working vector search query

---

## D28

### Indexing: HNSW vs IVFFlat

⬜ **Pending** · 2h

**Objectives**

- Index ke bagair search kyun slow hai
- Do index types ka tradeoff

**Tasks**

- [ ] Bina index ke 10k rows par query time measure karo
- [ ] IVFFlat index banao aur time dobara measure karo
- [ ] HNSW index banao aur compare karo (build time vs query time vs recall)
- [ ] Decision note: kis situation me kaunsa index

**Deliverable:** Index benchmark note

---

## D29

### Full retrieval pipeline

⬜ **Pending** · 2h

**Objectives**

- query -> embed -> search -> context assemble
- Top-k tuning

**Tasks**

- [ ] End-to-end retrieve() function likho
- [ ] Top-k=3 vs 5 vs 10 ka answer quality par asar dekho
- [ ] Context length budget manage karo (token limit ke andar)
- [ ] Duplicate/overlapping chunks filter karo

**Deliverable:** retriever.py

---

## D30

### Prompt assembly + citations

⬜ **Pending** · 2h

**Objectives**

- Retrieved context ko prompt me sahi tarah daalna
- Source attribution dena

**Tasks**

- [ ] RAG prompt template banao (context XML tags me)
- [ ] Model ko chunk IDs cite karne par majboor karo
- [ ] Citations ko source metadata se resolve karke show karo
- [ ] Jab context me jawab na ho to 'nahi pata' kehne wala instruction test karo

**Deliverable:** rag_answer.py with citations

---

## D31

### Hybrid search (keyword + vector)

⬜ **Pending** · 2h

**Objectives**

- Pure vector search kahan fail hota hai
- Full-text + vector ko combine karna

**Tasks**

- [ ] Postgres tsvector full-text search set karo
- [ ] Aisi queries dhoondo jahan keyword search jeete (names, IDs, exact terms)
- [ ] Reciprocal Rank Fusion (RRF) se dono results merge karo
- [ ] Pure vector vs hybrid ka side-by-side comparison

**Deliverable:** hybrid_search.py

---

## D32

### Re-ranking basics

⬜ **Pending** · 2h

**Objectives**

- Re-ranker kya karta hai
- Retrieve-then-rerank pattern

**Tasks**

- [ ] Top-20 retrieve karke LLM se top-5 rerank karao
- [ ] Cohere rerank / cross-encoder option explore karo
- [ ] Latency vs quality tradeoff measure karo
- [ ] Decide karo kab reranking worth hai

**Deliverable:** reranker.py

---

## D33

### Metadata filtering + multi-tenant RAG

⬜ **Pending** · 2h

**Objectives**

- Per-user document isolation
- Filtered vector search

**Tasks**

- [ ] user_id se filtered vector search karo (WHERE + vector order)
- [ ] Date range / document type filters add karo
- [ ] RLS policies test karo (dusre user ka data leak na ho)
- [ ] Multi-tenant schema ke pitfalls note karo

**Deliverable:** Filtered + secure retrieval

---

## D34

### RAG evaluation + Phase 2 mini-project

⬜ **Pending** · 2h

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

<sub>Generated by `scripts/track.py` — hath se edit mat karo.</sub>
