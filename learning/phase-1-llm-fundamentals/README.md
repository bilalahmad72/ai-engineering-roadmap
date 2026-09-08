# LLM Fundamentals + API Integration

> LLM APIs ko confidently call karna: streaming, structured output, tools, cost control.

`D05–D14` · roadmap ref `PHASE 1` · **0/10 days** `░░░░░░░░░░░░░░░░` 0%

Poore safar ka board: [README](../../README.md) · Live dashboard: [dashboard](https://bilalahmad72.github.io/ai-engineering-roadmap/)

---

## Is phase ke din

| Day | Topic | Status | Tasks | Notes |
|---|---|---|---|---|
| [`D05`](#d05) | Tokens, tokenization aur context window | ⬜ | 0/4 | — |
| [`D06`](#d06) | Sampling params + message roles | ⬜ | 0/4 | — |
| [`D07`](#d07) | Model landscape + multimodal | ⬜ | 0/4 | — |
| [`D08`](#d08) | OpenAI API hands-on | ⬜ | 0/4 | — |
| [`D09`](#d09) | Anthropic Messages API hands-on | ⬜ | 0/4 | — |
| [`D10`](#d10) | Streaming responses (SSE) code me | ⬜ | 0/4 | — |
| [`D11`](#d11) | Structured outputs / JSON mode | ⬜ | 0/4 | — |
| [`D12`](#d12) | Function calling / tool use - pehla taste | ⬜ | 0/4 | — |
| [`D13`](#d13) | Prompt engineering core | ⬜ | 0/4 | — |
| [`D14`](#d14) | Prompt injection, versioning + Phase 1 mini-project | ⬜ | 0/4 | — |

---

## D05

### Tokens, tokenization aur context window

⬜ **Pending** · 2h

**Objectives**

- Token kya hai aur cost/limits tokens me kyun measure hote hain
- Context window ka app design par asar

**Tasks**

- [ ] tiktoken (ya Anthropic count_tokens) se apne sample texts ke tokens ginno
- [ ] Urdu/Roman Urdu vs English text ka token count compare karo
- [ ] 3 models ke context windows aur per-1M pricing ka table banao
- [ ] Note karo: lambi chat history ka cost par kya asar padta hai

**Deliverable:** Token/cost comparison table

---

## D06

### Sampling params + message roles

⬜ **Pending** · 2h

**Objectives**

- temperature, top_p, max_tokens, stop sequences ka practical asar
- system / user / assistant roles ka sahi istemal

**Tasks**

- [ ] Ek hi prompt ko temperature 0 / 0.7 / 1.2 par chalao, outputs compare karo
- [ ] max_tokens chhota rakh kar dekho response kaise cut hota hai (stop_reason)
- [ ] System prompt badal kar tone/persona change karke dekho
- [ ] Findings notes me likho

**Deliverable:** params_experiment.py + observations

---

## D07

### Model landscape + multimodal

⬜ **Pending** · 2h

**Objectives**

- GPT / Claude / Gemini / Llama / Mistral ka comparison
- Kaunsa model kis kaam ke liye (cheap vs smart)

**Tasks**

- [ ] Har family ka latest model + pricing + context window note karo
- [ ] Multimodal (text+image+audio) support ka comparison banao
- [ ] Model selection cheatsheet: task -> recommended model
- [ ] Open-source vs API tradeoffs 5 points me likho

**Deliverable:** Model selection cheatsheet

---

## D08

### OpenAI API hands-on

⬜ **Pending** · 2h

**Objectives**

- Chat completions end-to-end
- Errors, retries, timeouts handle karna

**Tasks**

- [ ] openai SDK install + first chat completion
- [ ] Multi-turn conversation loop banao (history maintain karke)
- [ ] Rate limit / invalid key / timeout errors deliberately trigger karke handle karo
- [ ] Usage object se token count log karo

**Deliverable:** openai_chat.py (multi-turn CLI chat)

---

## D09

### Anthropic Messages API hands-on

⬜ **Pending** · 2h

**Objectives**

- Claude Messages API ka shape
- System prompt, stop_reason, prompt caching

**Tasks**

- [ ] anthropic SDK se first message call
- [ ] System prompt alag param me dena (OpenAI se farq note karo)
- [ ] Prompt caching try karo aur cost difference dekho
- [ ] OpenAI vs Anthropic request/response diff table banao

**Deliverable:** claude_chat.py + API diff table

---

## D10

### Streaming responses (SSE) code me

⬜ **Pending** · 2h

**Objectives**

- Dono providers se streaming
- Chunk parsing aur partial updates

**Tasks**

- [ ] OpenAI stream=True se token-by-token print karo
- [ ] Anthropic streaming events (content_block_delta) handle karo
- [ ] Streaming ke doraan error/disconnect handle karo
- [ ] FastAPI me /chat/stream proxy endpoint banao jo aage stream kare

**Deliverable:** Streaming proxy endpoint (Phase 4B ki base)

---

## D11

### Structured outputs / JSON mode

⬜ **Pending** · 2h

**Objectives**

- Model se reliable JSON nikalna
- Pydantic se validate karna

**Tasks**

- [ ] Pydantic model define karo (e.g. Invoice, Recipe)
- [ ] OpenAI structured outputs / response_format se JSON lo
- [ ] Claude me tool-schema trick se JSON lo
- [ ] Invalid JSON par retry/repair logic likho

**Deliverable:** structured_extract.py

---

## D12

### Function calling / tool use - pehla taste

⬜ **Pending** · 2h

**Objectives**

- Tool definition ka structure
- Tool result wapas model ko dena

**Tasks**

- [ ] Ek get_weather (mock) tool define karo JSON schema ke saath
- [ ] Model ka tool_use response parse karke tool chalao
- [ ] Result wapas bhej kar final answer lo
- [ ] Yehi cheez dono providers me karke syntax farq note karo

**Deliverable:** first_tool_call.py

---

## D13

### Prompt engineering core

⬜ **Pending** · 2h

**Objectives**

- Zero-shot, few-shot, CoT, role prompting
- Prompt templates + variables

**Tasks**

- [ ] Ek classification task lo aur zero-shot vs few-shot accuracy compare karo
- [ ] Chain-of-thought add karke reasoning task improve karo
- [ ] Prompt template class banao (variables inject karne ke liye)
- [ ] Output format control: XML tags vs JSON vs markdown

**Deliverable:** prompts/ folder with templates

---

## D14

### Prompt injection, versioning + Phase 1 mini-project

⬜ **Pending** · 2h

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

<sub>Generated by `scripts/track.py` — hath se edit mat karo.</sub>
