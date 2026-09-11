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
- [x] **Topic 2 — Dict**
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

---

## Topic 2 — Dict

**Aaj ka sabse ahem topic.** Har API response, har message, har tool definition
dict hai.

```python
user = {"name": "Bilal", "age": 28}      # Dart: Map<String, dynamic>
```

### 🔴 Padhna — `[]` vs `.get()`

| | `user["key"]` | `user.get("key", default)` |
|---|---|---|
| Key ho | value | value |
| Key na ho | **KeyError — crash** | default (ya `None`) |
| Kab | key ka hona **yaqeeni** ho | **bahar se aaya data** — hamesha |

**Asool:** *jo data bahar se aaya (API, JSON, user), uski har optional key
`.get()` se parho.* LLM APIs har field hamesha nahi bhejtin — `cache_tokens`
sirf caching par, `error` sirf ghalti par.

### Nested safe access — `.get()` ki zanjeer

```python
response.get("usage", {}).get("cache_tokens", 0)
```

Do qadam me:

```python
usage = response.get("usage", {})       # dict milti hai (asli ya KHAALI)
tokens = usage.get("cache_tokens", 0)   # us par doosra .get()
```

**`{}` default hi asal chaal hai.** Agar `{}` na ho aur `usage` na mile to
pehla `.get()` `None` dega, aur `None.get()` par crash:
`AttributeError: 'NoneType' object has no attribute 'get'`.

> **Yaad rakhne ka jumla:** *khaali dict aage barhne ke liye, asli default
> rukne ke liye.* Beech ki kariyon me `{}`, aakhri me asli value (`0`).
>
> **Dart me:** `response?['usage']?['cache_tokens'] ?? 0`. Python me `?.` hai
> hi nahi — `.get(key, {})` ki zanjeer uska jawab hai.

### Likhna, badalna, nikalna

```python
user["city"] = "Lahore"          # nayi key (ya purani badlo)
user.update({"age": 29})         # kai ek saath
user.pop("age")                  # nikalo AUR wapas lo
user.pop("xyz", "default")       # na mile to default — .get() jaisa
del user["city"]                 # sirf mita do, wapas kuch nahi
```

`pop()` vs `del`: `del` sirf mitata hai, `pop()` **mita kar wapas bhi deta hai**
— jab cheez hataani ho *aur* uski value chahiye ho.

### `in` sirf keys dekhta hai

```python
"role" in msg              # True    <- key
"system" in msg            # False   <- ye value hai!
"system" in msg.values()   # True
```

### Nested padhna — bayein se dayein, ek qadam ek dafa

```python
response["content"][0]["text"]
#  dict     list   dict   str
```

### Dict bhi alias hota hai

```python
last = messages[-1]          # naql nahi — usi dict ka doosra naam
last["timestamp"] = "..."    # messages[-1] me bhi aa gaya
```

Topic 1 wala asool dict par bhi: `=` naql nahi banata. Asli code me yehi
pattern roz hai — list se item nikaalo, badlo, list khud updated.

### Quotes — Python version ka masla

```python
f"{response["model"]}"     # sirf 3.12+ par chalta hai
f"{response['model']}"     # har jagah — bahar double, andar single
```

Deployment aksar purane Python par hota hai (Docker images, Lambda) — mehfooz
aadat doosri wali.

### 🖊️ Meri practice — Topic 2

`t2_dict.py` — Claude API response parse

```python
response = {
    "id": "msg_01abc",
    "model": "claude-opus-4",
    "content": [{"type": "text", "text": "Salam! Kaise madad karun?"}],
    "usage": {"input_tokens": 12, "output_tokens": 34, "cache_tokens": 100},
}

print(f"model: {response['model']}")
print(f"reply: {response['content'][0]['text']}")
print(f"total tokens: {response['usage']['input_tokens'] + response['usage']['output_tokens']}")
print(f"error: {response.get('error', 'no error')}")
print(f"cache tokens: {response.get('usage', {}).get('cache_tokens', 0)}")
```

```
model: claude-opus-4
reply: Salam! Kaise madad karun?
total tokens: 46
error: no error
cache tokens: 100
```

Chat history (list of dicts — jo har LLM API maangti hai):

```python
messages = [
    {"role": "system", "content": "Tum ek Flutter expert ho."},
    {"role": "user", "content": "Riverpod kya hai?"},
    {"role": "assistant", "content": "Riverpod ek state management library hai."},
]
messages.append({"role": "user", "content": "aur BLoC?"})

print(f"first role: {messages[0]['role']}")            # list -> [0] -> dict -> ['role']
print(f"last content: {messages[-1]['content']}")

last_message = messages[-1]                # alias — naql nahi
last_message["timestamp"] = "2026-09-11"   # messages[-1] me bhi aa gaya
popped_message = last_message.pop("timestamp")
print(f"popped: {popped_message}")
```

```
total messages: 4
first role: system
last content: aur BLoC?
True      <- "role" in first
False     <- "system" in first   (value hai, key nahi)
True      <- "system" in first.values()
{'role': 'user', 'content': 'aur BLoC?', 'timestamp': '2026-09-11'}
popped: 2026-09-11
```

### 🐛 Bug #5 — phir wahi khandan

```python
response.get("cache_tokens", 0)                       # top level par dhoonda -> 0 (ittefaqan sahi)
response.get("usage", {}).get("cache_tokens", 0)      # usage ke ANDAR -> 100 (sahi)
```

`cache_tokens` `usage` ke andar tha, top level par dhoonda. Output `0` aaya
kyunki top level par bhi nahi tha — **jawab ittefaqan sahi, code ghalat.**
Sabit kiya `usage` me `cache_tokens: 100` daal kar: purana code phir bhi `0`.

**Ab tak paanch bug, teen dafa output ittefaqan sahi.** Aadat:

> **"Agar mera code ghalat hota, to kya ye output badal jata?"**
> Jawab "nahi" hai to kuch test hi nahi hua.

## Code

- [`t1_list.py`](../../learning/phase-0-python-core/PY02-collections/t1_list.py)
- [`t2_dict.py`](../../learning/phase-0-python-core/PY02-collections/t2_dict.py)

## Open questions

- [ ] _(likhte jao)_
