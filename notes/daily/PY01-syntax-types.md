---
day: PY01
title: Syntax, variables, types aur strings
phase: Python Core
date: 2026-09-06
tags: [python, syntax, types, f-strings, formatting]
status: draft
---

# PY01 — Syntax, variables, types aur strings

> 🔄 **In progress** — topic-by-topic bharta ja raha hai.

## Topics

- [x] **Topic 1 — Variables aur types**
- [ ] Topic 2 — Type conversion
- [ ] Topic 3 — String methods
- [ ] Topic 4 — f-strings aur formatting
- [ ] Topic 5 — Truthiness aur membership

---

## Topic 1 — Variables aur types

### Syntax ka model

| Dart | Python |
|---|---|
| `{ }` se block | **indentation** (4 spaces) se block |
| line ke aakhir `;` | kuch nahi |
| `if (cond) {` | `if cond:` — colon laazmi, brackets nahi |
| `final String name = 'x';` | `name = "x"` — koi keyword, koi type nahi |
| `camelCase` | `snake_case` (constants CAPITAL) |

### Paanch bunyadi types

```python
age = 28            # int    (Python me size ki koi limit nahi)
price = 3.14        # float
name = "Bilal"      # str    ' aur " barabar hain
is_dev = True       # bool   <- CAPITAL True/False
middle = None       # None   <- Dart ka null, CAPITAL N
```

Dart wale yahan phanste hain: `true`/`false`/`null` chhote harf me likh dena.

### Type check karna

```python
type(age)                # <class 'int'>   poora type object
type(age).__name__       # 'int'           sirf naam
isinstance(age, int)     # True            check ke liye YEHI behtar hai
```

`type(x)` ko seedha print karo to `<class 'str'>` aata hai jo bhadda hai.
`.__name__` se sirf saaf naam milta hai.

> `__name__` wala pattern Python me bar bar milta hai — PY05 me
> `if __name__ == "__main__":` bhi isi khandan se hai.

### Float banane ka dhyaan

```python
hourly_rate = 20      # int
hourly_rate = 20.0    # float   <- .0 lagane se float banta hai
```

Lekin calculation me `.0` lagana zaroori nahi — `float * int` ka jawab khud hi
float hota hai:

```python
20.0 * 120     # 2400.0  (float)
```

### Format specs — f-string ka asli faida

`{variable}` ke baad **colon** lagao aur format ka rule likho:

```python
value = 2400.0

f"{value}"          # "2400.0"      raw
f"{value:.2f}"      # "2400.00"     2 decimal places
f"{value:,.2f}"     # "2,400.00"    comma + 2 decimals
f"{value:.6f}"      # "2400.000000" 6 decimals
f"{0.856:.1%}"      # "85.6%"       percentage
f"{name!r}"         # "'Bilal'"     quotes ke saath (debugging)
```

**Ye aage kyun kaam aayega:** LLM ki cost bohot chhote numbers me aati hai —
`0.0000225`. Bina `:.6f` ke Python usay `2.25e-05` print karta hai, jo kisi
client ko dikhane laayak nahi.

### Numbers me underscore

```python
1_000_000 == 1000000     # True — sirf parhne ke liye
```

Bare numbers (token limits, rates) hamesha `1_000_000` likho — ginne me aasan.

### Operator order

```python
tokens / 1_000_000 * rate     # dono barabar
tokens * rate / 1_000_000     # ye thoda behtar
```

`*` aur `/` ki priority barabar hai, bayein se dayein chalte hain. Doosra
version behtar hai: bara number pehle multiply hota hai, floating-point ki
chhoti ghaltiyon ka imkaan kam.

## Code

- [`t1_variables.py`](../../learning/phase-0-python-core/PY01-syntax-types/t1_variables.py)
  — variables, types, `.__name__`
- [`t1_formatting.py`](../../learning/phase-0-python-core/PY01-syntax-types/t1_formatting.py)
  — format specs par practice

Output:

```
full_name = Bilal Ahmad (type: str)
experience_years = 5 (type: int)
hourly_rate = 20.0 (type: float)
is_learning_ai = True (type: bool)
20.00/hour x 120 hours = 2,400.00 per month

Tokens: 15,432
Cost: $0.231480
Success: 85.7%
15,432 tokens = $0.231480 (85.7% success)
```

## Gotchas

| # | Galti | Sahi | Kyun |
|---|---|---|---|
| 1 | `type(x)` print karna | `type(x).__name__` | pehla `<class 'str'>` deta hai |
| 2 | `f"{value}"` cost ke liye | `f"{value:.6f}"` | chhote numbers `2.25e-05` ban jate hain |
| 3 | hardcoded number (`20 * 120`) | variable se calculate | value badle to sab jagah badalna pare |
| 4 | spec ka naam badal dena (`name` vs `full_name`) | wahi naam use karo | API fields exact match maangte hain |
| 5 | **ghalat variable uth jana** | calculation ke baad ek dafa haath se verify karo | dekho neeche |

### Sabse khatarnak bug: ghalat variable

```python
# GALAT — cost_per_million ki jagah success_rate
cost = input_tokens / 1_000_000 * success_rate   # $0.013221

# SAHI
cost = input_tokens * cost_per_million / 1_000_000   # $0.231480
```

Koi error nahi. Koi red line nahi. Program kaamyabi se chala aur output ki
shakal bhi bilkul theek thi — **sirf value 17 guna ghalat thi.**

Yehi qism ka bug production me sabse zyada nuqsan karta hai, kyunki khud ko
zahir nahi karta. **Bachao:** aisi har calculation ka jawab ek dafa calculator
par check karo — 2 second lagte hain.

## Open questions

- [ ] _(likhte jao)_
