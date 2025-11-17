def build_response(success: bool, message: str, data: object = None) -> dict:
    """Constrói resposta JSON padrão para a API.

    Retorna um dicionário que o Flask pode serializar automaticamente em JSON.
    """
    payload = {
        "success": bool(success),
        "message": message,
        "data": data if data is not None else None
    }
    return payload
