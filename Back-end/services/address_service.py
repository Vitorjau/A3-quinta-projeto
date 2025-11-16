import requests
import logging

logger = logging.getLogger(__name__)

class AddressServiceError(Exception):
    """Exceção para erros no serviço de endereço"""
    pass

def search_address_by_cep(cep: str) -> dict:
    """
    Busca endereço usando a API ViaCEP
    
    Args:
        cep: CEP em formato de string (sem caracteres especiais)
    
    Returns:
        dict com dados do endereço ou None se não encontrado
    
    Raises:
        AddressServiceError: Se houver erro na requisição
    """
    try:
        # Valida entrada
        if not isinstance(cep, str) or len(cep) != 8 or not cep.isdigit():
            raise AddressServiceError("CEP inválido")
        
        # Monta URL da API ViaCEP
        url = f"https://viacep.com.br/ws/{cep}/json/"
        
        # Faz requisição com timeout
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        # Verifica se CEP foi encontrado
        if data.get("erro"):
            return None
        
        # Retorna dados formatados
        return {
            "cep": data.get("cep", ""),
            "street": data.get("logradouro", ""),
            "neighborhood": data.get("bairro", ""),
            "city": data.get("localidade", ""),
            "state": data.get("uf", ""),
            "region": data.get("regiao", "")
        }
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao buscar CEP {cep}: {str(e)}")
        raise AddressServiceError(f"Erro ao conectar com API de CEP: {str(e)}")
    except Exception as e:
        logger.error(f"Erro desconhecido ao buscar CEP {cep}: {str(e)}")
        raise AddressServiceError(f"Erro ao processar CEP: {str(e)}")
