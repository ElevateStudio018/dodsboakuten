# -*- coding: utf-8 -*-
"""
Bygger statiska HTML-sidor för dodsboakuten.se.

    python3 tools/build.py

Innehållet (texter, tjänster, kontaktuppgifter) ligger i den här filen så att
sidhuvud/sidfot och tjänstesidor hålls konsekventa. Kör skriptet efter ändringar
så skrivs index.html och tjanster/*.html om.
"""
import os, html, hashlib, time

VERSION = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]

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

# Vanliga frågor per tjänst (bygger på uppgifter från dodsboakuten.se)
SERVICE_FAQ = {
    "tomma-dodsbo": [
        ("Hur lång tid tar det att tömma ett dödsbo?", "Det beror på bostadens storlek och mängden bohag. En mindre lägenhet går ofta på en dag, större villor och gårdar kan ta längre tid. Efter den kostnadsfria bedömningen får ni en tydlig tidsplan."),
        ("Måste vi sortera själva innan ni kommer?", "Nej. Vi sorterar bohaget strukturerat tillsammans med er eller enligt era instruktioner. Ni avgör vad som ska sparas, säljas, skänkas eller slängas."),
        ("Vad händer med saker som har ett värde?", "Vi går igenom hemmet och identifierar möbler, konst, smycken, design och samlarföremål innan något körs bort. Vi kan även köpa hela eller delar av bohaget."),
        ("Kan ni även städa efter tömningen?", "Ja. Städning och sanering ingår som tillval så att bostaden kan lämnas klar för försäljning eller överlämning."),
    ],
    "vardera-dodsbo": [
        ("Kostar värderingen något?", "Den första bedömningen av dödsboet är kostnadsfri. Därefter kommer vi överens om hur vi går vidare."),
        ("Vad kan ni värdera?", "Möbler, konst, smycken, silver, porslin, designföremål, antikviteter och samlingar, antingen hela hem eller enskilda föremål."),
        ("Behöver vi sälja till er efter värderingen?", "Nej. Värderingen är fristående. Många väljer att låta oss köpa delar av bohaget eller hjälpa till med tömning, men det är helt upp till er."),
    ],
    "kopa-dodsbo": [
        ("Köper ni hela dödsbon eller bara enstaka saker?", "Både och. Beroende på innehåll och situation köper vi hela dödsbon eller utvalda delar, till exempel antikviteter, möbler, konst, samlarföremål och verktyg."),
        ("Hur snabbt kan vi få ett bud?", "Vi gör en snabb värdering på plats och lämnar ett tydligt bud. I Göteborg kan vi ofta komma med kort varsel."),
        ("Vad händer med det ni inte köper?", "Det vi inte köper kan vi hjälpa till att forsla bort, skänka eller återvinna. Tömning och sanering hanteras via samma kontakt."),
    ],
    "dodsbostadning": [
        ("Vad ingår i dödsbostädningen?", "Städning av hela bostaden, inklusive källare, garage och förråd vid behov, anpassad efter vad som krävs inför försäljning, uthyrning eller besiktning med hyresvärd."),
        ("Kan ni tömma bostaden samtidigt?", "Ja. Dödsbostädning kombineras ofta med tömning och bortforsling av bohag, så att allt sköts i ett och samma uppdrag."),
        ("Vad gör ni om det luktar illa i bostaden?", "Vid lukt- eller hygienproblem utför vi sanering utöver städningen så att bostaden kan överlämnas i gott skick."),
    ],
    "roja-dodsbo": [
        ("Vad är skillnaden mellan att röja och tömma ett dödsbo?", "Röjning handlar om att sortera och gallra bland möbler, bohag och tillhörigheter, medan tömning innebär att bostaden lämnas helt tom. Vi hjälper till med båda, och ofta i samma uppdrag."),
        ("Tar ni hand om återvinningen?", "Ja. Allt som ska bort forslas bort och återvinns på rätt sätt. Vi sköter transport och avfallshantering."),
        ("Kan ni städa när röjningen är klar?", "Ja. Vi städar och återställer bostaden inför försäljning eller överlämning."),
    ],
    "sanering-dodsbo": [
        ("När behövs sanering istället för städning?", "När det finns lukt, fukt, ohyra eller hygienproblem som vanlig städning inte löser. Vi bedömer behovet på plats."),
        ("Hur snabbt kan ni vara på plats?", "Vid akuta situationer kan vi ofta vara på plats inom 24 timmar."),
        ("Kan sanering kombineras med tömning?", "Ja. Sanering, tömning och värdering hanteras via en och samma kontakt."),
    ],
    "samlarsanering": [
        ("Hur arbetar ni i kraftigt belamrade bostäder?", "Metodiskt och med respekt. Vi sorterar tillsammans med er eller enligt era önskemål så att viktiga föremål och dokument tas om hand innan bortforsling."),
        ("Vem kan anlita er för samlarsanering?", "Privatpersoner, anhöriga och fastighetsägare i Göteborg och hela Västsverige."),
        ("Sköter ni även städning och sanering efteråt?", "Ja. När bostaden är tömd rengör och återställer vi den, och utför sanering vid behov."),
    ],
    "blodsanering": [
        ("Vilka situationer hjälper ni till vid?", "Olyckor, dödsfall och andra händelser där blod, kroppsvätskor eller biologiskt material behöver saneras i bostäder eller lokaler."),
        ("Arbetar ni diskret?", "Ja. Vi arbetar diskret, snabbt och professionellt, med respekt för de drabbade."),
        ("Ingår luktsanering?", "Ja, vid behov neutraliserar vi lukt och återställer bostaden eller lokalen."),
    ],
    "liksanering": [
        ("Vad innebär liksanering?", "Sanering av biologiskt material och lukt efter ett dödsfall i bostaden, samt rengöring och återställning av bostaden eller lokalen."),
        ("Kan ni även tömma dödsboet efteråt?", "Ja. Liksanering kan kombineras med tömning, städning och värdering av dödsboet via samma kontaktperson."),
        ("Vilka anlitar er?", "Privatpersoner, anhöriga, fastighetsägare och företag i Göteborg och hela Västsverige."),
    ],
}

