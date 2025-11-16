import os
from datetime import timedelta

class Config:
    """Configuração base da aplicação"""
    SQLALCHEMY_DATABASE_URI = "sqlite:///protegepet.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key-change-in-production"
    JSON_SORT_KEYS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

class DevelopmentConfig(Config):
    """Configuração para desenvolvimento"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuração para produção"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Configuração para testes"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}
