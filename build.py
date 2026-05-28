#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur statique du site PNBS — Paris Nord Business School.
Reproduit le site (accueil, formations, fiches, alternance, entreprises,
campus, contact, blog) en pages HTML statiques partageant header/footer.

Usage :  python3 build.py
Sortie :  les fichiers .html à la racine de site-formation/ et dans formations/
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Données
# --------------------------------------------------------------------------
PHONE = "09 72 51 41 63"
EMAIL = "contact@pnbs.fr"
ADDRESS = "16-18 rue de la Poterie, 93200 Saint-Denis"

# Images servies en local (assets/img/), chemins relatifs à la racine du site.
IMG = {k: f"assets/img/{k}.jpg" for k in
       ["hero", "alt", "why", "ent", "campus", "cc", "ntc", "rem", "mbu", "t1", "t2", "t3"]}

# Icônes SVG (style trait, façon Lucide) — héritent de currentColor
ICONS = {
    "cap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/></svg>',
    "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><circle cx="12" cy="8" r="6"/><path d="M8.21 13.89 7 23l5-3 5 3-1.21-9.12"/></svg>',
    "trend": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "bag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>',
    "case": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><rect width="20" height="14" x="2" y="7" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "store": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="m2 7 2-4h16l2 4"/><path d="M4 7v13a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V7"/><path d="M2 7h20"/><path d="M9 21v-6h6v6"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-10 5L2 7"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "file": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    "euro": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M14 21a8 8 0 1 1 0-16M3 11h7M3 15h6"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M20 6 9 17l-5-5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M5 12h14M12 5l7 7-7 7"/></svg>',
    "back": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/></svg>',
    "wifi": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="1em" height="1em"><path d="M5 13a10 10 0 0 1 14 0M8.5 16.5a5 5 0 0 1 7 0M2 8.82a15 15 0 0 1 20 0"/><line x1="12" x2="12.01" y1="20" y2="20"/></svg>',
}


def icon(name):
    return ICONS.get(name, "")


# Étapes / textes partagés des fiches formation
CONDITIONS = [
    ("Dépôt de candidature", "En ligne ou par téléphone."),
    ("Étude du dossier", "Réponse sous 48 h."),
    ("Entretien de motivation", "En présentiel ou en visioconférence."),
    ("Tests de positionnement", "Pour adapter votre parcours."),
    ("Recherche d'entreprise", "Accompagnement à la recherche d'une entreprise d'accueil."),
    ("Signature du contrat", "Contrat d'apprentissage avec l'entreprise."),
    ("Délai d'accès", "De 1 à 6 mois selon la date de candidature et la signature du contrat."),
]
EVALUATION = ["Mises en situation professionnelle", "Entretien technique",
              "Présentation d'un projet professionnel", "Jury de certification"]
MODALITES = ["Présentiel", "Distanciel", "Blended learning"]
METHODES = ["Cours interactifs", "Études de cas", "Mises en situation",
            "Projets professionnels", "Accompagnement individualisé"]
MOYENS = ["Plateforme e-learning", "Supports pédagogiques numériques",
          "Outils collaboratifs", "Salles équipées"]
REMU = ["16-17 ans : 27 % à 39 % du SMIC", "18-20 ans : 43 % à 51 % du SMIC",
        "21-25 ans : 53 % à 61 % du SMIC", "26 ans et + : 100 % du SMIC"]

