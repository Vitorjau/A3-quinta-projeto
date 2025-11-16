from flask import Blueprint, request, jsonify
from database.models import db, Animal
from utils.response_builder import build_response
from utils.error_handlers import handle_error

animals_bp = Blueprint("animals", __name__, url_prefix="/animals")

@animals_bp.route("", methods=["GET"])
def get_all_animals():
    """GET /animals - Lista todos os animais"""
    try:
        animals = Animal.query.all()
        return build_response(
            success=True,
            message="Animais recuperados com sucesso",
            data=[animal.to_dict() for animal in animals]
        ), 200
    except Exception as e:
        return handle_error(e, "Erro ao recuperar animais")

@animals_bp.route("/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    """GET /animals/<id> - Retorna um animal específico"""
    try:
        animal = Animal.query.get(animal_id)
        if not animal:
            return build_response(
                success=False,
                message="Animal não encontrado"
            ), 404
        return build_response(
            success=True,
            message="Animal recuperado com sucesso",
            data=animal.to_dict()
        ), 200
    except Exception as e:
        return handle_error(e, "Erro ao recuperar animal")

@animals_bp.route("", methods=["POST"])
def create_animal():
    """POST /animals - Cria um novo animal"""
    try:
        data = request.get_json()
        
        # Validação básica
        required_fields = ["name", "species", "age", "size", "temperament", "city", "description", "history"]
        if not all(field in data for field in required_fields):
            return build_response(
                success=False,
                message="Campos obrigatórios faltando"
            ), 400
        
        animal = Animal(
            name=data.get("name"),
            species=data.get("species"),
            age=data.get("age"),
            size=data.get("size"),
            temperament=data.get("temperament"),
            city=data.get("city"),
            status=data.get("status", "Disponível"),
            image=data.get("image"),
            description=data.get("description"),
            history=data.get("history")
        )
        
        db.session.add(animal)
        db.session.commit()
        
        return build_response(
            success=True,
            message="Animal criado com sucesso",
            data=animal.to_dict()
        ), 201
    except Exception as e:
        db.session.rollback()
        return handle_error(e, "Erro ao criar animal")

@animals_bp.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    """PUT /animals/<id> - Atualiza um animal"""
    try:
        animal = Animal.query.get(animal_id)
        if not animal:
            return build_response(
                success=False,
                message="Animal não encontrado"
            ), 404
        
        data = request.get_json()
        
        # Atualiza apenas os campos fornecidos
        if "name" in data:
            animal.name = data["name"]
        if "species" in data:
            animal.species = data["species"]
        if "age" in data:
            animal.age = data["age"]
        if "size" in data:
            animal.size = data["size"]
        if "temperament" in data:
            animal.temperament = data["temperament"]
        if "city" in data:
            animal.city = data["city"]
        if "status" in data:
            animal.status = data["status"]
        if "image" in data:
            animal.image = data["image"]
        if "description" in data:
            animal.description = data["description"]
        if "history" in data:
            animal.history = data["history"]
        
        db.session.commit()
        
        return build_response(
            success=True,
            message="Animal atualizado com sucesso",
            data=animal.to_dict()
        ), 200
    except Exception as e:
        db.session.rollback()
        return handle_error(e, "Erro ao atualizar animal")

@animals_bp.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    """DELETE /animals/<id> - Deleta um animal"""
    try:
        animal = Animal.query.get(animal_id)
        if not animal:
            return build_response(
                success=False,
                message="Animal não encontrado"
            ), 404
        
        db.session.delete(animal)
        db.session.commit()
        
        return build_response(
            success=True,
            message="Animal deletado com sucesso"
        ), 200
    except Exception as e:
        db.session.rollback()
        return handle_error(e, "Erro ao deletar animal")
