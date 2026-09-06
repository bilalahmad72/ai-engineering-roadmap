---
day: D01
title: Python setup + syntax (Dart se mapping)
phase: Foundations
date: 2026-09-06
tags: [python, venv, pip, dart-mapping, json]
status: draft
---

# D01 — Python setup + syntax (Dart se mapping)

> 🔄 **In progress** — ye note session ke saath saath bharta ja raha hai.

## Environment (verify hua)

| Cheez | Version | Kahan |
|---|---|---|
| OS | Windows 11 Pro | — |
| Python | 3.13.14 | `C:\Users\Bilal\AppData\Local\Programs\Python\Python313\python.exe` |
| pip | 26.2 | bundled |
| Node | 22.13.1 | (is din ke liye zaroori nahi) |
| Git | 2.47.1 | — |
| Shell | Git Bash + PowerShell | — |

## TL;DR

_(din ke aakhir me bharna hai)_

## Concepts

### Virtual environment (venv) — aur ye Dart me kyun nahi hota

Dart me har project ka dependency isolation **automatic** hai. Python me nahi —
`pip install` by default sab kuch **globally** daal deta hai, is liye do projects
jinhe ek hi package ki alag versions chahiye, aapas me collide kar jate hain.
`venv` wahi isolation manually banata hai: ek folder jisme us project ka apna
Python interpreter aur apne packages hote hain.

| Flutter / Dart | Python |
|---|---|
| `pubspec.yaml` | `requirements.txt` |
| `.dart_tool/` + pub cache | `.venv/` folder |
| `dart pub add http` | `pip install httpx` |
| `dart pub get` | `pip install -r requirements.txt` |

**Asool:** naye Python project ka pehla command hamesha `python -m venv .venv` hai.

**Isolation ka live proof:** global pip 26.2 tha, lekin venv ke andar pip 26.1.2
nikla — venv apna alag pip bundle karta hai. Yani venv sirf packages nahi,
poora tooling isolate karta hai.

```powershell
python -m venv .venv          # banao (sirf ek dafa)
.\.venv\Scripts\Activate.ps1  # PowerShell me activate (har naye terminal me)
```

Git Bash me activate: `source .venv/Scripts/activate`

Activate hone ki nishani: prompt ke shuru me `(.venv)` aa jata hai. Har naya
terminal kholne par dobara activate karna parta hai — venv "yaad" nahi rehta.

`.venv/` folder **kabhi commit nahi hota** (`.gitignore` me hai). Repo me sirf
`requirements.txt` jata hai, jisse koi bhi wahi environment dobara bana sake —
bilkul `pubspec.yaml` ki tarah.

### Dart → Python cheatsheet

Verify hua `learning/phase-0-foundations/D01-python-setup/dart_to_python.py` chala kar.

#### Syntax

| Dart / Flutter | Python |
|---|---|
| `final String name = 'Bilal';` | `name: str = "Bilal"` (hint optional) |
| `var age = 28;` | `age = 28` |
| `true` / `false` / `null` | `True` / `False` / `None` (capital!) |
| `'Hello $name'` | `f"Hello {name}"` |
| `// comment` | `# comment` |
| `{ }` blocks | indentation (4 spaces) |

#### Collections

| Dart | Python |
|---|---|
| `List<String>` | `list` → `["a", "b"]` |
| `Map<String, dynamic>` | `dict` → `{"k": "v"}` |
| `Set<String>` | `set` → `{"a", "b"}` |
| — (Dart me nahi) | `tuple` → `(10, 20)` immutable |
| `list.add(x)` | `list.append(x)` |
| `list.map((s) => s.toUpperCase()).toList()` | `[s.upper() for s in list]` |
| `list.where((s) => s.length > 4).toList()` | `[s for s in list if len(s) > 4]` |
| `map['key']` | `dict["key"]` |
| `map['key'] ?? 'default'` | `dict.get("key", "default")` |

**List comprehension** Python ka sabse zyada dikhne wala idiom hai — `.map()` aur
`.where()` dono ka kaam ek line me: `[expression for x in list if condition]`.

#### Classes

| Dart | Python |
|---|---|
| `this.name` | `self.name` (aur `self` explicitly likhna parta hai) |
| constructor `User({required this.name})` | `def __init__(self, name): self.name = name` |
| `toString()` override | `@dataclass` khud bana deta hai |
| Equatable / Freezed | `@dataclass` (== aur repr free) |
| `{this.level = 1}` default | `level: int = 1` |

**`@dataclass` = Freezed ka halka version.** `__init__`, `__repr__` aur `==`
khud generate karta hai. Data models ke liye default choice yehi honi chahiye.

#### Functions

| Dart | Python |
|---|---|
| `String greet(String name)` | `def greet(name: str) -> str:` |
| `{String greeting = 'Hello'}` | `greeting: str = "Hello"` |
| named args ke liye `{}` zaroori | koi bhi param named ban sakta hai |

## Code

- [`dart_to_python.py`](../../learning/phase-0-foundations/D01-python-setup/dart_to_python.py)
  — 6 sections, chala kar verify kiya gaya

## Gotchas / jo phansa

Koi environment issue nahi aaya (dekho [ISSUES.md](../ISSUES.md) — abhi khali hai).
Lekin teen **language-level traps** mile jo Dart ki aadat se seedha takrate hain:

| # | Trap | Dart me | Python me | Kyun khatarnak |
|---|---|---|---|---|
| 1 | Type hints enforce nahi hote | `age = "str"` compile error | chal jata hai | `age: int` likhne ke bawajood runtime par string aa sakti hai. Hint sirf editor ke liye hai — validation khud karni paregi (isi liye aage **Pydantic** use karenge). |
| 2 | **`or` ≠ `??`** | `0 ?? 99` → `0` | `0 or 99` → `99` | `or` har **falsy** value par fallback le leta hai: `0`, `""`, `[]`, `{}`, `False`. |
| 3 | Coroutine call hote hi nahi chalta | `fetch()` turant start | `<coroutine object>` milta hai | `await` ya event loop ke bagair kuch nahi hota. Bhoolne par silent no-op. |

### Trap #2 ka asli LLM-code khatra

Ye theoretical nahi — LLM code me seedha bug banta hai:

```python
# GALAT — temperature=0 (deterministic output) chup-chaap 0.7 ban jayega
temperature = user_temp or 0.7

# GALAT — max_tokens=0 ya stream=False bhi isi tarah ud jayenge
max_tokens = user_max or 1000

# SAHI
temperature = user_temp if user_temp is not None else 0.7
```

`temperature=0` LLM apps me sabse zyada use hone wali value hai (structured
output, classification, evals). `or` use kiya to woh kabhi apply hi nahi hogi
aur output random aata rahega — aur error kahin nahi dikhega.

**Asool:** Python me `??` ka sahi tarjuma `or` nahi, **`X if X is not None else Y`** hai.

## Client angle

_(din ke aakhir me)_

## Open questions

- [ ] _(likhte jao)_

## Links

- [Python venv docs](https://docs.python.org/3/library/venv.html)
- [httpx docs](https://www.python-httpx.org/)
