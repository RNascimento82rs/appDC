-- Tabela de perfis de usuário
CREATE TABLE perfil (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    permissoes JSONB
);

-- Tabela de usuários
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    perfil_id INTEGER REFERENCES perfil(id),
    ativo BOOLEAN DEFAULT TRUE
);

-- Tabela de municípios
CREATE TABLE municipio (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

-- Tabela de SCIs
CREATE TABLE sci (
    id SERIAL PRIMARY KEY,
    municipio_id INTEGER REFERENCES municipio(id) ON DELETE CASCADE,
    nome VARCHAR(100) NOT NULL,
    data_criacao DATE DEFAULT CURRENT_DATE,
    ativo BOOLEAN DEFAULT TRUE
);

-- Tabela de campos personalizados para cada SCI
CREATE TABLE campo_personalizado (
    id SERIAL PRIMARY KEY,
    sci_id INTEGER REFERENCES sci(id) ON DELETE CASCADE,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL, -- Ex: texto, numero, data
    obrigatorio BOOLEAN DEFAULT FALSE,
    ordem INTEGER
);

-- Tabela de valores dos campos personalizados
CREATE TABLE valor_campo (
    id SERIAL PRIMARY KEY,
    campo_id INTEGER REFERENCES campo_personalizado(id) ON DELETE CASCADE,
    valor TEXT,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);