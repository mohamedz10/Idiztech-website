"""Génère mentions-legales.html et confidentialite.html (FR/NL/EN). Usage : python3 tools/build-legal.py ."""
import sys, html

OUT = sys.argv[1]
UPDATED = {"fr": "17 novembre 2026", "nl": "17 november 2026", "en": "17 November 2026"}
CO = {"addr": "Rue des Anciens Étangs 40, 1190 Forest, Belgique", "vat": "BE 0772.379.227",
      "mail": "info@idiztech.be", "tel": "+32 484 95 83 44", "telraw": "+32484958344"}
UI = {
    "fr": {"back": "Retour au site", "upd": "Dernière mise à jour", "legal": "Mentions légales", "privacy": "Confidentialité"},
    "nl": {"back": "Terug naar de site", "upd": "Laatst bijgewerkt", "legal": "Juridische informatie", "privacy": "Privacybeleid"},
    "en": {"back": "Back to the site", "upd": "Last updated", "legal": "Legal notice", "privacy": "Privacy policy"},
}
M = f'<a href="mailto:{CO["mail"]}">{CO["mail"]}</a>'
T = f'<a href="tel:{CO["telraw"]}">{CO["tel"]}</a>'

LEGAL = {
 "fr": ("Mentions légales & conditions d'utilisation", [
  ("Éditeur du site", f"<p>Le site www.idiztech.be est édité par <strong>Idiz Tech</strong>.</p><ul><li>Siège : {CO['addr']}</li><li>Numéro d'entreprise (BCE) et TVA : {CO['vat']}</li><li>E-mail : {M}</li><li>Téléphone : {T}</li></ul>"),
  ("Hébergement", "<p>Le site est hébergé par Netlify, Inc., San Francisco, Californie (États-Unis), <a href=\"https://www.netlify.com\" rel=\"noopener\">www.netlify.com</a>. Le nom de domaine est géré par Easyhost (Belgique).</p>"),
  ("Propriété intellectuelle", "<p>La structure du site, son design, ses textes et le logo Idiz Tech sont la propriété d'Idiz Tech. Toute reproduction, totale ou partielle, sans autorisation écrite préalable est interdite.</p><p>Les logos des clients présentés dans la section « Ils nous font confiance » restent la propriété de leurs titulaires respectifs. Ils sont reproduits uniquement pour illustrer des références professionnelles.</p>"),
  ("Conditions d'utilisation", "<p>En naviguant sur ce site, vous acceptez les présentes conditions. Le site a pour but de présenter les services d'Idiz Tech. Vous vous engagez à l'utiliser de manière licite et à ne pas porter atteinte à son fonctionnement.</p>"),
  ("Responsabilité", "<p>Les informations publiées sur ce site sont fournies à titre indicatif et peuvent être modifiées à tout moment. Elles ne constituent pas une offre contractuelle : chaque mission fait l'objet d'un devis ou d'un contrat distinct. Idiz Tech ne peut être tenue responsable des dommages résultant de l'utilisation du site, ni du contenu des sites externes vers lesquels il renvoie.</p>"),
  ("Données personnelles", "<p>Le traitement de vos données est décrit dans notre <a href=\"confidentialite.html\">politique de confidentialité</a>.</p>"),
  ("Droit applicable", "<p>Ces conditions sont régies par le droit belge. Tout litige relève de la compétence des tribunaux de l'arrondissement judiciaire de Bruxelles.</p>"),
 ]),
 "nl": ("Juridische informatie & gebruiksvoorwaarden", [
  ("Uitgever van de site", f"<p>De site www.idiztech.be wordt uitgegeven door <strong>Idiz Tech</strong>.</p><ul><li>Zetel: Rue des Anciens Étangs 40, 1190 Vorst, België</li><li>Ondernemingsnummer (KBO) en btw: {CO['vat']}</li><li>E-mail: {M}</li><li>Telefoon: {T}</li></ul>"),
  ("Hosting", "<p>De site wordt gehost door Netlify, Inc., San Francisco, Californië (Verenigde Staten), <a href=\"https://www.netlify.com\" rel=\"noopener\">www.netlify.com</a>. De domeinnaam wordt beheerd door Easyhost (België).</p>"),
  ("Intellectuele eigendom", "<p>De structuur, het design, de teksten en het logo van Idiz Tech zijn eigendom van Idiz Tech. Elke volledige of gedeeltelijke reproductie zonder voorafgaande schriftelijke toestemming is verboden.</p><p>De klantlogo's in de sectie “Zij vertrouwen ons” blijven eigendom van hun respectieve houders. Ze worden enkel weergegeven ter illustratie van professionele referenties.</p>"),
  ("Gebruiksvoorwaarden", "<p>Door deze site te bezoeken, aanvaardt u deze voorwaarden. De site stelt de diensten van Idiz Tech voor. U verbindt zich ertoe de site op een wettige manier te gebruiken en de werking ervan niet te verstoren.</p>"),
  ("Aansprakelijkheid", "<p>De informatie op deze site wordt ter informatie verstrekt en kan op elk moment worden gewijzigd. Ze vormt geen contractueel aanbod: elke opdracht maakt het voorwerp uit van een afzonderlijke offerte of overeenkomst. Idiz Tech kan niet aansprakelijk worden gesteld voor schade die voortvloeit uit het gebruik van de site, noch voor de inhoud van externe sites waarnaar wordt verwezen.</p>"),
  ("Persoonsgegevens", "<p>De verwerking van uw gegevens wordt beschreven in ons <a href=\"confidentialite.html\">privacybeleid</a>.</p>"),
  ("Toepasselijk recht", "<p>Deze voorwaarden worden beheerst door het Belgisch recht. Elk geschil valt onder de bevoegdheid van de rechtbanken van het gerechtelijk arrondissement Brussel.</p>"),
 ]),
 "en": ("Legal notice & terms of use", [
  ("Site publisher", f"<p>The website www.idiztech.be is published by <strong>Idiz Tech</strong>.</p><ul><li>Registered office: {CO['addr'].replace('Belgique','Belgium')}</li><li>Company (CBE) and VAT number: {CO['vat']}</li><li>Email: {M}</li><li>Phone: {T}</li></ul>"),
  ("Hosting", "<p>The site is hosted by Netlify, Inc., San Francisco, California (United States), <a href=\"https://www.netlify.com\" rel=\"noopener\">www.netlify.com</a>. The domain name is managed by Easyhost (Belgium).</p>"),
  ("Intellectual property", "<p>The structure, design, texts and logo of the site are the property of Idiz Tech. Any full or partial reproduction without prior written consent is prohibited.</p><p>The client logos shown in the “They trust us” section remain the property of their respective owners. They are displayed solely to illustrate professional references.</p>"),
  ("Terms of use", "<p>By browsing this site, you accept these terms. The site presents the services of Idiz Tech. You agree to use it lawfully and not to interfere with its operation.</p>"),
  ("Liability", "<p>The information on this site is provided for general information and may change at any time. It does not constitute a contractual offer: each assignment is covered by a separate quote or contract. Idiz Tech cannot be held liable for damage resulting from the use of the site, nor for the content of external sites it links to.</p>"),
  ("Personal data", "<p>How we process your data is described in our <a href=\"confidentialite.html\">privacy policy</a>.</p>"),
  ("Governing law", "<p>These terms are governed by Belgian law. Any dispute falls under the jurisdiction of the courts of the judicial district of Brussels.</p>"),
 ]),
}