FORMATIONS = [
    {
        "slug": "conseiller-commercial", "abbr": "Conseiller Commercial",
        "title": "TP Conseiller Commercial", "icon": "bag", "image": IMG["cc"],
        "level": "Bac", "rncp": "RNCP 37717", "duration": "12 mois",
        "certificateur": "Ministère du Travail, du Plein Emploi et de l'Insertion",
        "intro": "Le Conseiller Commercial est un professionnel de la vente qui accompagne les clients dans leurs décisions d'achat. Il analyse les besoins, propose des solutions adaptées et assure le suivi de la relation commerciale. Cette formation vous prépare à exercer dans tous les secteurs d'activité nécessitant une force de vente.",
        "objectifs": [
            "Prospecter un secteur de vente et organiser son activité commerciale",
            "Vendre en face à face des produits et des services aux entreprises et aux particuliers",
            "Assurer le suivi de la relation client et fidéliser la clientèle",
            "Maîtriser les techniques de négociation commerciale",
        ],
        "competences": ["Prospection et développement commercial", "Techniques de vente et de négociation",
                         "Gestion de la relation client", "Analyse du marché et de la concurrence",
                         "Utilisation des outils CRM", "Communication commerciale"],
        "blocs": [
            ("Bloc 1 — Prospecter un secteur de vente", [
                "Assurer une veille professionnelle et commerciale",
                "Mettre en œuvre un plan d'actions commerciales",
                "Prospecter à distance et physiquement un secteur géographique",
                "Analyser ses performances commerciales et en rendre compte"]),
            ("Bloc 2 — Vendre en face à face", [
                "Représenter l'entreprise et contribuer à la valorisation de son image",
                "Conduire un entretien de vente",
                "Assurer le suivi de ses ventes",
                "Fidéliser en consolidant l'expérience client"]),
        ],
        "debouches": ["Conseiller commercial", "Attaché commercial", "Chargé de clientèle",
                      "Commercial terrain", "Vendeur conseil"],
        "poursuite": "TP Négociateur Technico-Commercial (Bac+2)",
        "prerequis": ["Être âgé de 16 à 29 ans révolus (sans limite d'âge pour les personnes en situation de handicap)",
                      "Niveau 3ᵉ ou équivalent", "Maîtrise des savoirs de base (lire, écrire, compter)",
                      "Motivation pour les métiers du commerce et de la vente"],
    },
    {
        "slug": "negociateur-technico-commercial", "abbr": "NTC",
        "title": "TP Négociateur Technico-Commercial", "icon": "trend", "image": IMG["ntc"],
        "level": "Bac+2", "rncp": "RNCP 39063", "duration": "12 mois",
        "certificateur": "Ministère du Travail, du Plein Emploi et de l'Insertion",
        "intro": "Le Négociateur Technico-Commercial est un expert de la relation commerciale B2B. Il développe et fidélise un portefeuille clients en proposant des solutions techniques adaptées. Véritable interface entre l'entreprise et ses clients, il combine compétences techniques et commerciales pour conclure des affaires complexes.",
        "objectifs": [
            "Élaborer une stratégie de prospection et la mettre en œuvre",
            "Négocier une solution technique et commerciale personnalisée",
            "Gérer le portefeuille client et développer le chiffre d'affaires",
            "Maîtriser les techniques de vente complexe en B2B",
        ],
        "competences": ["Stratégie de prospection multicanale", "Négociation commerciale complexe",
                         "Analyse technique des besoins clients", "Gestion de portefeuille clients B2B",
                         "Veille technologique et concurrentielle", "Pilotage de l'activité commerciale"],
        "blocs": [
            ("Bloc 1 — Élaborer une stratégie commerciale et la mettre en œuvre", [
                "Assurer une veille commerciale intégrant les enjeux du développement durable",
                "Concevoir et mettre en œuvre un plan d'actions commerciales",
                "Prospecter un secteur défini pour développer son portefeuille clients",
                "Analyser ses performances et proposer des axes d'amélioration"]),
            ("Bloc 2 — Négocier une solution et consolider l'expérience client", [
                "Représenter l'entreprise et valoriser son image",
                "Concevoir une proposition technique et commerciale",
                "Négocier une solution technique et commerciale",
                "Réaliser le bilan, ajuster son activité et consolider la relation"]),
        ],
        "debouches": ["Négociateur technico-commercial", "Technico-commercial", "Chargé d'affaires",
                      "Business Developer", "Attaché commercial B2B"],
        "poursuite": "TP Responsable d'Établissement Marchand (Bac+3)",
        "prerequis": ["Être âgé de 16 à 29 ans révolus (sans limite d'âge pour les personnes en situation de handicap)",
                      "Être titulaire d'un diplôme de niveau Bac ou équivalent",
                      "Avoir un intérêt pour les techniques de vente et la relation client",
                      "Bonne expression orale et écrite en français"],
    },
    {
        "slug": "responsable-etablissement-marchand", "abbr": "REM",
        "title": "TP Responsable d'Établissement Marchand", "icon": "store", "image": IMG["rem"],
        "level": "Bac+3", "rncp": "RNCP 38666", "duration": "12 mois",
        "certificateur": "Ministère du Travail, du Plein Emploi et de l'Insertion",
        "intro": "Le Responsable d'Établissement Marchand pilote l'activité d'un point de vente ou d'un centre de profit. Il manage une équipe, gère la performance commerciale et optimise la rentabilité de son établissement. Ce manager opérationnel assure le développement commercial tout en garantissant la satisfaction client.",
        "objectifs": [
            "Piloter l'offre produits d'un établissement marchand",
            "Manager l'équipe d'un établissement marchand",
            "Piloter la performance commerciale et financière",
            "Développer la relation client et l'attractivité du point de vente",
        ],
        "competences": ["Management d'équipe commerciale", "Pilotage de la performance commerciale",
                         "Gestion financière d'un centre de profit", "Merchandising et animation commerciale",
                         "Gestion des stocks et approvisionnements", "Leadership et communication managériale"],
        "blocs": [
            ("Bloc 1 — Piloter l'offre produits", [
                "Réaliser une veille sur les produits et services",
                "Analyser les ventes et définir les plans d'actions",
                "Construire et mettre en œuvre le plan merchandising",
                "Gérer les stocks et optimiser les approvisionnements"]),
            ("Bloc 2 — Manager l'équipe", [
                "Recruter et intégrer un collaborateur",
                "Planifier et coordonner l'activité de l'équipe",
                "Accompagner la performance individuelle et collective",
                "Conduire et animer les réunions d'équipe"]),
            ("Bloc 3 — Piloter la performance", [
                "Analyser les résultats et définir les plans d'actions",
                "Élaborer les budgets prévisionnels",
                "Assurer la gestion financière courante",
                "Développer la relation client et l'attractivité"]),
        ],
        "debouches": ["Responsable de magasin", "Responsable de point de vente", "Responsable de rayon",
                      "Chef de secteur", "Directeur adjoint de magasin"],
        "poursuite": "Master Manager de Business Unit (Bac+5)",
        "prerequis": ["Être âgé de 16 à 29 ans révolus (sans limite d'âge pour les personnes en situation de handicap)",
                      "Être titulaire d'un diplôme de niveau Bac+2 ou équivalent",
                      "Expérience dans le commerce ou la distribution (souhaitée)",
                      "Aptitudes managériales et sens de l'organisation"],
    },
    {
        "slug": "manager-business-unit", "abbr": "MBU",
        "title": "Master Manager de Business Unit", "icon": "spark", "image": IMG["mbu"],
        "level": "Bac+5", "rncp": "RNCP 35961", "duration": "24 mois",
        "certificateur": "Institut de Formation Commerciale Permanente (IFOCOP)",
        "intro": "Le Manager de Business Unit est un dirigeant opérationnel qui pilote un centre de profit ou une unité d'affaires. Il élabore la stratégie commerciale, manage les équipes, gère le budget et assure le développement de l'activité. Ce leader accompli combine vision stratégique et excellence opérationnelle.",
        "objectifs": [
            "Élaborer et déployer la stratégie commerciale d'une business unit",
            "Manager et développer les talents d'une équipe pluridisciplinaire",
            "Piloter la performance financière et opérationnelle",
            "Développer le business et conduire les projets de transformation",
        ],
        "competences": ["Stratégie commerciale et marketing", "Management stratégique des équipes",
                         "Pilotage financier et budgétaire", "Développement commercial grands comptes",
                         "Conduite du changement et transformation digitale", "Leadership et prise de décision"],
        "blocs": [
            ("Bloc 1 — Élaborer la stratégie commerciale", [
                "Réaliser un diagnostic stratégique",
                "Définir la stratégie marketing et commerciale",
                "Élaborer le business plan", "Piloter le déploiement de la stratégie"]),
            ("Bloc 2 — Manager les équipes", [
                "Définir l'organisation de la business unit",
                "Recruter, former et développer les talents",
                "Piloter la performance collective et individuelle",
                "Conduire le changement et accompagner la transformation"]),
            ("Bloc 3 — Piloter la performance financière", [
                "Élaborer et suivre les budgets", "Analyser les indicateurs de performance",
                "Optimiser la rentabilité", "Reporting et communication financière"]),
            ("Bloc 4 — Développer le business", [
                "Identifier les opportunités de développement",
                "Négocier et conclure des affaires stratégiques",
                "Développer les partenariats", "Piloter les projets de transformation digitale"]),
        ],
        "debouches": ["Manager de Business Unit", "Directeur commercial", "Directeur de centre de profit",
                      "Responsable développement commercial", "Directeur des opérations"],
        "poursuite": None,
        "prerequis": ["Être âgé de 16 à 29 ans révolus (sans limite d'âge pour les personnes en situation de handicap)",
                      "Être titulaire d'un diplôme de niveau Bac+3 ou équivalent",
                      "Expérience professionnelle en management ou commerce (souhaitée)",
                      "Capacités d'analyse, de synthèse et de leadership"],
    },
]

