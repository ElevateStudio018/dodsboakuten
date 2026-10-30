# -*- coding: utf-8 -*-
"""
Bygger statiska HTML-sidor för dodsboakuten.se.

    python3 tools/build.py

Innehållet (texter, tjänster, kontaktuppgifter) ligger i den här filen så att
sidhuvud/sidfot och tjänstesidor hålls konsekventa. Kör skriptet efter ändringar
så skrivs index.html och tjanster/*.html om.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Företagsuppgifter (från dodsboakuten.se)
# ---------------------------------------------------------------------------
PHONE_DISPLAY = "070-559 04 65"
PHONE_TEL = "+46705590465"
EMAIL = "info@dodsboakuten.se"
ADDRESS = "Exportgatan 73, 422 46 Hisings Backa"
HOURS = "Måndag–fredag 08:00–18:00"
HOURS_EXTRA = "Helger enligt överenskommelse"
SITE_URL = "https://dodsboakuten.se"

AREAS_MAIN = ["Göteborg", "Mölndal", "Partille", "Lerum", "Kungälv", "Ale", "Stenungsund", "Kungsbacka"]
AREAS_REGION = ["Halmstad", "Varberg", "Falkenberg", "Borås", "Uddevalla", "Trollhättan", "Lysekil", "Tjörn"]

# ---------------------------------------------------------------------------
# Tjänster
# ---------------------------------------------------------------------------
SERVICES = [
    dict(
        slug="tomma-dodsbo", nav="Tömma dödsbo", title="Tömma dödsbo",
        h1="Tömma dödsbo i Göteborg & Västsverige",
        short="Komplett hjälp med sortering, bortforsling och återvinning av bohag. Vi tar hand om hela hemmet, från små lägenheter till stora villor och gårdar.",
        img="tomning", img_alt="Flyttkartonger vid ett fönster i en lägenhet som töms",
        lead="Att tömma ett dödsbo är ofta det mest omfattande praktiska momentet efter ett dödsfall. Vi gör det tryggt, respektfullt och effektivt, ofta med start inom 24 timmar.",
        body=[
            ("Så hjälper vi dig", "Vi tömmer dödsbon i Göteborg och hela Västsverige, i allt från små lägenheter till stora villor och gårdar. Arbetet omfattar strukturerad sortering av bohaget, bortforsling, återvinning och, när det behövs, städning och sanering. Du har en och samma kontaktperson genom hela processen."),
            ("Värdefulla föremål tas om hand", "Innan något körs bort går vi igenom hemmet och identifierar möbler, konst, smycken, design och samlarföremål som kan ha ett värde. Värderingen ingår som en naturlig del av tömningen, och vi kan även köpa hela eller delar av bohaget."),
            ("Göteborg och hela regionen", "Vi är verksamma i hela Göteborgsområdet, bland annat Hisingen, Linné, Majorna, Askim, Västra Frölunda och centrala Göteborg, samt i Halland, Bohuslän och övriga Västsverige."),
        ],
        includes=["Strukturerad sortering av bohag", "Bortforsling, transport och återvinning", "Identifiering och värdering av värdefulla föremål", "Möjlighet till köp av hela eller delar av bohaget", "Städning och sanering vid behov", "En kontaktperson genom hela uppdraget"],
        related=["vardera-dodsbo", "kopa-dodsbo", "dodsbostadning"],
        meta="Tömma dödsbo i Göteborg och Västsverige. Snabb, trygg och respektfull hjälp med sortering, bortforsling och återvinning. Kostnadsfri bedömning, ofta på plats inom 24 timmar.",
    ),
    dict(
        slug="vardera-dodsbo", nav="Värdera dödsbo", title="Värdera dödsbo",
        h1="Värdering av dödsbo i Göteborg",
        short="Professionell värdering av bohag, möbler, konst, smycken, design och samlarföremål. Vi hjälper dig att se vad som har ett värde innan något körs bort.",
        img="vardering", img_alt="Porslinsservis på ett antikt matbord",
        lead="I ett dödsbo finns ofta föremål med ett värde som är lätt att missa. Vi erbjuder en kostnadsfri första bedömning och en professionell värdering av bohaget.",
        body=[
            ("Vad vi värderar", "Vi värderar hela hem eller enskilda föremål: möbler, konst, smycken, silver, porslin, designföremål och samlingar. Målet är att du ska få en tydlig bild av vad som finns i dödsboet innan beslut fattas om försäljning, tömning eller köp."),
            ("Kostnadsfri första bedömning", "Vi börjar alltid med en kostnadsfri bedömning av dödsboet. Därefter går vi igenom hur vi bäst går vidare, oavsett om det handlar om att vi köper delar av bohaget, hjälper till med tömning eller enbart gör en värdering."),
            ("Diskret och respektfullt", "Vi har erfarenhet av många dödsbon och vet att situationen är känslig. Allt arbete sker diskret, med respekt för både de anhöriga och den avlidnes hem."),
        ],
        includes=["Kostnadsfri första bedömning på plats", "Värdering av möbler, konst, smycken och design", "Genomgång av samlingar och antikviteter", "Rådgivning kring försäljning eller köp", "Kan kombineras med tömning och städning"],
        related=["kopa-dodsbo", "tomma-dodsbo", "roja-dodsbo"],
        meta="Värdera dödsbo i Göteborg. Kostnadsfri första bedömning och professionell värdering av bohag, antikviteter, konst och samlarföremål i hela Västsverige.",
    ),
    dict(
        slug="kopa-dodsbo", nav="Köpa dödsbo", title="Köpa dödsbo",
        h1="Vi köper dödsbo i Göteborg & Västsverige",
        short="Vi köper hela eller delar av dödsbon: antikviteter, möbler, konst, samlarföremål och verktyg. Snabb värdering och personlig service.",
        img="kop", img_alt="Silverföremål och antikviteter på ett bord",
        lead="Vi köper hela eller delar av dödsbon i Göteborg och hela Västsverige. Du får en snabb värdering på plats och en enkel, trygg process från första kontakt till tömt hem.",
        body=[
            ("Köp av hela eller delar av bohaget", "Beroende på innehåll och situation köper vi hela dödsbon eller utvalda delar. Vi gör en snabb värdering på plats och lämnar ett tydligt bud. Det som inte köps kan vi hjälpa till att forsla bort, skänka eller återvinna."),
            ("Vad köper vi?", "Antikviteter som möbler, konst, porslin och silver. Bohag och möbler i gott skick. Samlarföremål, verktyg, retro och design. Hör av dig så berättar vi vad som är aktuellt för just ert dödsbo."),
            ("Komplett hjälp genom hela processen", "Värdering, köp, tömning och sanering hanteras via en och samma kontakt. Det gör processen enklare för dig som anhörig och innebär att hemmet kan lämnas tomt och klart utan att du behöver samordna flera aktörer."),
        ],
        includes=["Snabb värdering på plats", "Köp av antikviteter, möbler, konst och samlarföremål", "Köp av hela dödsbon eller utvalda delar", "Bortforsling av det som inte köps", "Tömning och sanering via samma kontakt"],
        related=["vardera-dodsbo", "tomma-dodsbo", "roja-dodsbo"],
        meta="Köpa dödsbo Göteborg. Vi köper hela eller delar av dödsbon, antikviteter, möbler och samlarföremål i hela Västsverige. Snabb värdering och personlig service.",
    ),
    dict(
        slug="dodsbostadning", nav="Dödsbostädning", title="Dödsbostädning",
        h1="Dödsbostädning i Göteborg & Västsverige",
        short="Noggrann städning och återställning av bostaden efter tömning, så att den kan lämnas till försäljning, uthyrning eller överlämning.",
        img="stadning", img_alt="Professionell städning av ett handfat med skyddshandskar",
        lead="När bostaden är tömd behöver den ofta städas och återställas inför försäljning, uthyrning eller överlämning till hyresvärd. Vi tar hand om hela momentet.",
        body=[
            ("Städning av hela bostaden", "Vi städar lägenheter, villor, källare, garage och förråd. Städningen anpassas efter bostadens skick och vad som krävs inför nästa steg, oavsett om det är en visning eller en besiktning med hyresvärden."),
            ("Tömning och bortforsling i samma uppdrag", "Dödsbostädning kombineras ofta med tömning och bortforsling av bohag. Vi samordnar allt så att du slipper flera olika leverantörer och tidsplaner."),
            ("Återställning inför överlämning", "Målet är att bostaden ska kunna lämnas i ett bra skick. Vid behov utför vi även sanering av lukt och hygienproblem, så att hemmet är redo att överlämnas."),
        ],
        includes=["Städning av lägenheter, villor, källare, garage och förråd", "Tömning och bortforsling i samma uppdrag", "Återställning inför försäljning eller överlämning", "Sanering vid lukt- och hygienproblem", "Hjälp i hela Västsverige"],
        related=["tomma-dodsbo", "sanering-dodsbo", "roja-dodsbo"],
        meta="Dödsbostädning i Göteborg och Västsverige. Professionell städning, tömning och återställning av bostaden efter dödsfall. Snabb hjälp med personlig service.",
    ),
    dict(
        slug="roja-dodsbo", nav="Röja dödsbo", title="Röja dödsbo",
        h1="Röja dödsbo i Göteborg & Västsverige",
        short="Röjning, sortering och bortforsling av möbler, bohag och tillhörigheter, med återvinning och städning via en och samma kontakt.",
        img="rojning", img_alt="Flyttkartonger staplade i ett rum",
        lead="Vi hjälper privatpersoner och anhöriga att röja dödsbon i Göteborg och hela Västsverige. Röjning, tömning, städning och sanering hanteras genom en enda kontakt.",
        body=[
            ("Röjning och sortering", "Vi går strukturerat igenom möbler, bohag och tillhörigheter tillsammans med dig eller enligt era önskemål. Det som ska sparas, säljas, skänkas eller slängas sorteras tydligt."),
            ("Bortforsling och återvinning", "Allt som ska bort forslas bort och återvinns på rätt sätt. Vi tar hand om transport, avfallshantering och återvinning så att bostaden kan tömmas effektivt."),
            ("Städning och återställning", "Efter röjningen städar och återställer vi bostaden inför försäljning eller överlämning. Vi arbetar i Göteborgsregionen, Halland, Bohuslän och övriga Västsverige."),
        ],
        includes=["Sortering av möbler, bohag och tillhörigheter", "Bortforsling med återvinning", "Städning och återställning av bostaden", "Komplett lösning med en kontaktperson", "Snabb och personlig service"],
        related=["tomma-dodsbo", "dodsbostadning", "samlarsanering"],
        meta="Röja dödsbo i Göteborg och Västsverige. Hjälp med röjning, sortering, bortforsling och städning av dödsbo. Snabb, trygg och personlig service.",
    ),
    dict(
        slug="sanering-dodsbo", nav="Sanering av dödsbo", title="Sanering av dödsbo",
        h1="Sanering av dödsbo i Göteborg",
        short="Diskret och professionell sanering av bostäder efter tömning, inklusive lukt- och hygienproblem, så att bostaden återställs i gott skick.",
        img="sanering", img_alt="Sanerare i skyddskläder dammsuger ett vardagsrum",
        lead="Ibland behöver en bostad mer än städning. Vi utför diskret och professionell sanering av dödsbon i Göteborg och Västsverige, ofta med start inom 24 timmar.",
        body=[
            ("När sanering behövs", "Efter ett dödsfall kan det finnas lukt, fukt, ohyra eller hygienproblem som kräver sanering snarare än vanlig städning. Vi bedömer behovet på plats och återställer bostaden i ett bra skick."),
            ("Diskret och respektfullt", "Vi arbetar diskret, respektfullt och effektivt för att säkerställa att bostaden återställs i ett bra skick. Vi har erfarenhet av många olika typer av uppdrag och vet vad som krävs."),
            ("Helhetslösning", "Sanering kombineras ofta med tömning och värdering. Vi tar ansvar för hela kedjan så att du som anhörig eller fastighetsägare har en kontakt att vända dig till."),
        ],
        includes=["Bedömning av saneringsbehov på plats", "Noggrann sanering av bostaden efter tömning", "Hantering av lukt- och hygienproblem", "Återställning av bostaden", "Kombineras med tömning och värdering"],
        related=["dodsbostadning", "samlarsanering", "liksanering"],
        meta="Sanering av dödsbo i Göteborg och Västsverige. Diskret och professionell sanering, luktsanering och återställning av bostäder. Snabb hjälp vid akuta behov.",
    ),
    dict(
        slug="samlarsanering", nav="Samlarsanering", title="Samlarsanering",
        h1="Samlarsanering i Göteborg & Västsverige",
        short="Erfaren och respektfull hjälp vid kraftigt belamrade bostäder. Sortering, bortforsling, avfallshantering och återställning.",
        img="samlarsanering", img_alt="Ett gammalt skåp i ett rum med solljus genom fönstret",
        lead="Vid kraftigt belamrade bostäder krävs ofta erfarenhet, struktur och respektfull hantering. Vi hjälper privatpersoner, anhöriga och fastighetsägare i Göteborg och hela Västsverige.",
        body=[
            ("Strukturerad sortering och röjning", "Vi går igenom bostaden metodiskt och sorterar det som ska sparas, säljas, skänkas eller slängas. Arbetet planeras tillsammans med dig så att viktiga föremål och dokument tas om hand."),
            ("Bortforsling och avfallshantering", "Stora volymer kräver rätt logistik. Vi sköter bortforsling, återvinning och avfallshantering så att bostaden kan tömmas effektivt och säkert."),
            ("Rengöring och återställning", "När bostaden är tömd rengör och återställer vi den. Vid behov utför vi även sanering. Allt sker diskret och med respekt för den som bott i hemmet."),
        ],
        includes=["Metodisk sortering och röjning", "Bortforsling, återvinning och avfallshantering", "Rengöring och återställning av bostaden", "Sanering vid behov", "Diskret hantering med en kontaktperson"],
        related=["sanering-dodsbo", "roja-dodsbo", "dodsbostadning"],
        meta="Samlarsanering i Göteborg och Västsverige. Diskret och professionell hjälp vid kraftigt belamrade bostäder: sortering, bortforsling, städning och återställning.",
    ),
    dict(
        slug="blodsanering", nav="Blodsanering", title="Blodsanering",
        h1="Blodsanering i Göteborg & Västsverige",
        short="Professionell sanering av blod, kroppsvätskor och biologiskt material efter olyckor eller dödsfall. Diskret, snabbt och säkert.",
        img="sanering", img_alt="Sanerare i skyddsutrustning rengör ett rum",
        lead="Efter olyckor, dödsfall eller andra händelser med blod och biologiskt material krävs professionell sanering. Vi hjälper privatpersoner, anhöriga, fastighetsägare och företag, diskret och snabbt.",
        body=[
            ("Sanering av biologiskt material", "Vi sanerar blod, kroppsvätskor och biologiskt material på ett säkert och hygieniskt sätt, med rätt utrustning och metoder. Arbetet utförs av personal med erfarenhet av saneringsuppdrag."),
            ("Luktsanering", "Vid behov neutraliserar vi lukt och återställer bostaden eller lokalen så att den kan användas igen."),
            ("Rengöring och återställning", "Efter saneringen rengör och återställer vi bostaden eller fastigheten. Vi kan även hjälpa till med tömning av bostaden om det behövs."),
        ],
        includes=["Sanering av blod, kroppsvätskor och biologiskt material", "Luktsanering och neutralisering", "Rengöring och återställning av bostad eller lokal", "Diskret, professionell hantering", "Hjälp till privatpersoner, fastighetsägare och företag"],
        related=["liksanering", "sanering-dodsbo", "samlarsanering"],
        meta="Blodsanering i Göteborg och Västsverige. Diskret och professionell sanering av blod, kroppsvätskor och biologiskt material efter olyckor eller dödsfall.",
    ),
    dict(
        slug="liksanering", nav="Liksanering", title="Liksanering",
        h1="Liksanering i Göteborg & Västsverige",
        short="Diskret och professionell sanering efter dödsfall: biologiskt material, lukt och återställning av bostäder och lokaler.",
        img="rum", img_alt="Ett tomt rum i en äldre bostad med fönster och två fåtöljer",
        lead="Vi utför liksanering för privatpersoner, anhöriga, fastighetsägare och företag i Göteborg och hela Västsverige. Arbetet sker diskret, snabbt och professionellt.",
        body=[
            ("Sanering efter dödsfall", "När en person avlidit i bostaden kan det krävas sanering av biologiskt material innan hemmet kan användas eller tömmas. Vi har erfarenhet av dessa uppdrag och arbetar med stor respekt för situationen."),
            ("Luktsanering", "Vi neutraliserar lukt och återställer bostaden eller lokalen i ett skick där den kan lämnas vidare."),
            ("Komplett hjälp", "Liksanering kan kombineras med tömning, städning och värdering av dödsboet. Du har en kontaktperson genom hela processen, och vi samarbetar med flera aktörer i branschen för att kunna erbjuda helhetslösningar."),
        ],
        includes=["Sanering av biologiskt material efter dödsfall", "Luktsanering", "Rengöring och återställning av bostaden", "Kombineras med tömning och städning av dödsboet", "Diskret hantering med en kontaktperson"],
        related=["blodsanering", "sanering-dodsbo", "tomma-dodsbo"],
        meta="Liksanering i Göteborg och Västsverige. Diskret och professionell sanering efter dödsfall, inklusive luktsanering och återställning av bostäder och lokaler.",
    ),
]
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
MAIN_SLUGS = ["tomma-dodsbo", "vardera-dodsbo", "kopa-dodsbo", "dodsbostadning"]
SECONDARY_SLUGS = ["roja-dodsbo", "sanering-dodsbo", "samlarsanering", "blodsanering", "liksanering"]

FAQ = [
    ("Hur snabbt kan ni komma?", "Vid akuta situationer kan vi ofta vara på plats inom 24 timmar. Ring oss på %s så går vi igenom läget direkt." % PHONE_DISPLAY),
    ("Vad kostar en första bedömning?", "Den första bedömningen av dödsboet är kostnadsfri. Efter att vi sett bostaden och gått igenom era önskemål lämnar vi ett tydligt förslag på upplägg."),
    ("Vilka områden arbetar ni i?", "Vi utgår från Hisings Backa i Göteborg och arbetar i hela Göteborgsregionen samt Halland, Bohuslän och övriga Västsverige, bland annat Mölndal, Partille, Lerum, Kungälv, Kungsbacka, Borås, Halmstad, Varberg, Falkenberg, Uddevalla och Trollhättan."),
    ("Köper ni hela dödsbon?", "Ja. Vi köper hela eller delar av dödsbon beroende på innehåll och situation, till exempel antikviteter, möbler, konst, samlarföremål och verktyg. Det som inte köps kan vi hjälpa till att forsla bort."),
    ("Kan ni hjälpa till med allt, från tömning till städning?", "Ja. Vi erbjuder en komplett lösning där värdering, köp, tömning, bortforsling, städning och sanering hanteras genom en och samma kontakt. Vi samarbetar också med flera aktörer i branschen när det behövs."),
    ("Hur går sortering av bohaget till?", "Vi sorterar bohaget strukturerat tillsammans med er eller enligt era instruktioner. Värdefulla föremål identifieras innan något körs bort, och ni avgör vad som ska sparas, säljas, skänkas eller slängas."),
    ("Vilka tider har ni öppet?", "%s. %s." % (HOURS, HOURS_EXTRA)),
]

PROCESS = [
    ("Kontakt", "Ring eller skicka en förfrågan. Vi lyssnar in situationen och bokar en tid som passar er."),
    ("Kostnadsfri bedömning", "Vi besöker bostaden, går igenom bohaget och ger en tydlig bild av vad som behöver göras."),
    ("Gemensam planering", "Tillsammans bestämmer vi omfattning, tidsplan och vad som ska sparas, säljas, skänkas eller bort."),
    ("Genomförande", "Vi tömmer, värderar, köper, städar och sanerar enligt planen, med en kontaktperson hela vägen."),
    ("Överlämning", "Bostaden lämnas tom och klar för försäljning, uthyrning eller överlämning till hyresvärd."),
]

WHY = [
    ("Snabb hjälp vid akuta behov", "Vi kan ofta vara på plats inom 24 timmar när situationen kräver det."),
    ("Helhetslösning från start till klart hem", "Värdering, köp, tömning, städning och sanering via en och samma kontakt."),
    ("Erfarenhet från många dödsbon", "Från små lägenheter till stora villor och gårdar. Vi vet vad som krävs."),
    ("Respektfull och diskret hantering", "Vi arbetar med omtanke om både de anhöriga och den avlidnes hem."),
    ("Samarbeten i branschen", "Vi samarbetar med mäklare, jurister och städföretag när uppdraget kräver det."),
    ("Hela Västsverige", "Göteborgsregionen, Halland, Bohuslän och övriga Västra Götaland."),
]

# ---------------------------------------------------------------------------
# Hjälpfunktioner
# ---------------------------------------------------------------------------
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.8 2z"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

def e(s):
    return html.escape(s, quote=True)

def head(title, desc, canonical, rel, extra_ld=""):
    return f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/video/hero-poster.webp">
<meta property="og:locale" content="sv_SE">
<meta name="theme-color" content="#242424">
<link rel="icon" href="{rel}assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/css/style.css">
{extra_ld}
</head>
<body>
"""