# ---------------------------------------------------------------------------
# Hjälpfunktioner
# ---------------------------------------------------------------------------
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.8 2z"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 12.5l2.8 2.8L16 9.5"/></svg>'
ICON_SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v6c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>'

def e(s):
    return html.escape(s, quote=True)

def head(title, desc, canonical, rel, extra=""):
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
<meta name="theme-color" content="#232323">
<link rel="icon" href="{rel}assets/img/favicon.png" type="image/png">
<link rel="preload" href="{rel}assets/fonts/poppins-latin-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{rel}assets/fonts/poppins-latin-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{rel}assets/css/style.css?v={VERSION}">
{extra}
</head>
<body>
"""

NAV = [("Hem", ""), ("Tjänster", "#tjanster"), ("Om oss", "#om-oss"), ("Omdömen", "#omdomen"), ("Vanliga frågor", "#faq"), ("Kontakt", "#kontakt")]

def header(rel, home):
    nav = "".join(f'<a href="{home}{h}">{e(t)}</a>' for t, h in NAV)
    mobile = "".join(f'<a href="{home}{h}">{e(t)}</a>' for t, h in NAV[2:])
    subs = "".join(f'<a class="sub" href="{rel}tjanster/{s["slug"]}.html">{e(s["title"])}</a>' for s in SERVICES)
    return f"""
<a class="skip" href="#main">Hoppa till innehållet</a>
<header class="header" id="top">
  <div class="header__inner">
    <a class="header__logo" href="{home or 'index.html'}" aria-label="Dödsboakuten, till startsidan">
      <img src="{rel}assets/img/logo-wordmark-dark.png" alt="Dödsboakuten" width="1773" height="680">
    </a>
    <nav class="header__nav" aria-label="Huvudmeny">{nav}</nav>
    <a class="btn btn--brand btn--sm header__cta" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
    <button class="header__toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Öppna menyn"><span></span><span></span><span></span></button>
  </div>
  <nav class="header__mobile" id="mobile-nav" hidden aria-label="Mobilmeny">
    <a href="{home or 'index.html'}">Hem</a>
    <a href="{home}#tjanster">Tjänster</a>
    {subs}
    {mobile}
    <a class="btn btn--brand btn--block" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring {PHONE_DISPLAY}</a>
  </nav>