CAMPUS = [
    ("Paris / Saint-Denis", "16-18 rue de la Poterie, 93200 Saint-Denis", "09 72 51 41 63", False),
    ("Évry", "34 Cr Blaise Pascal, 91000 Évry-Courcouronnes", "09 72 51 41 63", False),
    ("Lille", "Au Lillenium, 2 rue du Faubourg des Postes, 59000 Lille", "03 20 29 68 94", False),
    ("Lyon", "Le Gemellyon bât. Sud, 59 bd Marius Vivier-Merle, 69003 Lyon", "07 69 19 53 25", False),
    ("Marseille", "9 bis rue Jacques Réattu, 13009 Marseille", "09 71 52 71 17", False),
    ("Rouen", "57 avenue de Bretagne, 76100 Rouen", "07 83 37 98 92", False),
    ("Toulouse", "Prochaine ouverture", "07 75 79 29 74", True),
    ("Montpellier", "Prochaine ouverture", "07 66 61 60 41", True),
    ("Bordeaux", "Prochaine ouverture", "", True),
]


# --------------------------------------------------------------------------
# Layout (header / footer / page)
# --------------------------------------------------------------------------
def R(path, depth):
    return ("../" * depth) + path


def header(active, depth):
    links = [("index.html", "Accueil"), ("formations.html", "Formations"),
             ("alternance.html", "Alternance"), ("entreprises.html", "Entreprises"),
             ("campus.html", "Campus"), ("blog.html", "Blog"), ("contact.html", "Contact")]
    items = ""
    for href, label in links:
        cls = ' class="is-active"' if href == active else ""
        items += f'<li><a href="{R(href, depth)}"{cls}>{label}</a></li>'
    return f'''<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{R("index.html", depth)}">
      <span class="brand__mark">{icon("cap")}</span>
      <span class="brand__name">PNBS<small>Paris Nord Business School</small></span>
    </a>
    <nav><ul class="nav__links" id="nav-links">{items}</ul></nav>
    <div class="nav__cta">
      <a class="btn btn--primary" href="{R("contact.html", depth)}">Candidature {icon("arrow")}</a>
      <button class="nav__toggle" id="nav-toggle" aria-label="Menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>'''


def footer(depth):
    formations = "".join(
        f'<li><a href="{R("formations/" + f["slug"] + ".html", depth)}">{f["title"].replace("TP ", "").replace("Master ", "")}</a></li>'
        for f in FORMATIONS)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="{R("index.html", depth)}">
          <span class="brand__mark">{icon("cap")}</span>
          <span class="brand__name">PNBS<small>Paris Nord Business School</small></span>
        </a>
        <p>Centre de Formation d'Apprentis spécialisé dans les métiers du commerce, de la vente et du management.</p>
        <span class="footer-qualiopi">{icon("shield")} Certifié Qualiopi</span>
      </div>
      <div>
        <h4>Formations</h4>
        <ul>{formations}</ul>
      </div>
      <div>
        <h4>Liens utiles</h4>
        <ul>
          <li><a href="{R("alternance.html", depth)}">Alternance</a></li>
          <li><a href="{R("entreprises.html", depth)}">Entreprises</a></li>
          <li><a href="{R("contact.html", depth)}">Candidature</a></li>
          <li><a href="{R("campus.html", depth)}">Campus</a></li>
          <li><a href="{R("blog.html", depth)}">Blog</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact — Paris</h4>
        <ul class="footer-contact">
          <li>{icon("pin")} <span>{ADDRESS}</span></li>
          <li>{icon("phone")} <a href="tel:+33972514163">{PHONE}</a></li>
          <li>{icon("mail")} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <p style="margin-top:14px;font-size:.84rem;">9 campus : Paris, Évry, Lille, Lyon, Marseille, Rouen, Toulouse, Montpellier, Bordeaux</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> PNBS — Paris Nord Business School. Tous droits réservés.</span>
      <span><a href="#">Mentions légales</a><a href="#">Politique de confidentialité</a></span>
    </div>
  </div>
</footer>'''


def page(title, body, active, depth, description=""):
    desc = description or "PNBS — Paris Nord Business School : CFA certifié Qualiopi, formations en alternance du Bac au Bac+5 dans le commerce, la vente et le management."
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — PNBS</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700;1,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R("assets/styles.css", depth)}">
</head>
<body>
{header(active, depth)}
<main>
{body}
</main>
{footer(depth)}
<script src="{R("assets/main.js", depth)}"></script>
</body>
</html>'''


# --------------------------------------------------------------------------
# Composants réutilisables
# --------------------------------------------------------------------------
def stats_band():
    data = [("trend", "85 %", "Taux de réussite"), ("case", "500+", "Entreprises partenaires"),
            ("users", "1 200+", "Apprenants formés"), ("pin", "9", "Campus en France")]
    cells = "".join(
        f'<div class="stat"><div class="ic">{icon(i)}</div><div class="num">{n}</div><div class="lbl">{l}</div></div>'
        for i, n, l in data)
    return f'<section class="stats-band"><div class="container"><div class="stats">{cells}</div></div></section>'


def course_card(f, depth):
    return f'''<a class="card course-card" href="{R("formations/" + f["slug"] + ".html", depth)}">
  <div class="course-card__media">
    <img src="{R(f["image"], depth)}" alt="{f["title"]}" loading="lazy">
    <span class="course-card__level">{f["level"]}</span>
  </div>
  <div class="course-card__body">
    <div class="course-card__title"><span class="ic">{icon(f["icon"])}</span><h3>{f["title"]}</h3></div>
    <p>{f["intro"][:135].rsplit(" ", 1)[0]}…</p>
    <div class="course-card__meta"><span>{icon("file")} {f["rncp"]}</span><span>{icon("clock")} {f["duration"]}</span></div>
    <span class="course-card__link">Voir la formation {icon("arrow")}</span>
  </div>
</a>'''


