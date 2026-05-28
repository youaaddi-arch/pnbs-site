# Site PNBS — Paris Nord Business School

Site vitrine statique reproduisant le site PNBS (CFA commerce / vente / management,
certifié Qualiopi). 100 % HTML/CSS/JS, sans backend ni build complexe — déployable
tel quel sur n'importe quel hébergement statique (Vercel, Netlify, GitHub Pages, OVH…).

## Pages

| Fichier | Page |
|---|---|
| `index.html` | Accueil (hero, stats, formations, alternance, atouts, débouchés, partenaires, témoignages) |
| `formations.html` | Liste des 4 formations |
| `formations/*.html` | Fiches détaillées (Conseiller Commercial, NTC, REM, Manager de Business Unit) |
| `alternance.html` | L'alternance, rémunération, cadre légal |
| `entreprises.html` | Partenariat entreprise (recruter un alternant) |
| `campus.html` | Les 9 campus |
| `contact.html` | Contact + formulaire de candidature |
| `blog.html` | Blog (à venir) |

## Structure

```
site-formation/
├── index.html, formations.html, ...   ← pages générées
├── formations/                        ← fiches formation générées
├── assets/
│   ├── styles.css   ← design (bordeaux / doré, titres serif)
│   ├── main.js      ← menu mobile + formulaire
│   └── img/         ← images
└── build.py         ← générateur (contenu + gabarits)
```

## Modifier le contenu

Tout le contenu (formations, campus, textes) vit dans **`build.py`**.
Après modification, régénérer les pages :

```bash
cd site-formation
python3 build.py
```

Les fichiers `.html` sont régénérés à partir des gabarits et des données.

## Lancer en local

```bash
cd site-formation
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

## Formulaire de contact

Le formulaire (`contact.html`) est en **mode démo** (aucune donnée envoyée).
Pour un envoi réel, brancher un service comme Formspree, ou un endpoint d'API,
dans `assets/main.js` (fonction de soumission).

## À personnaliser

- **Images** : remplacer les fichiers de `assets/img/` (photos d'illustration libres).
- **Coordonnées / mentions légales** : variables en haut de `build.py`.
