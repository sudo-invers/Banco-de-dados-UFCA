
CREATE TABLE IF NOT EXISTS usuario (
    "usuario_id" INTEGER,
    "email" VARCHAR,
    "senha" VARCHAR,
    "tipo_usuario" VARCHAR,

    PRIMARY KEY ("usuario_id")
);

CREATE TABLE IF NOT EXISTS endereco (
    "endereco_id" INTEGER,
    "rua" VARCHAR,
    "bairro" VARCHAR,
    "cidade" VARCHAR,
    "numero" VARCHAR,

    PRIMARY KEY ("endereco_id")
);

CREATE TABLE IF NOT EXISTS pessoa (
    "pessoa_id" INTEGER,
    "endereco_id" INTEGER,
    "nome" VARCHAR,
    "telefone" VARCHAR,
    "n_inscricao_tributaria" VARCHAR,
    "data_nascimento" DATE,

    PRIMARY KEY ("pessoa_id"),

    CONSTRAINT "FK_PESSOA_endereco_id"
    FOREIGN KEY ("endereco_id")
    REFERENCES endereco ("endereco_id")
);

CREATE TABLE IF NOT EXISTS acusado (
    "acusado_id" INTEGER,
    "pessoa_id" INTEGER,

    PRIMARY KEY ("acusado_id"),

    CONSTRAINT "FK_ACUSADO_pessoa_id"
    FOREIGN KEY ("pessoa_id")
    REFERENCES pessoa ("pessoa_id")
);

CREATE TABLE IF NOT EXISTS acusador (
    "acusador_id" INTEGER,
    "pessoa_id" INTEGER,
    "usuario_id" INTEGER,

    PRIMARY KEY ("acusador_id"),

    CONSTRAINT "FK_ACUSADOR_pessoa_id"
    FOREIGN KEY ("pessoa_id")
    REFERENCES pessoa ("pessoa_id")
);

CREATE TABLE IF NOT EXISTS prefeitura (
    "prefeitura_id" INTEGER,
    "endereco_id" INTEGER,
    "cnpj" VARCHAR,

    PRIMARY KEY ("prefeitura_id"),

    CONSTRAINT "FK_PREFEITURA_endereco_id"
    FOREIGN KEY ("endereco_id")
    REFERENCES endereco ("endereco_id")
);

CREATE TABLE IF NOT EXISTS gestor (
    "gestor_id" INTEGER,
    "prefeitura_id" INTEGER,
    "usuario_id" INTEGER,
    "pessoa_id" INTEGER,
    "status_gestor" VARCHAR,

    PRIMARY KEY ("gestor_id"),

    CONSTRAINT "FK_GESTOR_prefeitura_id"
    FOREIGN KEY ("prefeitura_id")
    REFERENCES prefeitura ("prefeitura_id")
);

CREATE TABLE IF NOT EXISTS mediador (
    "mediador_id" INTEGER,
    "pessoa_id" INTEGER,
    "usuario_id" INTEGER,
    "prefeitura_id" INTEGER,
    "status_mediador" VARCHAR,

    PRIMARY KEY ("mediador_id"),

    CONSTRAINT "FK_MEDIADOR_prefeitura_id"
    FOREIGN KEY ("prefeitura_id")
    REFERENCES prefeitura ("prefeitura_id"),

    CONSTRAINT "FK_MEDIADOR_pessoa_id"
    FOREIGN KEY ("pessoa_id")
    REFERENCES pessoa ("pessoa_id"),

    CONSTRAINT "FK_MEDIADOR_usuario_id"
    FOREIGN KEY ("usuario_id")
    REFERENCES usuario ("usuario_id")
);

CREATE TABLE IF NOT EXISTS audiencia (
    "audiencia_id" INTEGER NOT NULL,
    "mediador_id" INTEGER NOT NULL,
    "endereco_id" INTEGER NOT NULL,
    "status_audiencia" VARCHAR,
    "data_audiencia" TIMESTAMP NOT NULL,

    PRIMARY KEY ("audiencia_id"),

    CONSTRAINT "FK_AUDIENCIA_mediador_id"
    FOREIGN KEY ("mediador_id")
    REFERENCES mediador ("mediador_id"),

    CONSTRAINT "FK_AUDIENCIA_endereco_id"
    FOREIGN KEY ("endereco_id")
    REFERENCES endereco ("endereco_id")
);

CREATE TABLE IF NOT EXISTS acordo (
    "acordo_id" INTEGER NOT NULL,
    "audiencia_id" INTEGER NOT NULL,
    "status_acordo" VARCHAR NOT NULL,
    "data_acordo" DATE NOT NULL,

    PRIMARY KEY ("acordo_id"),

    CONSTRAINT "FK_ACORDO_audiencia_id"
    FOREIGN KEY ("audiencia_id")
    REFERENCES audiencia ("audiencia_id")
);



CREATE TABLE IF NOT EXISTS denuncia (
    "denuncia_id" INTEGER NOT NULL,
    -- pode ser nulo, pois a denúncia é feita antes da audiência ser marcada
    "audiencia_id" INTEGER,
    "acusador_id" INTEGER NOT NULL,
    "acusado_id" INTEGER NOT NULL,
    "causa_denuncia" VARCHAR NOT NULL,
    "detalhamento" VARCHAR,
    "data_denuncia" TIMESTAMP NOT NULL,

    PRIMARY KEY ("denuncia_id"),

    CONSTRAINT "FK_DENUNCIA_audiencia_id"
    FOREIGN KEY ("audiencia_id")
    REFERENCES audiencia ("audiencia_id"),

    CONSTRAINT "FK_DENUNCIA_acusador_id"
    FOREIGN KEY ("acusador_id")
    REFERENCES acusador ("acusador_id"),

    CONSTRAINT "FK_DENUNCIA_acusado_id"
    FOREIGN KEY ("acusado_id")
    REFERENCES acusado ("acusado_id")
);
