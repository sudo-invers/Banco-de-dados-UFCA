--------- Novo BD ---------


CREATE TABLE IF NOT EXISTS "USUARIO" (
  "usuario_id" INTEGER,
  "email" VARCHAR,
  "senha" VARCHAR,
  "tipo_usuario" VARCHAR,

  PRIMARY KEY ("usuario_id")
);

CREATE TABLE IF NOT EXISTS "ENDERECO" (
  "endereco_id" INTEGER,
  "rua" VARCHAR,
  "bairro" VARCHAR,
  "cidade" VARCHAR,
  "numero" VARCHAR,

  PRIMARY KEY ("endereco_id")
);

CREATE TABLE IF NOT EXISTS "PESSOA" (
  "pessoa_id" INTEGER,
  "endereco_id" INTEGER,
  "nome" VARCHAR,
  "telefone" VARCHAR,
  "n_inscricao_tributaria" VARCHAR,
  "data_nascimento" DATE,

  PRIMARY KEY ("pessoa_id"),
  
  CONSTRAINT "FK_PESSOA_endereco_id"
  	FOREIGN KEY ("endereco_id")
	    REFERENCES "ENDERECO"("endereco_id")
);

CREATE TABLE IF NOT EXISTS "ACUSADO" (
  "acusado_id" INTEGER,
  "pessoa_id" INTEGER,
  
  PRIMARY KEY ("acusado_id"),

  CONSTRAINT "FK_ACUSADO_pessoa_id"
    FOREIGN KEY ("pessoa_id")
      REFERENCES "PESSOA"("pessoa_id")
);

CREATE TABLE IF NOT EXISTS "ACUSADOR" (
  "acusador_id" INTEGER,
  "pessoa_id" INTEGER,
  "usuario_id" INTEGER,
  
  PRIMARY KEY ("acusador_id"),
  
  CONSTRAINT "FK_ACUSADOR_pessoa_id"
    FOREIGN KEY ("pessoa_id")
      REFERENCES "PESSOA"("pessoa_id")
);

CREATE TABLE IF NOT EXISTS "PREFEITURA" (
  "prefeitura_id" INTEGER,
  "endereco_id" INTEGER,
  "cnpj" VARCHAR,

  PRIMARY KEY ("prefeitura_id"),
  
  CONSTRAINT "FK_PREFEITURA_endereco_id"
    FOREIGN KEY ("endereco_id")
      REFERENCES "ENDERECO"("endereco_id")
);

CREATE TABLE IF NOT EXISTS "GESTOR" (
  "gestor_id" INTEGER,
  "prefeitura_id" INTEGER,
  "usuario_id" INTEGER,
  "pessoa_id" INTEGER,
  "status_gestor" VARCHAR,

  PRIMARY KEY ("gestor_id"),

  CONSTRAINT "FK_GESTOR_prefeitura_id"
    FOREIGN KEY ("prefeitura_id")
      REFERENCES "PREFEITURA"("prefeitura_id")
);

CREATE TABLE IF NOT EXISTS "MEDIADOR" (
  "mediador_id" INTEGER,
  "pessoa_id" INTEGER,
  "usuario_id" INTEGER,
  "prefeitura_id" INTEGER,
  "status_mediador" VARCHAR,
  
  PRIMARY KEY ("mediador_id"),
  
  CONSTRAINT "FK_MEDIADOR_prefeitura_id"
    FOREIGN KEY ("prefeitura_id")
      REFERENCES "PREFEITURA"("prefeitura_id"),

  CONSTRAINT "FK_MEDIADOR_pessoa_id"
    FOREIGN KEY ("pessoa_id")
      REFERENCES "PESSOA"("pessoa_id"),
      
  CONSTRAINT "FK_MEDIADOR_usuario_id"
    FOREIGN KEY ("usuario_id")
      REFERENCES "USUARIO"("usuario_id")
);

CREATE TABLE IF NOT EXISTS "AUDIENCIA" (
  "audiencia_id" INTEGER NOT NULL,
  "mediador_id" INTEGER NOT NULL,
  "endereco_id" INTEGER NOT NULL,
  "status_audiencia" VARCHAR,
  "data_audiencia" TIMESTAMP NOT NULL,
  
  PRIMARY KEY ("audiencia_id"),
  
  CONSTRAINT "FK_AUDIENCIA_mediador_id"
    FOREIGN KEY ("mediador_id")
      REFERENCES "MEDIADOR"("mediador_id"),

  CONSTRAINT "FK_AUDIENCIA_endereco_id"
  	FOREIGN KEY ("endereco_id")
	    REFERENCES "ENDERECO"("endereco_id")
);

CREATE TABLE IF NOT EXISTS "ACORDO" (
  "acordo_id" INTEGER NOT NULL,
  "audiencia_id" INTEGER NOT NULL,
  "status_acordo" VARCHAR NOT NULL,
  "data_acordo" DATE NOT NULL,

  PRIMARY KEY ("acordo_id"),

  CONSTRAINT "FK_ACORDO_audiencia_id"
    FOREIGN KEY ("audiencia_id")
      REFERENCES "AUDIENCIA"("audiencia_id")
);



CREATE TABLE IF NOT EXISTS "DENUNCIA" (
  "denuncia_id" INTEGER NOT NULL,
  "audiencia_id" INTEGER, -- pode ser nulo, pois a denúncia é feita antes da audiência ser marcada
  "acusador_id" INTEGER NOT NULL,
  "acusado_id" INTEGER NOT NULL,
  "causa_denuncia" VARCHAR NOT NULL,
  "detalhamento" VARCHAR,
  "data_denuncia" TIMESTAMP NOT NULL,

  PRIMARY KEY ("denuncia_id"),

  CONSTRAINT "FK_DENUNCIA_audiencia_id"
    FOREIGN KEY ("audiencia_id")
      REFERENCES "AUDIENCIA"("audiencia_id"),

  CONSTRAINT "FK_DENUNCIA_acusador_id"
    FOREIGN KEY ("acusador_id")
      REFERENCES "ACUSADOR"("acusador_id"),

  CONSTRAINT "FK_DENUNCIA_acusado_id"
    FOREIGN KEY ("acusado_id")
      REFERENCES "ACUSADO"("acusado_id")
);

