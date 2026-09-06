#!/usr/bin/env python3
"""
Progress tracker for the Flutter -> AI Engineer roadmap.

Single source of truth:
  data/curriculum/*.json  -> the static day-by-day plan (rarely changes)
  data/progress.json      -> status of every day/task (agents update this)

Everything else (README board, ROADMAP.md, PROGRESS.md, docs/ dashboard)
is GENERATED. Never hand-edit generated files.

Usage:
  python scripts/track.py status              # summary + what's running/next
  python scripts/track.py next                # next pending day, full detail
  python scripts/track.py show D05            # one day's detail
  python scripts/track.py start D05           # mark running
  python scripts/track.py done D05            # mark done (all tasks checked)
  python scripts/track.py pause D05           # running -> pending
  python scripts/track.py skip D05 "reason"   # mark skipped
  python scripts/track.py task D05 2          # toggle task #2 (1-based) of D05
  python scripts/track.py note D05 path.md    # attach a note file to a day
  python scripts/track.py log D05 "text"      # append a log line
  python scripts/track.py sync                # regenerate all output files
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Windows consoles default to cp1252 and choke on the status emoji.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, OSError):  # pragma: no cover
    pass

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM_DIR = ROOT / "data" / "curriculum"
PROGRESS_FILE = ROOT / "data" / "progress.json"
DOCS_DIR = ROOT / "docs"

STATUSES = ("pending", "running", "done", "skipped")
STATUS_EMOJI = {"pending": "⬜", "running": "🟡", "done": "✅", "skipped": "⏭️"}
STATUS_LABEL = {
    "pending": "Pending",
    "running": "Running",
    "done": "Done",
    "skipped": "Skipped",
}


# --------------------------------------------------------------------------
# load / save
# --------------------------------------------------------------------------


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load_curriculum() -> list[dict]:
    blocks = []
    for path in sorted(CURRICULUM_DIR.glob("*.json")):
        blocks.append(json.loads(path.read_text(encoding="utf-8")))
    blocks.sort(key=lambda b: b.get("order", 99))
    if not blocks:
        sys.exit(f"No curriculum files found in {CURRICULUM_DIR}")
    return blocks


def all_days(blocks: list[dict]) -> list[tuple[dict, dict]]:
    return [(b, d) for b in blocks for d in b["days"]]


def default_day_state() -> dict:
    return {
        "status": "pending",
        "started": None,
        "completed": None,
        "tasks_done": [],
        "notes": [],
        "log": [],
    }


def load_progress(blocks: list[dict]) -> dict:
    if PROGRESS_FILE.exists():
        progress = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    else:
        progress = {
            "meta": {
                "owner": "Bilal Ahmad",
                "pace": "~2 hours/day, 6 days/week",
                "started": None,
                "updated": None,
            },
            "days": {},
        }
    # backfill any newly added curriculum days
    for _block, day in all_days(blocks):
        progress["days"].setdefault(day["id"], default_day_state())
    return progress


def save_progress(progress: dict) -> None:
    progress["meta"]["updated"] = now()
    PROGRESS_FILE.write_text(
        json.dumps(progress, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def find_day(blocks: list[dict], day_id: str) -> tuple[dict, dict]:
    day_id = day_id.upper()
    for block, day in all_days(blocks):
        if day["id"] == day_id:
            return block, day
    sys.exit(f"Unknown day id: {day_id}")


# --------------------------------------------------------------------------
# stats
# --------------------------------------------------------------------------


def compute_stats(blocks: list[dict], progress: dict) -> dict:
    days = all_days(blocks)
    total = len(days)
    counts = {s: 0 for s in STATUSES}
    tasks_total = 0
    tasks_done = 0
    hours_done = 0.0
    hours_total = 0.0
    for _block, day in days:
        state = progress["days"][day["id"]]
        counts[state["status"]] += 1
        tasks_total += len(day["tasks"])
        tasks_done += len([i for i in state["tasks_done"] if i < len(day["tasks"])])
        hours_total += day.get("hours", 2)
        if state["status"] == "done":
            hours_done += day.get("hours", 2)
    finished = counts["done"] + counts["skipped"]
    return {
        "total_days": total,
        "counts": counts,
        "finished": finished,
        "percent": round(finished / total * 100) if total else 0,
        "tasks_total": tasks_total,
        "tasks_done": tasks_done,
        "hours_total": hours_total,
        "hours_done": hours_done,
        "weeks_remaining": round((total - finished) / 6, 1),
    }


def block_stats(block: dict, progress: dict) -> dict:
    total = len(block["days"])
    done = len(
        [d for d in block["days"] if progress["days"][d["id"]]["status"] in ("done", "skipped")]
    )
    running = len([d for d in block["days"] if progress["days"][d["id"]]["status"] == "running"])
    status = "done" if done == total else ("running" if running or done else "pending")
    return {
        "total": total,
        "done": done,
        "running": running,
        "percent": round(done / total * 100) if total else 0,
        "status": status,
    }


def bar(percent: int, width: int = 20) -> str:
    filled = round(percent / 100 * width)
    return "█" * filled + "░" * (width - filled)


# --------------------------------------------------------------------------
# generators
# --------------------------------------------------------------------------


def gen_readme(blocks: list[dict], progress: dict, stats: dict) -> str:
    L = []
    A = L.append
    A("# 🚀 Flutter Developer → AI/GenAI Engineer")
    A("")
    A("**Bilal Ahmad** · Senior Flutter Developer → Flutter + AI Integration Specialist")
    A("")
    A(
        "Learning in public. Ye repo ek **live progress board** hai — har din ka plan, status "
        "aur notes yahin track hote hain."
    )
    A("")
    A(
        "### 👉 [Interactive dashboard]"
        "(https://bilalahmad72.github.io/ai-engineering-roadmap/)"
    )
    A("")
    A("| | |")
    A("|---|---|")
    A(f"| **Progress** | `{bar(stats['percent'])}` **{stats['percent']}%** |")
    A(f"| **Days** | {stats['finished']} / {stats['total_days']} complete |")
    A(f"| **Tasks** | {stats['tasks_done']} / {stats['tasks_total']} checked |")
    A(f"| **Hours logged** | {stats['hours_done']:.0f} / {stats['hours_total']:.0f} h |")
    A(f"| **Pace** | {progress['meta'].get('pace', '')} |")
    A(f"| **Est. remaining** | ~{stats['weeks_remaining']} weeks |")
    A(f"| **Last updated** | {progress['meta'].get('updated') or '—'} |")
    A("")
    A(
        f"{STATUS_EMOJI['done']} Done &nbsp; {STATUS_EMOJI['running']} In progress &nbsp; "
        f"{STATUS_EMOJI['pending']} Pending &nbsp; {STATUS_EMOJI['skipped']} Skipped"
    )
    A("")

    running = [
        (b, d) for b, d in all_days(blocks) if progress["days"][d["id"]]["status"] == "running"
    ]
    nxt = next(
        ((b, d) for b, d in all_days(blocks) if progress["days"][d["id"]]["status"] == "pending"),
        None,
    )
    A("## 📍 Abhi kahan hoon")
    A("")
    if running:
        for b, d in running:
            A(f"- 🟡 **In progress:** `{d['id']}` — {d['title']}  _( {b['title']} )_")
    else:
        A("- Koi din abhi running nahi hai.")
    if nxt:
        A(f"- ⬜ **Next up:** `{nxt[1]['id']}` — {nxt[1]['title']}  _( {nxt[0]['title']} )_")
    else:
        A("- 🎉 Sab days complete!")
    A("")
    A("---")
    A("")
    A("## 🗺️ Phases")
    A("")
    A("| # | Phase | Days | Progress | Status |")
    A("|---|---|---|---|---|")
    for i, block in enumerate(blocks, 1):
        bs = block_stats(block, progress)
        first, last = block["days"][0]["id"], block["days"][-1]["id"]
        A(
            f"| {i} | **{block['title']}** | `{first}–{last}` | "
            f"`{bar(bs['percent'], 12)}` {bs['percent']}% | "
            f"{STATUS_EMOJI[bs['status']]} {STATUS_LABEL[bs['status']]} |"
        )
    A("")
    A("---")
    A("")
    A("## 📅 Day-by-day board")
    A("")
    A("_Click a phase to expand._")
    A("")
    for block in blocks:
        bs = block_stats(block, progress)
        open_attr = " open" if bs["status"] == "running" else ""
        A(f"<details{open_attr}>")
        A(
            f"<summary><b>{STATUS_EMOJI[bs['status']]} {block['title']}</b> — "
            f"{bs['done']}/{bs['total']} days ({bs['percent']}%) · "
            f"<code>{block['roadmap_ref']}</code></summary>"
        )
        A("")
        A(f"> {block['goal']}")
        A("")
        A("| Day | Topic | Tasks | Status | Notes |")
        A("|---|---|---|---|---|")
        for day in block["days"]:
            st = progress["days"][day["id"]]
            tdone = len([i for i in st["tasks_done"] if i < len(day["tasks"])])
            notes = (
                " ".join(f"[📝]({n})" for n in st["notes"]) if st["notes"] else "—"
            )
            A(
                f"| `{day['id']}` | [{day['title']}](ROADMAP.md#{anchor(day)}) | "
                f"{tdone}/{len(day['tasks'])} | {STATUS_EMOJI[st['status']]} | {notes} |"
            )
        A("")
        A("</details>")
        A("")
    A("---")
    A("")
    A("## 🤖 Is repo ke agents")
    A("")
    A("Claude Code me ye subagents available hain (`.claude/agents/`):")
    A("")
    A("| Agent | Kaam |")
    A("|---|---|")
    A(
        "| `progress-tracker` | Din start/complete karna, tasks tick karna, "
        "status batana, sab kuch regenerate + commit |"
    )
    A(
        "| `note-taker` | Aaj jo seekha uske structured notes `notes/daily/` me likhna "
        "aur day se link karna |"
    )
    A(
        "| `daily-planner` | Aaj ka plan dena, pending/running/done ka review, "
        "pace check aur schedule adjust |"
    )
    A("")
    A("Manual CLI bhi hai:")
    A("")
    A("```bash")
    A("python scripts/track.py status      # abhi kahan ho")
    A("python scripts/track.py next        # agla din")
    A("python scripts/track.py start D01   # din shuru")
    A("python scripts/track.py task D01 2  # task 2 tick")
    A("python scripts/track.py done D01    # din complete")
    A("python scripts/track.py sync        # sab files regenerate")
    A("```")
    A("")
    A("---")
    A("")
    A("## 📂 Repo structure")
    A("")
    A("```")
    A("data/curriculum/     day-by-day plan (source of truth, hand-written)")
    A("data/progress.json   status of every day + task (agents update this)")
    A("notes/daily/         per-day learning notes")
    A("scripts/track.py     tracker CLI + generator")
    A(".claude/agents/      progress-tracker, note-taker, daily-planner")
    A("docs/index.html      interactive dashboard (GitHub Pages)")
    A("ROADMAP.md           full day-by-day detail (generated)")
    A("PROGRESS.md          activity log (generated)")
    A("```")
    A("")
    A("> ⚠️ `README.md`, `ROADMAP.md`, `PROGRESS.md` aur `docs/` **generated** hain — ")
    A("> inko hath se edit mat karo, `data/` edit karke `track.py sync` chalao.")
    A("")
    A("---")
    A("")
    A(
        "<sub>Original roadmap: "
        "[flutter-to-ai-engineer-roadmap.md](flutter-to-ai-engineer-roadmap.md)</sub>"
    )
    return "\n".join(L) + "\n"


def anchor(day: dict) -> str:
    text = f"{day['id']} {day['title']}"
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    return slug


def gen_roadmap(blocks: list[dict], progress: dict, stats: dict) -> str:
    L = []
    A = L.append
    A("# 📖 Day-by-Day Roadmap")
    A("")
    A(
        f"{stats['total_days']} learning days · ~2 hours/day · 6 days/week · "
        f"≈{round(stats['total_days'] / 6)} weeks"
    )
    A("")
    A("_Generated from `data/curriculum/` — edit those files, not this one._")
    A("")
    for block in blocks:
        bs = block_stats(block, progress)
        A("---")
        A("")
        A(f"## {block['title']}")
        A("")
        A(
            f"`{block['days'][0]['id']}–{block['days'][-1]['id']}` · "
            f"roadmap ref `{block['roadmap_ref']}` · "
            f"{bs['done']}/{bs['total']} done"
        )
        A("")
        A(f"> **Goal:** {block['goal']}")
        A("")
        for day in block["days"]:
            st = progress["days"][day["id"]]
            A(f"### {day['id']} — {day['title']}")
            A("")
            A(
                f"{STATUS_EMOJI[st['status']]} **{STATUS_LABEL[st['status']]}** · "
                f"{day.get('hours', 2)}h · ref `{day['ref']}`"
            )
            A("")
            A("**Objectives**")
            A("")
            for o in day["objectives"]:
                A(f"- {o}")
            A("")
            A("**Tasks**")
            A("")
            for i, t in enumerate(day["tasks"]):
                box = "x" if i in st["tasks_done"] else " "
                A(f"- [{box}] {t}")
            A("")
            A(f"**Deliverable:** {day['deliverable']}")
            A("")
            if st["notes"]:
                A("**Notes:** " + ", ".join(f"[{Path(n).name}]({n})" for n in st["notes"]))
                A("")
    return "\n".join(L) + "\n"


def gen_progress_md(blocks: list[dict], progress: dict, stats: dict) -> str:
    L = []
    A = L.append
    A("# 📊 Progress Log")
    A("")
    A(
        f"**{stats['percent']}% complete** — {stats['finished']}/{stats['total_days']} days, "
        f"{stats['tasks_done']}/{stats['tasks_total']} tasks, "
        f"{stats['hours_done']:.0f}h logged."
    )
    A("")
    A(f"Last updated: {progress['meta'].get('updated') or '—'}")
    A("")
    A("## Status breakdown")
    A("")
    A("| Status | Days |")
    A("|---|---|")
    for s in STATUSES:
        A(f"| {STATUS_EMOJI[s]} {STATUS_LABEL[s]} | {stats['counts'][s]} |")
    A("")
    A("## Activity")
    A("")
    entries = []
    for _block, day in all_days(blocks):
        st = progress["days"][day["id"]]
        for line in st["log"]:
            entries.append((line.get("at", ""), day["id"], day["title"], line.get("text", "")))
    if not entries:
        A("_Abhi koi activity record nahi hui. `track.py start D01` se shuru karo._")
    else:
        entries.sort(reverse=True)
        A("| When | Day | Topic | Event |")
        A("|---|---|---|---|")
        for at, did, title, text in entries:
            A(f"| {at} | `{did}` | {title} | {text} |")
    A("")
    return "\n".join(L) + "\n"


def gen_dashboard(blocks: list[dict], progress: dict, stats: dict) -> str:
    payload = {
        "meta": progress["meta"],
        "stats": stats,
        "blocks": [
            {
                "title": b["title"],
                "ref": b["roadmap_ref"],
                "goal": b["goal"],
                "stats": block_stats(b, progress),
                "days": [
                    {
                        **d,
                        "state": progress["days"][d["id"]],
                    }
                    for d in b["days"]
                ],
            }
            for b in blocks
        ],
    }
    data = json.dumps(payload, ensure_ascii=False)
    return DASHBOARD_TEMPLATE.replace("__DATA__", data)


DASHBOARD_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Engineering Roadmap — Progress</title>
<style>
  :root{
    --bg:#f7f8fa; --panel:#fff; --border:#e3e6eb; --text:#14161a; --muted:#5c6470;
    --done:#16a34a; --running:#d97706; --pending:#9aa2ad; --skipped:#7c3aed; --accent:#2563eb;
  }
  @media (prefers-color-scheme: dark){
    :root{ --bg:#0e1116; --panel:#161b22; --border:#2a313b; --text:#e6e9ee; --muted:#9aa4b2;
           --done:#3fb950; --running:#e3a008; --pending:#6b7480; --skipped:#a78bfa; --accent:#58a6ff; }
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--text);
    font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;}
  .wrap{max-width:1080px;margin:0 auto;padding:32px 20px 80px}
  h1{font-size:26px;margin:0 0 4px} .sub{color:var(--muted);margin:0 0 24px}
  .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:24px}
  .card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:14px 16px}
  .card .k{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
  .card .v{font-size:24px;font-weight:650;margin-top:4px}
  .track{height:10px;background:var(--border);border-radius:999px;overflow:hidden}
  .fill{height:100%;background:var(--accent);border-radius:999px;transition:width .4s}
  .filters{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0}
  .filters button{background:var(--panel);border:1px solid var(--border);color:var(--text);
    border-radius:999px;padding:6px 14px;font-size:13px;cursor:pointer}
  .filters button.on{background:var(--accent);border-color:var(--accent);color:#fff}
  .phase{background:var(--panel);border:1px solid var(--border);border-radius:12px;margin-bottom:14px;overflow:hidden}
  .phead{display:flex;align-items:center;gap:12px;padding:14px 16px;cursor:pointer;user-select:none}
  .phead:hover{background:rgba(127,127,127,.06)}
  .phead h2{font-size:16px;margin:0;flex:1}
  .pct{font-size:13px;color:var(--muted);white-space:nowrap}
  .mini{width:90px}
  .pbody{display:none;padding:0 16px 14px;border-top:1px solid var(--border)}
  .phase.open .pbody{display:block}
  .goal{color:var(--muted);font-size:13px;margin:12px 0 14px}
  .day{border:1px solid var(--border);border-radius:10px;margin-bottom:8px}
  .dhead{display:flex;align-items:center;gap:10px;padding:10px 12px;cursor:pointer}
  .dhead:hover{background:rgba(127,127,127,.05)}
  .dot{width:9px;height:9px;border-radius:50%;flex:none}
  .id{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted)}
  .dtitle{flex:1;font-weight:520}
  .pill{font-size:11px;padding:2px 9px;border-radius:999px;border:1px solid var(--border);color:var(--muted)}
  .dbody{display:none;padding:2px 14px 14px;font-size:14px}
  .day.open .dbody{display:block}
  .lbl{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:12px 0 5px}
  ul{margin:0;padding-left:20px} li{margin:3px 0}
  li.checked{color:var(--muted);text-decoration:line-through}
  .deliv{margin-top:12px;padding:9px 12px;background:var(--bg);border-radius:8px;font-size:13px}
  a{color:var(--accent)}
  footer{margin-top:32px;color:var(--muted);font-size:12px;text-align:center}
</style>
</head>
<body>
<div class="wrap">
  <h1>Flutter Developer → AI/GenAI Engineer</h1>
  <p class="sub" id="sub"></p>
  <div class="cards" id="cards"></div>
  <div class="track"><div class="fill" id="bigbar"></div></div>
  <div class="filters" id="filters"></div>
  <div id="phases"></div>
  <footer id="foot"></footer>
</div>
<script>
const DATA = __DATA__;
const COLOR = {done:'var(--done)',running:'var(--running)',pending:'var(--pending)',skipped:'var(--skipped)'};
const LABEL = {done:'Done',running:'In progress',pending:'Pending',skipped:'Skipped'};
let filter = 'all';

const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

function render(){
  const s = DATA.stats;
  document.getElementById('sub').textContent =
    (DATA.meta.pace || '') + ' · last updated ' + (DATA.meta.updated || '—');
  document.getElementById('cards').innerHTML = [
    ['Complete', s.percent + '%'],
    ['Days', s.finished + ' / ' + s.total_days],
    ['Tasks', s.tasks_done + ' / ' + s.tasks_total],
    ['Hours', Math.round(s.hours_done) + ' / ' + Math.round(s.hours_total)],
    ['Weeks left', '~' + s.weeks_remaining]
  ].map(([k,v]) => '<div class="card"><div class="k">'+k+'</div><div class="v">'+v+'</div></div>').join('');
  document.getElementById('bigbar').style.width = s.percent + '%';

  document.getElementById('filters').innerHTML =
    ['all','running','pending','done','skipped'].map(f =>
      '<button data-f="'+f+'" class="'+(f===filter?'on':'')+'">'+
      (f==='all'?'All':LABEL[f])+
      (f==='all'?' ('+s.total_days+')':' ('+(s.counts[f]||0)+')')+'</button>').join('');

  document.getElementById('phases').innerHTML = DATA.blocks.map((b,bi) => {
    const days = b.days.filter(d => filter==='all' || d.state.status===filter);
    if(!days.length) return '';
    const open = (filter!=='all' || b.stats.status==='running') ? ' open' : '';
    return '<div class="phase'+open+'" data-b="'+bi+'">'
      + '<div class="phead"><span class="dot" style="background:'+COLOR[b.stats.status]+'"></span>'
      + '<h2>'+esc(b.title)+'</h2>'
      + '<div class="track mini"><div class="fill" style="width:'+b.stats.percent+'%"></div></div>'
      + '<span class="pct">'+b.stats.done+'/'+b.stats.total+'</span></div>'
      + '<div class="pbody"><div class="goal">'+esc(b.goal)+'</div>'
      + days.map(d => dayHtml(d)).join('')
      + '</div></div>';
  }).join('');

  document.querySelectorAll('.phead').forEach(el =>
    el.onclick = () => el.parentElement.classList.toggle('open'));
  document.querySelectorAll('.dhead').forEach(el =>
    el.onclick = () => el.parentElement.classList.toggle('open'));
  document.querySelectorAll('.filters button').forEach(el =>
    el.onclick = () => { filter = el.dataset.f; render(); });
}

function dayHtml(d){
  const st = d.state.status;
  return '<div class="day">'
    + '<div class="dhead"><span class="dot" style="background:'+COLOR[st]+'"></span>'
    + '<span class="id">'+d.id+'</span><span class="dtitle">'+esc(d.title)+'</span>'
    + '<span class="pill">'+d.state.tasks_done.length+'/'+d.tasks.length+' tasks</span>'
    + '<span class="pill">'+LABEL[st]+'</span></div>'
    + '<div class="dbody">'
    + '<div class="lbl">Objectives</div><ul>'
    + d.objectives.map(o => '<li>'+esc(o)+'</li>').join('') + '</ul>'
    + '<div class="lbl">Tasks</div><ul>'
    + d.tasks.map((t,i) => '<li class="'+(d.state.tasks_done.includes(i)?'checked':'')+'">'+esc(t)+'</li>').join('')
    + '</ul>'
    + '<div class="deliv"><b>Deliverable:</b> '+esc(d.deliverable)+'</div>'
    + (d.state.notes.length
        ? '<div class="lbl">Notes</div><ul>' + d.state.notes.map(n =>
            '<li><a href="../'+n+'">'+esc(n.split('/').pop())+'</a></li>').join('') + '</ul>'
        : '')
    + '</div></div>';
}
render();
document.getElementById('foot').textContent =
  'Generated by scripts/track.py — do not edit by hand.';
</script>
</body>
</html>
"""


