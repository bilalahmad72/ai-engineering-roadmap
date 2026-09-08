---
day: PY01
title: Syntax, variables, types aur strings
phase: Python Core
date: 2026-09-06
tags: [python, syntax, types, f-strings, formatting]
status: complete
---

# PY01 — Syntax, variables, types aur strings

> ✅ **Complete** — 4 topics, 5 practice files, 3 asli bugs pakre gaye.

## Topics

- [x] **Topic 1 — Variables aur types**
- [x] **Topic 2 — Type conversion**
- [x] **Topic 3 — String methods**
- [x] **Topic 4 — f-strings deep dive**

---

## Topic 1 — Variables aur types

### Syntax ka model

| Dart | Python |
|---|---|
| `{ }` se block | **indentation** (4 spaces) se block |
| line ke aakhir `;` | kuch nahi |
| `if (cond) {` | `if cond:` — colon laazmi, brackets nahi |
| `final String name = 'x';` | `name = "x"` — koi keyword, koi type nahi |
| `camelCase` | `snake_case` (constants CAPITAL) |

### Paanch bunyadi types

```python
age = 28            # int    (Python me size ki koi limit nahi)
price = 3.14        # float
name = "Bilal"      # str    ' aur " barabar hain
is_dev = True       # bool   <- CAPITAL True/False
middle = None       # None   <- Dart ka null, CAPITAL N
```

Dart wale yahan phanste hain: `true`/`false`/`null` chhote harf me likh dena.

### Type check karna

```python
type(age)                # <class 'int'>   poora type object
type(age).__name__       # 'int'           sirf naam
isinstance(age, int)     # True            check ke liye YEHI behtar hai
```

`type(x)` ko seedha print karo to `<class 'str'>` aata hai jo bhadda hai.
`.__name__` se sirf saaf naam milta hai.

> `__name__` wala pattern Python me bar bar milta hai — PY05 me
> `if __name__ == "__main__":` bhi isi khandan se hai.

### Float banane ka dhyaan

```python
hourly_rate = 20      # int
hourly_rate = 20.0    # float   <- .0 lagane se float banta hai
```

Lekin calculation me `.0` lagana zaroori nahi — `float * int` ka jawab khud hi
float hota hai:

```python
20.0 * 120     # 2400.0  (float)
```

### Format specs — f-string ka asli faida

`{variable}` ke baad **colon** lagao aur format ka rule likho:

```python
value = 2400.0

f"{value}"          # "2400.0"      raw
f"{value:.2f}"      # "2400.00"     2 decimal places
f"{value:,.2f}"     # "2,400.00"    comma + 2 decimals
f"{value:.6f}"      # "2400.000000" 6 decimals
f"{0.856:.1%}"      # "85.6%"       percentage
f"{name!r}"         # "'Bilal'"     quotes ke saath (debugging)
```

**Ye aage kyun kaam aayega:** LLM ki cost bohot chhote numbers me aati hai —
`0.0000225`. Bina `:.6f` ke Python usay `2.25e-05` print karta hai, jo kisi
client ko dikhane laayak nahi.

### Numbers me underscore

```python
1_000_000 == 1000000     # True — sirf parhne ke liye
```

Bare numbers (token limits, rates) hamesha `1_000_000` likho — ginne me aasan.

### Operator order

```python
tokens / 1_000_000 * rate     # dono barabar
tokens * rate / 1_000_000     # ye thoda behtar
```

`*` aur `/` ki priority barabar hai, bayein se dayein chalte hain. Doosra
version behtar hai: bara number pehle multiply hota hai, floating-point ki
chhoti ghaltiyon ka imkaan kam.


### Meri practice — Topic 1

`t1_variables.py`

```python
full_name = "Bilal Ahmad"
experience_years = 5
hourly_rate = 20.0
is_learning_ai = True

print(f"full_name = {full_name} (type: {type(full_name).__name__})")

hours_per_month = 120
total_earnings = hourly_rate * hours_per_month

print(
    f"{hourly_rate:.2f}/hour x {hours_per_month} hours "
    f"= {total_earnings:,.2f} per month"
)
```

