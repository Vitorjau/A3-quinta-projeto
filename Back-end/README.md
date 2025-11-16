# Animal Adoption Back-End

API RESTful em Python com Flask para gerenciamento de animais, adoções, contatos e feedback.

## 🚀 Quick Start

### Requisitos
- Python 3.8+
- pip

### Instalação

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# ou
source venv/bin/activate  # macOS/Linux
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure variáveis de ambiente:
```bash
cp .env.example .env
# Edite .env conforme necessário
```

4. Inicie o servidor:
```bash
python app.py
```

O servidor rodará em `http://localhost:3001`

## 📋 Endpoints

### Animais
- `GET /animals` - Lista todos os animais
- `GET /animals/<id>` - Obtém detalhes de um animal
- `POST /animals` - Cria novo animal
- `PUT /animals/<id>` - Atualiza animal
- `DELETE /animals/<id>` - Deleta animal

### Adoções
- `GET /adoptions` - Lista todas as adoções
- `POST /adoptions` - Cria solicitação de adoção
- `DELETE /adoptions/<id>` - Cancela adoção

### Endereços
- `GET /address/<cep>` - Busca endereço por CEP (ViaCEP)

### Contatos e Feedback
- `POST /contact` - Submete formulário de contato
- `POST /feedback` - Submete feedback

## 🗂️ Estrutura do Projeto

```
Back-end/
├── app.py                 # Ponto de entrada da aplicação
├── config.py              # Configurações (dev/prod/test)
├── requirements.txt       # Dependências Python
├── .env.example          # Exemplo de variáveis de ambiente
├── database/
│   └── models.py         # Modelos SQLAlchemy
├── routes/
│   ├── animals_routes.py      # Endpoints de animais
│   ├── adoption_routes.py     # Endpoints de adoções
│   ├── address_routes.py      # Endpoints de endereço
│   └── contact_routes.py      # Endpoints de contato/feedback
├── services/
│   └── address_service.py     # Integração com ViaCEP
└── utils/
    ├── response_builder.py    # Construtor de respostas
    └── error_handlers.py      # Tratamento de erros
```

## 🔗 Integração com Front-End

O back-end está configurado para aceitar requisições do front-end em:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:5174` (Alternativa)

CORS está habilitado em `app.py`

## 📦 Dependências Principais

- **Flask 3.0.0** - Framework web
- **Flask-CORS 4.0.0** - Suporte CORS
- **Flask-SQLAlchemy 3.1.1** - ORM
- **SQLAlchemy 2.0.23** - Banco de dados
- **requests** - HTTP client (ViaCEP)
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 🗄️ Banco de Dados

Usa SQLite com SQLAlchemy ORM. O banco é criado automaticamente ao iniciar a aplicação.

### Modelos

**Animal**
```python
- id, name, species, age, size, temperament, city, status
- image, description, history, created_at, updated_at
```

**Adoption**
```python
- id, animal_id, adopter_name, adopter_email, adopter_phone
- address_cep, address_street, address_number, address_complement
- address_neighborhood, address_city, address_state, adoption_message
- status, created_at, updated_at
```

**Contact**
```python
- id, name, email, subject, message, created_at
```

**Feedback**
```python
- id, mensagem, created_at
```

## 🔍 Serviços

### AddressService (ViaCEP)
Integra com API ViaCEP para buscar endereços por CEP:
```python
from services.address_service import search_address_by_cep

# Busca endereço
address = search_address_by_cep("01310100")
```

## 📝 Exemplo de Uso

### Criar Animal
```bash
curl -X POST http://localhost:3001/animals \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Rex",
    "species": "Cachorro",
    "age": 3,
    "size": "Médio",
    "temperament": "Dócil",
    "city": "São Paulo",
    "description": "Cachorro amigável"
  }'
```

### Buscar CEP
```bash
curl http://localhost:3001/address/01310100
```

### Criar Solicitação de Adoção
```bash
curl -X POST http://localhost:3001/adoptions \
  -H "Content-Type: application/json" \
  -d '{
    "animal_id": 1,
    "adopter_name": "João",
    "adopter_email": "joao@email.com",
    "adopter_phone": "11999999999",
    "address_cep": "01310100",
    "address_street": "Avenida Paulista",
    "address_number": "1000",
    "address_city": "São Paulo",
    "address_state": "SP",
    "adoption_message": "Amo muito animais!"
  }'
```

## 🚦 Health Check

```bash
curl http://localhost:3001/health
```

## 📧 Contato

Para questões sobre este projeto, submeta feedback através da aplicação.
