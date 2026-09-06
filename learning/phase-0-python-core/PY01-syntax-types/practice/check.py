"""
PY01 checker.

Run:  python learning\\phase-0-python-core\\PY01-syntax-types\\practice\\check.py
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))                      # exercises.py yahan hai
sys.path.insert(0, str(HERE.parents[2]))           # checklib.py learning/ me hai

import exercises as ex  # noqa: E402
from checklib import check, group, header, safe, summary  # noqa: E402

header("PY01 — syntax, variables, types, strings")

group("EX1 — f-string")
check("EX1.a", safe(ex.greet, "Bilal", "Lahore"), "Assalamu alaikum Bilal, Lahore se!")
check("EX1.b", safe(ex.greet, "Saira", "Karachi"), "Assalamu alaikum Saira, Karachi se!")

group("EX2 — type conversion")
check("EX2.a", safe(ex.to_int_or_zero, "42"), 42)
check("EX2.b", safe(ex.to_int_or_zero, "  7  "), 7, "int() khud spaces handle kar leta hai")
check("EX2.c", safe(ex.to_int_or_zero, "abc"), 0, "ValueError ko except karo")
check("EX2.d", safe(ex.to_int_or_zero, ""), 0)
check("EX2.e", safe(ex.to_int_or_zero, "-5"), -5, "minus wale bhi chalne chahiyein")

group("EX3 — string cleaning")
check("EX3.a", safe(ex.clean_name, "  bilal AHMAD  "), "Bilal Ahmad")
check("EX3.b", safe(ex.clean_name, "SAIRA khan"), "Saira Khan")
check("EX3.c", safe(ex.clean_name, "ali"), "Ali")

group("EX4 — split + join")
check("EX4.a", safe(ex.initials, "bilal ahmad"), "B. A.")
check("EX4.b", safe(ex.initials, "Muhammad Ali Khan"), "M. A. K.")
check("EX4.c", safe(ex.initials, "ali"), "A.", "ek hi lafz par bhi chalna chahiye")

group("EX5 — number formatting")
check("EX5.a", safe(ex.format_price, 1234.5), "$1,234.50")
check("EX5.b", safe(ex.format_price, 99), "$99.00")
check("EX5.c", safe(ex.format_price, 1000000), "$1,000,000.00", "f\"{v:,.2f}\"")

group("EX6 — token cost")
check("EX6.a", safe(ex.token_cost, 1500, 15.0), "$0.022500")
check("EX6.b", safe(ex.token_cost, 1000000, 3.0), "$3.000000")
check("EX6.c", safe(ex.token_cost, 0, 15.0), "$0.000000")

group("EX7 — config parsing")
check("EX7.a", safe(ex.parse_config_line, "MODEL=claude-opus-4"), ("MODEL", "claude-opus-4"))
check("EX7.b", safe(ex.parse_config_line, "  API_KEY = sk-123  "), ("API_KEY", "sk-123"))
check("EX7.c", safe(ex.parse_config_line, "BROKEN"), ("BROKEN", ""))
check(
    "EX7.d",
    safe(ex.parse_config_line, "TOKEN=abc=def=="),
    ("TOKEN", "abc=def=="),
    'split("=", 1) — sirf pehle = par todo',
)

group("EX8 — truthiness")
check("EX8.a", safe(ex.describe_input, ""), "empty")
check("EX8.b", safe(ex.describe_input, "   "), "empty", "strip() ke baad check karo")
check("EX8.c", safe(ex.describe_input, "kya hai?"), "question")
check("EX8.d", safe(ex.describe_input, "hello"), "short")
check("EX8.e", safe(ex.describe_input, "a" * 60), "long")
check(
    "EX8.f",
    safe(ex.describe_input, "b" * 60 + "?"),
    "question",
    "question ka check long se PEHLE hona chahiye",
)

summary("PY01")