def sync(blocks: list[dict], progress: dict) -> dict:
    stats = compute_stats(blocks, progress)
    (ROOT / "README.md").write_text(gen_readme(blocks, progress, stats), encoding="utf-8")
    (ROOT / "ROADMAP.md").write_text(gen_roadmap(blocks, progress, stats), encoding="utf-8")
    (ROOT / "PROGRESS.md").write_text(gen_progress_md(blocks, progress, stats), encoding="utf-8")
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "index.html").write_text(gen_dashboard(blocks, progress, stats), encoding="utf-8")
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")
    return stats


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------


def add_log(state: dict, text: str) -> None:
    state["log"].append({"at": now(), "text": text})


def print_day(block: dict, day: dict, state: dict) -> None:
    print(f"\n{STATUS_EMOJI[state['status']]} {day['id']} — {day['title']}")
    print(f"   Phase: {block['title']} · {day.get('hours', 2)}h · ref {day['ref']}")
    print(f"   Status: {STATUS_LABEL[state['status']]}")
    print("\n   Objectives:")
    for o in day["objectives"]:
        print(f"     • {o}")
    print("\n   Tasks:")
    for i, t in enumerate(day["tasks"], 1):
        box = "x" if (i - 1) in state["tasks_done"] else " "
        print(f"     [{box}] {i}. {t}")
    print(f"\n   Deliverable: {day['deliverable']}")
    if state["notes"]:
        print("   Notes: " + ", ".join(state["notes"]))
    print()


