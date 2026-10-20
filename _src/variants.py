"""Copy der 6 Varianten. Nur Hero + Closing-CTA unterscheiden sich.

Regel: nie "gratis", "kostenlos" oder "0 €" – man zahlt regulär und
bekommt qualifizierte Monatszahlungen erstattet.
{{CHECKOUT}} wird beim Build durch den UTM-Checkout-Link ersetzt.
"""

FINEPRINT = '<p class="moneyback_fineprint">Mit Code <strong class="mono">SPRICHEINFACH</strong> · Pro monatlich</p>'
FINAL_FINEPRINT = '<p class="moneyback_fineprint">Pro monatlich · Bis zu drei Monatszahlungen zurück bei erfüllten Voraussetzungen</p>'


def left(eyebrow, h1, intro, cta):
    return f"""<div><p class="kicker moneyback_eyebrow">{eyebrow}</p><h1 class="hed">{h1}</h1><p class="moneyback_intro">{intro}</p><div class="moneyback_actions"><a class="btn btn-accent" href="{{{{CHECKOUT}}}}">{cta}</a><a class="moneyback_text-link" href="#so-funktionierts">So funktioniert’s <span aria-hidden="true">↓</span></a></div>{FINEPRINT}</div>"""


def hero(left_html, right_html, extra_cls=""):
    return f'<section class="moneyback_hero {extra_cls}"><div class="wrap moneyback_hero-grid">{left_html}{right_html}</div></section>'


def final(eyebrow, h2, cta):
    return f'<section class="moneyback_final"><div class="wrap"><p class="kicker moneyback_eyebrow">{eyebrow}</p><h2 class="hed">{h2}</h2><a href="{{{{CHECKOUT}}}}" class="btn btn-accent">{cta}</a>{FINAL_FINEPRINT}</div></section>'


def code_box(copy_button=False):
    btn = '<button type="button" class="vx-copy" data-copy="SPRICHEINFACH">Kopieren</button>' if copy_button else ""
    return f'<div class="moneyback_receipt-code"><span class="kicker">Dein Code im Checkout</span><strong class="mono">SPRICHEINFACH</strong>{btn}</div>'


# ── V1: ganz simpel erklärt ────────────────────────────────────────────────
V1_RIGHT = """<div class="vx-simple" aria-label="So einfach geht's">
<p class="kicker">So einfach geht’s</p>
<ol>
<li><span class="vx-n mono">1</span><div><strong>Code einlösen.</strong><span>Pro monatlich wählen, <b class="mono">SPRICHEINFACH</b> ist schon drin.</span></div></li>
<li><span class="vx-n mono">2</span><div><strong>Sprechen statt tippen.</strong><span>10.000 Wörter im Monat – Mails, Notizen, Nachrichten.</span></div></li>
<li><span class="vx-n mono">3</span><div><strong>Geld zurück.</strong><span>Für jeden geschafften Monat. Bis zu drei Mal.</span></div></li>
</ol>
</div>"""

# ── V2: Tipp-vs-Sprich-Rennen ──────────────────────────────────────────────
V2_RIGHT = """<div class="moneyback_receipt vx-race" data-race>
<div class="moneyback_receipt-top"><span class="kicker">Tippen gegen Sprechen</span><span class="mono vx-race-clock" data-clock>0:00</span></div>
<p class="vx-race-task">Dieselbe E-Mail, 67 Wörter. Wer ist zuerst fertig?</p>
<div class="vx-lane" data-lane="type">
  <div class="vx-lane-head"><span>⌨️ Tippen <small class="mono">~40 Wörter/Min.</small></span><span class="mono" data-count>0</span></div>
  <div class="vx-bar"><i data-bar></i></div>
  <p class="vx-lane-text" data-text></p>
</div>
<div class="vx-lane vx-lane--sprich" data-lane="speak">
  <div class="vx-lane-head"><span>🎙️ Sprich <small class="mono">~150 Wörter/Min.</small></span><span class="mono" data-count>0</span></div>
  <div class="vx-bar"><i data-bar></i></div>
  <p class="vx-lane-text" data-text></p>
</div>
<p class="vx-race-result" data-result aria-live="polite"></p>
<button type="button" class="btn btn-accent vx-race-start" data-start>Rennen starten</button>
</div>"""

