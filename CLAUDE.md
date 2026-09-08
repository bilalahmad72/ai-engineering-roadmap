# CLAUDE.md

Bilal Ahmad ka **Flutter Developer → AI/GenAI Engineer** learning repo.
Ye ek learning tracker hai, product codebase nahi.

## Architecture

Ek hi asool: **data source of truth hai, baaqi sab generated hai.**

```
data/curriculum/*.json   78-day plan — hand-written, rarely changes
data/progress.json       har din/task ka status — sirf track.py isay likhta hai
        ↓  python scripts/track.py sync
README.md                                 progress board
ROADMAP.md                                poora day-by-day detail
PROGRESS.md                               activity log
docs/index.html                           interactive dashboard (GitHub Pages)
learning/<phase-folder>/README.md         har phase ka apna index
```

Har curriculum block me ek `folder` field hai (jaise `phase-0-python-core`).
Us folder me `README.md` khud generate hota hai — usme phase ka goal, saare din,
tasks, notes ke links, aur **practice files ki auto-discovered list** hoti hai
(`learning/<folder>/<DAYID>-*/**.py`). GitHub par folder kholte hi poora phase
ek jagah nazar aata hai.

## Kabhi mat karo

- `README.md`, `ROADMAP.md`, `PROGRESS.md`, `docs/index.html` ko hath se edit
  karna — ye har sync par overwrite ho jate hain.
- `data/progress.json` ko hath se edit karna — `scripts/track.py` use karo.
- Progress khud se maan lena. Sirf woh record karo jo user ne actually bataya.

## Agents

| Agent | Kab |
|---|---|
| `progress-tracker` | Din start/done, task tick, status poochna, commit |
| `note-taker` | Session ke baad `notes/daily/` me structured notes |
| `daily-planner` | Aaj ka plan, pace review, schedule adjust |

`daily-planner` read-only hai. State sirf `progress-tracker` badalta hai.

## Tracker CLI

```bash
python scripts/track.py status | next | show D05
python scripts/track.py start D05 | done D05 | pause D05 | skip D05 "reason"
python scripts/track.py task D05 2      # toggle task 2 (1-based)
python scripts/track.py note D05 notes/daily/D05-tokens.md
python scripts/track.py log D05 "text"
python scripts/track.py sync
```

Har mutating command khud hi sab kuch regenerate kar deti hai — `sync` alag se
chalane ki zaroorat nahi.

## Curriculum badalna ho to

`data/curriculum/*.json` edit karo, phir `python scripts/track.py sync`.
Naye days automatically `pending` state ke saath `progress.json` me aa jate hain
(purani progress safe rehti hai). Day IDs (`D01`…`D66`) **kabhi reuse mat karo** —
notes aur log unhi se linked hain.

## Teaching method (sabse zaroori rule)

**Kabhi bhi mukammal working script likh kar mat do jo Bilal sirf chala kar
output paste kare.** Ye passive hai — samajh aa jata hai, yaad kuch nahi rehta.

Har chhote topic ka loop (classic tutoring, purane andaz me):

1. **Concept parhao** — chhota, misalon ke saath, Flutter/Dart analogy ke saath.
2. **Note karo** — `notes/daily/` me foran save. Note me **dono** hone chahiyein:
   - **Concept** jo maine parhaya (misalein, Dart analogy, gotchas)
   - **"Meri practice"** section — Bilal ka **apna likha code + asli output**,
     aur us topic me jo bug ya seekh mili
3. **5-6 use cases** — grip banane ke liye. Lekin **EK WAQT ME EK SAWAL**.
4. **Woh code + output bhejte hain** → review (kya theek, kya behtar, **kyun**)
   → phir **agla** sawal.
5. Topic par grip ban jaye to agla topic.

### 🔴 EK SAWAL EK BAAR

Exercises ki poori list ek saath **mat** do. Ek file me 8 TODO functions dump
karna Bilal ke liye kaam nahi karta — woh overwhelm ho jate hain aur pata nahi
chalta ke seekh kya rahe hain. Ek sawal → jawab → review → agla sawal.

Solution tabhi likho jab woh khud koshish kar chuke hon, ya explicitly maangein
("bata do"). Error aana **acchi baat hai** — usay `notes/ISSUES.md` me record karo.

Tracker (`scripts/track.py`) sirf **peeche peeche** record karta rahe — usay
beech me la kar flow mat toro.

Solution tabhi likho jab woh khud koshish kar chuke hon, ya explicitly maangein
("bata do"). Error aana **acchi baat hai** — usay `notes/ISSUES.md` me record karo.

Reference code (jo maine likha) sirf tab jab woh apna version likh chuke hon —
comparison ke liye, shuru me nahi.

## Zabaan

User Roman Urdu me baat karta hai. Jawab Roman Urdu me, technical terms English me.
Code aur code comments English me. Notes bhi isi mix me.

## Context

- Bilal Senior Flutter Developer hai — Dart, Riverpod/BLoC, Dio, Postgres/Supabase
  already aata hai. Ye cheezein dobara mat samjhao; naye concepts ko inse jodo.
- Maqsad: Upwork/Fiverr par AI integration gigs. Har topic ka "client angle"
  matter karta hai.
- Deep math, PyTorch, model training aur fine-tuning is roadmap ka hissa NAHI hai.
