from flask import Blueprint, request
from services.address_service import search_address_by_cep
from utils.response_builder import build_response
from utils.error_handlers import handle_error

address_bp = Blueprint("address", __name__, url_prefix="/address")

@address_bp.route("/<cep>", methods=["GET"])
def get_address(cep):
    """GET /address/<cep> - Busca endereço por CEP usando API externa"""
    try:
        # Remove caracteres especiais do CEP
        clean_cep = cep.replace("-", "").replace(" ", "").strip()
        
        # Valida CEP
        if len(clean_cep) != 8 or not clean_cep.isdigit():
            return build_response(
                success=False,
                message="CEP inválido. Use apenas 8 dígitos."
            ), 400
        
        # Busca endereço usando ViaCEP
        address_data = search_address_by_cep(clean_cep)
        
        if not address_data:
            return build_response(
                success=False,
                message="CEP não encontrado"
            ), 404
        
        return build_response(
            success=True,
            message="Endereço encontrado com sucesso",
            data=address_data
        ), 200
    except Exception as e:
        return handle_error(e, "Erro ao buscar endereço")
