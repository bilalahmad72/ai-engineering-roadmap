---
day: PY02
title: "Collections: list, tuple, dict, set"
phase: Python Core
date: 2026-09-09
tags: [python, list, dict, set, tuple, mutability]
status: draft
---

# PY02 — Collections

> 🔄 **In progress** — topic-by-topic bharta ja raha hai.

**Ye din PY01 se zyada ahem hai.** AI ka poora kaam collections par chalta hai:

```python
{"content": [...], "usage": {...}}                    # API response -> dict
[{"role": "user", "content": "hi"}, ...]              # chat history -> list of dicts
["chunk 1", "chunk 2", ...]                           # RAG chunks   -> list
```

## Topics

- [x] **Topic 1 — List**
- [ ] Topic 2 — Dict
- [ ] Topic 3 — Set
- [ ] Topic 4 — Tuple

---

## Topic 1 — List

### Banana

```python
skills = ["Flutter", "Dart"]
empty = []
list("abc")        # ["a", "b", "c"]
[0] * 3            # [0, 0, 0]
```

Dart ki `List<T>` hi hai, bas type nahi likhna parta. **Ek bara farq:** Python
ki list me alag-alag types ek saath rakhe ja sakte hain — `["Bilal", 28, True]`
bilkul jaiz hai. Dart me `List<dynamic>` chahiye hoti.

### Daalna — `append` vs `extend`

| Python | Dart | Kya |
|---|---|---|
| `.append(x)` | `.add(x)` | **ek** cheez |
| `.extend([a, b])` | `.addAll(...)` | **kai** cheezein |
| `.insert(0, x)` | `.insert(0, x)` | khaas jagah |

```python
a = ["x"]
a.append(["y", "z"])     # ["x", ["y", "z"]]   <- list ke andar list!
a.extend(["y", "z"])     # ["x", "y", "z"]     <- alag alag
```

### Nikalna

```python
skills.remove("Dart")    # value se hatao (pehla milne wala)
skills.pop()             # aakhri nikalo AUR wapas do
skills.pop(0)            # index se nikalo aur wapas do
del skills[1]            # mita do
```

`pop()` cheez **wapas deta hai**, `remove()` sirf hata deta hai.

### Padhna

```python
skills[0]        skills[-1]        # pehla, aakhri
skills[1:3]      skills[:2]        # slicing
skills[-2:]      skills[::-1]      # aakhri 2, ulti list
len(skills)      "Dart" in skills  # ginti, maujoodgi
```

### 🔴 `sort()` `None` deta hai

```python
sorted_nums = nums.sort()    # sorted_nums ab None hai!
```

**Asool:** *Python me jo method cheez ko khud badalta hai, wo `None` deta hai.*

Ye sirf `sort()` par nahi — `append()`, `reverse()`, `clear()` sab `None` dete
hain. **Pehchan naam se hoti hai:**

| Shakal | Kya karta hai | Misal |
|---|---|---|
| Hukum (`sort`, `reverse`) | cheez khud badalta hai → `None` | `nums.sort()` |
| Sifat (`sorted`, `reversed`) | **nayi** cheez banata hai | `sorted(nums)` |

```python
nums.sort()               # nums khud badli
new = sorted(nums)        # nayi list, nums salamat
```

> **Dart se farq:** Dart me `list.sort()` bhi in-place hai, lekin uska compiler
> `void` ko assign karne par **error** deta hai. Python chup-chaap `None` rakh
> deta hai — bug agli line par `TypeError: 'NoneType' object is not subscriptable`
> ban kar nikalta hai.

### 🔴 `=` naql nahi banata

```python
backup = original         # NAYI list nahi — usi list ka DOOSRA NAAM
backup = original.copy()  # nayi list
```

```
   original ──┐                      original2 ──> ["a","b","c","d"]
              ├──> ["a","b","c","d"]
   backup ────┘                      backup2  ──> ["a","b","c"]
```

**Sahi lafz ahem hai:** `backup = original` "clone" nahi banata — clone ka matlab
hi naql hota hai. Yahan naql banti hi nahi, sirf **doosra naam** milta hai.

Sabit karne ka tareeqa:

```python
original is backup        # True   <- bilkul wohi cheez
original2 is backup2      # False  <- alag cheezein
```

`is` poochta hai *"kya ye **wohi** cheez hai?"*, `==` poochta hai
*"kya **value** ek jaisi hai?"* — do alag lists jinme same cheezein hon:
`==` → True, `is` → False.

**Aage ke liye flag:** `.copy()` **shallow** hai. List ke andar dicts hon (asli
chat history: `[{"role": "user", ...}]`) to bahar wali list nayi banti hai lekin
**andar ke dicts wahi purane rehte hain**. D40 (agent memory) me ye matter karega.

### 🖊️ Meri practice — Topic 1

`t1_list.py` — chat history

```python
messages = []
messages.append("user: salam")
messages.append("assistant: walaikum salam")
messages.append("user: python sikhao")

print(messages)
print(f"count: {len(messages)}")
print(f"first: {messages[0]}")
print(f"last: {messages[-1]}")
print(f"last two: {messages[-2:]}")
```

```
['user: salam', 'assistant: walaikum salam', 'user: python sikhao']
count: 3
first: user: salam
last: user: python sikhao
last two: ['assistant: walaikum salam', 'user: python sikhao']
```

History trimming (context window bharne se bachne ke liye):

```python
history.append("user: aur batao")
history.extend(["assistant: ji", "user: shukriya"])

trimmed_history = history[-4:]     # sirf aakhri 4
```

```
9
['assistant: theek hai', 'user: aur batao', 'assistant: ji', 'user: shukriya']
4
```

### Client angle — trimming itni saadi nahi hoti

`[-4:]` chalta hai lekin asli app me do masail dete hai:

1. **Jori toot jati hai** — trimmed list `assistant` se shuru ho gayi, yani jawab
   pehle aur sawal ghayab. Kuch APIs isay reject kar deti hain. Asal me **joron
   me** (user+assistant) trim karna parta hai, ginti se nahi.
2. **System prompt ur jata hai** — wo hamesha list ke shuru me hota hai, aur
   `[-4:]` usay sabse pehle kaat deta hai. Asli code me system prompt alag rakha
   jata hai, phir baqi history trim hoti hai.

Hal D40 (agent memory) me — abhi sirf jaan lena kaafi hai ke
**"aakhri N rakh lo" kaafi nahi hota.**

### Chhoti tasheeh — keyword vs built-in

`sorted` **keyword nahi, built-in function hai.**

| | Misalein |
|---|---|
| Keyword (reserved, naam nahi ban sakta) | `if`, `for`, `def`, `return`, `True`, `None` |
| Built-in function (pehle se maujood) | `sorted()`, `len()`, `print()`, `sum()` |

`sorted = 5` likhna jaiz hai (bura khayal, lekin jaiz). `if = 5` → SyntaxError.

## Code

- [`t1_list.py`](../../learning/phase-0-python-core/PY02-collections/t1_list.py)

## Open questions

- [ ] _(likhte jao)_
