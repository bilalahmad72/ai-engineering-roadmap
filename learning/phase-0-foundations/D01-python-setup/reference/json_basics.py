"""
D01 — JSON handling in Python.

Aage har din LLM API se JSON aayega. Ye file woh 4 cheezein cover karti hai
jo roz kaam aayengi + 3 traps jo pehli dafa sabko phansate hain.

Run:  python learning/phase-0-foundations/D01-python-setup/json_basics.py
"""

import json
from datetime import datetime, timezone
from pathlib import Path


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n  {title}\n{'=' * 60}")


HERE = Path(__file__).parent


# ---------------------------------------------------------------------------
section("1. Chaar functions — bas yehi yaad rakhne hain")
# ---------------------------------------------------------------------------
# Dart:                              Python:
#   jsonDecode(string)      ->         json.loads(string)    string -> dict
#   jsonEncode(map)         ->         json.dumps(dict)      dict   -> string
#   (file parhna alag)      ->         json.load(file)       file   -> dict
#   (file likhna alag)      ->         json.dump(dict, file) dict   -> file
#
# Yaad rakhne ka tareeqa: 's' ka matlab STRING hai.
#   loads/dumps = string ke saath | load/dump = file ke saath

raw = '{"model": "claude-opus-4", "tokens": 1523, "cached": true}'

data = json.loads(raw)               # string -> dict
print("loads ->", data, type(data).__name__)
print("access:", data["model"], "|", data["tokens"])

back = json.dumps(data)              # dict -> string
print("dumps ->", back, type(back).__name__)

# NOTE: JSON ka `true` Python me `True` ban gaya (capital). null -> None.


# ---------------------------------------------------------------------------
section("2. Nested JSON — jaise asli LLM response hota hai")
# ---------------------------------------------------------------------------
# Ye bilkul us shape me hai jo D08/D09 me OpenAI/Anthropic se milega.

api_response = json.loads("""
{
  "id": "msg_01abc",
  "model": "claude-opus-4",
  "stop_reason": "end_turn",
  "content": [
    {"type": "text", "text": "Assalamu alaikum! Kaise madad karun?"}
  ],
  "usage": {"input_tokens": 12, "output_tokens": 34}
}
""")

# Nested access — Dart me `res['content'][0]['text']` bilkul same hai
text = api_response["content"][0]["text"]
tokens_in = api_response["usage"]["input_tokens"]
tokens_out = api_response["usage"]["output_tokens"]

print("reply     :", text)
print("tokens    :", tokens_in, "in +", tokens_out, "out =", tokens_in + tokens_out)
print("stop      :", api_response["stop_reason"])

# Cost estimate — D05 me isi ko poora karenge
cost = (tokens_in / 1_000_000 * 15) + (tokens_out / 1_000_000 * 75)
print(f"cost      : ${cost:.8f}")


# ---------------------------------------------------------------------------
section("3. TRAP: missing key = crash")
# ---------------------------------------------------------------------------
# Sabse aam production bug. LLM APIs har field hamesha nahi bhejtin.

try:
    _ = api_response["error"]                      # ye key hai hi nahi
except KeyError as e:
    print("CRASH:", type(e).__name__, e, "<- app mar jayegi")

# SAHI tareeqa — .get() default ke saath (Dart ke ?? jaisa, lekin dict par safe)
print("SAFE :", api_response.get("error", "no error"))
print("SAFE :", api_response.get("usage", {}).get("cache_tokens", 0), "<- nested chaining")

# Asool: API response se koi bhi optional field HAMESHA .get() se parho.


# ---------------------------------------------------------------------------
section("4. TRAP: Urdu/emoji \\u escape ban jate hain")
# ---------------------------------------------------------------------------
urdu = {"greeting": "السلام علیکم", "emoji": "🚀"}

print("default          :", json.dumps(urdu))
print("ensure_ascii=False:", json.dumps(urdu, ensure_ascii=False))

# Default me non-ASCII \uXXXX ban jata hai. Technically valid hai, lekin logs
# aur files me na-qabil-e-parh. Urdu content ke liye HAMESHA ensure_ascii=False.


# ---------------------------------------------------------------------------
section("5. TRAP: datetime JSON-serializable nahi hai")
# ---------------------------------------------------------------------------
record = {"user": "bilal", "at": datetime.now(timezone.utc)}

try:
    json.dumps(record)
except TypeError as e:
    print("CRASH:", e)

# FIX 1 — khud convert karo (sabse saaf)
record_fixed = {**record, "at": record["at"].isoformat()}
print("FIX 1:", json.dumps(record_fixed))

# FIX 2 — default= callback (jab nested me kahin bhi datetime ho sakta ho)
print("FIX 2:", json.dumps(record, default=str))


# ---------------------------------------------------------------------------
section("6. File read/write (load / dump)")
# ---------------------------------------------------------------------------
out_file = HERE / "sample_output.json"

payload = {
    "day": "D01",
    "topic": "Python setup",
    "learned": ["venv", "dart->python mapping", "json"],
    "note": "Urdu bhi chalti hai: ٹھیک ہے",
    "saved_at": datetime.now(timezone.utc).isoformat(),
}

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
print("likha:", out_file.name)

with open(out_file, encoding="utf-8") as f:
    loaded = json.load(f)
print("parha:", loaded["topic"], "|", loaded["learned"])

# encoding="utf-8" Windows par LAAZMI hai — default cp1252 hai jo Urdu par
# UnicodeEncodeError deta hai. (Yehi bug is repo ke track.py me bhi aaya tha.)

print("\n" + "=" * 60)
print("  Ho gaya. sample_output.json khol kar dekho.")
print("=" * 60)
