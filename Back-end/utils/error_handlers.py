import logging
import traceback
from typing import Tuple

from .response_builder import build_response

logger = logging.getLogger(__name__)


def handle_error(exc: Exception, message: str = "Erro interno do servidor", status_code: int = 500) -> Tuple[dict, int]:
    """Registra o erro e retorna uma resposta JSON padronizada.

    Retorna uma tupla `(payload_dict, status_code)` que os handlers nas rotas podem retornar diretamente.
    """
    # Log detalhado para debugging
    logger.error("%s", str(exc))
    tb = traceback.format_exc()
    logger.debug(tb)

    # Não vazamos stack trace para o cliente; apenas uma mensagem genérica e, opcionalmente, o texto do erro
    payload = build_response(
        success=False,
        message=message,
        data={"error": str(exc)}
    )
    return payload, status_code