```
full_name = Bilal Ahmad (type: str)
experience_years = 5 (type: int)
hourly_rate = 20.0 (type: float)
is_learning_ai = True (type: bool)
20.00/hour x 120 hours = 2,400.00 per month
```

`t1_formatting.py`

```python
input_tokens = 15432
cost_per_million = 15.0
success_rate = 0.8567

print(f"Tokens: {input_tokens:,}")
cost = input_tokens * cost_per_million / 1_000_000
print(f"Cost: ${cost:.6f}")
print(f"Success: {success_rate:.1%}")
print(f"{input_tokens:,} tokens = ${cost:.6f} ({success_rate:.1%} success)")
```

```
Tokens: 15,432
Cost: $0.231480
Success: 85.7%
15,432 tokens = $0.231480 (85.7% success)
```

---

## Topic 2 — Type conversion

### Kyun zaroori hai

**Bahar se aane wala har data string hota hai** — `.env`, API response, user
input, command line. Usay number banana apna kaam hai.

### Conversion ka behaviour

| Code | Natija |
|---|---|
| `int("42")` | `42` |
| `int("  42  ")` | `42` — spaces khud hat jati hain |
| `int("3.9")` | ❌ **ValueError** — string me decimal ho to seedha nahi |
| `int(3.9)` | `3` — **kaat deta hai**, round nahi (`round(3.9)` = 4) |
| `float("3.9")` | `3.9` |
| `int(float("3.9"))` | `3` — do qadam me |

**Asool:** string se number banana ho to hamesha `float()` — wo poore aur
decimal dono sambhalta hai. `int()` `"30.5"` par mar jata hai.

### Truthiness — asal asool

`bool(x)` ye nahi poochta "iska matlab kya hai", ye poochta hai
**"kya ye khaali hai?"**

Falsy sirf ye hain: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`.
**Baqi poori duniya truthy hai.**

```python
bool("False")   # True   <- 5 characters hain, khaali nahi
bool("0")       # True   <- ek character hai
bool("")        # False  <- khaali
bool(0)         # False
bool(5)         # True   <- number bhi truthy hota hai agar zero na ho
```

> **Har type khud batata hai ke uska "khaali" kya hai:**
> string → `""`, number → `0`, list → `[]`.
>
> Isi liye `bool(0)` False hai lekin `bool("0")` True — quotes lagate hi cheez
> number se string ban gayi.

**Asli bug:** `.env` me `DEBUG=False` likha ho aur seedha `bool()` laga dein to
jawab hamesha `True` aayega. String "False" khaali nahi hai.

### "Ye number hai?" check karne ke 3 tareeqe

| Tareeqa | Kab | Khamiyan |
|---|---|---|
| `isinstance(x, (int, float))` | jab cheez pehle se number ho sakti hai | strings par kaam nahi karta |
| `"4096".isdigit()` | saade poore positive numbers | `"30.5"` → False, `"-5"` → False |
| `try: float(x) except ValueError` | **asli project me yehi** | thoda lamba |

Verify kiya hua muqabla:

```
'4096'   -> isdigit: True,  float works: True
'30.5'   -> isdigit: False, float works: True     <- yahan farq
'claude' -> isdigit: False, float works: False
```

**EAFP** — Python ka andaz: *"Easier to Ask Forgiveness than Permission"*.
Pehle poochne ke bajaye karke dekho, ghalti ho to sambhal lo.

### Testing ka asool

Do tareeqon ka moazna karna ho to **sirf input badlo, test nahi**. Teen
values par teen alag converters (`int`/`float`/`str`) lagane se compare karne ko
kuch bachta hi nahi. Yehi asool aage evals aur prompt A/B testing me bhi hai.

Aur: `str()` kabhi `ValueError` nahi deta — har cheez par chalta hai. Jo test
har surat me `True` de, wo test nahi hai.


### Meri practice — Topic 2

`t2_conversion.py`

```python
timeout_str = "30.5"
timeout_float = float(timeout_str)     # do qadam: str -> float -> int
timeout = int(timeout_float)

