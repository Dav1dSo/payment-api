# Aplicação Flask com WebSockets e API de Pagamento

Este projeto é uma aplicação Flask que utiliza WebSockets para comunicação em tempo real e SQLAlchemy com PostgreSQL para gerenciar dados de pagamentos. A API permite realizar operações de pagamento e monitorar transações em tempo real.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python.
- **Flask-SocketIO**: Extensão para adicionar suporte a WebSockets em Flask.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interação com o banco de dados.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional.
- **Flask-Migrate**: Ferramenta para gerenciar migrações de banco de dados.

## Requisitos

- Python 3.7 ou superior
- PostgreSQL
- `pip` para instalar pacotes Python

## Instalação

1. **Clone o repositório**

    ```bash
    git clone https://github.com/Dav1dSo/payment-api.git
    cd payment-api
    ```

2. **Crie e ative um ambiente virtual**

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3. **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados**

    Crie um banco de dados PostgreSQL e configure as credenciais no arquivo `.env`. Exemplo de configuração `.env`:

    ```env
    DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
    ```

    Para cria o banco execute: 
    ```
        docker-compose up -d 
    ```

    Não esqueça de guardar suas credenciais com segurança em ambientes reais.
5. **Inicialize o banco de dados**

    ```bash
    flask db upgrade
    ```

6. **Inicie a aplicação**

    ```bash
    flask run
    ```

## Uso

A aplicação expõe uma API para gerenciamento de pagamentos e utiliza WebSockets para atualizações em tempo real.