def cta_band(depth, title="Lancez-vous en alternance",
             text="Rejoignez PNBS dans le centre le plus proche de chez vous et démarrez votre carrière."):
    return f'''<section class="section"><div class="container">
  <div class="cta-band">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="hero__cta">
      <a class="btn btn--gold" href="{R("contact.html", depth)}">Déposer ma candidature {icon("arrow")}</a>
      <a class="btn btn--outline-light" href="tel:+33972514163">{icon("phone")} Être rappelé</a>
    </div>
  </div>
</div></section>'''


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_index():
    depth = 0
    cards = "".join(course_card(f, depth) for f in FORMATIONS)
    features = [
        ("euro", "Formation 100 % gratuite", "Aucun coût pour l'apprenant, tout est financé par l'OPCO."),
        ("trend", "Rémunération dès le 1er jour", "Un salaire calculé selon votre âge et votre année."),
        ("case", "Expérience professionnelle", "4 jours par semaine en entreprise, dès le départ."),
        ("award", "Diplôme reconnu par l'État", "Des titres certifiés RNCP, du Bac au Bac+5."),
        ("users", "Accompagnement personnalisé", "Un référent dédié tout au long du parcours."),
        ("shield", "500+ entreprises partenaires", "Un réseau pour trouver votre alternance."),
    ]
    feat = "".join(
        f'<div class="feature"><span class="ic">{icon(i)}</span><div><strong>{t}</strong><span style="font-size:.88rem;color:var(--ink-soft)">{d}</span></div></div>'
        for i, t, d in features)
    debouches = [
        ("bag", "Commerce &amp; Vente", ["Conseiller commercial", "Attaché commercial", "Chargé de clientèle"]),
        ("users", "Management", ["Responsable de magasin", "Chef de secteur", "Directeur adjoint"]),
        ("trend", "Business Development", ["Business Developer", "Chargé d'affaires", "Key Account Manager"]),
        ("spark", "Stratégie", ["Directeur commercial", "Manager de Business Unit", "Directeur des opérations"]),
    ]
    deb = "".join(
        f'<div class="card"><div class="ic">{icon(i)}</div><h3>{t}</h3><ul class="jobs">' +
        "".join(f"<li>{j}</li>" for j in jobs) + "</ul></div>"
        for i, t, jobs in debouches)
    sectors = ["Grande distribution", "Luxe &amp; Mode", "Tech &amp; Digital", "Banque &amp; Assurance",
               "Immobilier", "Restauration", "Automobile", "E-commerce"]
    sec = "".join(f'<div class="sector"><span class="ic">{icon("case")}</span>{s}</div>' for s in sectors)
    testis = [
        (IMG["t1"], "L'alternance chez PNBS m'a permis de décrocher un CDI avant même la fin de ma formation. L'accompagnement est exceptionnel.", "Sarah M.", "TP Négociateur Technico-Commercial — Bac+2"),
        (IMG["t2"], "Grâce à PNBS, j'ai pu évoluer rapidement vers un poste de responsable de magasin. La formation est très professionnalisante.", "Karim B.", "TP Responsable d'Établissement Marchand — Bac+3"),
        (IMG["t3"], "Le Master MBU m'a donné les outils stratégiques pour piloter une business unit. Une formation d'excellence.", "Julie L.", "Master Manager de Business Unit — Bac+5"),
    ]
    tst = "".join(
        f'''<div class="card testi"><img src="{img}" alt="{name}" loading="lazy"><div class="testi__body">
        <div class="stars">★★★★★</div><p class="quote">« {q} »</p>
        <div class="who"><strong>{name}</strong><span>{role}</span></div></div></div>'''
        for img, q, name, role in testis)

    body = f'''
<section class="hero"><div class="container"><div class="hero__grid">
  <div>
    <span class="badge-pill">{icon("cap")} CFA certifié Qualiopi — Du Bac au Bac+5</span>
    <h1>Formez-vous aux métiers du <span class="em">commerce</span> et du <span class="em">management</span></h1>
    <span class="lead-underline"></span>
    <p>Formations en alternance certifiées RNCP, 100 % gratuites pour l'apprenant. Rejoignez les 1 200+ apprenants qui nous font confiance.</p>
    <div class="hero__cta">
      <a class="btn btn--primary" href="formations.html">Découvrir nos formations {icon("arrow")}</a>
      <a class="btn btn--ghost" href="contact.html">Candidater</a>
    </div>
  </div>
  <div class="hero__media">
    <img src="{IMG['hero']}" alt="Apprenants PNBS en formation" loading="eager">
    <div class="float-card float-card--tr"><span class="ic ic--gold">{icon("award")}</span><div><strong style="font-size:1.05rem">Qualiopi</strong><span>Certifié qualité</span></div></div>
    <div class="float-card float-card--bl"><span class="ic ic--wine">{icon("trend")}</span><div><strong>85%</strong><span>Taux de réussite</span></div></div>
  </div>
</div></div></section>

{stats_band()}

<section class="section section--cream"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("book")} Nos parcours</span>
    <h2>Formations en <span class="em">alternance</span></h2>
    <span class="underline-gold"></span>
    <p>Du Bac au Bac+5, des parcours certifiés RNCP pour accéder aux métiers du commerce et du management.</p>
  </div>
  <div class="grid grid--2">{cards}</div>
  <div class="text-center" style="margin-top:36px"><a class="btn btn--ghost" href="formations.html">Toutes les formations {icon("arrow")}</a></div>
</div></section>

<section class="section"><div class="container">
  <div class="split">
    <div class="split__media">
      <img src="{IMG['alt']}" alt="Alternance en entreprise" loading="lazy">
      <div class="float-card float-card--bl"><span class="ic ic--wine">{icon("clock")}</span><div><strong style="font-size:1.1rem">1j / 4j</strong><span>CFA / Entreprise</span></div></div>
    </div>
    <div>
      <span class="eyebrow">{icon("clock")} Rythme alternance</span>
      <h2>L'alternance, le meilleur <span class="em">tremplin professionnel</span></h2>
      <span class="lead-underline"></span>
      <p>Chez PNBS, vous alternez 1 jour en CFA et 4 jours en entreprise. Rémunéré, formé et accompagné vers l'emploi dès le premier jour.</p>
      <a class="btn btn--primary" href="alternance.html">Tout savoir sur l'alternance {icon("arrow")}</a>
    </div>
  </div>
</div></section>

<section class="section section--cream"><div class="container">
  <div class="split split--reverse">
    <div class="split__media">
      <img src="{IMG['why']}" alt="Campus PNBS" loading="lazy">
      <div class="float-card float-card--bl"><span class="ic ic--wine">{icon("pin")}</span><div><strong style="font-size:1.1rem">9 campus</strong><span>partout en France</span></div></div>
    </div>
    <div>
      <span class="eyebrow">{icon("award")} Nos engagements</span>
      <h2>Pourquoi choisir <span class="em">PNBS</span> ?</h2>
      <span class="lead-underline"></span>
      <p>Nos formations sont conçues pour répondre aux besoins réels des entreprises et garantir une insertion professionnelle rapide.</p>
      <div class="feature-list">{feat}</div>
    </div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("target")} Débouchés</span>
    <h2>Des métiers qui <span class="em-gold">recrutent</span></h2>
    <span class="underline-gold"></span>
    <p>Nos formations ouvrent les portes des secteurs les plus dynamiques du marché.</p>
  </div>
  <div class="grid grid--4">{deb}</div>
</div></section>

<section class="section section--cream"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("shield")} Nos partenaires</span>
    <h2>500+ entreprises nous font <span class="em">confiance</span></h2>
    <span class="underline-gold"></span>
    <p>Grandes enseignes, PME et start-ups : nos partenaires recrutent nos apprenants en alternance dans toute la France.</p>
  </div>
  <div class="pill-grid">{sec}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("award")} Témoignages</span>
    <h2>Ils ont choisi <span class="em">PNBS</span></h2>
    <span class="underline-gold"></span>
    <p>Ce que nos apprenants disent de leur expérience.</p>
  </div>
  <div class="grid grid--3">{tst}</div>
</div></section>

{cta_band(depth)}
'''
    return page("Accueil", body, "index.html", depth)


