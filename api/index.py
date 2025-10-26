import os
import sys

# Ajouter le répertoire parent au path pour importer l'app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Export pour Vercel - l'app Flask elle-même
app = app
