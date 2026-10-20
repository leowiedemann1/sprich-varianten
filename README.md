# Sprich – 6 Landingpage-Varianten

Sechs Varianten von [sprich.ai/spricheinfach](https://www.sprich.ai/spricheinfach) für einen MVP-/Copy-Test (Lehrveranstaltung).
Variiert werden nur Headline, Copy, CTA und das Hero-Element. Logo, CI, Bedingungen und FAQ sind wortgleich zum Original.

**Live:** https://leowiedemann1.github.io/sprich-varianten/ · alle Links in [LINKS.md](LINKS.md)

| | Winkel | Interaktiv |
|---|---|---|
| v1 | Ganz simpel erklärt | – |
| v2 | Speed | Tipp-vs-Sprich-Rennen |
| v3 | Challenge | Runden füllen sich animiert |
| v4 | Marke / Tukan | Tukan-Video-Loop |
| v5 | Schmerzpunkt | Code-Kopieren-Button |
| v6 | Privatsphäre | – |

## Ändern

Copy steht in `_src/variants.py`. Danach neu bauen:

```bash
python3 _src/build.py
python3 -m http.server 8765   # → http://localhost:8765/
```

`_src/original.html` ist der SSR-Snapshot der Originalseite (Stand 2026-10-20), aus dem Nav, Inhalt und Footer übernommen werden.
Alle CTAs → echter Checkout mit `utm_source=lehrveranstaltung&utm_campaign=spricheinfach-test&utm_content=v1…v6`.
Alle Seiten sind `noindex`.
