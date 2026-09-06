"""
D01 practice checker. Tumhare exercises.py ko test karta hai.

Run:  python learning\\phase-0-foundations\\D01-python-setup\\practice\\check.py

Har fail par batata hai: kya expected tha, kya mila, aur ek hint.
"""

import json
import sys
import tempfile
from dataclasses import is_dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, OSError):
    pass

import exercises as ex  # noqa: E402

PASS, FAIL = [], []


def check(name: str, got, expected, hint: str = "") -> None:
    if got == expected:
        PASS.append(name)
        print(f"  PASS  {name}")
    else:
        FAIL.append(name)
        print(f"  FAIL  {name}")
        print(f"        expected : {expected!r}")
        print(f"        got      : {got!r}")
        if hint:
            print(f"        hint     : {hint}")


def safe(fn, *args):
    try:
        return fn(*args)
    except Exception as e:
        return f"<{type(e).__name__}: {e}>"


print("\n" + "=" * 64)
print("  D01 PRACTICE CHECK")
print("=" * 64)

# --- EX1 ------------------------------------------------------------------
print("\nEX1 — list comprehension")
check(
    "EX1.a",
    safe(ex.long_skills_upper, ["Dart", "Flutter", "Go", "Postgres"]),
    ["FLUTTER", "POSTGRES"],
    "[<transform> for s in skills if <condition>]",
)
check("EX1.b", safe(ex.long_skills_upper, []), [], "khali list par khali list aani chahiye")
check("EX1.c", safe(ex.long_skills_upper, ["Go", "AI"]), [], "koi bhi 4 se lamba nahi hai")

# --- EX2 ------------------------------------------------------------------
print("\nEX2 — safe dict access")
check("EX2.a", safe(ex.get_model_name, {"model": "claude-opus-4"}), "claude-opus-4")
check("EX2.b", safe(ex.get_model_name, {"id": "msg_1"}), "unknown", "dict.get(key, default)")
check("EX2.c", safe(ex.get_model_name, {}), "unknown", "KeyError nahi aana chahiye")

# --- EX3 ------------------------------------------------------------------
print("\nEX3 — null safety trap")
check("EX3.a", safe(ex.resolve_temperature, None), 0.7)
check("EX3.b", safe(ex.resolve_temperature, 0.9), 0.9)
check(
    "EX3.c",
    safe(ex.resolve_temperature, 0.0),
    0.0,
    "`or` use kiya? 0.0 falsy hai. `X if X is not None else Y` socho",
)

# --- EX4 ------------------------------------------------------------------
print("\nEX4 — dataclass")
if not is_dataclass(ex.ModelUsage):
    FAIL.append("EX4.dataclass")
    print("  FAIL  EX4.dataclass")
    print("        ModelUsage abhi @dataclass nahi hai")
    print("        hint     : class ke upar @dataclass lagao aur fields likho")
else:
    PASS.append("EX4.dataclass")
    print("  PASS  EX4.dataclass")
    a = safe(lambda: ex.ModelUsage("claude", 100))
    b = safe(lambda: ex.ModelUsage("claude", 100))
    check("EX4.default", getattr(a, "cached", "<missing>"), False, "cached: bool = False")
    check("EX4.equality", a == b, True, "dataclass == free deta hai")
    check(
        "EX4.repr",
        repr(a),
        "ModelUsage(name='claude', tokens=100, cached=False)",
        "field order: name, tokens, cached",
    )

# --- EX5 ------------------------------------------------------------------
print("\nEX5 — nested JSON parse")
sample = json.dumps(
    {
        "content": [{"type": "text", "text": "Hi"}],
        "usage": {"input_tokens": 10, "output_tokens": 20},
    }
)
check("EX5.a", safe(ex.extract_reply, sample), ("Hi", 30), "json.loads() pehle, phir nested access")
sample2 = json.dumps(
    {
        "content": [{"type": "text", "text": "السلام علیکم"}],
        "usage": {"input_tokens": 5, "output_tokens": 7},
    }
)
check("EX5.b", safe(ex.extract_reply, sample2), ("السلام علیکم", 12))

# --- EX6 ------------------------------------------------------------------
print("\nEX6 — JSON file write (Urdu safe)")
tmp = Path(tempfile.gettempdir()) / "d01_check.json"
tmp.unlink(missing_ok=True)
payload = {"greeting": "السلام علیکم", "emoji": "🚀", "n": 1}
err = None
try:
    ex.save_note(str(tmp), payload)
except Exception as e:
    err = f"<{type(e).__name__}: {e}>"

if err:
    FAIL.append("EX6.write")
    print(f"  FAIL  EX6.write\n        crash    : {err}")
    print("        hint     : open(path, 'w', encoding='utf-8')")
elif not tmp.exists():
    FAIL.append("EX6.write")
    print("  FAIL  EX6.write\n        file bani hi nahi")
else:
    PASS.append("EX6.write")
    print("  PASS  EX6.write")
    text = tmp.read_text(encoding="utf-8")
    check("EX6.roundtrip", json.loads(text), payload)
    check(
        "EX6.no_escape",
        "\\u" not in text,
        True,
        "ensure_ascii=False chahiye — file me asli Urdu nazar aaye",
    )
    check("EX6.indent", "\n" in text.strip(), True, "indent=2 se multi-line banti hai")
    tmp.unlink(missing_ok=True)

# --- summary --------------------------------------------------------------
total = len(PASS) + len(FAIL)
print("\n" + "=" * 64)
print(f"  {len(PASS)}/{total} PASS")
if FAIL:
    print(f"  Baqi hain: {', '.join(FAIL)}")
    print("\n  exercises.py me sirf inhe theek karo, phir dobara chalao.")
else:
    print("\n  Sab green. D01 practice complete — ab batao, main review karunga.")
print("=" * 64 + "\n")

sys.exit(1 if FAIL else 0)
