"""Baut v1..v6 aus dem SSR-Markup der Originalseite sprich.ai/spricheinfach.

Gleich bleiben: Nav, Logo, CSS, Fonts, "So funktioniert's", Monatsziel,
Bedingungen, FAQ, Footer (wortgleich). Pro Variante getauscht: Hero + Closing-CTA.

Aufruf:  python3 _src/build.py   (aus dem Repo-Root)
"""
import re
from pathlib import Path

from variants import VARIANTS

ROOT = Path(__file__).resolve().parent.parent
ORIGINAL = (ROOT / "_src" / "original.html").read_text()
SITE = "https://www.sprich.ai"
CHECKOUT = (
    SITE + "/pricing?plan=monthly&amp;promo=SPRICHEINFACH"
    "&amp;utm_source=lehrveranstaltung&amp;utm_medium=landingpage"
    "&amp;utm_campaign=spricheinfach-test&amp;utm_content={vid}"
)

HEAD = """<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="robots" content="noindex, nofollow"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<link rel="icon" href="https://www.sprich.ai/favicon.ico"/>
<link rel="stylesheet" href="../assets/css/fonts.css"/>
<link rel="stylesheet" href="../assets/css/site.css"/>
<link rel="stylesheet" href="../assets/css/variants.css"/>
</head>"""

THEME_JS = """<script>
document.querySelector('.hp-theme-toggle')?.addEventListener('click',()=>{
  const r=document.documentElement;
  r.dataset.theme = r.dataset.theme==='dark' ? 'light' : 'dark';
});
</script>"""


def section(html, cls):
    """Return (start, end) of the <section class="cls"> ... </section> block."""
    start = html.index(f'<section class="{cls}"')
    end = html.index("</section>", start) + len("</section>")
    return start, end


def build_base():
    s = ORIGINAL
    # Body ohne Next.js-Skripte
    body = s[s.index("<body"):s.index("</body>") + len("</body>")]
    body = re.sub(r"<script[\s\S]*?</script>", "", body)
    # Kein Cookie-Banner auf dieser Seite, kein Hamburger ohne JS-Menü
    body = body.replace('<button type="button" class="consent_footer_link">Cookie-Einstellungen</button>', "")
    body = re.sub(r'<button class="h-nav-hamburger"[\s\S]*?</button>', "", body)
    # Assets lokal, restliche Links auf sprich.ai
    body = body.replace('src="/images/wordmark-', 'src="../assets/img/wordmark-')
    body = re.sub(r'href="/(?!/)', f'href="{SITE}/', body)
    html_open = re.search(r"<html[^>]*>", s).group(0)
    html_open = re.sub(r'\s*(data-theme|style)="[^"]*"', "", html_open)
    return html_open, body


def render(vid, v, html_open, body):
    checkout = CHECKOUT.format(vid=vid)
    a, b = section(body, "moneyback_hero")
    body = body[:a] + v["hero"] + body[b:]
    a, b = section(body, "moneyback_final")
    body = body[:a] + v["final"] + body[b:]
    # Alle Checkout-Links (Original + Variante) auf UTM-Link mit Variante
    body = re.sub(r'href="https://www\.sprich\.ai/pricing\?plan=monthly&amp;promo=SPRICHEINFACH"', f'href="{checkout}"', body)
    body = body.replace("{{CHECKOUT}}", checkout)
    scripts = THEME_JS + "".join(f'<script src="../assets/js/{js}" defer></script>' for js in v.get("js", []))
    body = body.replace("</body>", scripts + "</body>")
    head = HEAD.format(title=v["title"], description=v["description"])
    return f"<!DOCTYPE html>{html_open}{head}{body}</html>\n"


PAGES_URL = "https://leowiedemann1.github.io/sprich-varianten"


def strip_tags(s):
    s = s.replace("-<br/>", "-").replace("<br/>", " ").replace("&nbsp;", " ")
    return re.sub(r"<[^>]+>", "", s).strip()


def headline(v):
    return re.search(r"<h1[^>]*>([\s\S]*?)</h1>", v["hero"]).group(1)


def render_index(html_open):
    cards = []
    for vid, v in VARIANTS.items():
        cta = re.search(r'class="btn btn-accent" href="[^"]*">([^<]+)</a>', v["hero"]).group(1)
        cards.append(f"""<a class="vx-card" href="{vid}/">
<span class="kicker">{vid.upper()} · {v['name']}</span>
<h2 class="hed">{headline(v)}</h2>
<p class="vx-card-hyp"><b>Hypothese:</b> {v['hypothesis']}</p>
<p class="vx-card-cta"><span class="mono">CTA</span> {cta}</p>
<span class="vx-card-url mono">{PAGES_URL}/{vid}/</span>
</a>""")
    head = HEAD.format(title="Sprich · 6 Landingpage-Varianten", description="Übersicht der sechs Testvarianten").replace("../assets", "assets")
    return f"""<!DOCTYPE html>{html_open}{head}<body><div class="homepage moneyback vx-index">
<nav class="h-nav"><div class="wrap h-nav-inner"><a href="https://www.sprich.ai/" class="h-nav-brand" aria-label="sprich.ai"><img src="assets/img/wordmark-black.svg" alt="" width="98" height="28"/></a></div></nav>
<main><section class="moneyback_hero"><div class="wrap">
<p class="kicker moneyback_eyebrow">MVP-Test · Geld-zurück-Angebot</p>
<h1 class="hed">Eine Seite.<br/><em>Sechs Varianten.</em></h1>
<p class="moneyback_intro">Gleiches Angebot, gleiche Bedingungen, gleiche Marke. Variiert werden nur Headline, Copy, Call to Action und das Element im Hero. Original: <a class="moneyback_text-link" href="https://www.sprich.ai/spricheinfach">sprich.ai/spricheinfach</a></p>
<div class="vx-grid">{''.join(cards)}</div>
<p class="moneyback_fineprint">Alle CTAs führen zum echten Checkout mit <span class="mono">utm_content=v1…v6</span>.</p>
</div></section></main></div></body></html>
"""


def main():
    html_open, body = build_base()
    for vid, v in VARIANTS.items():
        out = ROOT / vid / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(render(vid, v, html_open, body))
        print("wrote", out.relative_to(ROOT))
    (ROOT / "index.html").write_text(render_index(html_open))
    links = "\n".join(f"- **{vid.upper()} · {v['name']}** – {strip_tags(headline(v))}  \n  {PAGES_URL}/{vid}/" for vid, v in VARIANTS.items())
    (ROOT / "LINKS.md").write_text(f"# Sprich – 6 Landingpage-Varianten\n\nÜbersicht: {PAGES_URL}/\n\n{links}\n")
    print("wrote index.html, LINKS.md")


if __name__ == "__main__":
    main()
