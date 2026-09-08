# AI Agents & Tool Use

> Agent = LLM + tools + loop + memory. MCP tum already daily use karte ho - yahan usay formalize karna hai.

`D35–D48` · roadmap ref `PHASE 3` · **0/14 days** `░░░░░░░░░░░░░░░░` 0%

Poore safar ka board: [README](../../README.md) · Live dashboard: [dashboard](https://bilalahmad72.github.io/ai-engineering-roadmap/)

---

## Is phase ke din

| Day | Topic | Status | Tasks | Notes |
|---|---|---|---|---|
| [`D35`](#d35) | Agent actually kya hai | ⬜ | 0/4 | — |
| [`D36`](#d36) | Tool schemas deep dive | ⬜ | 0/4 | — |
| [`D37`](#d37) | Raw agent loop (bina framework) | ⬜ | 0/4 | — |
| [`D38`](#d38) | Multi-step aur parallel tool calls | ⬜ | 0/4 | — |
| [`D39`](#d39) | ReAct pattern | ⬜ | 0/4 | — |
| [`D40`](#d40) | Short-term memory + context management | ⬜ | 0/4 | — |
| [`D41`](#d41) | Long-term memory (vector DB) | ⬜ | 0/4 | — |
| [`D42`](#d42) | Planning & task decomposition | ⬜ | 0/4 | — |
| [`D43`](#d43) | Guardrails & validation | ⬜ | 0/4 | — |
| [`D44`](#d44) | Human-in-the-loop approvals | ⬜ | 0/4 | — |
| [`D45`](#d45) | MCP concepts | ⬜ | 0/4 | — |
| [`D46`](#d46) | Custom MCP server banao | ⬜ | 0/4 | — |
| [`D47`](#d47) | MCP server ko client se jorna | ⬜ | 0/4 | — |
| [`D48`](#d48) | Framework chuno + Phase 3 mini-project | ⬜ | 0/4 | — |

---

## D35

### Agent actually kya hai

⬜ **Pending** · 2h

**Objectives**

- Agent vs chatbot vs workflow ka farq
- Loop, tools, memory, termination

**Tasks**

- [ ] Agent ki definition apne lafzon me likho: LLM + tools + loop + memory
- [ ] Claude Code khud kaise agent hai, uska breakdown likho
- [ ] 3 real use cases likho jo tum Fiverr par bech sakte ho
- [ ] Agent loop ka pseudocode likho (stop condition ke saath)

**Deliverable:** Agent concepts note

---

## D36

### Tool schemas deep dive

⬜ **Pending** · 2h

**Objectives**

- Accha tool schema kaise likhein
- Description hi asli prompt hai

**Tasks**

- [ ] 5 tools ke JSON schemas likho (search, read_file, send_email, db_query, calculator)
- [ ] Required vs optional params, enums, nested objects use karo
- [ ] Buri vs achi tool description ka A/B test karo
- [ ] Dekho model galat schema par kaise fail hota hai

**Deliverable:** tools/ schema library

---

## D37

### Raw agent loop (bina framework)

⬜ **Pending** · 2h

**Objectives**

- Poora agent loop khud likhna
- Fundamentals framework se pehle

**Tasks**

- [ ] while loop: call model -> agar tool_use hai to chalao -> result wapas -> repeat
- [ ] Max iterations limit lagao (infinite loop se bachne ke liye)
- [ ] Conversation history properly maintain karo
- [ ] Har step log karo taake debugging aasan ho

**Deliverable:** agent.py (raw loop, ~100 lines)

---

## D38

### Multi-step aur parallel tool calls

⬜ **Pending** · 2h

**Objectives**

- Ek turn me multiple tools
- Sequential vs parallel execution

**Tasks**

- [ ] Aisa task do jisme 3 tools chahiye (multi-step chain)
- [ ] Parallel tool calls handle karo (asyncio.gather)
- [ ] Tool failure handle karo (error result wapas model ko do)
- [ ] Tool call sequence visualize/log karo

**Deliverable:** Multi-tool agent

---

## D39

### ReAct pattern

⬜ **Pending** · 2h

**Objectives**

- Reason + Act loop
- Thinking traces ka faida

**Tasks**

- [ ] ReAct prompt likho: Thought -> Action -> Observation
- [ ] Apne raw agent ko ReAct style me convert karo
- [ ] Extended thinking / reasoning models se compare karo
- [ ] Note: kab ReAct zaroori hai aur kab overkill

**Deliverable:** react_agent.py

---

## D40

### Short-term memory + context management

⬜ **Pending** · 2h

**Objectives**

- Conversation history ko context window me fit rakhna
- Summarization aur trimming

**Tasks**

- [ ] Sliding window trimming implement karo
- [ ] Purani history ka summary bana kar replace karo
- [ ] Token budget tracker banao
- [ ] Long conversation par test karo, cost measure karo

**Deliverable:** memory/short_term.py

---

## D41

### Long-term memory (vector DB)

⬜ **Pending** · 2h

**Objectives**

- Persistent memory RAG ke through
- Kya yaad rakhna hai aur kya nahi

**Tasks**

- [ ] Phase 2 wala pgvector reuse karke memory store banao
- [ ] Agent ko save_memory aur recall_memory tools do
- [ ] Facts extract karke store karo (poori chat nahi)
- [ ] Nayi session me recall test karo

**Deliverable:** memory/long_term.py

---

## D42

### Planning & task decomposition

⬜ **Pending** · 2h

**Objectives**

- Bara goal chhote steps me todna
- Plan-then-execute pattern

**Tasks**

- [ ] Planner prompt banao jo task ko steps me tode
- [ ] Steps ko execute karke progress track karo
- [ ] Re-planning add karo jab koi step fail ho
- [ ] Single-agent vs orchestrator+subagents ka concept note karo

**Deliverable:** planner_agent.py

---

## D43

### Guardrails & validation

⬜ **Pending** · 2h

**Objectives**

- Agent ko galat kaam se rokna
- Input/output validation layers

**Tasks**

- [ ] Tool-level permission checks lagao (kaunsa tool kis condition me chale)
- [ ] Output validation: schema + business rules
- [ ] Destructive actions ke liye allowlist/denylist
- [ ] Deliberately galat instruction de kar guardrail test karo

**Deliverable:** guardrails.py

---

## D44

### Human-in-the-loop approvals

⬜ **Pending** · 2h

**Objectives**

- Approval step se pehle rukna
- Resumable agent state

**Tasks**

- [ ] Risky tools ko 'requires_approval' mark karo
- [ ] Agent ko pause karke approval maango, phir resume karo
- [ ] Agent state serialize/deserialize karo (DB me save)
- [ ] Claude Code ka permission prompt pattern study karke note karo

**Deliverable:** Approval-gated agent

---

## D45

### MCP concepts

⬜ **Pending** · 2h

**Objectives**

- MCP kyun exist karta hai
- Server vs client, transports

**Tasks**

- [ ] MCP spec ka overview parho (tools, resources, prompts)
- [ ] stdio vs HTTP/SSE transport ka farq note karo
- [ ] Apne installed MCP servers ki list banao aur unke tools inspect karo
- [ ] MCP vs plain function calling: kab kya use karein

**Deliverable:** MCP concepts note

---

## D46

### Custom MCP server banao

⬜ **Pending** · 2h

**Objectives**

- Apna MCP server likhna
- Tools expose karna

**Tasks**

- [ ] MCP Python (ya TypeScript) SDK install karo
- [ ] 3 tools wala server banao (koi real kaam - e.g. is roadmap repo ka progress read/update)
- [ ] Local me test karo MCP inspector se
- [ ] Error handling + input validation add karo

**Deliverable:** Custom MCP server

---

## D47

### MCP server ko client se jorna

⬜ **Pending** · 2h

**Objectives**

- Real client me integrate karna
- Debugging

**Tasks**

- [ ] Apna server Claude Code / Claude Desktop me register karo
- [ ] Asli tasks par tools chala kar test karo
- [ ] Logs dekh kar issues debug karo
- [ ] Server ka README + usage docs likho

**Deliverable:** Working MCP integration + docs

---

## D48

### Framework chuno + Phase 3 mini-project

⬜ **Pending** · 2h

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

<sub>Generated by `scripts/track.py` — hath se edit mat karo.</sub>