</header>
<main id="main">
"""

def footer(rel, home):
    links = "".join(f'<a href="{rel}tjanster/{s["slug"]}.html">{e(s["title"])}</a>' for s in SERVICES)
    return f"""
</main>
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <img class="footer__logo" src="{rel}assets/img/logo-dark.png" alt="Dödsboakuten – vi tar hand om allt" width="1773" height="838">
      </div>
      <div class="footer__links">{links}</div>
      <address>
        Dödsboakuten<br>
        {e(ADDRESS)}<br>
        Telefon: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
        Mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>
        {e(HOURS)}
      </address>
    </div>
    <p class="footer__copy">© <span data-year>2026</span> Dödsboakuten · Dödsbo i Göteborg &amp; Västsverige · Kostnadsfri bedömning, ofta på plats inom 24 timmar</p>
  </div>
</footer>
<div class="call-fab">
  <a class="btn btn--dark" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring oss</a>
  <a class="btn btn--brand" href="{home}#kontakt">Begär offert</a>
</div>
<script src="{rel}assets/js/main.js?v={VERSION}" defer></script>
</body>
</html>
"""

def faq_html(items):
    return "".join(f'<details class="faq__item"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in items)

def steps_html():
    return "".join(f'<div class="step"><span class="step__num">{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(PROCESS, 1))

def contact_html(rel, home):
    svc_opts = "".join(f'<option>{e(s["title"])}</option>' for s in SERVICES)
    return f"""
<section class="contact" id="kontakt">
  <div class="contact__panel" aria-hidden="true"></div>
  <div class="container contact__grid">
    <div>
      <p class="contact__kicker">Kontakt</p>
      <h2 class="display display--sm">Berätta om situationen,<br>så återkommer vi snabbt.</h2>
      <p class="contact__lead">Den första bedömningen är alltid kostnadsfri. Ring, mejla eller fyll i formuläret så hör vi av oss, oftast samma dag.</p>
      <div class="contact__details">
        <div><span>Telefon</span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
        <div><span>E-post</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div><span>Adress</span><p>{e(ADDRESS)}</p></div>
        <div><span>Öppettider</span><p>{e(HOURS)}<br>{e(HOURS_EXTRA)}</p></div>
      </div>
    </div>
    <form class="form" action="https://formspree.io/f/DIN-FORM-ID" method="POST" novalidate>
      <div class="field"><label for="f-name">Namn *</label><input id="f-name" name="Namn" type="text" autocomplete="name" required></div>
      <div class="field"><label for="f-phone">Telefon *</label><input id="f-phone" name="Telefon" type="tel" autocomplete="tel" required></div>
      <div class="field"><label for="f-email">E-post</label><input id="f-email" name="E-post" type="email" autocomplete="email"></div>
      <div class="field"><label for="f-city">Ort där bostaden finns</label><input id="f-city" name="Ort" type="text" placeholder="T.ex. Göteborg"></div>
      <div class="field"><label for="f-type">Vad behöver du hjälp med?</label><select id="f-type" name="Tjänst"><option>Hela processen</option>{svc_opts}<option>Osäker, vill rådgöra</option></select></div>
      <div class="field"><label for="f-size">Typ av bostad</label><select id="f-size" name="Bostad"><option>Lägenhet</option><option>Villa / radhus</option><option>Gård / lantbruk</option><option>Förråd, garage eller lokal</option><option>Annat</option></select></div>
      <div class="field"><label for="f-msg">Meddelande</label><textarea id="f-msg" name="Meddelande" placeholder="Beskriv gärna bostaden, önskad tidpunkt och om något är brådskande."></textarea></div>
      <p class="hp" aria-hidden="true"><label>Lämna tomt<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
      <input type="hidden" name="_subject" value="Offertförfrågan via dodsboakuten.se">
      <button class="btn btn--brand btn--block" type="submit">Skicka förfrågan</button>
      <p class="form__status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
