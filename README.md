
# Hospital Management System

Este projeto é um sistema de gerenciamento hospitalar desenvolvido com Flask, permitindo que administradores, médicos e pacientes realizem operações essenciais como gerenciamento de pacientes, compromissos, inventário, faturamento e geração de relatórios.

## Estrutura do Sistema

### Diretórios

- **app/**: Contém os arquivos principais da aplicação Flask.
  - **__init__.py**: Inicializa o aplicativo Flask, banco de dados e login.
  - **models.py**: Define os modelos para usuários, pacientes, médicos, inventário e faturamento.
  - **routes.py**: Define as rotas para as diferentes funcionalidades.
  - **forms.py**: Contém os formulários usados no sistema.
  - **templates/**: Contém os templates HTML para as diferentes páginas.
  - **static/**: Contém o arquivo CSS (`style.css`) e o arquivo JavaScript (`main.js`).

- **schema.sql**: Script SQL para criação das tabelas no banco de dados.

## Funcionalidades

### 1. Autenticação de Usuários
- **Função**: Administradores, médicos e pacientes podem se cadastrar e fazer login. O sistema direciona o usuário para um dashboard apropriado baseado em seu papel.
- **Tecnologia**: Flask-Login, Bcrypt para senhas criptografadas.

### 2. Gerenciamento de Pacientes
- **Função**: Administradores e médicos podem gerenciar pacientes, visualizar e editar detalhes, e marcar compromissos.
- **Modelos Relacionados**: User, Patient, Appointment.

### 3. Gerenciamento de Médicos
- **Função**: Administradores podem gerenciar os perfis de médicos. Médicos podem visualizar seus compromissos e gerenciar pacientes.
- **Modelos Relacionados**: User, Doctor, Appointment.

### 4. Gerenciamento de Inventário
- **Função**: Administradores podem adicionar, editar e remover itens do inventário, com alertas para estoque baixo.
- **Modelos Relacionados**: Inventory.

### 5. Faturamento e Pagamentos
- **Função**: Criação de faturas para pacientes, processamento de pagamentos e rastreamento de faturas pendentes e pagas.
- **Modelos Relacionados**: Billing, Payment.

### 6. Relatórios e Análises
- **Função**: Administradores podem gerar relatórios financeiros, de pacientes e de desempenho dos médicos.
- **Tecnologia**: Geração dinâmica de relatórios com Flask.

## Como Executar

### 1. Clonar o Repositório
```bash
git clone <URL-do-repositório>
cd hospital_management_system
```

### 2. Criar o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scriptsctivate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados
Inicialize o banco de dados executando o arquivo SQL:
```bash
sqlite3 hospital.db < schema.sql
```

### 5. Executar o Servidor
```bash
python run.py
```

A aplicação estará disponível em `http://127.0.0.1:5000/`.

## Dependências
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login
- Bcrypt

## Contribuição
Sinta-se à vontade para fazer pull requests ou abrir issues para melhorias.

## Licença
Este projeto é de uso livre para fins educacionais.