# truthiness
print(bool("False"))   # True   <- 5 characters, khaali nahi
print(bool("0"))       # True   <- ek character
print(bool(""))        # False  <- khaali
print(bool(5))         # True   <- number bhi truthy, agar zero na ho

# isinstance
print(isinstance(30, int))                       # True
print(isinstance("only string", (int, float)))   # False

# isdigit vs float() — ek hi test, teen inputs
try:
    float(test_decimal)
    is_number = True
except ValueError:
    is_number = False
```

```
'4096'   -> isdigit: True,  float works: True
'30.5'   -> isdigit: False, float works: True     <- yahan farq
'claude' -> isdigit: False, float works: False
```

**Yahan mehsoos hua:** teen dafa qareeb qareeb ek jaisa `try/except` block likhna
para — sirf variable ka naam badla. **Isi takleef ka hal function hai** (PY04).

---

## Topic 3 — String methods

### Safai

```python
text.strip()      # dono taraf ki spaces, \n aur \t bhi
text.lstrip()     # sirf bayein
text.rstrip()     # sirf dayein
```

**`strip()` hamesha behtar hai** `lstrip`/`rstrip` se — input ki shakal ke
baare me kam farz karo. Agar space na ho to kuch bigarta bhi nahi.

### Case, todna, jorna

```python
"bilal ahmad".title()        # "Bilal Ahmad"     har lafz
"bilal ahmad".capitalize()   # "Bilal ahmad"     sirf pehla
"a=b=c".split("=", 1)        # ["a", "b=c"]      sirf PEHLE par todo
",".join(["a", "b"])         # "a,b"
```

**`join()` ulta hai** — separator par method chalta hai, list par nahi:
`"-".join(list)`, kabhi `list.join("-")` nahi.

**`split("=", 1)` ka doosra argument ahem hai:** API keys me `=` aa sakta hai
(base64 me aksar aata hai), is liye sirf pehle par todna chahiye.

### Dhoondna

```python
"opus" in "claude-opus-4"             # True    <- contains
"file.pdf".endswith(".pdf")           # True
"claude-x".startswith("claude")       # True
len("claude")                         # 6       <- .length NAHI
```

### Slicing

```python
word[0]     # pehla
word[-1]    # aakhri     <- Dart me ye nahi hai
word[:7]    # shuru se 7 tak
word[-4:]   # aakhri 4
```

### Immutability

Strings badalti nahi — har method **nayi** string deta hai:

```python
text.strip()             # natija kho gaya
text = text.strip()      # natija rakha
```

### Client angle — API key masking

Log me poori API key likhna bari security ghalti hai (logs share hote hain,
GitHub par chale jate hain, support tickets me paste hote hain). Sirf kinare
dikhao:

```python
f"{value[:7]}...{value[-4:]}"     # sk-ant-...z123
```

### Validation

`.env` parhne ke baad hamesha check karo, warna galti runtime par API error
banti hai:

```python
key.endswith("_API_KEY")
value.startswith("sk-ant-")
len(value) > 20
```


### Meri practice — Topic 3

`t3_strings.py`

```python
raw_line = "   ANTHROPIC_API_KEY = sk-ant-api03-xyz123   \n"

parts = raw_line.strip().split("=", 1)
key = parts[0].strip()
value = parts[1].strip()

# masking — log me poori key kabhi nahi
prefix = value[:7]
postfix = value[-4:]
print(f"Using API Key: {prefix}...{postfix}")

