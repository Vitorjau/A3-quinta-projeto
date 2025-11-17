# Como testar nosso projeto

Olá, professor — este é um guia curto e direto para executar e verificar o funcionamento do projeto (front-end + back-end).

Objetivo: subir os dois servidores localmente, executar os principais fluxos e confirmar respostas esperadas.

Pré-requisitos
- Sistema: Windows (os comandos abaixo são para PowerShell). Git Bash/WSL também funcionam com pequenas adaptações.
- Python 3.11/3.12 instalado (usamos `py -0p` para checar). Se usar Windows, marque "Add Python to PATH" na instalação.
- Node.js + npm instalados.

1) Backend (Flask)

- Abra um PowerShell e execute:

```powershell
cd C:\Users\VitorJau\Desktop\projeto_a3_quinta\A3-quinta-projeto\Back-end
# Criar (se necessário) e ativar virtualenv
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1

# Atualizar pip e instalar dependências
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Iniciar servidor
python app.py
```

- Saída esperada no terminal do back-end: logs do Flask e uma linha de health, por exemplo:

```
 * Running on http://0.0.0.0:3001
```

2) Frontend (Vite + React)

- Em outro PowerShell:

```powershell
cd C:\Users\VitorJau\Desktop\projeto_a3_quinta\A3-quinta-projeto\Front-end
npm install
npm run dev
```

- Normalmente o front rodará em `http://localhost:5173`.

3) Health check & testes rápidos (curl / PowerShell)

- Health (back-end):
```powershell
Invoke-RestMethod http://localhost:3001/health
# Esperado: {"status":"ok","message":"Server is running"}
```

- Listar animais (inicialmente vazio):
```bash
curl http://localhost:3001/animals
```

- Criar animal (exemplo):
```bash
curl -X POST http://localhost:3001/animals \
  -H "Content-Type: application/json" \
  -d '{"name":"Belinha","species":"Gato","age":2,"size":"Pequeno","temperament":"Dócil","city":"São Paulo","description":"Gata fofa","history":"Resgatada"}'
```

- Buscar CEP (ViaCEP):
```bash
curl http://localhost:3001/address/01310100
```

- Criar adoção (substitua `animal_id` conforme retorno anterior):
```bash
curl -X POST http://localhost:3001/adoptions \
  -H "Content-Type: application/json" \
  -d '{"animal_id":1,"adopter_name":"João","adopter_email":"joao@example.com","address_cep":"01310100","address_street":"Avenida Paulista","address_number":"1000","address_city":"São Paulo","address_state":"SP"}'
```

- Enviar feedback (feedback.html usa jQuery POST para este endpoint):
```bash
curl -X POST http://localhost:3001/feedback -H "Content-Type: application/json" -d '{"mensagem":"Ótimo site!"}'
```

4) Parar os servidores

- No terminal onde cada servidor foi iniciado: `Ctrl+C` (forma mais segura).
- Alternativa (PowerShell) — parar por porta:
```powershell
Get-NetTCPConnection -LocalPort 3001 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
Get-NetTCPConnection -LocalPort 5173 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

5) O que verificar para avaliar funcionamento
- Health: `GET /health` retorna `{"status":"ok"}`.
- CRUD de animais: `POST /animals` cria; `GET /animals` lista; `GET /animals/<id>` retorna detalhes.
- Busca de CEP: `GET /address/<cep>` retorna rua, bairro, cidade e UF.
- Formulário de adoção: cria registro em `POST /adoptions` com campos de endereço.
- Feedback/Contato: `POST /feedback` e `POST /contact` aceitam mensagens.

Observações rápidas
- Se ocorrer erro de execução de scripts no PowerShell, rode:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- Se houver erro de incompatibilidade de pacotes com Python 3.14, use Python 3.12 (o projeto foi testado com 3.11/3.12).

Agradecemos por avaliar nosso trabalho — se preferir, posso preparar um pequeno roteiro de testes com casos (ex.: criar 3 animais, simular uma adoção, confirmar base de dados) para facilitar a correção. Boa avaliação!