def header(rel, home):
    def href(anchor):
        return f"{home}#{anchor}"
    nav_items = [("Tjänster", href("tjanster")), ("Så fungerar det", href("process")), ("Om oss", href("om-oss")), ("Omdömen", href("omdomen")), ("Vanliga frågor", href("faq")), ("Kontakt", href("kontakt"))]
    nav = "".join(f'<a href="{h}">{e(t)}</a>' for t, h in nav_items)
    mnav = "".join(f'<a href="{h}">{e(t)}</a>' for t, h in nav_items)
    return f"""
<a class="skip" href="#main" style="position:absolute;left:-9999px">Hoppa till innehållet</a>
<div class="topbar">
  <div class="container topbar__inner">
    <span class="topbar__hours"><b>Öppet</b> {e(HOURS)} · Akut hjälp, ofta inom 24 timmar</span>
    <span>Ring oss direkt: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></span>
  </div>
</div>
<header class="header">
  <div class="container header__inner">
    <a class="header__logo" href="{home}" aria-label="Dödsboakuten, till startsidan">
      <img class="logo-dark" src="{rel}assets/img/logo-wordmark-dark.png" alt="Dödsboakuten" width="1773" height="680">
      <img class="logo-light" src="{rel}assets/img/logo-wordmark-light.png" alt="" width="1773" height="680">
    </a>
    <nav class="nav" aria-label="Huvudmeny">{nav}</nav>
    <div class="header__actions">
      <a class="header__phone" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
      <a class="btn btn--brand" href="{href("kontakt")}">Begär offert</a>
    </div>
    <button class="burger" aria-expanded="false" aria-controls="mobile-menu" aria-label="Öppna menyn"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <nav aria-label="Mobilmeny">{mnav}</nav>
  <div class="mobile-menu__foot">
    <a class="tel" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <a class="btn btn--brand" href="{href("kontakt")}">Begär kostnadsfri bedömning</a>
  </div>
</div>
<main id="main">
"""