# validation
print(f"Key ends with _API_KEY : {key.endswith('_API_KEY')}")
print(f"value starts with sk-ant- : {value.startswith('sk-ant-')}")
print(f"value length > 20 : {len(value) > 20}")
```

```
key = 'ANTHROPIC_API_KEY'
value = 'sk-ant-api03-xyz123'
Using API Key: sk-ant-...z123
Key ends with _API_KEY : True
value starts with sk-ant- : True
value length > 20 : False
```

**Debugging ka tareeqa jo kaam aaya:** har qadam ka natija print karke dekha —
`split()` ke baad list nazar aayi aur pata chala ke uske andar ab bhi spaces
bachi hain. Bina us print ke aage ka `strip()` samajh na aata.


---

## Topic 4 — f-strings deep dive

### Andar expression bhi chalta hai

```python
f"{tokens * 2}"          # hisaab
f"{tokens / 1000:.1f}"   # hisaab + format
f"{name.upper()}"        # method call
```

Lekin bara logic f-string ke andar mat daalo — pehle variable banao, phir daalo.

### Alignment — tables ke liye

```python
f"{name:<10}"     # bayein,  width 10
f"{name:>10}"     # dayein
f"{name:^10}"     # beech me
f"{tokens:<11,}"  # align PEHLE, comma BAAD me
f"{5:03d}"        # "005"  zeros se bharo
```

### `{var=}` — debugging ka shortcut

```python
tokens = 1500
f"{tokens=}"          # "tokens=1500"        naam AUR value
f"{cost * 2 = }"      # "cost * 2 = 0.457"   spaces waise hi aate hain
```

**Sabse kaam ka:** variable ka naam khud likh kar aata hai, is liye **ghalat naam
likhne ka imkaan hi khatam** — aur wahi bug mujhe teen dafa mila tha.

### Quotes aur literal braces

```python
f"{d['key']}"        # bahar double, andar single
f"{{literal}}"       # "{literal}" — do braces = ek brace
```

### Meri practice — Topic 4

`t4_fstrings.py` — usage report table

```python
model_a, tokens_a, cost_a = "claude-opus-4", 15234, 0.2285
model_b, tokens_b, cost_b = "claude-haiku-4", 892450, 0.7139

print(f"{'MODEL':<16} {'TOKENS':<11} {'COST'}")
print(f"{model_a:<16} {tokens_a:<11,} ${cost_a:.4f}")
print(f"{model_b:<16} {tokens_b:<11,} ${cost_b:.4f}")

print(f"{tokens_a=}")
print(f"{cost_a * 2 = }")
```

```
MODEL            TOKENS      COST
claude-opus-4    15,234      $0.2285
claude-haiku-4   892,450     $0.7139
tokens_a=15234
cost_a * 2 = 0.457
```

**Seekh:** ek column me **ek hi format**. Pehli koshish me `.3f` aur `.4f` mila
diye thay — table ki seedh toot gayi aur value bhi round ho gayi (`0.7139` ->
`0.714`). Client ko cost report dikhate waqt ye ghalat hai.

### File naming — dash kabhi nahi

```python
import t4-fstrings      # SyntaxError — Python ise "t4 minus fstrings" parhta hai
import t4_fstrings      # sahi
```

Python files hamesha `snake_case`. Folder ke naam me dash chalta hai
(`PY01-syntax-types`), sirf `.py` files me nahi.

## Code

- [`t1_variables.py`](../../learning/phase-0-python-core/PY01-syntax-types/t1_variables.py)
  — variables, types, `.__name__`
- [`t1_formatting.py`](../../learning/phase-0-python-core/PY01-syntax-types/t1_formatting.py)
  — format specs
- [`t2_conversion.py`](../../learning/phase-0-python-core/PY01-syntax-types/t2_conversion.py)
  — conversion, truthiness, isdigit vs float
- [`t3_strings.py`](../../learning/phase-0-python-core/PY01-syntax-types/t3_strings.py)
  — .env parsing, key masking, validation
- [`t4_fstrings.py`](../../learning/phase-0-python-core/PY01-syntax-types/t4_fstrings.py)
  — alignment table, `{var=}` debug

## Gotchas

| # | Galti | Sahi | Kyun |
|---|---|---|---|
| 1 | `type(x)` print karna | `type(x).__name__` | pehla `<class 'str'>` deta hai |
| 2 | `f"{value}"` cost ke liye | `f"{value:.6f}"` | chhote numbers `2.25e-05` ban jate hain |
| 3 | hardcoded number (`20 * 120`) | variable se calculate | value badle to sab jagah badalna pare |
| 4 | spec ka naam badal dena (`name` vs `full_name`) | wahi naam use karo | API fields exact match maangte hain |
| 5 | **ghalat variable uth jana** | calculation ke baad ek dafa haath se verify karo | dekho neeche |

### Sabse khatarnak bug: ghalat variable

```python
# GALAT — cost_per_million ki jagah success_rate
cost = input_tokens / 1_000_000 * success_rate   # $0.013221

