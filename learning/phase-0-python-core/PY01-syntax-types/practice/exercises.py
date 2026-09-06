"""
PY01 PRACTICE — syntax, variables, types, strings.

8 exercises. Har function ke andar `TODO` hai — usay apne code se badlo.

RULES:
  1. Google/docs dekhna JAIZ hai. Ready-made jawab copy karna nahi.
  2. Har change ke baad SAVE (Ctrl+S) — Python me hot reload nahi hota.
  3. Check chalao:
     python learning\\phase-0-python-core\\PY01-syntax-types\\practice\\check.py
  4. Jo FAIL ho sirf usay theek karo. Sab green hone tak repeat.

Andaza: 45-60 minute. Atak jao to poochho — hint milega, jawab nahi.
"""


# ===========================================================================
# EX1 — f-string basics
# ===========================================================================
def greet(name: str, city: str) -> str:
    """
    Ye exact jumla banao (f-string use karo, + se jorna nahi):

        greet("Bilal", "Lahore")  ->  "Assalamu alaikum Bilal, Lahore se!"

    Hint: f"...{variable}..."
    """
    return ""  # TODO


# ===========================================================================
# EX2 — Type conversion
# ===========================================================================
def to_int_or_zero(value: str) -> int:
    """
    String ko int me badlo. Agar badla NA ja sake to 0 return karo.

        to_int_or_zero("42")     -> 42
        to_int_or_zero("  7  ")  -> 7      (extra spaces chalti hain)
        to_int_or_zero("abc")    -> 0
        to_int_or_zero("")       -> 0

    Hint: int("abc") ValueError phenkta hai. try/except ki zaroorat paregi —
    ye PY07 ka topic hai, lekin yahan chhota sa istemal seekh lo:

        try:
            ...
        except ValueError:
            ...
    """
    return 0  # TODO


# ===========================================================================
# EX3 — String cleaning
# ===========================================================================
def clean_name(raw: str) -> str:
    """
    User ka likha hua ganda naam saaf karo:
      - aage peeche ki spaces hatao
      - har lafz ka pehla harf capital, baqi small

        clean_name("  bilal AHMAD  ")  -> "Bilal Ahmad"
        clean_name("SAIRA khan")       -> "Saira Khan"

    Hint: do string methods chahiye — ek spaces ke liye, ek capitalization ke
    liye. Dono ko chain kiya ja sakta hai: raw.method1().method2()
    """
    return ""  # TODO


# ===========================================================================
# EX4 — Split + join + slicing
# ===========================================================================
def initials(full_name: str) -> str:
    """
    Poore naam se initials banao — har lafz ka pehla harf, capital,
    dot aur space ke saath.

        initials("bilal ahmad")        -> "B. A."
        initials("Muhammad Ali Khan")  -> "M. A. K."

    Hint: split() se lafz alag karo, har lafz ka [0] lo, upper() karo,
    phir join() se joro. Ek comprehension me sab ho sakta hai.
    """
    return ""  # TODO


# ===========================================================================
# EX5 — Number formatting
# ===========================================================================
def format_price(amount: float) -> str:
    """
    Amount ko is format me do: dollar sign, 2 decimal places,
    aur hazaar ke liye comma.

        format_price(1234.5)    -> "$1,234.50"
        format_price(99)        -> "$99.00"
        format_price(1000000)   -> "$1,000,000.00"

    Hint: f-string ke andar format spec: f"{value:,.2f}"
    Comma = thousands separator, .2f = 2 decimal places.
    """
    return ""  # TODO


# ===========================================================================
# EX6 — Chhoti si LLM cost calculation
# ===========================================================================
def token_cost(tokens: int, price_per_million: float) -> str:
    """
    Tokens ki cost nikalo aur 6 decimal places tak string me do.

        cost = (tokens / 1,000,000) * price_per_million

        token_cost(1500, 15.0)   -> "$0.022500"
        token_cost(1000000, 3.0) -> "$3.000000"
        token_cost(0, 15.0)      -> "$0.000000"

    Hint: f"{value:.6f}" — yahan comma NAHI chahiye.
    """
    return ""  # TODO


# ===========================================================================
# EX7 — Parsing (asli kaam jaisa)
# ===========================================================================
def parse_config_line(line: str) -> tuple[str, str]:
    """
    .env file ki ek line ko (key, value) tuple me todo.
    Dono taraf ki extra spaces hat jani chahiyein.

        parse_config_line("MODEL=claude-opus-4")    -> ("MODEL", "claude-opus-4")
        parse_config_line("  API_KEY = sk-123  ")   -> ("API_KEY", "sk-123")

    Agar line me "=" hai hi nahi, to (line.strip(), "") return karo:

        parse_config_line("BROKEN")                 -> ("BROKEN", "")

    Hint: split("=", 1) — doosra argument matlab sirf PEHLE = par todo.
    (Value me bhi "=" ho sakta hai, jaise base64 keys me.)
    """
    return ("", "")  # TODO


# ===========================================================================
# EX8 — Truthiness aur membership
# ===========================================================================
def describe_input(text: str) -> str:
    """
    Text ke baare me batao:
      - agar text khaali hai (ya sirf spaces)      -> "empty"
      - warna agar usme "?" maujood hai            -> "question"
      - warna agar 50 se zyada characters hain     -> "long"
      - warna                                       -> "short"

        describe_input("")             -> "empty"
        describe_input("   ")          -> "empty"
        describe_input("kya hai?")     -> "question"
        describe_input("hello")        -> "short"
        describe_input("a" * 60)       -> "long"

    Hint: khaali check ke liye strip() ke baad `not` use karo.
    "?" dhoondne ke liye `in` operator: "?" in text
    Order ahem hai — upar wali condition pehle check hogi.
    """
    return ""  # TODO


if __name__ == "__main__":
    print("Ye file khud kuch nahi chalati. check.py chalao:")
    print("  python learning\\phase-0-python-core\\PY01-syntax-types\\practice\\check.py")
