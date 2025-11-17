"""
Flask application entry point
Main application initialization, configuration, and Blueprint registration
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import config
from database.models import db
from routes.animals_routes import animals_bp
from routes.adoption_routes import adoption_bp
from routes.address_routes import address_bp
from routes.contact_routes import contact_bp, feedback_bp

def create_app(config_name: str = None) -> Flask:
    """
    Application factory function
    
    Args:
        config_name: Configuração a usar ('development', 'production', 'testing')
                     Se None, usa variável de ambiente FLASK_ENV
    
    Returns:
        Flask application instance
    """
    # Define configuração
    if config_name is None:
        config_name = os.getenv("FLASK_ENV", "development")
    
    # Cria aplicação Flask
    app = Flask(__name__)
    
    # Carrega configuração
    app.config.from_object(config[config_name])
    
    # Inicializa extensões
    db.init_app(app)
    CORS(app, 
         origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:3000"],
         supports_credentials=True,
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization"])
    
    # Registra blueprints
    app.register_blueprint(animals_bp)
    app.register_blueprint(adoption_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(feedback_bp)
    
    # Contexto de aplicação para operações de banco de dados
    with app.app_context():
        db.create_all()
    
    # Health check endpoint
    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "ok", "message": "Server is running"}), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "message": "Recurso não encontrado", "data": None}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"success": False, "message": "Erro interno do servidor", "data": None}), 500
    
    return app

if __name__ == "__main__":
    # Executa servidor de desenvolvimento
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=3001,
        debug=True
    )
