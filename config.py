import os
from datetime import timedelta

class Config:
    """Configuration de base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'robinet-des-intelligences-2024-super-secret-key'
    
    # Configuration Flask
    DEBUG = False
    TESTING = False
    
    # Configuration des fichiers
    UPLOAD_FOLDER = 'livre'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Configuration de session
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    
    # Configuration email (pour les notifications)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Informations de contact
    CONTACT_PHONE_1 = '+228 90 15 62 76'
    CONTACT_EMAIL = 'contact@robinet-intelligences.com'
    CONTACT_ADDRESS = 'Lomé, Togo'
    
    # Configuration des prix (en FCFA)
    DELIVERY_FREE_THRESHOLD = 0  # Livraison gratuite à partir de 0 FCFA
    DELIVERY_COST = 0  # Coût de livraison standard

class DevelopmentConfig(Config):
    """Configuration pour le développement"""
    DEBUG = True
    
class ProductionConfig(Config):
    """Configuration pour la production"""
    DEBUG = False
    
    # En production, utiliser des variables d'environnement
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'robinet-des-intelligences-prod-key-2024'
    
    # Configuration de sécurité
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Configuration spécifique à Vercel
    UPLOAD_FOLDER = '/tmp'  # Vercel utilise /tmp pour les fichiers temporaires

class TestingConfig(Config):
    """Configuration pour les tests"""
    TESTING = True
    DEBUG = True

# Configuration par défaut
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
