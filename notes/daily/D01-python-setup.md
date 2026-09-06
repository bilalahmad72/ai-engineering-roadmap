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

## Code

_(learning/phase-0-foundations/D01-python-setup/ me)_

## Gotchas / jo phansa

_(dekho [ISSUES.md](../ISSUES.md))_

## Client angle

_(din ke aakhir me)_

## Open questions

- [ ] _(likhte jao)_

## Links

- [Python venv docs](https://docs.python.org/3/library/venv.html)
- [httpx docs](https://www.python-httpx.org/)
