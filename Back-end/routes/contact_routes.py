from flask import Blueprint, request
from database.models import db, Contact, Feedback
from utils.response_builder import build_response
from utils.error_handlers import handle_error

contact_bp = Blueprint("contact", __name__, url_prefix="/contact")

@contact_bp.route("", methods=["POST"])
def create_contact():
    """POST /contact - Recebe mensagem de contato"""
    try:
        data = request.get_json()
        
        required_fields = ["name", "email", "message"]
        if not all(field in data for field in required_fields):
            return build_response(
                success=False,
                message="Campos obrigatórios faltando"
            ), 400
        
        contact = Contact(
            name=data.get("name"),
            email=data.get("email"),
            subject=data.get("subject"),
            message=data.get("message")
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return build_response(
            success=True,
            message="Mensagem de contato recebida com sucesso",
            data=contact.to_dict()
        ), 201
    except Exception as e:
        db.session.rollback()
        return handle_error(e, "Erro ao receber mensagem de contato")

feedback_bp = Blueprint("feedback", __name__, url_prefix="/feedback")

@feedback_bp.route("", methods=["POST"])
def create_feedback():
    """POST /feedback - Recebe feedback do usuário"""
    try:
        data = request.get_json()
        
        if "mensagem" not in data or not data.get("mensagem"):
            return build_response(
                success=False,
                message="Mensagem não pode estar vazia"
            ), 400
        
        feedback = Feedback(
            mensagem=data.get("mensagem")
        )
        
        db.session.add(feedback)
        db.session.commit()
        
        return build_response(
            success=True,
            message="Feedback recebido com sucesso",
            data=feedback.to_dict()
        ), 201
    except Exception as e:
        db.session.rollback()
        return handle_error(e, "Erro ao receber feedback")
