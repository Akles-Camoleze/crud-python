#!/bin/sh
set -e

# Definir a variável de ambiente PGPASSWORD com a senha do usuário
export PGPASSWORD="$DB_PASSWORD"

# Executar os comandos no PostgreSQL
psql -v ON_ERROR_STOP=1 --username "$DB_USER" --dbname "$DB_NAME" <<-EOSQL
  -- Inserção de dados na tabela tb_pessoa
  INSERT INTO "$DB_SCHEMA".tb_pessoa (pe_id, pe_nome, pe_sobrenome, pe_idade, pe_cpf)
  VALUES
    (1, 'Akles', 'Pires Camoleze', 20, '12345678909'),
    (2, 'Pedro', 'Tunico', 48, '29600188009');

  -- Inserção de dados na tabela tb_dispositivo
  INSERT INTO "$DB_SCHEMA".tb_dispositivo (di_id, di_nome)
  VALUES
    (1, 'Celular'),
    (2, 'Computador'),
    (3, 'Tablet'),
    (4, 'Relógio'),
    (5, 'Notebook');

  -- Inserção de dados na tabela tb_disp_pessoa
  INSERT INTO "$DB_SCHEMA".tb_disp_pessoa (dpe_id, di_id, pe_id)
  VALUES
    (1, 1, 1),
    (2, 2, 1),
    (3, 3, 1),
    (4, 3, 2),
    (5, 5, 2);
EOSQL

# Limpar a variável de ambiente PGPASSWORD após o uso
unset PGPASSWORD