def build_formations():
    depth = 0
    cards = "".join(course_card(f, depth) for f in FORMATIONS)
    body = f'''
<section class="page-hero"><div class="container">
  <span class="eyebrow">{icon("book")} Nos parcours</span>
  <h1>Nos formations en <span class="em-gold">alternance</span></h1>
  <p>Du Bac au Bac+5, 4 titres certifiés RNCP pour construire votre carrière dans le commerce, la vente et le management. 100 % gratuites pour l'apprenant.</p>
  <span class="underline-gold"></span>
</div></section>
<section class="section section--cream"><div class="container">
  <div class="grid grid--2">{cards}</div>
</div></section>
{cta_band(depth)}
'''
    return page("Formations", body, "formations.html", depth)


def build_formation_detail(f):
    depth = 1
    objs = "".join(f"<li>{o}</li>" for o in f["objectifs"])
    comp = "".join(f'<div class="chip">{c}</div>' for c in f["competences"])
    blocs = "".join(
        f'<div class="bloc"><h4>{t}</h4><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"
        for t, items in f["blocs"])
    evalu = "".join(f"<li>{e}</li>" for e in EVALUATION)
    deb = "".join(f'<div class="chip">{d}</div>' for d in f["debouches"])
    prereq = "".join(f"<li>{p}</li>" for p in f["prerequis"])
    steps = "".join(
        f'<div class="step"><div class="step__num">{n:02d}</div><div><strong>{t}</strong>{d}</div></div>'
        for n, (t, d) in enumerate(CONDITIONS, 1))
    moda = "".join(f'<div class="chip">{m}</div>' for m in MODALITES)
    meth = "".join(f"<li>{m}</li>" for m in METHODES)
    moy = "".join(f"<li>{m}</li>" for m in MOYENS)
    remu = "".join(f"<li>{r}</li>" for r in REMU)
    poursuite = ""
    if f["poursuite"]:
        poursuite = f'''<div class="info-card" style="margin-top:24px"><h3>{icon("arrow")} Poursuite d'études</h3>
        <p style="margin:0">{f["poursuite"]}</p></div>'''

    body = f'''
<section class="fhero"><div class="container">
  <a class="breadcrumb" href="../formations.html">{icon("back")} Retour aux formations</a>
  <div class="fhero__tags">
    <span class="tag tag--gold">{f["level"]}</span>
    <span class="tag">{icon("file")} {f["rncp"]}</span>
    <span class="tag">{icon("clock")} {f["duration"]}</span>
  </div>
  <h1>{f["title"]}</h1>
  <p>{f["intro"]}</p>
  <div class="fhero__cta">
    <a class="btn btn--gold" href="../contact.html">Déposer ma candidature {icon("arrow")}</a>
    <a class="btn btn--outline-light" href="tel:+33972514163">{icon("phone")} Être rappelé</a>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="split">
    <div>
      <span class="eyebrow">{icon("target")} Objectifs pédagogiques</span>
      <h2>Ce que vous saurez <span class="em">faire</span></h2>
      <span class="lead-underline"></span>
      <ul class="check-list">{objs}</ul>
    </div>
    <div class="info-card">
      <h3>{icon("award")} Compétences développées</h3>
      <div class="tag-row">{comp}</div>
    </div>
  </div>
</div></section>

<section class="section section--cream"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("book")} Programme</span>
    <h2>Programme de <span class="em">formation</span></h2>
    <span class="underline-gold"></span>
  </div>
  <div style="max-width:820px;margin:0 auto">{blocs}</div>
  <div class="grid grid--2" style="max-width:820px;margin:28px auto 0">
    <div class="info-card"><h3>{icon("check")} Modalités d'évaluation</h3><ul class="check-list">{evalu}</ul></div>
    <div class="info-card"><h3>{icon("case")} Débouchés professionnels</h3><div class="tag-row">{deb}</div>{poursuite}</div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("check")} Admission</span>
    <h2>Prérequis &amp; conditions d'<span class="em">accès</span></h2>
    <span class="underline-gold"></span>
  </div>
  <div class="split" style="align-items:start">
    <div class="info-card"><h3>{icon("check")} Prérequis</h3><ul class="check-list">{prereq}</ul></div>
    <div class="steps">{steps}</div>
  </div>
</div></section>

<section class="section section--cream"><div class="container">
  <div class="grid grid--3">
    <div class="info-card">
      <h3>{icon("clock")} Durée &amp; rythme</h3>
      <div class="info-row"><span class="k">Durée</span><span class="v">{f["duration"]}</span></div>
      <div class="info-row"><span class="k">Rythme</span><span class="v">1j CFA / 4j entreprise</span></div>
      <h3 style="margin-top:18px">{icon("book")} Modalités</h3>
      <div class="tag-row">{moda}</div>
    </div>
    <div class="info-card"><h3>{icon("users")} Méthodes pédagogiques</h3><ul class="check-list">{meth}</ul></div>
    <div class="info-card"><h3>{icon("wifi")} Moyens pédagogiques</h3><ul class="check-list">{moy}</ul></div>
  </div>
  <div class="grid grid--3" style="margin-top:24px">
    <div class="info-card">
      <h3>{icon("award")} Certification</h3>
      <div class="info-row"><span class="k">Niveau</span><span class="v">{f["level"]}</span></div>
      <div class="info-row"><span class="k">Code</span><span class="v">{f["rncp"]}</span></div>
      <div class="info-row"><span class="k">Certificateur</span><span class="v" style="font-size:.82rem">{f["certificateur"]}</span></div>
    </div>
    <div class="price-box">
      <div class="big">100 % GRATUIT</div>
      <p>Formation financée par l'OPCO de l'entreprise dans le cadre du contrat d'apprentissage.</p>
      <h3 style="color:#fff;border:0;justify-content:center;margin:18px 0 6px">{icon("euro")} Rémunération</h3>
      <ul style="list-style:none;padding:0;margin:0;text-align:left;font-size:.86rem;color:rgba(255,255,255,.9)">{remu}</ul>
    </div>
    <div class="result-stat">
      <div class="eyebrow" style="justify-content:center">{icon("trend")} Indicateurs 2024</div>
      <div class="num">85 %</div>
      <div class="lbl">Taux de réussite</div>
      <p style="font-size:.78rem;color:var(--muted);margin-top:14px">Données mises à jour annuellement. Indicateurs conformes aux exigences Qualiopi.</p>
    </div>
  </div>
  <p class="text-center" style="margin-top:28px;font-size:.86rem;color:var(--ink-soft)">
    <strong>Accessibilité</strong> — Nos formations sont accessibles aux personnes en situation de handicap. Un référent handicap étudie les aménagements possibles. Contact : {EMAIL} — {PHONE}
  </p>
</div></section>

{cta_band(depth, title=f"Intéressé par le {f['abbr']} ?", text="Déposez votre candidature en ligne ou faites-vous rappeler par un conseiller.")}
'''
    return page(f["title"], body, "formations.html", depth, description=f["intro"][:155])