def footer(rel, home):
    svc = "".join(f'<li><a href="{rel}tjanster/{s["slug"]}.html">{e(s["title"])}</a></li>' for s in SERVICES)
    areas = "".join(f"<li>{e(a)}</li>" for a in AREAS_MAIN[:1] + AREAS_REGION[:7])
    return f"""
</main>
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="{rel}assets/img/logo-light.png" alt="Dödsboakuten – vi tar hand om allt" width="1773" height="838">
        <p>Trygg helhetsleverantör för hantering av dödsbon i Göteborg och Västsverige. Tömning, värdering, köp, städning och sanering, med respekt, diskretion och omtanke.</p>
        <p class="muted" style="font-size:14px">{e(ADDRESS)}</p>
      </div>
      <div>
        <h4>Tjänster</h4>
        <ul>{svc}</ul>
      </div>
      <div>
        <h4>Vi finns i</h4>
        <ul>{areas}<li><a href="{home}#omraden">Hela Västsverige</a></li></ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{e(HOURS)}</li>
          <li>{e(HOURS_EXTRA)}</li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> Dödsboakuten. Alla rättigheter förbehållna.</span>
      <span>Exportgatan 73, Hisings Backa · Göteborg</span>
    </div>
  </div>
</footer>
<div class="call-fab">
  <a class="btn btn--ink" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring {PHONE_DISPLAY}</a>
  <a class="btn btn--brand" href="{home}#kontakt">Begär offert</a>
</div>
<script src="{rel}assets/js/main.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Startsidan
# ---------------------------------------------------------------------------
def build_index():
    rel, home = "", "index.html"
    ld = {
        "@context": "https://schema.org", "@type": "LocalBusiness", "name": "Dödsboakuten",
        "url": SITE_URL, "telephone": PHONE_TEL, "email": EMAIL, "image": SITE_URL + "/assets/img/logo-full-light.png",
        "address": {"@type": "PostalAddress", "streetAddress": "Exportgatan 73", "postalCode": "422 46", "addressLocality": "Hisings Backa", "addressCountry": "SE"},
        "areaServed": AREAS_MAIN + AREAS_REGION,
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"}],
        "description": "Tömning, värdering, köp, städning och sanering av dödsbo i Göteborg och Västsverige.",
    }
    import json
    extra = '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    extra += '\n<script type="application/ld+json">%s</script>' % json.dumps(faq_ld, ensure_ascii=False)
    extra += f'\n<link rel="preload" as="image" href="assets/video/hero-poster.webp" fetchpriority="high">'

    out = head("Dödsboakuten | Dödsbo i Göteborg – tömning, värdering, köp & sanering",
               "Dödsboakuten hjälper anhöriga med tömning, värdering, köp, städning och sanering av dödsbo i Göteborg och hela Västsverige. Kostnadsfri bedömning, ofta på plats inom 24 timmar.",
               SITE_URL + "/", rel, extra)
    out += header(rel, home)

    # Hero
    out += f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="hero__media" aria-hidden="true">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/video/hero-poster.webp">
      <source src="assets/video/hero-mobile.mp4" type="video/mp4" media="(max-width: 760px)">
      <source src="assets/video/hero.mp4" type="video/mp4">
    </video>
  </div>
  <div class="container hero__inner">
    <div class="hero__content">
      <p class="eyebrow">Dödsbo i Göteborg &amp; Västsverige</p>
      <h1 class="h1 hero__title" id="hero-title">Vi tar hand om allt, <em>så att ni kan ta hand om varandra.</em></h1>
      <p class="hero__text">Tömning, värdering, köp, städning och sanering av dödsbo. En kontaktperson genom hela processen, med respekt för hemmet och för er som står mitt i det.</p>
      <div class="hero__cta">
        <a class="btn btn--brand" href="#kontakt">Begär kostnadsfri bedömning</a>
        <a class="btn btn--outline" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring {PHONE_DISPLAY}</a>
      </div>
    </div>
    <ul class="hero__facts">
      <li><b>Ofta inom 24 timmar</b><span>Snabb hjälp vid akuta situationer</span></li>
      <li><b>Kostnadsfri bedömning</b><span>Vi börjar alltid med ett besök utan kostnad</span></li>
      <li><b>Hela Västsverige</b><span>Göteborg, Halland, Bohuslän och Västra Götaland</span></li>
    </ul>
  </div>
</section>
"""

    # Intro
    out += f"""
<section class="section section--paper" id="om" aria-labelledby="intro-title">
  <div class="container">
    <div class="intro">
      <div class="reveal">
        <p class="eyebrow">Om Dödsboakuten</p>
        <h2 class="intro__statement" id="intro-title" style="margin-top:18px">En trygg helhetsleverantör när ett hem ska <em>avvecklas med omtanke.</em></h2>
      </div>
      <div class="intro__body reveal">
        <p class="lead">Att hantera ett dödsbo är känslomässigt tungt och fullt av praktiska uppgifter. Dödsboakuten tar ansvar för hela processen, från första bedömning till tömt, städat och överlämnat hem.</p>
        <p>Vi hjälper privatpersoner, anhöriga och fastighetsägare i Göteborg, Halland och hela Västsverige. Uppdragen spänner från små lägenheter till stora villor och gårdar, och vi arbetar alltid snabbt, respektfullt och med personlig kontakt. När uppdraget kräver det samarbetar vi med mäklare, jurister och städföretag för att kunna erbjuda en komplett lösning.</p>
        <ul class="intro__points">
          <li><span>01</span>Tömning, bortforsling och återvinning av bohag</li>
          <li><span>02</span>Värdering och köp av möbler, antikviteter och samlarföremål</li>
          <li><span>03</span>Städning och sanering så att bostaden kan lämnas vidare</li>
        </ul>
        <a class="link" href="#om-oss">Möt personen bakom Dödsboakuten {ICON_ARROW}</a>
      </div>
    </div>
    <figure class="intro__media reveal">
      <img src="assets/img/fonster.webp" srcset="assets/img/fonster-800.webp 800w, assets/img/fonster.webp 1600w" sizes="(min-width: 1240px) 1160px, 100vw" alt="Ett äldre hem med lampa och spegel vid fönstret" loading="lazy" width="1600" height="900">
      <figcaption>Varje hem bär på en historia. Vi hanterar den med respekt.</figcaption>
    </figure>
  </div>
</section>
"""

    # Tjänster
    cards = ""
    for i, slug in enumerate(MAIN_SLUGS, 1):
        s = SERVICE_BY_SLUG[slug]
        cards += f"""
      <a class="service reveal" href="tjanster/{s['slug']}.html">
        <div class="service__media"><img src="assets/img/{s['img']}-800.webp" alt="{e(s['img_alt'])}" loading="lazy" width="800" height="1000"><span class="service__num">0{i}</span></div>
        <h3>{e(s['title'])}</h3>
        <p>{e(s['short'])}</p>
        <span class="link">Läs mer {ICON_ARROW}</span>
      </a>"""
    sec = ""
    for slug in SECONDARY_SLUGS:
        s = SERVICE_BY_SLUG[slug]
        sec += f"""
        <a href="tjanster/{s['slug']}.html"><div><h3>{e(s['title'])}</h3><p>{e(s['short'])}</p></div>{ICON_ARROW}</a>"""
    out += f"""
<section class="section" id="tjanster" aria-labelledby="tjanster-title">
  <div class="container">
    <div class="section-head section-head--split reveal">
      <div>
        <p class="eyebrow">Våra tjänster</p>
        <h2 class="h2" id="tjanster-title" style="margin-top:18px">Allt som behöver göras, genom en kontakt.</h2>
      </div>
      <p class="lead">Vi erbjuder hjälp genom hela processen, från sortering och värdering till bortforsling, återvinning och städning. Välj det ni behöver, eller låt oss ta hand om helheten.</p>
    </div>
    <div class="services">{cards}
    </div>
    <div class="services-secondary">
      <div class="services-secondary__intro reveal">
        <p class="eyebrow">Sanering &amp; specialuppdrag</p>
        <h3 class="h3">När bostaden kräver mer än städning</h3>
        <p class="muted">Vissa uppdrag kräver särskild erfarenhet, utrustning och diskretion. Vi hjälper privatpersoner, anhöriga, fastighetsägare och företag.</p>
      </div>
      <div class="services-list reveal">{sec}
      </div>
    </div>
  </div>
</section>
"""

    # Varför
    why = "".join(f'<div class="why__item"><span>0{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(WHY, 1))
    out += f"""
<section class="section section--dark" id="varfor" aria-labelledby="varfor-title">
  <div class="container">
    <div class="why">
      <div class="why__aside reveal">
        <p class="eyebrow">Varför Dödsboakuten</p>
        <h2 class="h2" id="varfor-title">Erfarenhet, snabbhet och respekt för hemmet.</h2>
        <p class="lead">Vi vet att ett dödsbo är mer än ett bohag. Därför arbetar vi strukturerat, diskret och alltid med en personlig kontakt.</p>
        <div><a class="btn btn--brand" href="#kontakt">Kontakta oss</a></div>
      </div>
      <div class="why__list reveal">{why}</div>
    </div>
  </div>
</section>
"""

    # Process
    steps = "".join(f'<div class="step reveal"><span class="step__num">{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(PROCESS, 1))
    out += f"""
<section class="section section--paper" id="process" aria-labelledby="process-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Så fungerar det</p>
      <h2 class="h2" id="process-title">Fem steg från första samtal till tomt, klart hem.</h2>
    </div>
    <div class="process">{steps}</div>
    <div class="process-cta reveal">
      <a class="btn btn--ink" href="#kontakt">Boka kostnadsfri bedömning</a>
      <span class="muted">Eller ring oss direkt på <a href="tel:{PHONE_TEL}" style="color:var(--ink);font-weight:500">{PHONE_DISPLAY}</a></span>
    </div>
  </div>
</section>
"""

    # Områden
    tags = "".join(f'<li class="is-main">{e(a)}</li>' for a in AREAS_MAIN) + "".join(f"<li>{e(a)}</li>" for a in AREAS_REGION)
    out += f"""
<section class="section" id="omraden" aria-labelledby="omraden-title">
  <div class="container">
    <div class="areas">
      <div class="areas__media reveal">
        <img src="assets/img/goteborg.webp" srcset="assets/img/goteborg-800.webp 800w, assets/img/goteborg.webp 1600w" sizes="(min-width: 960px) 50vw, 100vw" alt="Kanal och äldre bebyggelse i centrala Göteborg" loading="lazy" width="1600" height="1067">
      </div>
      <div class="areas__body reveal">
        <p class="eyebrow">Där vi finns</p>
        <h2 class="h2" id="omraden-title">Göteborg, Halland, Bohuslän och hela Västsverige.</h2>
        <p class="lead">Vi utgår från Hisings Backa och arbetar i hela Göteborgsregionen. Vi tar även uppdrag längs kusten och inåt landet, i hela Västra Götaland och Halland.</p>
        <ul class="area-tags">{tags}</ul>
        <p class="muted" style="font-size:15px">Saknas din ort? Hör av dig, vi hjälper ofta till även utanför de områden som listas här.</p>
      </div>
    </div>
  </div>
</section>
"""

    # Team
    out += f"""
<section class="section section--paper" id="om-oss" aria-labelledby="team-title">
  <div class="container">
    <div class="team">
      <div class="team__portrait reveal">
        <img src="assets/img/profil.jpg" alt="Ansvarig på Dödsboakuten i företagets arbetströja" width="281" height="328" loading="lazy">
      </div>
      <div class="team__body reveal">
        <p class="eyebrow">Möt oss</p>
        <h2 class="h2" id="team-title">Personlig kontakt, från första samtalet till sista nyckeln.</h2>
        <div class="team__role">
          <b>Din kontaktperson på Dödsboakuten</b>
          <span>Ansvarig · Göteborg &amp; Västsverige</span>
        </div>
        <p class="team__quote">”Ett dödsbo är ett helt liv i föremål. Vårt jobb är att göra det praktiska enkelt, så att ni får utrymme för det som är svårt.”</p>
        <p>Dödsboakuten drivs med erfarenhet från många dödsbon i Göteborg och Västsverige, från små lägenheter till stora villor och gårdar. Du har samma person att vända dig till genom hela uppdraget, och vi arbetar alltid med respekt, diskretion och omtanke om både hemmet och de anhöriga.</p>
        <div class="team__contact">
          <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

    # Omdömen (inga publicerade omdömen finns på nuvarande webbplats eller i hittade källor;
    # sektionen är förberedd och fylls med riktiga kundomdömen när de finns.)
    out += f"""
<section class="section" id="omdomen" aria-labelledby="omdomen-title">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Kundomdömen</p>
      <h2 class="h2" id="omdomen-title">Förtroende byggs i varje uppdrag.</h2>
    </div>
    <!--
      REDAKTIONELL NOT: Här läggs riktiga kundomdömen in när de finns (t.ex. från Google).
      Mall per omdöme:
      <figure class="review">
        <div class="review__stars">★★★★★</div>
        <blockquote>”Citat från kunden.”</blockquote>
        <figcaption><b>Förnamn E.</b>Göteborg · Tömning av dödsbo</figcaption>
      </figure>
    -->
    <div class="reviews-note reveal">
      <div>
        <h3>Referenser lämnas gärna på begäran.</h3>
        <p>Vi publicerar endast omdömen från verkliga kunder. Vill du höra hur tidigare uppdragsgivare upplevt vårt arbete, eller har du själv anlitat oss och vill dela din upplevelse, hör av dig så hjälper vi dig vidare.</p>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:12px">
        <a class="btn btn--ink" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring {PHONE_DISPLAY}</a>
        <a class="btn btn--outline-ink" href="mailto:{EMAIL}?subject=Omdöme%20om%20Dödsboakuten">Lämna ett omdöme</a>
      </div>
    </div>
  </div>
</section>
"""

    # FAQ
    faq = "".join(f'<details class="faq__item"><summary>{e(q)}<span aria-hidden="true"></span></summary><p>{e(a)}</p></details>' for q, a in FAQ)
    out += f"""
<section class="section section--paper" id="faq" aria-labelledby="faq-title">
  <div class="container">
    <div class="faq">
      <div class="faq__aside reveal">
        <p class="eyebrow">Vanliga frågor</p>
        <h2 class="h2" id="faq-title">Det här undrar många.</h2>
        <p class="lead">Hittar du inte svaret? Ring oss så reder vi ut det tillsammans.</p>
        <div><a class="btn btn--outline-ink" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a></div>
      </div>
      <div class="faq__list reveal">{faq}</div>
    </div>
  </div>
</section>
"""

    # Kontakt
    svc_opts = "".join(f'<option>{e(s["title"])}</option>' for s in SERVICES)
    out += f"""
<section class="section section--dark" id="kontakt" aria-labelledby="kontakt-title">
  <div class="container">
    <div class="contact">
      <div class="contact__info reveal">
        <p class="eyebrow">Kontakt &amp; offert</p>
        <h2 class="h2" id="kontakt-title">Berätta om situationen, så återkommer vi snabbt.</h2>
        <p class="lead">Den första bedömningen är alltid kostnadsfri. Ring, mejla eller fyll i formuläret så hör vi av oss, oftast samma dag.</p>
        <div class="contact__rows">
          <div><span>Telefon</span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
          <div><span>E-post</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
          <div><span>Besöksadress</span><p>{e(ADDRESS)}</p></div>
          <div><span>Öppettider</span><p>{e(HOURS)}<br><span style="text-transform:none;letter-spacing:0;font-size:15px;color:rgba(255,255,255,.62)">{e(HOURS_EXTRA)}</span></p></div>
        </div>
      </div>
      <form class="form reveal" action="https://formspree.io/f/DIN-FORM-ID" method="POST" novalidate>
        <div class="form__grid">
          <div class="field"><label for="f-name">Namn *</label><input id="f-name" name="Namn" type="text" autocomplete="name" required></div>
          <div class="field"><label for="f-phone">Telefon *</label><input id="f-phone" name="Telefon" type="tel" autocomplete="tel" required></div>
          <div class="field"><label for="f-email">E-post</label><input id="f-email" name="E-post" type="email" autocomplete="email"></div>
          <div class="field"><label for="f-city">Ort där bostaden finns</label><input id="f-city" name="Ort" type="text" autocomplete="address-level2" placeholder="T.ex. Göteborg"></div>
          <div class="field"><label for="f-type">Vad behöver du hjälp med?</label><select id="f-type" name="Tjänst"><option>Hela processen (tömning, värdering, städning)</option>{svc_opts}<option>Osäker, vill rådgöra</option></select></div>
          <div class="field"><label for="f-size">Typ av bostad</label><select id="f-size" name="Bostad"><option>Lägenhet</option><option>Villa / radhus</option><option>Gård / lantbruk</option><option>Förråd, garage eller lokal</option><option>Annat</option></select></div>
          <div class="field field--full"><label for="f-msg">Beskriv gärna situationen</label><textarea id="f-msg" name="Meddelande" placeholder="Till exempel storlek på bostaden, önskad tidpunkt och om något är brådskande."></textarea></div>
        </div>
        <p class="hp" aria-hidden="true"><label>Lämna tomt<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
        <input type="hidden" name="_subject" value="Offertförfrågan via dodsboakuten.se">
        <div class="form__foot">
          <button class="btn btn--brand" type="submit">Skicka förfrågan</button>
          <small>Vi behandlar dina uppgifter konfidentiellt och använder dem bara för att återkomma till dig.</small>
        </div>
        <p class="form__status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
"""
    out += footer(rel, home)
    write(os.path.join(ROOT, "index.html"), out)

# ---------------------------------------------------------------------------
# Tjänstesidor
# ---------------------------------------------------------------------------
def build_service(s):
    rel, home = "../", "../index.html"
    canonical = f"{SITE_URL}/tjanster/{s['slug']}.html"
    import json
    ld = {"@context": "https://schema.org", "@type": "Service", "name": s["title"], "serviceType": s["title"],
          "provider": {"@type": "LocalBusiness", "name": "Dödsboakuten", "telephone": PHONE_TEL, "url": SITE_URL},
          "areaServed": AREAS_MAIN + AREAS_REGION, "description": s["meta"]}
    extra = '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False)
    out = head(f"{s['title']} Göteborg | Dödsboakuten", s["meta"], canonical, rel, extra)
    out += header(rel, home)

    body = ""
    for h, p in s["body"]:
        body += f"<h2>{e(h)}</h2><p>{e(p)}</p>"
    checks = "".join(f"<li>{ICON_CHECK}<span>{e(i)}</span></li>" for i in s["includes"])
    related = "".join(f'<a href="{SERVICE_BY_SLUG[r]["slug"]}.html">{e(SERVICE_BY_SLUG[r]["title"])}{ICON_ARROW}</a>' for r in s["related"])
    steps = "".join(f'<div class="step"><span class="step__num">{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(PROCESS, 1))

    out += f"""
<section class="page-hero">
  <div class="page-hero__media" aria-hidden="true"><img src="{rel}assets/img/{s['img']}.webp" alt="" width="1600" height="1000" fetchpriority="high"></div>
  <div class="container page-hero__inner">
    <nav class="breadcrumb" aria-label="Brödsmulor"><a href="{home}">Start</a><span>/</span><a href="{home}#tjanster">Tjänster</a><span>/</span><span>{e(s['title'])}</span></nav>
    <p class="eyebrow">{e(s['title'])}</p>
    <h1 class="h1">{e(s['h1'])}</h1>
    <p class="lead">{e(s['lead'])}</p>
    <div class="hero__cta">
      <a class="btn btn--brand" href="{home}#kontakt">Begär kostnadsfri bedömning</a>
      <a class="btn btn--outline" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="article">
      <div class="article__body">
        {body}
        <h2>Det här ingår</h2>
        <ul class="checklist">{checks}</ul>
      </div>
      <aside class="aside">
        <div class="aside__card">
          <h3>Behöver du hjälp snabbt?</h3>
          <p>Vid akuta situationer kan vi ofta vara på plats inom 24 timmar. Ring oss så går vi igenom läget direkt.</p>
          <a class="btn btn--brand" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
          <p style="font-size:14px">{e(HOURS)}<br>{e(HOURS_EXTRA)}</p>
        </div>
        <div>
          <h4>Relaterade tjänster</h4>
          <div class="aside__links">{related}</div>
        </div>
        <div>
          <h4>Vi finns i</h4>
          <p class="muted" style="font-size:15px">{e(", ".join(AREAS_MAIN + AREAS_REGION))} och övriga Västsverige.</p>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--paper section--tight">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Så fungerar det</p>
      <h2 class="h2">Från första samtal till klart hem.</h2>
    </div>
    <div class="process">{steps}</div>
  </div>
</section>

<section class="cta-band">
  <div class="container cta-band__inner">
    <h2>Kostnadsfri bedömning av dödsboet. Ring {PHONE_DISPLAY} eller skicka en förfrågan.</h2>
    <a class="btn btn--ink" href="{home}#kontakt">Begär offert {ICON_ARROW}</a>
  </div>
</section>
"""
    out += footer(rel, home)
    write(os.path.join(ROOT, "tjanster", f"{s['slug']}.html"), out)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("skrev", os.path.relpath(path, ROOT))

def build_sitemap():
    urls = [SITE_URL + "/"] + [f"{SITE_URL}/tjanster/{s['slug']}.html" for s in SERVICES]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n"
    write(os.path.join(ROOT, "sitemap.xml"), xml)
    write(os.path.join(ROOT, "robots.txt"), f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

if __name__ == "__main__":
    build_index()
    for s in SERVICES:
        build_service(s)
    build_sitemap()
