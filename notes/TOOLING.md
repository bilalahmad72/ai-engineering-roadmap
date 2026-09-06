# 🛠️ Tooling Guide — VS Code for Python

Flutter ke liye VS Code already aata hai. Ye guide sirf woh **farq** batati hai
jo Python me hai, aur woh buttons/shortcuts jo is poore roadmap me roz chahiye.

> Windows shortcuts likhe hain. `Ctrl` = Control key.

---

## 1. Zaroori extensions

| Extension | ID | Kyun |
|---|---|---|
| **Python** | `ms-python.python` | Laazmi. Run button, debugging, interpreter selection |
| **Pylance** | `ms-python.vscode-pylance` | Python extension ke saath khud aa jata hai. IntelliSense + type checking |
| **Ruff** | `charliermarsh.ruff` | Linter + formatter. Dart ke `dart format` + analyzer ka jawab |

### Install karne ka tareeqa (UI se)

1. Bayein (left) sidebar me **Extensions** icon — chaar chokor wala (`Ctrl+Shift+X`)
2. Search box me `Python` likhein
3. Woh wala chunein jiska publisher **Microsoft** ho (sabse upar, sabse zyada downloads)
4. Neela **Install** button dabayein
5. Wahi `Ruff` ke liye dohrayein (publisher: **Astral Software**)

Install ke baad VS Code reload maang sakta hai — **Reload** kar dein.

---

## 2. Interpreter select karna (sabse ahem step)

Ye woh cheez hai jo Python me sab se zyada confusion paida karti hai, aur Dart
me iska koi equivalent hi nahi.

**Masla:** system par kai Python ho sakte hain — global wala, aur har project ka
apna `.venv`. VS Code ko batana parta hai ke **kaunsa** use karna hai. Agar galat
select ho, to terminal me package install hoga lekin editor "module not found"
ki red line dikhata rahega.

**Tareeqa:**

1. `Ctrl+Shift+P` → Command Palette khulega (Flutter me bhi yehi use karte ho)
2. Likhein: `Python: Select Interpreter`
3. Woh option chunein jisme `.venv` likha ho —
   `Python 3.13.14 ('.venv': venv) .\.venv\Scripts\python.exe`
4. Neeche dayein (bottom-right) status bar me `.venv` nazar aana chahiye

**Confirm:** koi bhi `.py` file kholein, neeche status bar me Python version ke
saath `('.venv': venv)` likha hona chahiye.

---

## 3. File aur folder banana

| Kaam | Tareeqa |
|---|---|
| **Nayi file** | Explorer (`Ctrl+Shift+E`) me folder par right-click → **New File** → naam + `.py` |
| **Naya folder** | Right-click → **New Folder** |
| **Toolbar se** | Explorer panel ke header par hover karein — chaar chhote icons aate hain: new file, new folder, refresh, collapse |
| **Terminal se** | `New-Item -ItemType File practice/test.py` (PowerShell) |
| **Rename** | File par `F2` |
| **Delete** | File select karke `Delete` |
| **Path copy** | Right-click → **Copy Relative Path** (terminal me chalane ke liye) |

> **Extension zaroori hai:** `.py` likhna mat bhoolein. Bina extension ke VS Code
> ko pata nahi chalta ke ye Python hai — na syntax colors aayenge, na Run button.

---

## 4. File chalana — 3 tareeqe

| Tareeqa | Kaise | Kab |
|---|---|---|
| **Run button** | Upar dayein kone me ▶️ play icon | Sabse tez, roz ka istemal |
| **Terminal** | `python path\to\file.py` | Jab arguments dene hon |
| **Debug** | `F5` | Jab step-by-step dekhna ho |

Play button ke pas ek chhota **▼ arrow** bhi hai → "Run Python File" aur
"Debug Python File" ke options.

---

## 5. Terminal

| Kaam | Shortcut |
|---|---|
| Terminal kholna/band karna | ``Ctrl+` `` (backtick) |
| Naya terminal | ``Ctrl+Shift+` `` |
| Command cancel karna | `Ctrl+C` |
| Screen saaf karna | `cls` (PowerShell) ya `clear` |
| Purana command | ⬆️ arrow key |

