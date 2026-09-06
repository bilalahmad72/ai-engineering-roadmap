# 🔧 Issues & Fixes Log

Har woh error jo raaste me aaya, aur uska asli fix. Ye file sabse zyada kaam
aati hai — 3 mahine baad jab wahi error dobara aayega, jawab yahan milega.

**Format:** har issue ka apna section, newest neeche add hota hai.

---

## Template

### ISS-000 · <chhota title>

| | |
|---|---|
| **Day** | Dxx |
| **Date** | YYYY-MM-DD |
| **Environment** | Windows 11 · Python 3.13.14 · Git Bash / PowerShell |
| **Status** | ✅ Fixed / 🔄 Workaround / ❌ Open |

**Kya hua**

Error message ya galat behaviour, exact text ke saath:

```
<paste actual error>
```

**Wajah**

Asal wajah kya thi (guess nahi — jo verify hua).

**Fix**

```bash
<exact command jo kaam kar gaya>
```

**Seekh**

Ek line: aage isse kaise bacha ja sakta hai.

---

<!-- naye issues yahan se neeche add karo -->

### ISS-001 · `No such file or directory` — path me folder reh gaya

| | |
|---|---|
| **Day** | PY01 |
| **Date** | 2026-09-06 |
| **Environment** | Windows 11 · Python 3.13.14 · PowerShell (VS Code terminal) |
| **Status** | ✅ Fixed |

**Kya hua**

```
python.exe: can't open file
'd:\AI Engineering Roadmap\learning\phase-0-python-core\t1_variables.py':
[Errno 2] No such file or directory
```

**Wajah**

Code me koi masla nahi tha — path adhoora tha. Beech ka folder
`PY01-syntax-types` likhna reh gaya. Asli path:

```
learning\phase-0-python-core\PY01-syntax-types\t1_variables.py
```

**Fix**

```powershell
python learning\phase-0-python-core\PY01-syntax-types\t1_variables.py
```

**Seekh**

- `[Errno 2] No such file or directory` ka matlab **hamesha** path ghalat hai,
  code nahi. Error ke andar jo path likha hai usay ghor se parho — batata hai
  Python ne kahan dhoonda.
- Path haath se likhna hi mat: **▶️ Run button** use karo (VS Code khud sahi
  path banata hai), ya file par right-click → **Copy Relative Path**.