# ── V3: Challenge mit drei Runden ──────────────────────────────────────────
V3_RIGHT = """<div class="moneyback_receipt vx-challenge" data-challenge>
<div class="moneyback_receipt-top"><span class="kicker">Deine Challenge · Beispiel</span><span aria-hidden="true">↗</span></div>
<div class="vx-rounds">
""" + "".join(
    f"""<div class="vx-round" data-round>
  <div class="vx-round-head"><span>Runde {i}<small> · Monat {i}</small></span><span class="mono"><span data-count>0</span> / 10.000</span></div>
  <div class="vx-bar"><i data-bar></i></div>
  <span class="vx-stamp mono">erstattet ✓</span>
</div>""" for i in (1, 2, 3)
) + """</div>
<div class="moneyback_receipt-rule"></div>
<p class="vx-challenge-total"><span>Drei Runden geschafft</span><strong data-total>0 von 3 Monaten zurück</strong></p>
<a class="btn btn-accent moneyback_redeem vx-full" href="{{CHECKOUT}}">Challenge annehmen</a>
</div>"""

# ── V4: Tukan ──────────────────────────────────────────────────────────────
V4_RIGHT = """<div class="vx-toucan" aria-hidden="true">
<video autoplay muted loop playsinline preload="auto" poster="../assets/video/toucan-hero-poster.jpg">
<source src="../assets/video/toucan-hero.webm" type="video/webm"/>
<source src="../assets/video/toucan-hero.mp4" type="video/mp4"/>
</video>
</div>"""

# ── V5: Schmerzpunkt, Original-Card mit Copy-Button ────────────────────────
V5_RIGHT = f"""<div class="moneyback_receipt"><div class="moneyback_receipt-top"><span class="kicker">Dein Feierabend zahlt sich aus</span><span aria-hidden="true">↗</span></div><p class="moneyback_big-number">Bis zu <strong>3</strong></p><p class="moneyback_receipt-title">Monatszahlungen zurück.</p><div class="moneyback_receipt-rule"></div><div class="moneyback_redemption">{code_box(copy_button=True)}<div class="moneyback_receipt-actions"><a class="btn btn-accent moneyback_redeem" href="{{{{CHECKOUT}}}}">Angebot einlösen</a><p class="moneyback_fineprint moneyback_redeem-note">Monatsabo und Code werden für dich vorausgewählt.</p></div></div></div>"""

# ── V6: Privatsphäre ───────────────────────────────────────────────────────
V6_RIGHT = f"""<div class="moneyback_receipt vx-privacy">
<div class="moneyback_receipt-top"><span class="kicker">Wir zählen Wörter. Wir lesen keine Texte.</span><svg class="vx-lock" aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/></svg></div>
<ul class="vx-privacy-list">
<li><span>Spracherkennung</span><strong>auf deinem Mac</strong></li>
<li><span>Cloud-Upload deiner Diktate</span><strong>nie</strong></li>
<li><span>Fürs Angebot übermittelt</span><strong>nur Wortanzahl + Zeitpunkt</strong></li>
</ul>
<div class="vx-chips"><span class="chip">100 % lokal</span><span class="chip">Apple Silicon</span><span class="chip">Made in Germany</span></div>
<div class="moneyback_receipt-rule"></div>
<div class="moneyback_redemption">{code_box()}<div class="moneyback_receipt-actions"><a class="btn btn-accent moneyback_redeem" href="{{{{CHECKOUT}}}}">Privat diktieren</a><p class="moneyback_fineprint moneyback_redeem-note">Monatsabo und Code werden für dich vorausgewählt.</p></div></div>
</div>"""


