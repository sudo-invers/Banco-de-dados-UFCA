
CREATE TABLE IF NOT EXISTS usuarios (
    "usuario_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "email" VARCHAR NOT NULL UNIQUE,
    "senha" VARCHAR NOT NULL,
    "tipo_usuario" VARCHAR NOT NULL,

    PRIMARY KEY ("usuario_id")
);

CREATE TABLE IF NOT EXISTS enderecos (
    "endereco_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "rua" VARCHAR,
    "bairro" VARCHAR,
    "cidade" VARCHAR,
    "numero" VARCHAR,

    PRIMARY KEY ("endereco_id")
);

CREATE TABLE IF NOT EXISTS pessoas (
    "pessoa_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "endereco_id" INTEGER,
    "nome" VARCHAR NOT NULL,
    "telefone" VARCHAR,
    "n_inscricao_tributaria" VARCHAR,
    "data_nascimento" DATE,

    PRIMARY KEY ("pessoa_id"),

    CONSTRAINT "FK_PESSOA_endereco_id"
        FOREIGN KEY ("endereco_id")
        REFERENCES enderecos ("endereco_id")
);

CREATE TABLE IF NOT EXISTS acusados (
    "acusado_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "pessoa_id" INTEGER NOT NULL,

    PRIMARY KEY ("acusado_id"),

    CONSTRAINT "FK_ACUSADOS_pessoa_id"
        FOREIGN KEY ("pessoa_id")
        REFERENCES pessoas ("pessoa_id")
);

CREATE TABLE IF NOT EXISTS acusadores (
    "acusador_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "pessoa_id" INTEGER NOT NULL,
    "usuario_id" INTEGER, -- nulo para denúncias anônimas

    PRIMARY KEY ("acusador_id"),

    CONSTRAINT "FK_ACUSADORES_pessoa_id"
        FOREIGN KEY ("pessoa_id")
        REFERENCES pessoas ("pessoa_id"),

    CONSTRAINT "FK_ACUSADORES_usuario_id"
        FOREIGN KEY ("usuario_id")
        REFERENCES usuarios ("usuario_id")
);

CREATE TABLE IF NOT EXISTS prefeituras (
    "prefeitura_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "endereco_id" INTEGER NOT NULL,
    "cnpj" VARCHAR NOT NULL,

    PRIMARY KEY ("prefeitura_id"),

    CONSTRAINT "FK_PREFEITURAS_endereco_id"
        FOREIGN KEY ("endereco_id")
        REFERENCES enderecos ("endereco_id")
);

CREATE TABLE IF NOT EXISTS gestores (
    "gestor_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "prefeitura_id" INTEGER NOT NULL,
    "usuario_id" INTEGER NOT NULL,
    "pessoa_id" INTEGER NOT NULL,
    "status_gestor" VARCHAR NOT NULL,

    PRIMARY KEY ("gestor_id"),

    CONSTRAINT "FK_GESTORES_prefeitura_id"
        FOREIGN KEY ("prefeitura_id")
        REFERENCES prefeituras ("prefeitura_id"),

    CONSTRAINT "FK_GESTORES_usuario_id"
        FOREIGN KEY ("usuario_id")
        REFERENCES usuarios ("usuario_id"),

    CONSTRAINT "FK_GESTORES_pessoa_id"
        FOREIGN KEY ("pessoa_id")
        REFERENCES pessoas ("pessoa_id")
);

CREATE TABLE IF NOT EXISTS mediadores (
    "mediador_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "pessoa_id" INTEGER NOT NULL,
    "usuario_id" INTEGER,
    "prefeitura_id" INTEGER NOT NULL,
    "status_mediador" VARCHAR NOT NULL,

    PRIMARY KEY ("mediador_id"),

    CONSTRAINT "FK_MEDIADORES_prefeitura_id"
        FOREIGN KEY ("prefeitura_id")
        REFERENCES prefeituras ("prefeitura_id"),

    CONSTRAINT "FK_MEDIADORES_pessoa_id"
        FOREIGN KEY ("pessoa_id")
        REFERENCES pessoas ("pessoa_id"),

    CONSTRAINT "FK_MEDIADORES_usuario_id"
        FOREIGN KEY ("usuario_id")
        REFERENCES usuarios ("usuario_id")
);

CREATE TABLE IF NOT EXISTS audiencias (
    "audiencia_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "mediador_id" INTEGER NOT NULL,
    "endereco_id" INTEGER NOT NULL,
    "status_audiencia" VARCHAR NOT NULL,
    "data_audiencia" TIMESTAMP NOT NULL,

    PRIMARY KEY ("audiencia_id"),

    CONSTRAINT "FK_AUDIENCIAS_mediador_id"
        FOREIGN KEY ("mediador_id")
        REFERENCES mediadores ("mediador_id"),

    CONSTRAINT "FK_AUDIENCIAS_endereco_id"
        FOREIGN KEY ("endereco_id")
        REFERENCES enderecos ("endereco_id")
);

CREATE TABLE IF NOT EXISTS acordos (
    "acordo_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "audiencia_id" INTEGER NOT NULL,
    "status_acordo" VARCHAR NOT NULL,
    "data_acordo" DATE NOT NULL,

    PRIMARY KEY ("acordo_id"),

    CONSTRAINT "FK_ACORDOS_audiencia_id"
        FOREIGN KEY ("audiencia_id")
        REFERENCES audiencias ("audiencia_id")
);



CREATE TABLE IF NOT EXISTS denuncias (
    "denuncia_id" INTEGER GENERATED ALWAYS AS IDENTITY,
    "audiencia_id" INTEGER, -- pode ser nulo, pois a denúncia é feita antes da audiência ser marcada
    "acusador_id" INTEGER NOT NULL,
    "acusado_id" INTEGER NOT NULL,
    "causa_denuncia" VARCHAR NOT NULL,
    "detalhamento" VARCHAR,
    "data_denuncia" TIMESTAMP NOT NULL,

    PRIMARY KEY ("denuncia_id"),

    CONSTRAINT "FK_DENUNCIAS_audiencia_id"
        FOREIGN KEY ("audiencia_id")
        REFERENCES audiencias ("audiencia_id"),

    CONSTRAINT "FK_DENUNCIAS_acusador_id"
        FOREIGN KEY ("acusador_id")
        REFERENCES acusadores ("acusador_id"),

    CONSTRAINT "FK_DENUNCIAS_acusado_id"
        FOREIGN KEY ("acusado_id")
        REFERENCES acusados ("acusado_id")
);
