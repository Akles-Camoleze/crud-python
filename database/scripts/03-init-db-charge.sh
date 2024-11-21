#!/bin/sh
set -e

# Definir a variável de ambiente PGPASSWORD com a senha do usuário
export PGPASSWORD="$DB_PASSWORD"

# Executar os comandos no PostgreSQL
psql -v ON_ERROR_STOP=1 --username "$DB_USER" --dbname "$DB_NAME" <<-EOSQL
  -- Inserção de dados na tabela tb_pessoa
  INSERT INTO "$DB_SCHEMA".tb_pessoa (pe_id, pe_nome, pe_sobrenome, pe_idade, pe_cpf)
  VALUES
    (nextval('$DB_SCHEMA.seq_pessoa'), 'Akles', 'Pires Camoleze', 20, '12345678909'),
    (nextval('$DB_SCHEMA.seq_pessoa'), 'Pedro', 'Tunico', 48, '29600188009');

  -- Inserção de dados na tabela tb_dispositivo
  INSERT INTO "$DB_SCHEMA".tb_dispositivo (di_id, di_nome)
  VALUES
    (nextval('$DB_SCHEMA.seq_dispositivo'), 'Celular'),
    (nextval('$DB_SCHEMA.seq_dispositivo'), 'Computador'),
    (nextval('$DB_SCHEMA.seq_dispositivo'), 'Tablet'),
    (nextval('$DB_SCHEMA.seq_dispositivo'), 'Relógio'),
    (nextval('$DB_SCHEMA.seq_dispositivo'), 'Notebook');

  -- Inserção de dados na tabela tb_disp_pessoa
  INSERT INTO "$DB_SCHEMA".tb_disp_pessoa (dpe_id, di_id, pe_id)
  VALUES
    (nextval('$DB_SCHEMA.seq_disp_pessoa'), 1, 1),
    (nextval('$DB_SCHEMA.seq_disp_pessoa'), 2, 1),
    (nextval('$DB_SCHEMA.seq_disp_pessoa'), 3, 1),
    (nextval('$DB_SCHEMA.seq_disp_pessoa'), 3, 2),
    (nextval('$DB_SCHEMA.seq_disp_pessoa'), 5, 2);
EOSQL

# Limpar a variável de ambiente PGPASSWORD após o uso
unset PGPASSWORD