VARIANTS = {
    "v1": dict(
        name="Ganz simpel",
        hypothesis="Die einfachste Erklärung des Angebots konvertiert am besten.",
        title="Sprich 10.000 Wörter. Wir zahlen dir den Monat zurück.",
        description="Diktiere 10.000 Wörter im Monat mit Sprich und hol dir die Monatszahlung zurück – bis zu drei Mal.",
        hero=hero(
            left(
                "Ganz einfach erklärt",
                "Sprich 10.000 Wörter im Monat.<br/><em>Wir zahlen dir den Monat zurück.</em>",
                "Du diktierst Mails, Notizen und Ideen, statt sie zu tippen. Schaffst du das Ziel, bekommst du deine Monatszahlung erstattet. Bis zu drei Mal.",
                "Jetzt starten",
            ),
            V1_RIGHT,
        ),
        final=final("In drei Schritten zum Geld zurück", "Sprich einfach.<br/><em>Es lohnt sich.</em>", "Jetzt starten"),
    ),
    "v2": dict(
        name="Speed + Rennen",
        hypothesis="Ein erlebbarer Geschwindigkeitsvorteil (interaktiv) überzeugt mehr als Geld.",
        title="Sprechen ist 3× schneller. Und bringt dir bis zu 3 Monate zurück.",
        description="Sprechen ist rund dreimal schneller als Tippen. Probier Sprich aus und hol dir bis zu drei Monatszahlungen zurück.",
        hero=hero(
            left(
                "Tippen war gestern",
                "Sprechen ist 3×&nbsp;schneller.<br/><em>Und bringt dir bis zu 3&nbsp;Monate zurück.</em>",
                "Teste es selbst im Rennen. Diktier 10.000 Wörter im Monat und wir erstatten dir die Monatszahlung. Bis zu drei Mal.",
                "3× schneller schreiben",
            ),
            V2_RIGHT,
            extra_cls="vx-hero-long",
        ),
        final=final("Schneller schreiben beginnt jetzt", "Weniger tippen.<br/><em>Mehr schaffen.</em>", "3× schneller schreiben"),
        js=["race.js"],
    ),
    "v3": dict(
        name="Challenge",
        hypothesis="Gamification (Challenge, Runden) aktiviert mehr als ein Rabatt.",
        title="Die 10.000-Wörter-Challenge",
        description="Nimm die 10.000-Wörter-Challenge an: Schaffst du sie, bekommst du die Monatszahlung zurück. Drei Runden, drei Chancen.",
        hero=hero(
            left(
                "Drei Monate · Drei Runden",
                "Die 10.000-Wörter-<br/><em>Challenge.</em>",
                "Diktiere in einem Monat 10.000 Wörter und hol dir die Zahlung für diesen Monat zurück. Jede Runde zählt für sich: drei Runden, drei Chancen.",
                "Challenge annehmen",
            ),
            V3_RIGHT,
        ),
        final=final("Runde 1 wartet auf dich", "10.000 Wörter.<br/><em>Du schaffst das.</em>", "Runde 1 starten"),
        js=["challenge.js"],
    ),
    "v4": dict(
        name="Tukan",
        hypothesis="Starkes Markenbild + kurze emotionale Headline schlägt erklärende Copy.",
        title="Lass deine Stimme schreiben. Wir zahlen dir bis zu 3 Monate zurück.",
        description="Sprich – lokal auf deinem Mac, in jeder App. Diktiere 10.000 Wörter im Monat und hol dir bis zu drei Monatszahlungen zurück.",
        hero=hero(
            left(
                "Sprich einfach",
                "Lass deine Stimme schreiben.<br/><em>Wir zahlen dir bis zu 3&nbsp;Monate zurück.</em>",
                "Sprich diktiert lokal auf deinem Mac, in jeder App. Schaffst du 10.000 Wörter im Monat, erstatten wir dir die Monatszahlung. Bis zu drei Mal.",
                "Mit Stimme loslegen",
            ),
            V4_RIGHT,
            extra_cls="vx-hero-toucan vx-hero-long",
        ),
        final=final("Dein nächster Text beginnt mit deiner Stimme", "Lass deine Stimme<br/><em>schreiben.</em>", "Mit Stimme loslegen"),
    ),
    "v5": dict(
        name="Schmerzpunkt",
        hypothesis="Ein konkreter Alltagsschmerz (Mails nach Feierabend) zieht stärker als ein Feature.",
        title="Schluss mit Tippen nach Feierabend.",
        description="Die Mails, die liegen bleiben, sprichst du mit Sprich in Minuten weg. Bis zu drei Monatszahlungen zurück.",
        hero=hero(
            left(
                "Für alle, die abends noch Mails tippen",
                "Schluss mit Tippen<br/><em>nach Feierabend.</em>",
                "Die Mails, die liegen bleiben, sprichst du in Minuten weg. Und schaffst du 10.000 Wörter im Monat, erstatten wir dir die Monatszahlung. Bis zu drei Mal.",
                "Angebot einlösen – Code ist schon drin",
            ),
            V5_RIGHT,
        ),
        final=final("Heute Abend schon weniger tippen", "Feierabend ist<br/><em>Feierabend.</em>", "Angebot einlösen – Code ist schon drin"),
        js=["copy.js"],
    ),
    "v6": dict(
        name="Privatsphäre",
        hypothesis="Datenschutz/Lokalität ist für die Zielgruppe der stärkste Kaufgrund.",
        title="Deine Worte bleiben auf deinem Mac.",
        description="100 % lokal, keine Cloud: Diktiere mit Sprich 10.000 Wörter im Monat und hol dir bis zu drei Monatszahlungen zurück.",
        hero=hero(
            left(
                "100 % lokal · Made in Germany",
                "Deine Worte bleiben auf deinem Mac.<br/><em>Dein Geld kommt zurück.</em>",
                "Sprich erkennt deine Sprache direkt auf deinem Mac, ohne Cloud. Diktier 10.000 Wörter im Monat und hol dir bis zu drei Monatszahlungen zurück.",
                "Privat diktieren",
            ),
            V6_RIGHT,
            extra_cls="vx-hero-long",
        ),
        final=final("Privat diktieren, Geld zurückholen", "Lokal sprechen.<br/><em>Es lohnt sich.</em>", "Lokal loslegen"),
    ),
}