"""

def card_html(s, rel):
    return f"""
      <article class="card">
        <img src="{rel}assets/img/{s['img']}-800.webp" alt="{e(s['img_alt'])}" loading="lazy" width="800" height="600">
        <div class="card__body">
          <h3><a class="card__link" href="{rel}tjanster/{s['slug']}.html">{e(s['title'])}</a></h3>
          <p>{e(s['short'])}</p>
          <span class="card__more">Läs mer →</span>
        </div>
      </article>"""

# ---------------------------------------------------------------------------
# Startsidan
# ---------------------------------------------------------------------------
def build_index():
    import json
    rel, home = "", ""
    ld = {
        "@context": "https://schema.org", "@type": "LocalBusiness", "name": "Dödsboakuten",
        "url": SITE_URL, "telephone": PHONE_TEL, "email": EMAIL, "image": SITE_URL + "/assets/img/logo-full-light.png",
        "address": {"@type": "PostalAddress", "streetAddress": "Exportgatan 73", "postalCode": "422 46", "addressLocality": "Hisings Backa", "addressCountry": "SE"},
        "areaServed": AREAS_MAIN + AREAS_REGION,
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"}],
        "description": "Tömning, värdering, köp, städning och sanering av dödsbo i Göteborg och Västsverige.",
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    extra = '<script type="application/ld+json">%s</script>\n<script type="application/ld+json">%s</script>\n<link rel="preload" as="image" href="assets/video/hero-poster.webp" fetchpriority="high">' % (json.dumps(ld, ensure_ascii=False), json.dumps(faq_ld, ensure_ascii=False))

    out = head("Dödsboakuten | Dödsbo i Göteborg – tömning, värdering, köp & sanering",
               "Dödsboakuten hjälper anhöriga med tömning, värdering, köp, städning och sanering av dödsbo i Göteborg och hela Västsverige. Kostnadsfri bedömning, ofta på plats inom 24 timmar.",
               SITE_URL + "/", rel, extra)
    out += header(rel, home)

    out += f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="hero__media" aria-hidden="true">
    <video autoplay muted loop playsinline preload="metadata" poster="assets/video/hero-poster.webp">
      <source src="assets/video/hero-mobile.mp4" type="video/mp4" media="(max-width: 760px)">
      <source src="assets/video/hero.mp4" type="video/mp4">
    </video>
  </div>
  <div class="container hero__content">
    <h1 class="display hero__title" id="hero-title">Vi tar hand om allt.<br><em>Med omtanke.</em></h1>
    <p class="hero__lead">Tömning, värdering, köp, städning och sanering av dödsbo i Göteborg och hela Västsverige. En kontaktperson genom hela processen, ofta på plats inom 24 timmar.</p>
    <div class="hero__cta">
      <a class="btn btn--white" href="#kontakt">Boka kostnadsfri bedömning</a>
      <a class="btn btn--outline" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
    </div>
  </div>
</section>

<section class="about" id="om">
  <div class="container about__grid">
    <div class="about__text">
      <h2 class="h2">Om oss</h2>
      <p>Dödsboakuten är en trygg helhetsleverantör för hantering av dödsbon i Göteborg, Halland och hela Västsverige. Att ta hand om ett dödsbo är känslomässigt tungt och fullt av praktiska uppgifter. Därför tar vi ansvar för hela processen, från första bedömning till tömt, städat och överlämnat hem.</p>
      <p>Vi hjälper privatpersoner, anhöriga och fastighetsägare, i allt från små lägenheter till stora villor och gårdar. Vi arbetar snabbt, respektfullt och med personlig kontakt, och samarbetar med mäklare, jurister och städföretag när uppdraget kräver det.</p>
      <a class="btn btn--brand" href="#tjanster">Våra tjänster</a>
    </div>
    <div class="about__media">
      <img src="assets/img/fonster.webp" srcset="assets/img/fonster-800.webp 800w, assets/img/fonster.webp 1600w" sizes="(min-width: 960px) 50vw, 100vw" alt="Ett äldre hem med lampa och spegel vid fönstret" loading="lazy" width="1600" height="1200">
    </div>
  </div>
</section>

<section class="why" id="varfor">
  <div class="container why__grid">
    <div>
      <p class="kicker">Därför Dödsboakuten</p>
      <h2 class="display display--sm">Ett företag du kan lita på, <em>från första samtalet.</em></h2>
      <p class="why__lead">Snabb hjälp, en kontaktperson och respekt för hemmet. Så enkelt ska det vara att få ett dödsbo omhändertaget.</p>
      <a class="btn btn--brand" href="#kontakt">Kontakta oss</a>
    </div>
    <div class="why__stats">
      <div class="stat"><div class="stat__num">24<small>timmar</small></div><h3>Snabb hjälp</h3><p>Vid akuta situationer kan vi ofta vara på plats inom ett dygn.</p></div>
      <div class="stat"><div class="stat__num">0<small>kr</small></div><h3>Kostnadsfri bedömning</h3><p>Vi börjar alltid med ett besök utan kostnad och ett tydligt förslag.</p></div>
      <div class="stat"><div class="stat__num">1</div><h3>Kontaktperson</h3><p>Samma person genom hela uppdraget, från första samtal till överlämning.</p></div>
      <div class="stat"><div class="stat__num">9</div><h3>Tjänster under ett tak</h3><p>Tömning, värdering, köp, städning, röjning och fyra typer av sanering.</p></div>
    </div>
    <ul class="why__promises">
      <li>{ICON_SHIELD}Respektfull och diskret hantering</li>
      <li>{ICON_SHIELD}Erfarenhet från många dödsbon</li>
      <li>{ICON_SHIELD}Hela Göteborg, Halland, Bohuslän och Västsverige</li>
    </ul>
  </div>
</section>

<section class="services" id="tjanster">
  <div class="container">
    <h2 class="h2 h2--center">Våra tjänster</h2>
    <p class="services__lead">Allt som behöver göras när ett hem ska avvecklas, genom en och samma kontakt.</p>
    <div class="services__grid">{"".join(card_html(SERVICE_BY_SLUG[s], rel) for s in MAIN_SLUGS)}
    </div>
    <div class="services__sub">
      <h2 class="h2">Sanering &amp; specialuppdrag</h2>
      <p class="services__lead">När bostaden kräver mer än städning. Vi hjälper privatpersoner, anhöriga, fastighetsägare och företag.</p>
    </div>
    <div class="services__grid services__grid--5">{"".join(card_html(SERVICE_BY_SLUG[s], rel) for s in SECONDARY_SLUGS)}
    </div>
    <p class="services__extra">Osäker på vad ni behöver? <a href="tel:{PHONE_TEL}">Ring {PHONE_DISPLAY}</a> så går vi igenom situationen tillsammans.</p>
  </div>
</section>

<section class="steps" id="process">
  <div class="container">
    <h2 class="h2 h2--center">Så fungerar det</h2>
    <p class="steps__lead">Fem steg från första samtal till tomt, klart hem.</p>
    <div class="steps__grid">{steps_html()}</div>
    <div class="steps__cta"><a class="btn btn--dark" href="#kontakt">Boka kostnadsfri bedömning</a></div>
  </div>
</section>

<section class="areas" id="omraden">
  <div class="container areas__grid">
    <div class="areas__media">
      <img src="assets/img/goteborg.webp" srcset="assets/img/goteborg-800.webp 800w, assets/img/goteborg.webp 1600w" sizes="(min-width: 960px) 50vw, 100vw" alt="Kanal och äldre bebyggelse i centrala Göteborg" loading="lazy" width="1600" height="1200">
    </div>
    <div class="areas__text">
      <h2 class="h2">Göteborg, Halland, Bohuslän och hela Västsverige</h2>
      <p>Vi utgår från Hisings Backa och arbetar i hela Göteborgsregionen. Vi tar även uppdrag längs kusten och inåt landet, i hela Västra Götaland och Halland.</p>
      <ul class="tags">{"".join(f'<li class="is-main">{e(a)}</li>' for a in AREAS_MAIN)}{"".join(f'<li>{e(a)}</li>' for a in AREAS_REGION)}</ul>
      <p class="muted" style="margin-top:22px;font-size:15px">Saknas din ort? Hör av dig, vi hjälper ofta till även utanför de områden som listas här.</p>
    </div>
  </div>
</section>

<section class="team" id="om-oss">
  <div class="container team__grid">
    <div class="team__portrait">
      <img src="assets/img/profil.jpg" alt="Ansvarig på Dödsboakuten i företagets arbetströja" width="281" height="328" loading="lazy">
    </div>
    <div class="team__text">
      <p class="kicker">Möt oss</p>
      <h2 class="h2">Personlig kontakt hela vägen</h2>
      <div class="team__role"><b>Din kontaktperson på Dödsboakuten</b><span>Ansvarig · Göteborg &amp; Västsverige</span></div>
      <p class="team__quote">”Ett dödsbo är ett helt liv i föremål. Vårt jobb är att göra det praktiska enkelt, så att ni får utrymme för det som är svårt.”</p>
      <p>Dödsboakuten drivs med erfarenhet från många dödsbon i Göteborg och Västsverige, från små lägenheter till stora villor och gårdar. Du har samma person att vända dig till genom hela uppdraget, och vi arbetar alltid med respekt, diskretion och omtanke om både hemmet och de anhöriga.</p>
      <div class="team__contact">
        <a class="btn btn--dark btn--sm" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
        <a class="btn btn--ghost btn--sm" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
  </div>
</section>

<section class="reviews" id="omdomen">
  <div class="container">
    <h2 class="h2 h2--center">Kundomdömen</h2>
    <p class="services__lead">Förtroende byggs i varje uppdrag.</p>
    <!--
      REDAKTIONELL NOT: Lägg in riktiga kundomdömen här (t.ex. från Google) i <div class="reviews__grid">.
      Mall per omdöme:
      <figure class="review">
        <div class="review__stars">★★★★★</div>
        <blockquote>”Citat från kunden.”</blockquote>
        <figcaption><b>Förnamn E.</b>Göteborg · Tömning av dödsbo</figcaption>
      </figure>
    -->
    <div class="reviews__note">
      <div>
        <h3>Referenser lämnas gärna på begäran</h3>
        <p>Vi publicerar endast omdömen från verkliga kunder. Vill du höra hur tidigare uppdragsgivare upplevt vårt arbete, eller har du själv anlitat oss och vill dela din upplevelse, hör av dig.</p>
      </div>
      <div>
        <a class="btn btn--dark" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring {PHONE_DISPLAY}</a>
        <a class="btn btn--ghost" href="mailto:{EMAIL}?subject=Omdöme%20om%20Dödsboakuten">Lämna ett omdöme</a>
      </div>
    </div>
  </div>
</section>

<section class="faq-section" id="faq">
  <div class="container faq-grid">
    <div>
      <p class="kicker">Vanliga frågor</p>
      <h2 class="h2">Frågor om dödsbo</h2>
      <p class="lead">Hittar du inte svaret? Ring oss så reder vi ut det tillsammans.</p>
      <a class="btn btn--ghost" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
    </div>
    <div class="faq">{faq_html(FAQ)}</div>
  </div>
</section>
"""
    out += contact_html(rel, home)
    out += footer(rel, home)
    write(os.path.join(ROOT, "index.html"), out)