PRIVACY = {
 "fr": ("Politique de confidentialité", [
  ("Qui est responsable de vos données ?", f"<p><strong>Idiz Tech</strong>, {CO['addr']}, numéro d'entreprise {CO['vat']}, est responsable du traitement des données personnelles décrites ici. Pour toute question : {M}.</p>"),
  ("Quelles données et pourquoi ?", "<p>Ce site ne contient aucun formulaire et ne crée aucun compte. Nous traitons uniquement les données que vous nous transmettez vous-même lorsque vous nous écrivez ou nous appelez : nom, adresse e-mail, numéro de téléphone, entreprise et contenu de votre demande.</p><p>Nous les utilisons pour répondre à votre demande, préparer un devis et assurer le suivi de la relation commerciale. Base légale : les mesures précontractuelles prises à votre demande et notre intérêt légitime à répondre aux personnes qui nous contactent (articles 6.1.b et 6.1.f du RGPD).</p>"),
  ("Combien de temps les gardons-nous ?", "<p>Vos échanges sont conservés le temps nécessaire au traitement de votre demande, puis au maximum 3 ans après notre dernier contact, sauf si une relation contractuelle ou une obligation légale (par exemple comptable) impose une durée plus longue.</p>"),
  ("Cookies et stockage local", "<p>Ce site n'utilise aucun cookie publicitaire et aucun outil de mesure d'audience. Il enregistre seulement dans votre navigateur (stockage local) votre choix de langue et de thème clair ou sombre. Ces préférences ne nous sont jamais transmises et vous pouvez les effacer à tout moment depuis les réglages de votre navigateur.</p>"),
  ("Services tiers", "<ul><li><strong>Netlify</strong> (hébergement) : enregistre des journaux techniques, dont votre adresse IP, pour assurer le fonctionnement et la sécurité du site.</li><li><strong>Google Fonts</strong> : les polices du site sont chargées depuis les serveurs de Google, qui reçoit votre adresse IP.</li></ul><p>Ces prestataires peuvent traiter des données hors de l'Union européenne. Ces transferts sont encadrés par les garanties prévues par le RGPD (clauses contractuelles types ou décision d'adéquation).</p>"),
  ("Vos droits", f"<p>Vous pouvez à tout moment demander l'accès à vos données, leur rectification, leur effacement, la limitation du traitement ou leur portabilité, et vous opposer au traitement. Écrivez-nous à {M} : nous répondons dans un délai d'un mois.</p><p>Vous pouvez aussi introduire une plainte auprès de l'Autorité de protection des données (APD), rue de la Presse 35, 1000 Bruxelles, <a href=\"https://www.autoriteprotectiondonnees.be\" rel=\"noopener\">www.autoriteprotectiondonnees.be</a>.</p>"),
  ("Sécurité", "<p>Le site est servi exclusivement en HTTPS. Nous ne partageons pas vos données avec des tiers à des fins commerciales et limitons leur accès aux personnes qui en ont besoin pour traiter votre demande.</p>"),
  ("Modifications", "<p>Cette politique peut évoluer. La date de dernière mise à jour figure en haut de cette page.</p>"),
 ]),
 "nl": ("Privacybeleid", [
  ("Wie is verantwoordelijk voor uw gegevens?", f"<p><strong>Idiz Tech</strong>, Rue des Anciens Étangs 40, 1190 Vorst, België, ondernemingsnummer {CO['vat']}, is verantwoordelijk voor de verwerking van de hier beschreven persoonsgegevens. Voor vragen: {M}.</p>"),
  ("Welke gegevens en waarom?", "<p>Deze site bevat geen formulier en maakt geen accounts aan. We verwerken enkel de gegevens die u ons zelf bezorgt wanneer u ons mailt of belt: naam, e-mailadres, telefoonnummer, bedrijf en de inhoud van uw vraag.</p><p>We gebruiken ze om uw vraag te beantwoorden, een offerte op te stellen en de commerciële relatie op te volgen. Rechtsgrond: precontractuele maatregelen op uw verzoek en ons gerechtvaardigd belang om te antwoorden aan wie ons contacteert (artikelen 6.1.b en 6.1.f van de AVG).</p>"),
  ("Hoe lang bewaren we ze?", "<p>Uw berichten worden bewaard zolang nodig om uw vraag te behandelen, en daarna maximaal 3 jaar na ons laatste contact, tenzij een contractuele relatie of een wettelijke verplichting (bijvoorbeeld boekhoudkundig) een langere termijn vereist.</p>"),
  ("Cookies en lokale opslag", "<p>Deze site gebruikt geen advertentiecookies en geen tools voor bezoekersstatistieken. Hij bewaart enkel in uw browser (lokale opslag) uw taalkeuze en uw keuze voor een licht of donker thema. Deze voorkeuren worden nooit naar ons doorgestuurd en u kunt ze op elk moment wissen via de instellingen van uw browser.</p>"),
  ("Diensten van derden", "<ul><li><strong>Netlify</strong> (hosting): houdt technische logbestanden bij, waaronder uw IP-adres, voor de werking en beveiliging van de site.</li><li><strong>Google Fonts</strong>: de lettertypes van de site worden geladen vanaf de servers van Google, dat uw IP-adres ontvangt.</li></ul><p>Deze dienstverleners kunnen gegevens buiten de Europese Unie verwerken. Die doorgiften worden omkaderd door de waarborgen van de AVG (standaardcontractbepalingen of een adequaatheidsbesluit).</p>"),
  ("Uw rechten", f"<p>U kunt op elk moment inzage, verbetering, wissing, beperking van de verwerking of overdraagbaarheid van uw gegevens vragen, en bezwaar maken tegen de verwerking. Schrijf ons op {M}: we antwoorden binnen een maand.</p><p>U kunt ook klacht indienen bij de Gegevensbeschermingsautoriteit (GBA), Drukpersstraat 35, 1000 Brussel, <a href=\"https://www.gegevensbeschermingsautoriteit.be\" rel=\"noopener\">www.gegevensbeschermingsautoriteit.be</a>.</p>"),
  ("Beveiliging", "<p>De site wordt uitsluitend via HTTPS aangeboden. We delen uw gegevens niet met derden voor commerciële doeleinden en beperken de toegang tot de personen die ze nodig hebben om uw vraag te behandelen.</p>"),
  ("Wijzigingen", "<p>Dit beleid kan worden aangepast. De datum van de laatste update staat bovenaan deze pagina.</p>"),
 ]),
 "en": ("Privacy policy", [
  ("Who is responsible for your data?", f"<p><strong>Idiz Tech</strong>, {CO['addr'].replace('Belgique','Belgium')}, company number {CO['vat']}, is the controller of the personal data described here. For any question: {M}.</p>"),
  ("What data and why?", "<p>This site has no forms and creates no accounts. We only process the data you send us yourself when you email or call us: name, email address, phone number, company and the content of your request.</p><p>We use it to answer your request, prepare a quote and follow up on the business relationship. Legal basis: pre-contractual steps taken at your request and our legitimate interest in replying to people who contact us (Articles 6(1)(b) and 6(1)(f) GDPR).</p>"),
  ("How long do we keep it?", "<p>Your messages are kept for as long as needed to handle your request, then for at most 3 years after our last contact, unless a contract or a legal obligation (for example accounting) requires a longer period.</p>"),
  ("Cookies and local storage", "<p>This site uses no advertising cookies and no analytics tools. It only stores in your browser (local storage) your language choice and your light or dark theme. These preferences are never sent to us, and you can clear them at any time in your browser settings.</p>"),
  ("Third-party services", "<ul><li><strong>Netlify</strong> (hosting): keeps technical logs, including your IP address, to run and secure the site.</li><li><strong>Google Fonts</strong>: the site's fonts are loaded from Google's servers, which receive your IP address.</li></ul><p>These providers may process data outside the European Union. Such transfers are covered by the safeguards provided by the GDPR (standard contractual clauses or an adequacy decision).</p>"),
  ("Your rights", f"<p>You may at any time request access to, correction, erasure, restriction or portability of your data, and object to its processing. Write to us at {M}: we reply within one month.</p><p>You can also lodge a complaint with the Belgian Data Protection Authority (APD/GBA), Rue de la Presse 35, 1000 Brussels, <a href=\"https://www.dataprotectionauthority.be\" rel=\"noopener\">www.dataprotectionauthority.be</a>.</p>"),
  ("Security", "<p>The site is served over HTTPS only. We do not share your data with third parties for marketing purposes and limit access to the people who need it to handle your request.</p>"),
  ("Changes", "<p>This policy may change. The date of the last update is shown at the top of this page.</p>"),
 ]),
}

