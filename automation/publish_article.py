#!/usr/bin/env python3
"""Publie automatiquement le prochain article de la file d'attente.
Lancé par GitHub Actions le 1er et le 15 de chaque mois."""
import json, re, datetime, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "automation" / "articles_queue.json"

MOIS = ["", "janvier","février","mars","avril","mai","juin","juillet",
        "août","septembre","octobre","novembre","décembre"]

def fr_date(d): return f"{d.day} {MOIS[d.month]} {d.year}"

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em">'
         '<path d="M5 12h14M12 5l7 7-7 7"/></svg>')

def template():
    src = (ROOT / "contact.html").read_text(encoding="utf-8")
    head = src[:src.index("<main>")]
    footer = src[src.index("<footer"):]
    # menu : Blog actif
    head = head.replace('<a href="contact.html" class="is-active">Contact</a>',
                        '<a href="contact.html">Contact</a>')
    head = head.replace('<a href="blog.html">Blog</a>',
                        '<a href="blog.html" class="is-active">Blog</a>')
    return head, footer

def build_page(a, date_str):
    head, footer = template()
    head = re.sub(r'<title>.*?</title>', f"<title>{a['title']} — Blog PNBS</title>", head)
    head = re.sub(r'<meta name="description"[^>]*>',
                  f'<meta name="description" content="{a["desc"]}">', head)
    body = (
      '<section class="page-hero"><div class="container">'
      f'<span class="eyebrow">{a["cat"]}</span><h1>{a["title"]}</h1>'
      f'<p>{a["lead"]}</p><span class="underline-gold"></span></div></section>'
      '<section class="section"><div class="container"><div class="article">'
      f'<p class="article-meta">📅 {date_str} · {a["cat"]}</p>'
      f'{a["body"]}'
      '<div class="article-cta"><h3>Envie de vous lancer en alternance ?</h3>'
      '<p>Nos conseillers vous accompagnent gratuitement dans votre projet et la recherche d\'entreprise.</p>'
      f'<a class="btn btn--primary" href="contact.html">Déposer ma candidature {ARROW}</a></div>'
      '<p style="margin-top:30px"><a href="blog.html">← Retour au blog</a></p>'
      '</div></div></section>')
    return head + "<main>\n" + body + "\n</main>\n" + footer

def card(a, date_str):
    return (f'<a class="post-card" href="{a["slug"]}.html">'
            f'<div class="post-card__media"><img src="{a["img"]}" alt="{a["title"]}" loading="lazy">'
            f'<span class="post-tag">{a["cat"]}</span></div>'
            f'<div class="post-card__body"><p class="post-date">{date_str}</p>'
            f'<h3>{a["title"]}</h3><p>{a["lead"]}</p>'
            f'<span class="post-more">Lire l\'article {ARROW}</span></div></a>')

def main():
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    nxt = next((a for a in queue if not a["published"]), None)
    if not nxt:
        print("File d'attente vide — rien à publier."); return 0

    today = datetime.date.today()
    date_str = fr_date(today)

    # 1) page article
    (ROOT / f"{nxt['slug']}.html").write_text(build_page(nxt, date_str), encoding="utf-8")

    # 2) insérer la carte en tête de la grille du blog
    blog = (ROOT / "blog.html").read_text(encoding="utf-8")
    marker = "<!--AUTO-INSERT-->"
    if marker in blog and f'href="{nxt["slug"]}.html"' not in blog:
        blog = blog.replace(marker, marker + "\n" + card(nxt, date_str), 1)
        (ROOT / "blog.html").write_text(blog, encoding="utf-8")

    # 3) marquer comme publié
    nxt["published"] = True
    nxt["date"] = date_str
    QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Article publié : {nxt['slug']} ({date_str})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