# SAHI
cost = input_tokens * cost_per_million / 1_000_000   # $0.231480
```

Koi error nahi. Koi red line nahi. Program kaamyabi se chala aur output ki
shakal bhi bilkul theek thi — **sirf value 17 guna ghalat thi.**

Yehi qism ka bug production me sabse zyada nuqsan karta hai, kyunki khud ko
zahir nahi karta. **Bachao:** aisi har calculation ka jawab ek dafa calculator
par check karo — 2 second lagte hain.

### Ye bug teen dafa aaya — ek hi khandan

| Kab | Kya hua | Natija |
|---|---|---|
| Topic 1 | `cost_per_million` ki jagah `success_rate` | ghalat value, pakri gayi |
| Topic 2 | `str()` par `try/except` jo kabhi fail nahi hota | hamesha `True` |
| Topic 3 | `value_length` ki jagah `value_validation` | **ittefaqan sahi** |

Teenon: **ghalat variable uth gaya aur Python ne rok-tok nahi ki.** Dart me
teenon compile par pakre jate (type mismatch), Python me chup-chaap chalte hain.

---

## Concept — `bool` asal me `int` hai (Python crash kyun nahi hua)

### Ye bug

```python
value_validation = value.startswith("sk-ant-")   # bool -> True
value_length = len(value)                        # int  -> 19

print(value_validation > 20)   # ← ghalat variable. Crash NAHI hua, False aaya
```

Sawal: `True > 20` likhna to bemani hai — bool ka number se kya muqabla?
Python ne error kyun nahi diya?

### Wajah

Python me **`bool` alag type nahi, `int` ka hi ek chhota qism (subclass) hai.**
Sirf do qeematein rakh sakta hai:

```
True  == 1
False == 0
```

Khud dekh lo:

```python
True == 1          # True
False == 0         # True
isinstance(True, int)   # True    <- bool "hai hi" int
True + True        # 2
True * 5           # 5
True > 20          # False        <- yani 1 > 20
```

To `value_validation > 20` asal me `1 > 20` bana, jo bilkul jaiz muqabla hai —
is liye koi error nahi, khamoshi se `False`.

### Dart se farq

| | Dart | Python |
|---|---|---|
| `bool` aur `int` ka rishta | bilkul alag types | `bool` **hai hi** `int` |
| `true > 20` | ❌ compile error | ✅ chal jata hai → `False` |
| `true + true` | ❌ compile error | ✅ `2` |

Dart ka compiler ye ghalti pehle hi rok deta. Python me chalti rehti hai.

### Kabhi ye faidemand bhi hai

Boolean ko gin lena Python ka mashhoor idiom hai:

```python
results = [True, False, True, True]
sum(results)        # 3    <- kitne True hain
```

Aage evals me yehi kaam aayega: "20 test cases me se kitne pass hue" — bas
`sum()` laga do.

### Bachne ka tareeqa

1. **Unused variable** sabse saaf nishani hai. Yahan `value_length` banaya gaya
   aur kabhi use nahi hua — wahin ruk kar dekhna chahiye tha.
2. **Ruff** extension ye khud pakar leta hai ("local variable assigned but never
   used").
3. Bug theek karne ke baad **aisa test chalao jo pehle fail hota tha.** Yahan:
   key ko lamba karke dekho `True` aata hai ya nahi. Sirf "ab theek lag raha hai"
   kaafi nahi — purana ghalat code bhi `False` hi de raha tha.

## Open questions

- [ ] _(likhte jao)_