# ---------------------------------------------------------------------------
# Tjänstesidor
# ---------------------------------------------------------------------------
def build_service(s):
    import json
    rel, home = "../", "../index.html"
    canonical = f"{SITE_URL}/tjanster/{s['slug']}.html"
    faqs = SERVICE_FAQ.get(s["slug"], [])
    ld = {"@context": "https://schema.org", "@type": "Service", "name": s["title"], "serviceType": s["title"],
          "provider": {"@type": "LocalBusiness", "name": "Dödsboakuten", "telephone": PHONE_TEL, "url": SITE_URL},
          "areaServed": AREAS_MAIN + AREAS_REGION, "description": s["meta"]}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    extra = '<script type="application/ld+json">%s</script>\n<script type="application/ld+json">%s</script>' % (json.dumps(ld, ensure_ascii=False), json.dumps(faq_ld, ensure_ascii=False))
    out = head(f"{s['title']} Göteborg | Dödsboakuten", s["meta"], canonical, rel, extra)
    out += header(rel, home)

    body = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h, p in s["body"])
    includes = "".join(f'<div class="include">{ICON_CHECK}<p>{e(i)}</p></div>' for i in s["includes"])
    others = [x for x in SERVICES if x["slug"] != s["slug"]]
    rel_first = [SERVICE_BY_SLUG[r] for r in s["related"]]
    others = rel_first + [x for x in others if x not in rel_first]
    others_html = "".join(f'<a class="other" href="{o["slug"]}.html"><h3>{e(o["title"])}</h3><p>{e(o["short"])}</p><span class="more">Läs mer →</span></a>' for o in others[:4])

    out += f"""
<section class="page-hero">
  <div class="page-hero__media" aria-hidden="true"><img src="{rel}assets/img/{s['img']}.webp" alt="" width="1600" height="1000" fetchpriority="high"></div>
  <div class="container page-hero__content">
    <nav class="crumbs" aria-label="Brödsmulor"><a href="{home}">Hem</a><span>/</span><a href="{home}#tjanster">Tjänster</a><span>/</span><span>{e(s['title'])}</span></nav>
    <h1 class="display">{e(s['h1'])}</h1>
    <p class="lead">{e(s['lead'])}</p>
    <div class="hero__cta">
      <a class="btn btn--white" href="#kontakt">Boka kostnadsfri bedömning</a>
      <a class="btn btn--outline" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
    </div>
    <ul class="facts"><li>Kostnadsfri bedömning</li><li>Ofta på plats inom 24 timmar</li><li>En kontaktperson</li><li>Hela Västsverige</li></ul>
  </div>
</section>

<section class="svc-intro">
  <div class="container svc-intro__grid">
    <div>{body}</div>
    <aside class="svc-aside">
      <div class="stat">
        <h3>Behöver du hjälp snabbt?</h3>
        <p>Vid akuta situationer kan vi ofta vara på plats inom 24 timmar. Ring oss så går vi igenom läget direkt.</p>
        <a class="btn btn--brand btn--block" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
        <p>{e(HOURS)} · {e(HOURS_EXTRA)}</p>
      </div>
      <div class="step">
        <h3>Vi finns i</h3>
        <p>{e(", ".join(AREAS_MAIN + AREAS_REGION))} och övriga Västsverige.</p>
      </div>
    </aside>
  </div>
</section>

<section class="includes">
  <div class="container">
    <h2 class="h2 h2--center">Det här ingår</h2>
    <p class="includes__lead">Vi anpassar alltid upplägget efter bostaden och era önskemål.</p>
    <div class="includes__grid">{includes}</div>
  </div>
</section>

<section class="steps">
  <div class="container">
    <h2 class="h2 h2--center">Så går det till</h2>
    <p class="steps__lead">Fem steg från första samtal till klart hem.</p>
    <div class="steps__grid">{steps_html()}</div>
  </div>
</section>

<section class="svc-faq">
  <div class="container">
    <h2 class="h2 h2--center">Vanliga frågor om {e(s['title'].lower())}</h2>
    <div class="faq">{faq_html(faqs)}</div>
  </div>
</section>

<section class="others">
  <div class="container">
    <h2 class="h2 h2--center">Fler tjänster</h2>
    <div class="others__grid">{others_html}</div>
  </div>
</section>

<section class="cta-band">
  <div class="container cta-band__inner">
    <h2 class="display display--sm">Redo att få hjälp med dödsboet?</h2>
    <p>Kostnadsfri bedömning i Göteborg och hela Västsverige. Ring oss eller skicka en förfrågan så återkommer vi snabbt.</p>
    <div class="cta-band__actions">
      <a class="btn btn--dark" href="tel:{PHONE_TEL}">{ICON_PHONE}Ring {PHONE_DISPLAY}</a>
      <a class="btn btn--white" href="#kontakt">Skicka förfrågan</a>
    </div>
  </div>
</section>
"""
    out += contact_html(rel, home)
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
