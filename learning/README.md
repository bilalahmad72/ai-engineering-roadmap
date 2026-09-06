# 🧪 Learning Code

Har din ka practice code yahan rehta hai — taake baad me sab kuch dobara chalaya
ja sake aur portfolio/case study me reference diya ja sake.

```
learning/
  phase-0-foundations/
    D01-python-setup/
    D02-async-http/
    ...
  phase-1-llm-fundamentals/
    D05-tokens/
    ...
```

## Rules

- Ek din = ek folder. Folder ka naam day ID se shuru hota hai (`D01-...`).
- Har folder me chhota `README.md` — kya banaya, kaise chalana hai.
- Secrets kabhi commit nahi hote. API keys sirf `.env` me (jo `.gitignore` me hai).
  Har folder me `.env.example` rakho placeholder values ke saath.
- Code chalna chahiye. Adhoore experiments bhi rakho, lekin README me likh do
  ke kya kaam nahi kiya aur kyun.

## Virtual environment

Poore repo ke liye ek hi venv (`.venv/` root me, gitignored):

```bash
# Windows (Git Bash)
source .venv/Scripts/activate

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

Naye packages install karne ke baad:

```bash
pip freeze > requirements.txt
```
