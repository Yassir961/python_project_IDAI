import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    
    # Configuration de la base de données MySQL
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:@localhost/auth_python"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


