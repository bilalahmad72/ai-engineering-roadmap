# Python Core (scratch se)

> Python zero se poori tarah — sirf itna jitna is safar me chahiye, lekin woh mazbooti se. Maqsad: kisi bhi maujooda Python file ko khol kar samajh lena.

`PY01–PY12` · roadmap ref `PHASE 0.1 — expanded` · **1/12 days** `█░░░░░░░░░░░░░░░` 8%

Poore safar ka board: [README](../../README.md) · Live dashboard: [dashboard](https://bilalahmad72.github.io/ai-engineering-roadmap/)

---

## Is phase ke din

| Day | Topic | Status | Tasks | Notes |
|---|---|---|---|---|
| [`PY01`](#py01) | Syntax, variables, types aur strings | ✅ | 4/4 | [📝](../../notes/daily/PY01-syntax-types.md) [📝](../../notes/ISSUES.md) |
| [`PY02`](#py02) | Collections: list, tuple, dict, set | 🟡 | 1/4 | [📝](../../notes/daily/PY02-collections.md) |
| [`PY03`](#py03) | Control flow: if, loops, comprehensions | ⬜ | 0/4 | — |
| [`PY04`](#py04) | Functions poori tarah | ⬜ | 0/4 | — |
| [`PY05`](#py05) | Modules, imports aur project structure | ⬜ | 0/4 | — |
| [`PY06`](#py06) | Files, paths, JSON aur environment | ⬜ | 0/4 | — |
| [`PY07`](#py07) | Errors aur exceptions | ⬜ | 0/4 | — |
| [`PY08`](#py08) | OOP: classes, dataclass, properties | ⬜ | 0/4 | — |
| [`PY09`](#py09) | Iterators aur generators (streaming ki bunyad) | ⬜ | 0/4 | — |
| [`PY10`](#py10) | Async Python (asyncio) | ⬜ | 0/4 | — |
| [`PY11`](#py11) | Typing, stdlib aur Pythonic idioms | ⬜ | 0/4 | — |
| [`PY12`](#py12) | Doosron ka Python code parhna (asli imtihan) | ⬜ | 0/4 | — |

---

## PY01

### Syntax, variables, types aur strings

✅ **Done** · 2h · started 2026-09-06 · completed 2026-09-08

**Objectives**

- Python ka syntax model (indentation, no semicolons, no braces)
- Types, type conversion aur f-strings

**Tasks**

- [x] Topic 1: variables, 5 types, type().__name__, format specs (:,.2f / :.6f / :.1%)
- [x] Topic 2: int/float/str/bool conversion, truthiness rule, isdigit vs float(), EAFP
- [x] Topic 3: string methods — strip/split/join/slicing, .env parsing, API key masking, validation
- [x] Topic 4: f-string deep dive — alignment tables, padding, {var=} debug shortcut

**Deliverable:** 4 practice files + PY01 note (concept + apna code + output)

**Practice code**

- [`recall.py`](../../learning/phase-0-python-core/PY01-syntax-types/recall.py)
- [`t1_formatting.py`](../../learning/phase-0-python-core/PY01-syntax-types/t1_formatting.py)
- [`t1_variables.py`](../../learning/phase-0-python-core/PY01-syntax-types/t1_variables.py)
- [`t2_conversion.py`](../../learning/phase-0-python-core/PY01-syntax-types/t2_conversion.py)
- [`t3_strings.py`](../../learning/phase-0-python-core/PY01-syntax-types/t3_strings.py)
- [`t4_fstrings.py`](../../learning/phase-0-python-core/PY01-syntax-types/t4_fstrings.py)

**Notes**

- [PY01-syntax-types.md](../../notes/daily/PY01-syntax-types.md)
- [ISSUES.md](../../notes/ISSUES.md)

<details><summary>Activity log</summary>

- `2026-09-06 12:33 UTC` — Started
- `2026-09-06 12:33 UTC` — Practice setup ready: 8 exercises, 29 assertions
- `2026-09-06 12:49 UTC` — Method: one-question-at-a-time tutoring. Topic -> note -> 5-6 use cases -> next topic
- `2026-09-06 13:08 UTC` — Note added: notes/daily/PY01-syntax-types.md
- `2026-09-06 13:08 UTC` — Checked task 1
- `2026-09-06 13:08 UTC` — Topic 1 (variables/types) done — format specs practiced
- `2026-09-06 13:11 UTC` — Note added: notes/ISSUES.md
- `2026-09-06 13:11 UTC` — ISS-001: wrong path when running file manually — fixed, use Run button
- `2026-09-06 13:36 UTC` — Topic 1 complete: variables, types, format specs (:, / :.6f / :.1%). Silent wrong-variable bug caught and documented
- `2026-09-07 01:58 UTC` — Topic 2 complete: conversion, truthiness rule, isdigit vs float(), EAFP
- `2026-09-08 00:59 UTC` — Checked task 2
- `2026-09-08 00:59 UTC` — Topic 3 complete: string methods, .env parsing, key masking, validation. Bug: bool compared as int (True > 20)
- `2026-09-08 01:03 UTC` — Note: bool-is-int concept documented (why True > 20 did not crash)
- `2026-09-08 01:33 UTC` — Checked task 3
- `2026-09-08 01:33 UTC` — Checked task 4
- `2026-09-08 01:35 UTC` — Completed
- `2026-09-08 01:35 UTC` — PY01 complete — 4 topics, 5 practice files, notes me concept + practice dono
- `2026-09-08 01:49 UTC` — Recall check: 9/12. Answers strong, rules not yet verbal. Fix: har topic ke baad asool apne lafzon me likhwana

</details>

---

## PY02

### Collections: list, tuple, dict, set

🟡 **Running** · 2h · started 2026-09-08

**Objectives**

- Chaaron collections aur unka sahi istemal
- Indexing, slicing aur mutation

**Tasks**

- [x] list: append/extend/insert/remove/pop/sort/reverse + slicing [a:b:c]
- [ ] dict: get/keys/values/items/update/pop + nested access
- [ ] set: add/remove/union/intersection + duplicates hatana
- [ ] tuple: immutability, unpacking, swap; PRACTICE: exercises green karo

**Deliverable:** PY02 practice — sab tests green

**Practice code**

- [`t1_list.py`](../../learning/phase-0-python-core/PY02-collections/t1_list.py)

**Notes**

- [PY02-collections.md](../../notes/daily/PY02-collections.md)

<details><summary>Activity log</summary>

- `2026-09-08 01:49 UTC` — Started
- `2026-09-09 01:32 UTC` — Note added: notes/daily/PY02-collections.md
- `2026-09-09 01:32 UTC` — Checked task 1
- `2026-09-09 01:32 UTC` — Topic 1 (list) complete: append/extend, slicing, sort-returns-None, = is aliasing not copy

</details>

---

## PY03

### Control flow: if, loops, comprehensions

⬜ **Pending** · 2h

**Objectives**

- Conditions aur loops Python ke tareeqe se
- Comprehensions — Python ka signature idiom

**Tasks**

- [ ] if/elif/else, truthy-falsy values, ternary, match statement
- [ ] for + range/enumerate/zip, while, break/continue/else
- [ ] List/dict/set comprehensions, nested aur conditional
- [ ] PRACTICE: exercises green karo

**Deliverable:** PY03 practice — sab tests green

---

## PY04

### Functions poori tarah

⬜ **Pending** · 2h

**Objectives**

- Parameters ki saari qismein
- Scope, closures aur lambda

**Tasks**

- [ ] positional, default, keyword-only, *args, **kwargs
- [ ] Multiple return values (tuple unpacking), type hints
- [ ] Scope: local/global, aur mutable default argument ka mashhoor bug
- [ ] lambda, map/filter vs comprehension; PRACTICE: exercises green karo

**Deliverable:** PY04 practice — sab tests green

---

## PY05

### Modules, imports aur project structure

⬜ **Pending** · 2h

**Objectives**

- Code ko multiple files me todna
- import system samajhna

**Tasks**

- [ ] import x / from x import y / as alias, aur circular import ka masla
- [ ] __name__ == '__main__' ka asal matlab
- [ ] Apna module + package (__init__.py) banao aur use karo
- [ ] pip, requirements.txt, aur standard project layout; PRACTICE: exercises

**Deliverable:** Multi-file package jo chalta ho

---

## PY06

### Files, paths, JSON aur environment

⬜ **Pending** · 2h

**Objectives**

- File I/O safely
- JSON aur .env — roz ka kaam

**Tasks**

- [ ] open() + with statement (context manager) + encoding='utf-8'
- [ ] pathlib: Path, /, exists, mkdir, glob, read_text
- [ ] json loads/dumps/load/dump + ensure_ascii + default=
- [ ] os.getenv + python-dotenv; PRACTICE: D01 ke EX5/EX6 bhi complete karo

**Deliverable:** PY06 practice + D01 exercises green

---

## PY07

### Errors aur exceptions

⬜ **Pending** · 2h

**Objectives**

- Traceback parhna
- Errors ko sahi tarah handle karna

**Tasks**

- [ ] try/except/else/finally, multiple except, exception hierarchy
- [ ] raise, custom exception class, exception chaining (raise ... from)
- [ ] Traceback ko neeche se upar parhna — asli line dhoondna
- [ ] Anti-pattern: bare except aur silent pass; PRACTICE: exercises

**Deliverable:** PY07 practice — sab tests green

---

## PY08

### OOP: classes, dataclass, properties

⬜ **Pending** · 2h

**Objectives**

- Class banana aur use karna
- dataclass aur Pydantic ka farq

**Tasks**

- [ ] __init__, self, instance vs class attributes, methods
- [ ] __str__/__repr__/__eq__, @property, @staticmethod, @classmethod
- [ ] Inheritance + super(), aur composition kab behtar hai
- [ ] @dataclass; Pydantic ka taaruf (validation ke liye); PRACTICE: exercises

**Deliverable:** PY08 practice — sab tests green

---

## PY09

### Iterators aur generators (streaming ki bunyad)

⬜ **Pending** · 2h

**Objectives**

- yield kya karta hai
- Lazy evaluation — LLM streaming isi par chalti hai

**Tasks**

- [ ] Iterable vs iterator, for loop andar se kaise chalta hai
- [ ] yield se generator function, generator expression ( ) vs [ ]
- [ ] Memory ka farq: badi file line-by-line vs poori list me
- [ ] Generator se ek fake token stream banao; PRACTICE: exercises

**Deliverable:** Generator-based fake LLM stream

---

## PY10

### Async Python (asyncio)

⬜ **Pending** · 2h

**Objectives**

- async/await Python me — Dart se farq
- Concurrent calls

**Tasks**

- [ ] async def, await, coroutine vs Future, asyncio.run
- [ ] asyncio.gather (Dart Future.wait) se parallel calls
- [ ] async for, async with, aur async generator (streaming ke liye)
- [ ] Blocking code async ko kaise tabah karta hai; PRACTICE: exercises

**Deliverable:** PY10 practice — concurrent async script

---

## PY11

### Typing, stdlib aur Pythonic idioms

⬜ **Pending** · 2h

**Objectives**

- Type hints theek se
- Woh stdlib jo roz chahiye

**Tasks**

- [ ] typing: list[str], dict[str, Any], Optional, Union (|), Literal, TypedDict
- [ ] datetime + timezone, uuid, logging (print ki jagah)
- [ ] enumerate/zip/any/all/sorted(key=)/max(key=) patterns
- [ ] PEP 8 + Ruff se apna purana code saaf karo; PRACTICE: exercises

**Deliverable:** PY11 practice + Ruff-clean code

---

## PY12

### Doosron ka Python code parhna (asli imtihan)

⬜ **Pending** · 2h

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

<sub>Generated by `scripts/track.py` — hath se edit mat karo.</sub>
