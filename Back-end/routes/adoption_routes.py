from flask import Blueprint, request
from database.models import db, Adoption, Animal
from utils.response_builder import build_response
from utils.error_handlers import handle_error

adoption_bp = Blueprint("adoptions", __name__, url_prefix="/adoptions")

@adoption_bp.route("", methods=["GET"])
def get_all_adoptions():
    """GET /adoptions - Lista todas as adoções"""
    try:
        adoptions = Adoption.query.all()
        return build_response(
            success=True,
            message="Adoções recuperadas com sucesso",
            data=[adoption.to_dict() for adoption in adoptions]
        ), 200
    except Exception as e:
        return handle_error(e, "Erro ao recuperar adoções")

@adoption_bp.route("", methods=["POST"])
def create_adoption():
    """POST /adoptions - Registra uma nova adoção"""
    try:
        data = request.get_json()
        
        # Validação básica
        required_fields = [
            "animal_id", "adopter_name", "adopter_email",
            "address_cep", "address_street", "address_number",
            "address_city", "address_state"
        ]
        if not all(field in data for field in required_fields):
            return build_response(
                success=False,
                message="Campos obrigatórios faltando"
            ), 400
        
        # Verifica se o animal existe
        animal = Animal.query.get(data.get("animal_id"))
        if not animal:
            return build_response(
                success=False,
                message="Animal não encontrado"
            ), 404
        
        # Cria o registro de adoção
        adoption = Adoption(
            animal_id=data.get("animal_id"),
            adopter_name=data.get("adopter_name"),
            adopter_email=data.get("adopter_email"),
            adopter_phone=data.get("adopter_phone"),
            address_cep=data.get("address_cep"),
            address_street=data.get("address_street"),
            address_number=data.get("address_number"),
            address_complement=data.get("address_complement"),
            address_neighborhood=data.get("address_neighborhood"),
            address_city=data.get("address_city"),
            address_state=data.get("address_state"),
            adoption_message=data.get("adoption_message")
        )
        
        db.session.add(adoption)
        db.session.commit()
        
        return build_response(
            success=True,
            message="Adoção registrada com sucesso",
            data=adoption.to_dict()
        ), 201
    except Exception as e:
        db.session.rollback()
        return handle_error(e, "Erro ao registrar adoção")

@adoption_bp.route("/<int:adoption_id>", methods=["DELETE"])
def delete_adoption(adoption_id):
    """DELETE /adoptions/<id> - Deleta uma adoção"""
    try:
        adoption = Adoption.query.get(adoption_id)
        if not adoption:
            return build_response(
                success=False,
                message="Adoção não encontrada"
            ), 404
        
        db.session.delete(adoption)
        db.session.commit()
        
        return build_response(
            success=True,
            message="Adoção deletada com sucesso"
        ), 200
    except Exception as e:
        db.session.rollback()
        return handle_error(e, "Erro ao deletar adoção")