def build_alternance():
    depth = 0
    rows = [("16-17 ans", "27 % SMIC", "39 % SMIC"), ("18-20 ans", "43 % SMIC", "51 % SMIC"),
            ("21-25 ans", "53 % SMIC", "61 % SMIC"), ("26 ans et +", "100 % SMIC", "100 % SMIC")]
    table = "".join(f'<div class="info-row"><span class="k">{a}</span><span class="v">{y1} · {y2}</span></div>' for a, y1, y2 in rows)
    legal = [
        ("file", "Cadre légal", "Le contrat d'apprentissage est un contrat de travail (CDD ou CDI) encadré par le Code du travail (art. L6211-1 à L6261-2). L'apprenti bénéficie des mêmes droits que les autres salariés."),
        ("users", "Âge et conditions", "Ouvert aux jeunes de 16 à 29 ans révolus. Des dérogations existent (handicap sans limite d'âge, créateurs d'entreprise, sportifs de haut niveau)."),
        ("clock", "Durée du contrat", "De 6 mois à 3 ans selon le diplôme préparé, adaptable selon le niveau initial de l'apprenti et ses acquis."),
        ("shield", "Protection sociale", "Même protection que les autres salariés : sécurité sociale, mutuelle, congés payés (5 semaines min.) et congés pour examens."),
        ("euro", "Aides financières", "Jusqu'à 6 000 € d'aide de l'État pour l'entreprise. Formation intégralement financée par l'OPCO de la branche."),
        ("award", "Certification Qualiopi", "PNBS est certifié Qualiopi (« Actions de formation par apprentissage ») selon les 7 critères du Référentiel National Qualité."),
    ]
    legal_cards = "".join(
        f'<div class="card"><div class="ic">{icon(i)}</div><h3>{t}</h3><p>{d}</p></div>'
        for i, t, d in legal)
    body = f'''
<section class="page-hero"><div class="container">
  <span class="eyebrow">{icon("clock")} L'alternance chez PNBS</span>
  <h1>Un rythme unique : <span class="em-gold">1 jour</span> en CFA, <span class="em-gold">4 jours</span> en entreprise</h1>
  <p>La meilleure façon d'apprendre un métier. 85 % de réussite en 2024.</p>
  <span class="underline-gold"></span>
</div></section>

{stats_band()}

<section class="section"><div class="container">
  <div class="grid grid--4">
    <div class="card"><div class="ic">{icon("euro")}</div><h3>Rémunération</h3><p>Salaire dès le 1ᵉʳ jour, selon votre âge.</p></div>
    <div class="card"><div class="ic">{icon("cap")}</div><h3>Formation gratuite</h3><p>100 % financée par l'OPCO de l'entreprise.</p></div>
    <div class="card"><div class="ic">{icon("case")}</div><h3>Expérience pro</h3><p>4 jours par semaine en entreprise.</p></div>
    <div class="card"><div class="ic">{icon("award")}</div><h3>Diplôme RNCP</h3><p>Un titre reconnu par l'État.</p></div>
  </div>
</div></section>

<section class="section section--cream"><div class="container">
  <div class="split">
    <div>
      <span class="eyebrow">{icon("euro")} Rémunération de l'apprenti</span>
      <h2>Un salaire dès le <span class="em">premier jour</span></h2>
      <span class="lead-underline"></span>
      <p>La rémunération est calculée en pourcentage du SMIC, selon l'âge et l'année de formation. Chez PNBS, nos apprentis perçoivent entre 775 € et 1 802 € par mois (hors primes commerciales).</p>
    </div>
    <div class="info-card">
      <h3>{icon("euro")} Grille de rémunération</h3>
      <div class="info-row"><span class="k" style="font-weight:700;color:var(--ink)">Âge</span><span class="v">1ʳᵉ · 2ᵉ année</span></div>
      {table}
    </div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("shield")} Cadre légal</span>
    <h2>La réglementation de l'<span class="em">alternance</span></h2>
    <span class="underline-gold"></span>
    <p>Tout ce qu'il faut savoir sur le contrat d'apprentissage et les garanties qualité de PNBS.</p>
  </div>
  <div class="grid grid--3">{legal_cards}</div>
</div></section>

{cta_band(depth)}
'''
    return page("Alternance", body, "alternance.html", depth)


