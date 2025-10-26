# Le Robinet des Intelligences - Site Vitrine

Site vitrine professionnel pour la vente d'annales scolaires "Le Robinet des Intelligences".

## 📚 Description

Ce site présente et permet la vente en ligne d'annales pour les classes de Terminale dans les matières suivantes :
- **Mathématiques** (Terminale D)
- **SVT - Sciences de la Vie et de la Terre** (Terminale D)  
- **Philosophie** (Terminales A, C, D)

Chaque annale contient 15 épreuves complètes avec sujets et corrigés détaillés, conformes au nouveau programme APC 2024.

## 🚀 Déploiement sur Vercel

Ce projet est configuré pour être déployé sur Vercel avec le nom `robinetdesintelligence`.
- **Page d'accueil** attractive avec présentation des annales
- **Catalogue** complet avec filtres par matière
- **Pages détail** pour chaque livre avec informations complètes
- **Système de commande** en ligne avec formulaire détaillé
- **Page de contact** avec formulaire et FAQ
- **Design responsive** optimisé mobile et desktop
- **Interface moderne** avec Bootstrap 5 et animations CSS

## 🛠️ Technologies Utilisées

- **Backend** : Flask (Python)
- **Frontend** : HTML5, CSS3, JavaScript
- **Framework CSS** : Bootstrap 5.3.0
- **Icônes** : Font Awesome 6.4.0
- **Polices** : Google Fonts (Poppins)

## 📦 Installation

1. **Cloner le projet** (si applicable) ou utiliser les fichiers existants

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application** :
   ```bash
   python app.py
   ```

4. **Accéder au site** :
   Ouvrir http://localhost:5000 dans votre navigateur

## 📁 Structure du Projet

```
excel/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── README.md             # Documentation
├── livre/                # Images des annales
│   ├── IMG-20251026-WA0119.jpg  # SVT
│   ├── IMG-20251026-WA0120.jpg  # Maths
│   ├── IMG-20251026-WA0121.jpg  # Philosophie
│   └── ...
├── templates/            # Templates HTML
│   ├── base.html        # Template de base
│   ├── index.html       # Page d'accueil
│   ├── catalogue.html   # Page catalogue
│   ├── book_detail.html # Détail d'un livre
│   ├── contact.html     # Page de contact
│   ├── order.html       # Page de commande
│   ├── 404.html         # Page d'erreur 404
│   └── 500.html         # Page d'erreur 500
└── static/              # Fichiers statiques
    ├── css/
    │   └── style.css    # Styles personnalisés
    └── js/
        └── main.js      # JavaScript principal
```

## 🎨 Personnalisation

### Couleurs du Site
- **Primaire** : #2c5aa0 (Bleu)
- **Secondaire** : #f8b500 (Orange/Jaune)
- **Succès** : #28a745 (Vert)
- **Danger** : #dc3545 (Rouge)

### Modification des Livres
Pour ajouter/modifier des livres, éditer le dictionnaire `BOOKS_DATA` dans `app.py` :

```python
BOOKS_DATA = {
    'nouvelle_matiere': {
        'title': 'Titre de la Matière',
        'subtitle': 'Sous-titre',
        'description': 'Description',
        'class': 'Classe concernée',
        'price': 'Prix FCFA',
        'image': 'nom_image.jpg',
        'features': ['Caractéristique 1', 'Caractéristique 2']
    }
}
```

## 📞 Informations de Contact

- **Téléphone** : +229 90 15 62 76 / +229 94 82 57 55
- **Adresse** : Espoir Mavuenyegan, AGOUE, Bénin
- **Email** : contact@robinet-intelligences.com

## 🔧 Configuration de Production

Pour déployer en production :

1. **Désactiver le mode debug** dans `app.py` :
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

2. **Utiliser un serveur WSGI** comme Gunicorn :
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Configurer un reverse proxy** (Nginx recommandé)

4. **Sécuriser les communications** avec HTTPS

## 📱 Fonctionnalités Mobiles

- Design entièrement responsive
- Navigation optimisée tactile
- Formulaires adaptés mobile
- Images optimisées pour tous écrans

## 🎯 SEO et Performance

- Structure HTML sémantique
- Meta tags optimisés
- Images avec attributs alt
- Chargement optimisé des ressources
- Animations CSS performantes

## 🔒 Sécurité

- Validation des formulaires côté client et serveur
- Protection CSRF (à implémenter si nécessaire)
- Sanitisation des données utilisateur
- Gestion d'erreurs sécurisée

## 📈 Améliorations Futures

- [ ] Base de données pour les commandes
- [ ] Système de paiement en ligne
- [ ] Espace client
- [ ] Newsletter automatisée
- [ ] Analytics et statistiques
- [ ] Cache pour les performances
- [ ] API REST pour mobile

## 🤝 Support

Pour toute question ou problème :
1. Consulter cette documentation
2. Vérifier les logs d'erreur
3. Contacter l'équipe technique

---

**Développé pour Le Robinet des Intelligences - Votre partenaire de réussite scolaire** 🎓
