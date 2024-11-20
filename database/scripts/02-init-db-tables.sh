#!/bin/sh
set -e

# Definir a variável de ambiente PGPASSWORD com a senha do usuário
export PGPASSWORD="$DB_PASSWORD"

# Executar os comandos no PostgreSQL
psql -v ON_ERROR_STOP=1 --username "$DB_USER" --dbname "$DB_NAME" <<-EOSQL
  -- Criação do schema
  CREATE SCHEMA IF NOT EXISTS "$DB_SCHEMA";

  -- Criação da tabela tb_pessoa
  CREATE TABLE IF NOT EXISTS "$DB_SCHEMA".tb_pessoa (
    pe_id INTEGER NOT NULL PRIMARY KEY,
    pe_nome VARCHAR(50) NOT NULL,
    pe_sobrenome VARCHAR(255) NOT NULL,
    pe_idade INTEGER NOT NULL,
    pe_cpf VARCHAR(11) NOT NULL UNIQUE
  );

  -- Criação da tabela tb_dispositivo
  CREATE TABLE IF NOT EXISTS "$DB_SCHEMA".tb_dispositivo (
    di_id INTEGER NOT NULL PRIMARY KEY,
    di_nome VARCHAR(255) NOT NULL UNIQUE
  );

  -- Criação da tabela tb_disp_pessoa
  CREATE TABLE IF NOT EXISTS "$DB_SCHEMA".tb_disp_pessoa (
    dpe_id INTEGER NOT NULL PRIMARY KEY,
    di_id INTEGER NOT NULL,
    pe_id INTEGER NOT NULL,
    CONSTRAINT fk_dpe_pe_id FOREIGN KEY (pe_id) REFERENCES "$DB_SCHEMA".tb_pessoa (pe_id) ON DELETE CASCADE,
    CONSTRAINT fk_dpe_di_id FOREIGN KEY (di_id) REFERENCES "$DB_SCHEMA".tb_dispositivo (di_id) ON DELETE CASCADE
  );
EOSQL

# Limpar a variável de ambiente PGPASSWORD após o uso
unset PGPASSWORD
