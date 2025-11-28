# 📘 **PulseFlow — Engine de Automação Orientada a Eventos**

> **PulseFlow** é uma arquitetura modular de automação baseada em eventos, projetada para demonstrar conceitos avançados de Arquitetura de Software, desacoplamento, extensibilidade e organização profissional em Flask.
>
> O sistema permite criar **regras dinâmicas** que conectam **eventos → ações**, funcionando como uma mini–engine de automação que pode ser estendida com novos módulos, triggers, actions e serviços.

---

# 📚 **Sumário**

* [1. Visão Geral](#1-visão-geral)
* [2. Justificativa Arquitetural](#2-justificativa-arquitetural)
* [3. Arquitetura do Sistema](#3-arquitetura-do-sistema)
* [4. Extensões (`ext/`) e Modularização](#4-extensões-e-modularização)
* [5. Engine de Automação](#5-engine-de-automação)
* [6. Estrutura de Diretórios](#6-estrutura-de-diretórios)
* [7. Configuração Externa (TOML, ENV, Secrets)](#7-configuração-externa)
* [8. API e Blueprints](#8-api-e-blueprints)
* [9. Executando o Projeto](#9-executando-o-projeto)
* [10. Uso via Docker & Docker Compose](#10-uso-via-docker--docker-compose)
* [11. Exemplos de Uso da API](#11-exemplos-de-uso-da-api)
* [12. Expansões Futuras](#12-expansões-futuras)
* [13. Créditos](#13-créditos)

---

# 🧠 **1. Visão Geral**

PulseFlow é uma **engine de automação leve**, baseada no padrão:

```
Evento → Regra → Ação
```

Ele permite:

* Registrar **eventos** no sistema (ex: `user.registered`).
* Criar **regras** que vinculam eventos a ações.
* Executar **ações** sempre que um evento é disparado.
* Registrar logs de execução.
* Simular eventos manualmente via API.

A engine foi desenvolvida com foco em:

* Arquitetura limpa
* Extensões plugáveis
* Baixo acoplamento
* Modularidade
* Demonstração de boas práticas do Flask

---

# 🧩 **2. Justificativa Arquitetural**

O projeto utiliza uma combinação de:

* **Application Factory Pattern**
* **Extensões desacopladas via `init_app()`**
* **EventBus implementado manualmente**
* **Blueprints independentes**
* **Carregamento de configuração externo (settings.toml, .env, .secrets.toml)**
* **Padrão Observer / PubSub**
* **Database ORM com SQLAlchemy**
* **Pasta `instance/` seguindo convenção Flask**

Esses elementos foram escolhidos para:

### ✔ Evitar importações circulares

### ✔ Permitir múltiplos ambientes (dev, prod)

### ✔ Facilitar testes e manutenção

### ✔ Permitir extensão futura sem alterar o core da aplicação

### ✔ Demonstrar domínio de arquitetura profissional aplicada em Flask

PulseFlow funciona como uma **prova de conceito** de um sistema orientado a eventos expansível, similar (em miniatura) a plataformas como:

* Zapier
* n8n
* Temporal
* AWS EventBridge

---

# 🏛 **3. Arquitetura do Sistema**

A arquitetura do PulseFlow é organizada em camadas:

### **1. Extensões (`ext/`)**

Responsáveis por funcionalidades transversais do sistema:

* Banco de dados
* Sistema de eventos
* Carregamento de configuração

### **2. Engine de automação (`services/engine/`)**

Onde reside a lógica de:

* triggers
* actions
* dispatcher
* processamento de regras

### **3. Blueprints**

APIs separadas em:

* `/rules` — CRUD de regras
* `/simulate` — endpoint para disparar eventos

### **4. Modelos**

Representam regras e logs armazenados localmente na `instance/automation.db`.

### **5. Configuração Externa**

`settings.toml`, `.secrets.toml` e `.env` definem parâmetros facilmente modificáveis **sem alterar o código**.

---

# 🧩 **4. Extensões e Modularização**

A pasta **`ext/`** contém componentes desacoplados carregados no `create_app()`.

Cada extensão segue o padrão:

```python
def init_app(app):
    ...
```

Isso permite:

* carregar módulos em qualquer ordem
* usar o app factory
* evitar dependências circulares
* manter a raiz do projeto limpa

As extensões incluem:

### ✔ `database.py`

Inicializa o SQLAlchemy e cria as tabelas no `instance/`.

### ✔ `events.py`

Contém o **EventBus**, implementando um sistema publish/subscribe.

### ✔ `configuration.py`

Usa **Dynaconf** para carregar configs externas.

---

# ⚙️ **5. Engine de Automação**

Local: `services/engine/`

Componentes:

### **1. triggers**

Funções que definem eventos disparáveis pelo sistema.

### **2. actions**

Funções executadas quando regras são atendidas.

### **3. engine**

Core da automação:

* consulta regras no banco
* executa ações
* registra logs
* conecta-se ao EventBus

Fluxo:

```
Evento ocorre →
EventBus captura →
Engine consulta regras →
Executa ações →
Registra logs →
Retorna resposta
```

---

# 🗂️ **6. Estrutura de Diretórios**

```
PulseFlow/
│
├── engine_app/
│   ├── app.py
│   ├── ext/
│   ├── models/
│   ├── blueprints/
│   ├── services/
│   └── __init__.py
│
├── instance/
│   └── automation.db
│
├── settings.toml
├── .secrets.toml
├── .env
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# 🛠 **7. Configuração Externa**

## settings.toml

```toml
[default]
DEBUG = true
SQLALCHEMY_DATABASE_URI = "sqlite:///automation.db"
ENGINE_LOG_LEVEL = "DEBUG"
```

## .secrets.toml

```toml
[default]
SECRET_KEY = "sua_chave_super_secreta"
```

## .env

```env
FLASK_ENV=development
```

O uso de arquivos externos segue o padrão Flask:

* **configurável**
* **seguro**
* **fácil de versionar (exceto os secrets)**

---

# 🌐 **8. API e Blueprints**

### `/rules`

| Método | Rota      | Descrição                    |
| ------ | --------- | ---------------------------- |
| GET    | `/rules/` | Lista regras                 |
| POST   | `/rules/` | Cria regra `{event, action}` |

### `/simulate/event`

Dispara manualmente um evento:

Payload:

```json
{
  "event": "user.registered",
  "data": {"username": "marcio"}
}
```

---

# ▶️ **9. Executando o Projeto (sem Docker)**

### Criar venv:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar dependências:

```bash
pip install -r requirements.txt
```

### Rodar:

```bash
flask --app engine_app.app:create_app run
```

Banco será criado automaticamente em:

```
instance/automation.db
```

---

# 🐳 **10. Uso via Docker & Docker Compose**

### Build:

```bash
docker build -t pulseflow .
```

### Run:

```bash
docker run -p 5000:5000 pulseflow
```

### With compose:

```bash
docker-compose up --build
```

O container carrega configurações a partir de:

* `/app/settings.toml`
* `/app/.secrets.toml`
* `/app/.env`

---

# 🧪 **11. Exemplos de Uso da API**

### Criar regra

```bash
curl -X POST http://localhost:5000/rules/ \
    -H "Content-Type: application/json" \
    -d '{"event": "user.registered", "action": "log_action"}'
```

### Disparar evento

```bash
curl -X POST http://localhost:5000/simulate/event \
    -H "Content-Type: application/json" \
    -d '{"event": "user.registered", "data": {"name": "Márcio"}}'
```

### Listar regras

```bash
curl http://localhost:5000/rules/
```

---

# 🚀 **12. Expansões Futuras**

* Autenticação JWT
* Dashboard web (Admin UI)
* Workers assíncronos reais
* Sistema de filas (RabbitMQ/Redis)
* Plugins externos (arquitetura plugável)
* Editor visual de automações
* Exportação/importação de regras

---

# 📝 **13. Créditos**

Projeto desenvolvido para fins acadêmicos na disciplina de **Arquitetura de Software**, demonstrando boas práticas de organização, modularidade, desacoplamento e uso avançado do Flask.

---