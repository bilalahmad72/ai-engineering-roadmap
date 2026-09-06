"""
D01 PRACTICE — ye file TUM bharoge.

Har function ke andar abhi sirf `pass` (ya galat return) hai. Har ek ka spec
uske docstring me likha hai. Tumhara kaam: har function ko implement karna.

RULES:
  1. reference/ folder KHOLNA MANA HAI. Pehle apni yaadash se likho.
  2. Atak jao to Google/docs dekh lo — ye bilkul jaiz hai.
  3. Har baar likhne ke baad check chalao:

     python learning\\phase-0-foundations\\D01-python-setup\\practice\\check.py

  4. Jo fail ho, sirf usay theek karo. Sab green hone tak repeat.

6 exercises hain. Andaza: 30-40 minute.
"""

from dataclasses import dataclass  # noqa: F401  (EX4 me chahiye hoga)
import json  # noqa: F401  (EX5, EX6 me chahiye hoga)


# ===========================================================================
# EX1 — List comprehension  (Dart ka .map + .where)
# ===========================================================================
def long_skills_upper(skills: list[str]) -> list[str]:
    """
    `skills` me se sirf woh names lo jinki length 4 se ZYADA hai,
    aur unhe UPPERCASE me return karo. Order wahi rahe.

    long_skills_upper(["Dart", "Flutter", "Go", "Postgres"])
        -> ["FLUTTER", "POSTGRES"]

    Hint: ek hi list comprehension me filter aur transform dono ho sakte hain.
    """
    return []  # TODO


# ===========================================================================
# EX2 — Safe dict access  (Dart ka map['k'] ?? default)
# ===========================================================================
def get_model_name(response: dict) -> str:
    """
    `response` dict me se "model" key ka value return karo.
    Agar "model" key MAUJOOD NAHI hai, to "unknown" return karo.

    KeyError kabhi nahi aana chahiye.

    get_model_name({"model": "claude-opus-4"})  -> "claude-opus-4"
    get_model_name({"id": "msg_1"})             -> "unknown"
    get_model_name({})                          -> "unknown"
    """
    return ""  # TODO


# ===========================================================================
# EX3 — Null safety trap  (Dart ka ?? sahi tarah)
# ===========================================================================
def resolve_temperature(user_value: float | None) -> float:
    """
    Agar `user_value` None hai to default 0.7 return karo.
    Agar user_value koi bhi ASLI number hai (0.0 samet!) to WAHI return karo.

    resolve_temperature(None)  -> 0.7
    resolve_temperature(0.9)   -> 0.9
    resolve_temperature(0.0)   -> 0.0     <-- ye wala asli imtihan hai

    YAAD RAKHO: `or` yahan kaam NAHI karega. Kyun? 0.0 falsy hai.
    """
    return 0.7  # TODO


# ===========================================================================
# EX4 — Dataclass  (Dart ka Equatable/Freezed)
# ===========================================================================
# Neeche ek NORMAL class hai. Isay @dataclass me convert karo taake:
#   - __init__ khud bane (name, tokens, aur cached ka default False)
#   - == value equality de
#   - print karne par readable repr aaye
#
# Field order: name (str), tokens (int), cached (bool = False)


class ModelUsage:  # TODO: isay dataclass banao
    pass


# ===========================================================================
# EX5 — Nested JSON parse  (asli LLM response shape)
# ===========================================================================
def extract_reply(raw_json: str) -> tuple[str, int]:
    """
    `raw_json` ek JSON STRING hai (dict nahi). Usay parse karke
    (reply_text, total_tokens) ka tuple return karo.

    Shape:
    {
      "content": [{"type": "text", "text": "<reply yahan>"}],
      "usage": {"input_tokens": 10, "output_tokens": 20}
    }

    total_tokens = input_tokens + output_tokens

    extract_reply('{"content":[{"type":"text","text":"Hi"}],'
                  '"usage":{"input_tokens":10,"output_tokens":20}}')
        -> ("Hi", 30)
    """
    return ("", 0)  # TODO


# ===========================================================================
# EX6 — JSON file likhna, Urdu safe rakhte hue
# ===========================================================================
def save_note(path: str, data: dict) -> None:
    """
    `data` dict ko `path` par JSON file me likho, is tarah ke:
      - Urdu/emoji \\uXXXX escape me NA badlein (file me asli text nazar aaye)
      - indent 2 ho (readable)
      - Windows par UnicodeEncodeError na aaye

    Return kuch nahi karna, bas file likhni hai.

    Teen cheezein chahiye: open() ka ek argument, json.dump ke do arguments.
    """
    pass  # TODO


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Ye file khud kuch nahi chalati. check.py chalao:")
    print("  python learning\\phase-0-foundations\\D01-python-setup\\practice\\check.py")
