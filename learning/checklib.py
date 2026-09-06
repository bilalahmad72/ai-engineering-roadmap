"""
Chhoti test library — har din ki practice isay use karti hai.

Ye khud ek achhi Python file hai parhne ke liye: functions, default arguments,
f-strings, try/except aur list handling sab isme hain. PY05 (modules) ke baad
tum ise poori tarah samajh sakoge.

Use:
    from checklib import check, safe, summary

    check("EX1.a", safe(my_func, "input"), "expected")
    summary()
"""

from __future__ import annotations

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, OSError):
    pass

_PASS: list[str] = []
_FAIL: list[str] = []


def header(title: str) -> None:
    """Test run ke shuru me heading print karta hai."""
    print("\n" + "=" * 64)
    print(f"  {title}")
    print("=" * 64)


def group(name: str) -> None:
    """Ek exercise group ka title."""
    print(f"\n{name}")


def safe(fn, *args, **kwargs):
    """
    Function ko chalata hai. Agar exception aaye to crash karne ke bajaye
    ek readable string return karta hai — taake ek fail se poora test run
    na ruk jaye.
    """
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return f"<{type(e).__name__}: {e}>"


def check(name: str, got, expected, hint: str = "") -> bool:
    """Ek assertion. Pass/fail print karta hai aur result yaad rakhta hai."""
    if got == expected and type(got) is type(expected):
        _PASS.append(name)
        print(f"  PASS  {name}")
        return True

    _FAIL.append(name)
    print(f"  FAIL  {name}")
    print(f"        expected : {expected!r}   ({type(expected).__name__})")
    print(f"        got      : {got!r}   ({type(got).__name__})")
    if hint:
        print(f"        hint     : {hint}")
    return False


def summary(day: str = "") -> None:
    """Aakhir me total batata hai aur exit code set karta hai."""
    total = len(_PASS) + len(_FAIL)
    print("\n" + "=" * 64)
    print(f"  {len(_PASS)}/{total} PASS")
    if _FAIL:
        print(f"  Baqi hain: {', '.join(_FAIL)}")
        print("\n  Sirf inhe theek karo, phir dobara chalao.")
    else:
        msg = f"  Sab green! {day} practice complete." if day else "  Sab green!"
        print(f"\n{msg}")
        print("  Ab apna code bhejo — review karta hoon.")
    print("=" * 64 + "\n")
    sys.exit(1 if _FAIL else 0)