CSS = """
  :root{--bg:#0a0a0a;--fg:#f4f4f2;--mute:#8a8a87;--line:#232323;--soft:#141414;--accent:#f4f4f2;--on-accent:#0a0a0a;color-scheme:dark;
    --serif:"Instrument Serif",Georgia,serif;--sans:"Inter",system-ui,-apple-system,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace}
  :root[data-theme="light"]{--bg:#f5f5f2;--fg:#0b0b0b;--mute:#6a6a66;--line:#dededa;--soft:#ebebe7;--accent:#1d3fcf;--on-accent:#fff;color-scheme:light}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:var(--bg);color:var(--fg);font:300 17px/1.7 var(--sans);-webkit-font-smoothing:antialiased}
  a{color:inherit}
  :focus-visible{outline:1px solid var(--accent);outline-offset:3px}
  .wrap{max-width:820px;margin:0 auto;padding-left:max(24px,env(safe-area-inset-left,0px));padding-right:max(24px,env(safe-area-inset-right,0px))}
  header{border-bottom:1px solid var(--line);padding-top:env(safe-area-inset-top,0px)}
  header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;height:76px}
  .logo img{display:block;width:48px;height:48px;border-radius:50%;box-shadow:0 0 0 1px var(--line)}
  .tools{display:flex;align-items:center;gap:10px}
  .back{font-size:14px;color:var(--mute);text-decoration:none;white-space:nowrap}
  .back:hover{color:var(--fg)}
  .langs{display:flex;border:1px solid var(--line);border-radius:999px;padding:3px}
  .langs button{font:400 11px/1 var(--mono);letter-spacing:.08em;min-width:34px;min-height:30px;padding:0 9px;border-radius:999px;color:var(--mute);background:none;border:0;cursor:pointer}
  .langs button[aria-pressed="true"]{background:var(--accent);color:var(--on-accent)}
  main{padding-block:72px 96px}
  .eyebrow{font:400 12px/1.4 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
  h1{font:400 clamp(40px,7vw,72px)/1 var(--serif);letter-spacing:-.02em;margin:20px 0 48px;text-wrap:balance}
  h2{font:400 26px/1.2 var(--serif);margin:44px 0 12px}
  p,li{color:var(--mute);max-width:42em}
  p+p{margin-top:12px}
  ul{padding-left:1.2em;display:grid;gap:6px;margin-top:8px}
  strong{color:var(--fg);font-weight:400}
  main a{text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:4px}
  main a:hover{color:var(--fg)}
  article[hidden]{display:none}
  footer{border-top:1px solid var(--line);padding-block:32px;font-size:13px;color:var(--mute)}
  footer .wrap{display:flex;justify-content:space-between;gap:12px 24px;flex-wrap:wrap}
  footer a{text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:4px}
  @media (max-width:520px){.back span{display:none}.langs button{min-width:32px;padding:0 6px}.tools{gap:6px}}
"""