def main() -> None:
    argv = sys.argv[1:]
    cmd = argv[0] if argv else "status"
    blocks = load_curriculum()
    progress = load_progress(blocks)

    if cmd == "sync":
        stats = sync(blocks, progress)
        save_progress(progress)
        print(f"Synced. {stats['percent']}% — {stats['finished']}/{stats['total_days']} days.")
        return

    if cmd == "status":
        stats = compute_stats(blocks, progress)
        print(f"\n  {bar(stats['percent'])}  {stats['percent']}%")
        print(
            f"  {stats['finished']}/{stats['total_days']} days · "
            f"{stats['tasks_done']}/{stats['tasks_total']} tasks · "
            f"{stats['hours_done']:.0f}h logged · ~{stats['weeks_remaining']} weeks left\n"
        )
        for s in STATUSES:
            print(f"  {STATUS_EMOJI[s]} {STATUS_LABEL[s]:<9} {stats['counts'][s]}")
        print()
        for block in blocks:
            bs = block_stats(block, progress)
            print(
                f"  {STATUS_EMOJI[bs['status']]} {block['title']:<42} "
                f"{bar(bs['percent'], 10)} {bs['done']}/{bs['total']}"
            )
        run = [(b, d) for b, d in all_days(blocks) if progress["days"][d["id"]]["status"] == "running"]
        print()
        if run:
            for b, d in run:
                print(f"  🟡 Running: {d['id']} — {d['title']}")
        nxt = next(
            ((b, d) for b, d in all_days(blocks) if progress["days"][d["id"]]["status"] == "pending"),
            None,
        )
        if nxt:
            print(f"  ⬜ Next:    {nxt[1]['id']} — {nxt[1]['title']}")
        print()
        return

    if cmd == "next":
        nxt = next(
            ((b, d) for b, d in all_days(blocks) if progress["days"][d["id"]]["status"] == "pending"),
            None,
        )
        if not nxt:
            print("Sab days complete! 🎉")
            return
        print_day(nxt[0], nxt[1], progress["days"][nxt[1]["id"]])
        return

    if cmd == "show":
        block, day = find_day(blocks, argv[1])
        print_day(block, day, progress["days"][day["id"]])
        return

    # mutating commands below
    if cmd in ("start", "done", "pause", "skip", "task", "note", "log"):
        block, day = find_day(blocks, argv[1])
        state = progress["days"][day["id"]]

        if cmd == "start":
            state["status"] = "running"
            state["started"] = state["started"] or today()
            if not progress["meta"].get("started"):
                progress["meta"]["started"] = today()
            add_log(state, "Started")
            print(f"🟡 {day['id']} started — {day['title']}")

        elif cmd == "done":
            state["status"] = "done"
            state["completed"] = today()
            state["started"] = state["started"] or today()
            state["tasks_done"] = list(range(len(day["tasks"])))
            add_log(state, "Completed")
            print(f"✅ {day['id']} done — {day['title']}")

        elif cmd == "pause":
            state["status"] = "pending"
            add_log(state, "Paused")
            print(f"⬜ {day['id']} paused")

        elif cmd == "skip":
            state["status"] = "skipped"
            state["completed"] = today()
            reason = argv[2] if len(argv) > 2 else "no reason given"
            add_log(state, f"Skipped — {reason}")
            print(f"⏭️  {day['id']} skipped ({reason})")

        elif cmd == "task":
            idx = int(argv[2]) - 1
            if not 0 <= idx < len(day["tasks"]):
                sys.exit(f"{day['id']} has {len(day['tasks'])} tasks, got {argv[2]}")
            if idx in state["tasks_done"]:
                state["tasks_done"].remove(idx)
                add_log(state, f"Unchecked task {idx + 1}")
                print(f"[ ] {day['id']}.{idx + 1} — {day['tasks'][idx]}")
            else:
                state["tasks_done"] = sorted(state["tasks_done"] + [idx])
                add_log(state, f"Checked task {idx + 1}")
                print(f"[x] {day['id']}.{idx + 1} — {day['tasks'][idx]}")
            if state["status"] == "pending" and state["tasks_done"]:
                state["status"] = "running"
                state["started"] = state["started"] or today()
            if len(state["tasks_done"]) == len(day["tasks"]) and state["status"] != "done":
                print(f"    ℹ️  Saare tasks tick ho gaye — `track.py done {day['id']}` chalao.")

        elif cmd == "note":
            path = argv[2].replace("\\", "/")
            if path not in state["notes"]:
                state["notes"].append(path)
            add_log(state, f"Note added: {path}")
            print(f"📝 {day['id']} → {path}")

        elif cmd == "log":
            add_log(state, argv[2])
            print(f"🗒️  {day['id']}: {argv[2]}")

        stats = sync(blocks, progress)
        save_progress(progress)
        print(f"   Overall: {stats['percent']}% ({stats['finished']}/{stats['total_days']} days)")
        return

    print(__doc__)


if __name__ == "__main__":
    main()