def build_entreprises():
    depth = 0
    stats = [("500+", "Entreprises partenaires"), ("1 200+", "Apprenants formés"),
             ("85%", "Taux d'insertion en CDI"), ("4.8/5", "Satisfaction entreprises")]
    st = "".join(f'<div class="stat"><div class="num">{n}</div><div class="lbl">{l}</div></div>' for n, l in stats)
    advantages = [
        ("euro", "Formation 100 % financée", "La formation de votre apprenti est intégralement prise en charge par votre OPCO. Zéro coût pédagogique."),
        ("award", "Jusqu'à 6 000 € d'aide", "Aide de l'État à l'embauche d'un apprenti, cumulable avec les exonérations de cotisations sociales."),
        ("users", "Candidats pré-sélectionnés", "Des profils motivés et qualifiés, adaptés à vos besoins. Fini les CV non pertinents."),
        ("clock", "Rythme 1j CFA / 4j entreprise", "Votre apprenti est présent 80 % du temps en entreprise — l'un des rythmes les plus favorables."),
        ("shield", "Suivi pédagogique continu", "Un référent dédié assure le lien entre l'entreprise, l'apprenant et PNBS tout au long du contrat."),
        ("file", "Accompagnement administratif", "PNBS gère contrat, dépôt OPCO et conventions. Un interlocuteur unique."),
    ]
    adv = "".join(f'<div class="card"><div class="ic">{icon(i)}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in advantages)
    steps_data = [
        ("Exprimez votre besoin", "Contactez-nous par téléphone, email ou formulaire. Nous analysons votre besoin en compétences et définissons le profil idéal."),
        ("Recevez des candidatures ciblées", "Sous 48 h, nous vous proposons des profils pré-sélectionnés correspondant à vos critères. Job Dating sur demande."),
        ("Signez le contrat", "Nous gérons toutes les démarches administratives : contrat d'apprentissage, dépôt OPCO, formalités légales."),
        ("Lancez la formation", "Votre apprenti démarre son parcours en alternance, accompagné par un référent PNBS dédié."),
    ]
    steps = "".join(f'<div class="step"><div class="step__num">{n:02d}</div><div><strong>{t}</strong>{d}</div></div>'
                    for n, (t, d) in enumerate(steps_data, 1))
    body = f'''
<section class="fhero"><div class="container">
  <span class="eyebrow" style="color:var(--gold-soft)">{icon("case")} Partenariat entreprise</span>
  <h1>Recrutez vos futurs talents avec <span class="em-gold">PNBS</span></h1>
  <p>Plus de 500 entreprises nous font déjà confiance. Formation financée, candidats qualifiés, accompagnement de A à Z : l'alternance n'a jamais été aussi simple.</p>
  <div class="fhero__cta">
    <a class="btn btn--gold" href="contact.html">Recruter un alternant {icon("arrow")}</a>
    <a class="btn btn--outline-light" href="tel:+33972514163">{icon("phone")} {PHONE}</a>
  </div>
</div></section>

<section class="stats-band"><div class="container"><div class="stats">{st}</div></div></section>

<section class="section"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("target")} Vos avantages</span>
    <h2>Pourquoi recruter avec <span class="em">PNBS</span> ?</h2>
    <span class="underline-gold"></span>
    <p>L'alternance est un investissement stratégique. PNBS vous offre un accompagnement complet pour en maximiser les bénéfices.</p>
  </div>
  <div class="grid grid--3">{adv}</div>
</div></section>

<section class="section section--cream"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("check")} Processus</span>
    <h2>Comment ça <span class="em">marche</span> ?</h2>
    <span class="underline-gold"></span>
    <p>En 4 étapes simples, recrutez votre apprenti et lancez la formation.</p>
  </div>
  <div class="steps" style="max-width:780px;margin:0 auto">{steps}</div>
</div></section>

{cta_band(depth, title="Prêt à recruter votre alternant ?", text="Exprimez votre besoin : nous vous proposons des profils qualifiés sous 48 h.")}
'''
    return page("Entreprises", body, "entreprises.html", depth)


def build_campus():
    depth = 0
    cards = ""
    for name, addr, tel, soon in CAMPUS:
        soon_badge = '<span class="soon">Prochaine ouverture</span>' if soon else ''
        addr_html = "" if soon else f'<p>{icon("pin")} {addr}</p>'
        tel_html = f'<p style="margin-top:8px">{icon("phone")} <a href="tel:{tel.replace(" ", "")}">{tel}</a></p>' if tel else ''
        cards += f'''<div class="campus-card">
        <h3>{icon("pin")} {name} {soon_badge}</h3>{addr_html}{tel_html}</div>'''
    facilities = ["Salles équipées dernière génération", "Connexion Wi-Fi haut débit",
                  "Espaces de coworking collaboratifs", "Espaces de détente"]
    fac = "".join(f"<li>{f}</li>" for f in facilities)
    body = f'''
<section class="page-hero"><div class="container">
  <span class="eyebrow">{icon("pin")} Nos campus</span>
  <h1>9 campus en <span class="em-gold">France</span></h1>
  <p>Dont 6 ouverts et 3 prochaines ouvertures. Un environnement d'apprentissage moderne, au plus près de nos apprenants et entreprises partenaires.</p>
  <span class="underline-gold"></span>
</div></section>

<section class="section"><div class="container">
  <div class="split">
    <div>
      <span class="eyebrow">{icon("wifi")} Cadre de travail</span>
      <h2>Un environnement d'apprentissage <span class="em">moderne</span></h2>
      <span class="lead-underline"></span>
      <p>Nos campus offrent un cadre stimulant et professionnel, conçu pour favoriser l'apprentissage et les échanges entre apprenants.</p>
      <ul class="check-list">{fac}</ul>
    </div>
    <div class="split__media">
      <img src="{IMG['campus']}" alt="Campus PNBS" loading="lazy">
      <div class="float-card float-card--bl"><span class="ic ic--wine">{icon("clock")}</span><div><strong style="font-size:1.1rem">1j / 4j</strong><span>CFA / Entreprise</span></div></div>
    </div>
  </div>
</div></section>

<section class="section section--cream"><div class="container">
  <div class="section__head">
    <span class="eyebrow">{icon("pin")} Tous nos centres</span>
    <h2>Trouvez le campus le plus <span class="em">proche</span></h2>
    <span class="underline-gold"></span>
  </div>
  <div class="grid grid--3">{cards}</div>
</div></section>

{cta_band(depth, title="Visitez notre campus", text="Prenez rendez-vous pour découvrir nos locaux et échanger avec nos conseillers.")}
'''
    return page("Campus", body, "campus.html", depth)


def build_contact():
    depth = 0
    options = "".join(f'<option>{f["title"]}</option>' for f in FORMATIONS)
    body = f'''
<section class="page-hero"><div class="container">
  <span class="eyebrow">{icon("mail")} Contact &amp; candidature</span>
  <h1>Déposez votre <span class="em-gold">candidature</span></h1>
  <p>Une question, une candidature, un projet de recrutement ? Notre équipe vous répond sous 48 h.</p>
  <span class="underline-gold"></span>
</div></section>

<section class="section"><div class="container">
  <div class="contact-grid">
    <form class="form-card" id="contact-form" novalidate>
      <h3 style="font-family:var(--serif);font-size:1.4rem;margin-bottom:18px">Votre demande</h3>
      <div class="form-row">
        <div class="form-field"><label for="prenom">Prénom *</label><input id="prenom" name="prenom" required></div>
        <div class="form-field"><label for="nom">Nom *</label><input id="nom" name="nom" required></div>
      </div>
      <div class="form-row">
        <div class="form-field"><label for="email">Email *</label><input id="email" name="email" type="email" required></div>
        <div class="form-field"><label for="tel">Téléphone *</label><input id="tel" name="tel" type="tel" required></div>
      </div>
      <div class="form-field">
        <label for="profil">Vous êtes *</label>
        <select id="profil" name="profil" required>
          <option value="">— Sélectionnez —</option>
          <option>Candidat / futur apprenant</option>
          <option>Entreprise (recrutement d'un alternant)</option>
          <option>Autre</option>
        </select>
      </div>
      <div class="form-field">
        <label for="formation">Formation souhaitée</label>
        <select id="formation" name="formation">
          <option value="">— Indifférent / à définir —</option>
          {options}
        </select>
      </div>
      <div class="form-field"><label for="message">Votre message</label><textarea id="message" name="message" placeholder="Parlez-nous de votre projet…"></textarea></div>
      <p class="form-note">* Champs obligatoires. Vos données ne sont utilisées que pour traiter votre demande.</p>
      <button type="submit" class="btn btn--primary" style="margin-top:8px">Envoyer ma demande {icon("arrow")}</button>
      <div class="form-msg" id="form-msg" role="status"></div>
    </form>

    <aside class="contact-aside">
      <h3 style="font-family:var(--serif);font-size:1.4rem">Nous joindre</h3>
      <ul>
        <li><span class="ic">{icon("phone")}</span><div><strong>Téléphone</strong><span><a href="tel:+33972514163">{PHONE}</a></span></div></li>
        <li><span class="ic">{icon("mail")}</span><div><strong>Email</strong><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div></li>
        <li><span class="ic">{icon("pin")}</span><div><strong>Campus de Paris</strong><span>{ADDRESS}</span></div></li>
        <li><span class="ic">{icon("clock")}</span><div><strong>Horaires</strong><span>Lun. – Ven. · 9h – 18h</span></div></li>
      </ul>
      <div class="info-card" style="margin-top:22px;background:var(--cream)">
        <h3>{icon("shield")} Certifié Qualiopi</h3>
        <p style="margin:0;font-size:.92rem">PNBS est certifié au titre des « Actions de formation par apprentissage », gage de la qualité de nos parcours.</p>
      </div>
    </aside>
  </div>
</div></section>
'''
    return page("Contact", body, "contact.html", depth)


def build_blog():
    depth = 0
    body = f'''
<section class="page-hero"><div class="container">
  <span class="eyebrow">{icon("book")} Blog</span>
  <h1>Le blog <span class="em-gold">PNBS</span></h1>
  <p>Conseils alternance, métiers du commerce, actualités du CFA : nos articles arrivent très bientôt.</p>
  <span class="underline-gold"></span>
</div></section>
<section class="section"><div class="container text-center">
  <div class="info-card" style="max-width:620px;margin:0 auto">
    <div class="ic card" style="display:inline-grid;background:var(--wine);color:#fff;width:64px;height:64px;border:0;margin-bottom:18px;box-shadow:none">{icon("book")}</div>
    <h2>Articles en préparation</h2>
    <p>Notre équipe rédige actuellement les premiers articles. En attendant, contactez-nous pour toute question sur nos formations.</p>
    <a class="btn btn--primary" href="contact.html">Nous contacter {icon("arrow")}</a>
  </div>
</div></section>
'''
    return page("Blog", body, "blog.html", depth)


# --------------------------------------------------------------------------
# Écriture
# --------------------------------------------------------------------------
def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("écrit :", rel)


def main():
    write("index.html", build_index())
    write("formations.html", build_formations())
    write("alternance.html", build_alternance())
    write("entreprises.html", build_entreprises())
    write("campus.html", build_campus())
    write("contact.html", build_contact())
    write("blog.html", build_blog())
    for f in FORMATIONS:
        write(f"formations/{f['slug']}.html", build_formation_detail(f))
    print("\nOK — site PNBS généré.")


if __name__ == "__main__":
    main()
