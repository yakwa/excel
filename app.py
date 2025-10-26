from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
from datetime import datetime
from config import config

app = Flask(__name__)

# Configuration de l'application
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# Configuration des dossiers
UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']

# Données des livres (basées sur les images observées)
BOOKS_DATA = {
    'svt': {
        'title': 'SVT - Sciences de la Vie et de la Terre',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminale D',
        'price': '2500 FCFA',
        'image': 'IMG-20251026-WA0119.jpg',
        'features': [
            '15 épreuves complètes',
            'Corrigés détaillés',
            'Nouveau programme 2024',
            'Préparation APC 100%'
        ]
    },
    'maths': {
        'title': 'MATHS - Mathématiques',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminale D',
        'price': '3000 FCFA',
        'image': 'IMG-20251026-WA0120.jpg',
        'features': [
            '15 épreuves complètes',
            'Corrigés détaillés',
            'Formules essentielles',
            'Méthodes de résolution'
        ]
    },
    'philosophie': {
        'title': 'PHILOSOPHIE',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2500 FCFA',
        'image': 'IMG-20251026-WA0121.jpg',
        'features': [
            '15 épreuves complètes',
            'Dissertations corrigées',
            'Méthodes philosophiques',
            'Auteurs au programme'
        ]
    },
    'francais': {
        'title': 'FRANÇAIS',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2500 FCFA',
        'image': 'IMG-20251026-WA0122.jpg',
        'features': [
            '15 épreuves complètes',
            'Commentaires corrigés',
            'Techniques de rédaction',
            'Œuvres au programme'
        ]
    },
    'anglais': {
        'title': 'ANGLAIS',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2500 FCFA',
        'image': 'IMG-20251026-WA0123.jpg',
        'features': [
            '15 épreuves complètes',
            'Corrigés détaillés',
            'Grammaire et vocabulaire',
            'Expression écrite'
        ]
    },
    'histoire_geo': {
        'title': 'HISTOIRE-GÉOGRAPHIE',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2500 FCFA',
        'image': 'IMG-20251026-WA0124.jpg',
        'features': [
            '15 épreuves complètes',
            'Cartes et schémas',
            'Chronologies détaillées',
            'Méthodes de dissertation'
        ]
    },
    'physique_chimie': {
        'title': 'PHYSIQUE-CHIMIE',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminale D',
        'price': '3000 FCFA',
        'image': 'IMG-20251026-WA0125.jpg',
        'features': [
            '15 épreuves complètes',
            'Corrigés détaillés',
            'Formules et constantes',
            'Exercices pratiques'
        ]
    },
    'espagnol': {
        'title': 'ESPAGNOL',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2500 FCFA',
        'image': 'IMG-20251026-WA0126.jpg',
        'features': [
            '15 épreuves complètes',
            'Corrigés détaillés',
            'Grammaire et conjugaison',
            'Civilisation hispanique'
        ]
    },
    'allemand': {
        'title': 'ALLEMAND',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2500 FCFA',
        'image': 'IMG-20251026-WA0127.jpg',
        'features': [
            '15 épreuves complètes',
            'Corrigés détaillés',
            'Grammaire allemande',
            'Culture germanique'
        ]
    },
    'edhc': {
        'title': 'EDHC - Éducation aux Droits de l\'Homme',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2000 FCFA',
        'image': 'IMG-20251026-WA0128.jpg',
        'features': [
            '15 épreuves complètes',
            'Corrigés détaillés',
            'Droits et devoirs',
            'Citoyenneté active'
        ]
    },
    'eps': {
        'title': 'EPS - Éducation Physique et Sportive',
        'subtitle': '15 Épreuves pour tout le Programme',
        'description': 'Sujets et Corrigés - Nouveau programme APC 2024',
        'class': 'Terminales A,C,D',
        'price': '2000 FCFA',
        'image': 'IMG-20251026-WA0129.jpg',
        'features': [
            '15 épreuves complètes',
            'Théorie du sport',
            'Anatomie et physiologie',
            'Règlements sportifs'
        ]
    },
    'maths_complementaires': {
        'title': 'MATHS COMPLÉMENTAIRES',
        'subtitle': '15 Épreuves Spécialisées',
        'description': 'Sujets et Corrigés - Niveau avancé APC 2024',
        'class': 'Terminale D',
        'price': '3500 FCFA',
        'image': 'IMG-20251026-WA0130.jpg',
        'features': [
            '15 épreuves avancées',
            'Corrigés très détaillés',
            'Exercices complexes',
            'Préparation concours'
        ]
    }
}

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html', books=BOOKS_DATA)

@app.route('/catalogue')
def catalogue():
    """Page catalogue des livres"""
    return render_template('catalogue.html', books=BOOKS_DATA)

@app.route('/livre/<book_id>')
def book_detail(book_id):
    """Page détail d'un livre"""
    if book_id not in BOOKS_DATA:
        return render_template('404.html'), 404
    book = BOOKS_DATA[book_id]
    return render_template('book_detail.html', book=book, book_id=book_id, books=BOOKS_DATA)

@app.route('/about')
def about():
    """Page à propos"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Page de contact"""
    return render_template('contact.html')

@app.route('/commander/<book_id>')
def order(book_id):
    """Page de commande"""
    if book_id not in BOOKS_DATA:
        return render_template('404.html'), 404
    book = BOOKS_DATA[book_id]
    return render_template('order.html', book=book, book_id=book_id)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    """API pour traiter les messages de contact"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Ici vous pourriez sauvegarder en base de données ou envoyer un email
        # Pour l'instant, on simule juste la réception
        
        return jsonify({
            'success': True,
            'message': 'Votre message a été envoyé avec succès!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Erreur lors de l\'envoi du message.'
        }), 500

@app.route('/api/order', methods=['POST'])
def api_order():
    """API pour traiter les commandes"""
    try:
        data = request.get_json()
        book_id = data.get('book_id')
        customer_name = data.get('name')
        customer_phone = data.get('phone')
        customer_email = data.get('email')
        quantity = data.get('quantity', 1)
        
        if book_id not in BOOKS_DATA:
            return jsonify({
                'success': False,
                'message': 'Livre non trouvé.'
            }), 404
        
        book = BOOKS_DATA[book_id]
        
        # Ici vous pourriez sauvegarder la commande en base de données
        # et envoyer des notifications
        
        return jsonify({
            'success': True,
            'message': f'Commande reçue pour {book["title"]}. Nous vous contacterons bientôt!',
            'order_details': {
                'book': book['title'],
                'quantity': quantity,
                'total': book['price'],
                'contact_phone': '+228 90 15 62 76'
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Erreur lors de la commande.'
        }), 500

@app.route('/images/<filename>')
def serve_image(filename):
    """Servir les images des livres"""
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Pour Vercel
def handler(request):
    return app(request.environ, lambda status, headers: None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
