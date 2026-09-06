"""
D01 — Dart/Flutter se Python mapping.

Ye file parhne ke liye nahi, CHALANE ke liye hai. Har section me pehle
"PREDICT" comment hai — chalane se pehle andaza lagao output kya hoga,
phir chala kar dekho sahi tha ya nahi. Jahan galat ho, wahi asli seekh hai.

Run:  python learning/phase-0-foundations/D01-python-setup/dart_to_python.py
"""

from dataclasses import dataclass


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n  {title}\n{'=' * 60}")


# ---------------------------------------------------------------------------
section("1. Variables & types")
# ---------------------------------------------------------------------------
# Dart:   final String name = 'Bilal';  var age = 28;
# Python: koi final/var/let nahi. Type hints OPTIONAL hain aur runtime par
#         enforce NAHI hote — sirf editor/linter ke liye hain.

name: str = "Bilal"          # type hint (documentation jaisa)
age = 28                     # bina hint ke bhi bilkul theek
is_flutter_dev = True        # Dart: bool isX = true;  (Python me True/False capital)

# PREDICT: kya ye line error degi?
age = "ab main string hoon"  # Dart me compile error. Python me? ...

print(f"{name} | {age} | {is_flutter_dev}")
print("Type hint runtime par enforce nahi hota — isliye upar wali line chal gayi.")

# Dart string interpolation: 'Hello $name'  ->  Python f-string: f"Hello {name}"
print(f"f-string = Dart ka $interpolation: Hello {name}, next year {28 + 1}")


# ---------------------------------------------------------------------------
section("2. Collections")
# ---------------------------------------------------------------------------
# Dart List<String>  -> Python list
# Dart Map<String,x> -> Python dict
# Dart Set<String>   -> Python set
# Python me ek extra hai: tuple (immutable list)

skills = ["Flutter", "Dart", "Postgres"]        # list  (mutable)
profile = {"name": "Bilal", "years": 5}         # dict
unique_tags = {"ai", "flutter", "ai"}           # set   (duplicates khud hat jate hain)
coords = (10, 20)                               # tuple (immutable — badal nahi sakte)

skills.append("Python")                          # Dart: skills.add(...)
print("list :", skills)
print("dict :", profile, "| name =", profile["name"])
print("set  :", unique_tags, "<- 'ai' sirf ek dafa")
print("tuple:", coords)

# Dart:   skills.map((s) => s.toUpperCase()).toList()
# Python: list comprehension — ye Python ka sabse zyada use hone wala idiom hai
upper = [s.upper() for s in skills]
print("comprehension (Dart .map ka jawab):", upper)

# Dart:   skills.where((s) => s.length > 4).toList()
long_skills = [s for s in skills if len(s) > 4]
print("filter (Dart .where ka jawab):", long_skills)


# ---------------------------------------------------------------------------
section("3. Null safety — sabse bara farq")
# ---------------------------------------------------------------------------
# Dart me null safety COMPILE TIME par hai: String? name; name!.length
# Python me None hamesha allowed hai. Koi compiler nahi rokta.
# Isi liye Python me defensive checks khud likhne parte hain.

middle_name: str | None = None      # Dart: String? middleName;

# Dart:   final display = middleName ?? 'N/A';
display = middle_name or "N/A"       # ?? ka qareeb tareen jawab
print("?? equivalent:", display)

# SAVDHAAN: `or` falsy values par bhi chalta hai (0, "", [], False sab falsy hain)
count = 0
print("BUG:", count or 99, "<- 0 falsy hai, is liye 99 aa gaya (Dart me 0 aata)")
print("FIX:", count if count is not None else 99, "<- yeh sahi ?? equivalent hai")

# Dart:   profile?.name          -> Python me koi ?. operator NAHI hai
print("?. equivalent:", profile.get("email", "no email"), "<- dict.get(key, default)")


# ---------------------------------------------------------------------------
section("4. Classes")
# ---------------------------------------------------------------------------
# Dart:
#   class User {
#     final String name;
#     final int age;
#     User({required this.name, required this.age});
#   }


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name          # `self` = Dart ka `this` (lekin likhna LAAZMI hai)
        self.age = age

    def greet(self) -> str:
        return f"Hi {self.name}"


u = User(name="Bilal", age=28)
print("normal class:", u.greet())


# Behtar tareeqa — @dataclass. Ye Dart ke Freezed/Equatable jaisa hai:
# __init__, __repr__ aur == khud bana deta hai.
@dataclass
class Skill:
    name: str
    level: int = 1                # default value (Dart: {this.level = 1})


s1 = Skill("Flutter", 5)
s2 = Skill("Flutter", 5)
print("dataclass repr :", s1, "<- print karne par readable (Dart me toString likhna parta)")
print("dataclass ==   :", s1 == s2, "<- value equality free milti hai (Equatable jaisa)")


# ---------------------------------------------------------------------------
section("5. Functions & named parameters")
# ---------------------------------------------------------------------------
# Dart: String greet(String name, {String greeting = 'Hello'}) => '$greeting $name';


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting} {name}"


print(greet("Bilal"))                        # positional
print(greet("Bilal", greeting="Assalamu"))   # named — Python me koi bhi param named ban sakta hai

# Dart me {} lagana parta hai named ke liye. Python me har param dono tarah kaam karta hai.


# ---------------------------------------------------------------------------
section("6. Async ka jhalak (poora D02 me)")
# ---------------------------------------------------------------------------
# Dart:   Future<String> fetch() async { ... }      await fetch();
# Python: async def fetch() -> str: ...             await fetch()
#
# Concept 95% same hai. Ek bara farq:
#   Dart me async function call karte hi chalna shuru ho jata hai.
#   Python me coroutine tab tak nahi chalta jab tak await ya event loop na mile.


async def fetch_data() -> str:
    return "data"


coro = fetch_data()          # PREDICT: kya ye "data" return karega?
print("bina await:", coro, "<- coroutine object hai, result nahi!")
coro.close()                 # warning se bachne ke liye

print("\nDart Future.wait  ->  Python asyncio.gather   (D02 me hands-on)")

print("\n" + "=" * 60)
print("  Ho gaya. Ab jo predictions galat thay, unhe note me likho.")
print("=" * 60)