**Aham:** VS Code ka terminal project folder me hi khulta hai, aur agar interpreter
sahi select kiya ho to venv **khud activate** ho jata hai — prompt me `(.venv)`
nazar aayega. Agar na aaye, khud activate karein:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 6. Debugging (D02 ke baad se roz kaam aayegi)

`print()` se debug karna theek hai, lekin debugger bohot tez hai — aur Flutter me
aap already use karte ho, bilkul wahi cheez hai.

1. **Breakpoint lagayein** — line number ke bayein taraf click karein, laal gol nishan aayega
2. **`F5`** dabayein — code us line par ruk jayega
3. Bayein panel me **VARIABLES** — us waqt har variable ki value nazar aayegi
4. Upar controls:

| Button | Shortcut | Kaam |
|---|---|---|
| Continue | `F5` | Agle breakpoint tak chalao |
| Step Over | `F10` | Agli line (function ke andar mat jao) |
| Step Into | `F11` | Function ke **andar** jao |
| Stop | `Shift+F5` | Band karo |

**DEBUG CONSOLE** tab me aap live Python likh kar variables check kar sakte hain.

---

## 7. Roz ke shortcuts

| Shortcut | Kaam |
|---|---|
| `Ctrl+Shift+P` | Command Palette — **sab kuch** yahan se milta hai |
| `Ctrl+P` | File naam se kholo |
| `Ctrl+S` | Save (Python me save laazmi hai — hot reload nahi hota!) |
| `Ctrl+Shift+E` | Explorer (files) |
| `Ctrl+Shift+X` | Extensions |
| `Ctrl+Shift+G` | Git panel |
| `Ctrl+/` | Line comment on/off |
| `Alt+↑` / `Alt+↓` | Line upar/neeche move |
| `Shift+Alt+↓` | Line duplicate |
| `Ctrl+D` | Agla same word bhi select (multi-cursor) |
| `F2` | Rename symbol (poore project me) |
| `Ctrl+Space` | IntelliSense zabardasti bulao |
| `F12` | Definition par jao |
| `Alt+Shift+F` | Format document |

> **Flutter waali aadat jo yahan nahi chalegi:** hot reload. Python me har
> tabdeeli ke baad file dobara chalani parti hai. `Ctrl+S` phir ▶️.

---

## 8. Git — GUI se

Terminal ke commands aate hain, lekin VS Code ka Git panel tez hai:

1. `Ctrl+Shift+G` → Source Control
2. Har badli hui file nazar aayegi — naam par click karke **diff** dekhein
3. File ke pas **`+`** = stage (`git add`)
4. Upar message box me commit message likhein
5. **✓ Commit** button
6. **Sync Changes** button = push

**Rang ka matlab:** `U` = untracked (nayi), `M` = modified, `D` = deleted

---

## 9. Is repo ka apna workflow

```powershell
# 1. Repo VS Code me kholo
code "D:\AI Engineering Roadmap"

# 2. Terminal kholo (Ctrl+`) — (.venv) prompt me hona chahiye

# 3. Aaj ka kaam dekho
python scripts/track.py next

# 4. practice/exercises.py me code likho, phir check karo
python learning\phase-0-foundations\D01-python-setup\practice\check.py

# 5. Progress record karo
python scripts/track.py task D01 3
```

---

## 10. Common masail

| Masla | Wajah | Fix |
|---|---|---|
| Import par red squiggly, lekin code chalta hai | Galat interpreter | `Python: Select Interpreter` → `.venv` |
| `ModuleNotFoundError` | Package global me install hua, venv me nahi | `(.venv)` prompt check karein, phir `pip install` |
| Terminal me `(.venv)` nahi | Activate nahi hua | `.\.venv\Scripts\Activate.ps1` |
| Run button hi nahi dikh raha | Python extension nahi, ya file `.py` nahi | Extension install karein / naam theek karein |
| Code change kiya, output purana hi | Save nahi kiya | `Ctrl+S` — Python me hot reload nahi |
| `python` not recognized | PATH me nahi | Python installer se "Add to PATH" |

Naya masla aaye to [ISSUES.md](ISSUES.md) me record karein.
