# Idiz Tech · site web

Site vitrine statique de [Idiz Tech](https://www.idiztech.be) : noir et blanc, mode clair (boutons bleu roi), FR / NL / EN, texte qui s'écrit au scroll façon IA, bande de logos clients.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Tout le site (HTML, CSS, JS, traductions) |
| `logos/` | Logo Idiz Tech et logos clients |
| `tests/site.test.js` | Agent de test (Playwright, 47 vérifications) |
| `build-artifact.py` | Génère une version autonome avec les logos intégrés |

Seuls `index.html` et `logos/` sont nécessaires en ligne.

## Modifier les textes

Les textes des 3 langues sont dans l'objet `I18N` en bas de `index.html` (`fr`, `nl`, `en`). Chaque clé doit exister dans les trois langues : l'agent de test le vérifie.

## Tester

```bash
npm install
npx playwright install chromium
npm test
```

Les tests tournent aussi automatiquement sur GitHub à chaque push (onglet **Actions**).

## Mettre en ligne

Hébergement statique, par exemple Netlify : déployer le dossier tel quel (pas de build), puis pointer `www.idiztech.be` vers le site Netlify dans le DNS.
