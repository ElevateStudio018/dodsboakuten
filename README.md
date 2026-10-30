# Dödsboakuten – ny hemsida

Statisk hemsida för [Dödsboakuten](https://dodsboakuten.se), dödsbo i Göteborg & Västsverige.
Byggd utan ramverk: ren HTML, CSS och ett litet JavaScript. Kan publiceras direkt på valfritt webbhotell, GitHub Pages, Netlify eller Vercel.

## Struktur

```
index.html              Startsida (hero med video, tjänster, process, team, omdömen, FAQ, kontakt)
tjanster/*.html         Nio tjänstesidor (tömning, värdering, köp, städning, röjning, sanering, samlar-, blod-, liksanering)
assets/css/style.css    All stil
assets/js/main.js       Meny, hero-video, FAQ, formulär
assets/img/             Logotypvarianter, profilbild, tjänstebilder (webp)
assets/video/           Hero-video (desktop + mobil) och poster
tools/build.py          Genererar index.html, tjanster/*.html, sitemap.xml och robots.txt från innehållet i filen
```

Ändra innehåll (texter, tjänster, kontaktuppgifter, FAQ) i `tools/build.py` och kör:

```bash
python3 tools/build.py
```

## Att göra innan lansering

1. **Formulär**: byt `DIN-FORM-ID` i `tools/build.py` (formulärets `action`) mot ett riktigt Formspree-ID, eller koppla till annan mottagare. Tills dess öppnar formuläret besökarens e-postprogram med förfrågan ifylld till info@dodsboakuten.se.
2. **Teamsektionen**: nuvarande hemsida anger inget namn på personen på profilbilden. Lägg in namn och roll i sektionen `#om-oss` i `tools/build.py` när uppgifterna är bekräftade. Inget namn har hittats på.
3. **Kundomdömen**: inga publicerade omdömen hittades på nuvarande hemsida eller i externa källor (Google, Reco, Trustpilot, hitta.se). Sektionen `#omdomen` är förberedd med en HTML-mall i en kommentar. Lägg in riktiga omdömen där när de finns.
4. **Domän**: `SITE_URL` i `tools/build.py` styr canonical, sitemap och strukturerad data.

## Källor och licenser

- Logotyp och profilbild: hämtade från dodsboakuten.se (`assets/img/logga-original.png`, `assets/img/profil.jpg`).
- Övriga foton och hero-video: Pexels (fri licens, ingen attribution krävs). Hero-video: Erik Mclean, Pexels #40345327.
- Typsnitt: Poppins via Google Fonts.