def page(fname, content, title_key):
    arts = []
    for l in ["fr", "nl", "en"]:
        title, secs = content[l]
        body = "".join(f"<h2>{html.escape(h)}</h2>{b}" for h, b in secs)
        arts.append(f'''<article lang="{l}" data-l="{l}" data-title="{html.escape(title)} · Idiz Tech"{' hidden' if l != 'fr' else ''}>
      <div class="eyebrow">{UI[l]['upd']} · {UPDATED[l]}</div>
      <h1>{html.escape(title)}</h1>
      {body}
    </article>''')
    fr_title = content["fr"][0]
    doc = f'''<!doctype html>
<html lang="fr" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(fr_title)} · Idiz Tech</title>
<meta name="description" content="{html.escape(fr_title)} du site Idiz Tech.">
<link rel="canonical" href="https://www.idiztech.be/{fname}">
<link rel="icon" type="image/png" href="logos/idiz-tech.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<script>(function(){{try{{var t=localStorage.getItem('idiz-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
<style>{CSS}</style>
</head>
<body>
<header>
  <div class="wrap">
    <a href="./" class="logo" aria-label="Idiz Tech"><img src="logos/idiz-tech.png" alt="Idiz Tech" width="48" height="48"></a>
    <div class="tools">
      <a class="back" href="./">← <span data-ui="back">{UI['fr']['back']}</span></a>
      <div class="langs" role="group" aria-label="Langue">
        <button type="button" data-lang="fr" aria-pressed="true">FR</button>
        <button type="button" data-lang="nl" aria-pressed="false">NL</button>
        <button type="button" data-lang="en" aria-pressed="false">EN</button>
      </div>
    </div>
  </div>
</header>
<main class="wrap">
    {"".join(arts)}
</main>
<footer>
  <div class="wrap">
    <span>© <span id="y"></span> Idiz Tech · BE 0772.379.227</span>
    <span><a href="mentions-legales.html" data-ui="legal">{UI['fr']['legal']}</a> · <a href="confidentialite.html" data-ui="privacy">{UI['fr']['privacy']}</a></span>
  </div>
</footer>
<script>
(function(){{
  var UI={__import__('json').dumps(UI, ensure_ascii=False)};
  var store={{get:function(k){{try{{return localStorage.getItem(k)}}catch(e){{return null}}}},set:function(k,v){{try{{localStorage.setItem(k,v)}}catch(e){{}}}}}};
  document.getElementById('y').textContent=new Date().getFullYear();
  function apply(l){{
    document.documentElement.lang=l;
    document.querySelectorAll('article[data-l]').forEach(function(a){{a.hidden=a.dataset.l!==l; if(a.dataset.l===l) document.title=a.dataset.title;}});
    document.querySelectorAll('[data-ui]').forEach(function(e){{e.textContent=UI[l][e.dataset.ui];}});
    document.querySelectorAll('.langs button').forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.lang===l);}});
  }}
  var l=store.get('idiz-lang');
  if(!UI[l]){{var n=(navigator.language||'fr').slice(0,2).toLowerCase();l=UI[n]?n:'fr';}}
  apply(l);
  document.querySelectorAll('.langs button').forEach(function(b){{b.addEventListener('click',function(){{apply(b.dataset.lang);store.set('idiz-lang',b.dataset.lang);}});}});
}})();
</script>
</body>
</html>
'''
    open(f"{OUT}/{fname}", "w", encoding="utf-8").write(doc)
    print("wrote", fname, len(doc))

page("mentions-legales.html", LEGAL, "legal")
page("confidentialite.html", PRIVACY, "privacy")
