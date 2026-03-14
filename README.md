# Grupo08 - Banco de dados

# Como rodar o sistema

(É necessário PostgreSQL para que o sistema funcione: https://www.postgresql.org/download)

- Criar ambiente virtual com "python3 -m venv .env"
- logar no ambiente virtual: pelo Linux "source ./.venv/bin/activate" | pelo windows ".\env\Scripts\activate.ps1"
- Instalar dependências com o "pip install -r requeriments.txt"
- use o comando "python3 -m main"


# Sistema de Mediação de conflitos comunitários

Pergunta norteadora: De que forma um sistema de mediação de conflitos comunitários pode organizar casos, audiências e acordos, preservando sigilo e estatísticas públicas?

# Definição  e objetivos do projeto

O sistema de gerenciamento de conflitos comunitários é um projeto desenvolvido por alunos do curso de Engenharia de Software na disciplina de Banco de Dados para atuar como um facilitador na resolução dos conflitos comunitários capaz de registrar a todas informações relevantes em relação a esses conflitos tais como: dados de denúncias, acordos e audiências registrados por três tipos de usuários, os acusadores que denunciam o conflito, mediadores que acompanham e buscam solucionar os conflitos por meio das audiências e acordos e as prefeituras que cadastram os mediadores e recebem as estatísticas do sistema para serem publicadas. O sistema visa produzir estatísticas públicas com esses dados sem expor a privacidade dos envolvidos. 


Esse projeto possui como principais objetivos:

 - Facilitar o aprendizado de banco de dados utilizando um exemplo de problema real onde somos motivados a aplicar na prática planejamento, organização e modelagem de banco de dados
 
 - Elaborar requisitos e organização de um banco de dados aplicando entidades, relacionamentos, atributos, cardinalidades e tipos de dados.

 - Construir modelos conceitual, físico e lógico de fácil entendimento para serem utilizados no desenvolvimento do sistema e na construção do banco de dados.

 - Desenvolver habilidades interpessoais de resolução de problemas, trabalho em equipe e organização.

# Instruções básicas para compreender o projeto

Um Sistema de gerenciamento de conflitos comunitários trata-se de um software responsável por facilitar o processo de resolução de conflitos preservando o sigilo na produção de estatísticas públicas e permitindo que as denúncias sejam feitas sem a necessidade do cidadão sair de casa. Para desenvolver um sistema desse tipo é necessária uma organização clara dos dados em um banco de dados para que as estatísticas sejam geradas de maneira a facilitar a compreensão do que tem causado os conflitos e como seria possível resolvê-los mais facilmente. Dessa maneira, o seguinte projeto visa modelar e organizar essas informações desse Sistema para que seu desenvolvimento seja facilitado. 

O Banco de Dados desse sistema possuirá três categorias de usuários, também difinidos no modelo como entidades, que são: acusador, mediador e prefeitura. A prefeitura é responsável por acompanhar toda a cidade por meio das estatísticas e dos mediadores que são os funcionários que atuam na resolução dos conflitos e os acusadores podem ser quaisquer cidadãos daquele município que desejam denúnciar alguma injustiça que tenham vivenciado na comunidade.

As demais entidades serão voltadas a informações dentro do sistema: denúncias, audiências, acordos, endereços e estatísticas.

Cada uma dessas entidades possui diversos atributos especificados posteriormente no [modelo conceitual](https://lucid.app/lucidspark/b70cc641-59a2-40bb-931c-fe3e7eaa2408/edit?viewport_loc=-1382%2C-496%2C4656%2C2213%2C0_0&invitationId=inv_30809952-c4bf-4a87-bb95-0981bc8d1def) e na Definição do problema. 

Além disso, dentre os principais relacionamentos temos os de Acusador -> Denúncia (O acusador faz o registro da denúncia) ,Prefeitura -> Mediador(A prefeitura cadastra os mediadores), Mediador -> Denúcia -> Audiência(O mediador recebe a denúncia e marca a audiência), Audiência -> Acordo (Uma audiência pode resultar em Acordo) e Prefeitura -> Estatísticas(A prefeitura recebe as estatísticas). Teremos outros relacionamentos vinculados com endereços, usuários e ações, que são especificados nos modelos de banco de dados.


# Requisitos para execução 

[RF01] Registro de informações do acusador
- O sistema deve permitir cadastrar acusadores com os campos obrigatórios: Nome, CPF, Endereço e Idade, validar todos os dados e não concluir o cadastro se algum dado estiver inválido ou em branco, permitindo também a atualização dessas informações.

[RF02] Registro de informações do acusado
- O sistema deve permitir cadastrar acusados com os campos obrigatórios: Nome, CPF, Endereço e Idade, validar todos os dados e não concluir o cadastro se algum dado estiver inválido ou em branco, permitindo também a atualização dessas informações.

[RF03] Registro de denúncia
- O sistema deve permitir que o acusador registre uma denúncia, associando acusador, acusado, causa do fato e endereço, validar todos os campos obrigatórios, permitir associar endereços já cadastrados ou cadastrar novos, e definir o status inicial da denúncia como “registrada”.

[RF04] Registro de endereço
- O sistema deve permitir cadastrar endereços com os campos obrigatórios Rua, Bairro e Cidade, permitir reutilizar endereços já cadastrados ou cadastrar novos, e associar os endereços a acusadores, acusados e denúncias

[RF05] Encaminhamento da denúncia para mediador
- O sistema deve permitir que a prefeitura atribua manual ou automaticamente um mediador disponível a uma denúncia, registrar o vínculo mediador–denúncia no banco de dados, atualizar o status da denúncia para “em mediação” e notificar o mediador responsável

[RF06] Registro de acordo
- O sistema deve permitir registrar acordos apenas para denúncias com status “em mediação”, registrar acusador, acusado, mediador, status e resultado do acordo, gerar automaticamente um ID único para cada acordo e associar o acordo à denúncia correspondente.

[RF07] Marcação de audiência
- O sistema deve permitir marcar audiências apenas para denúncias com status “em mediação”, associar a audiência ao mediador responsável, registrar data, hora e local da audiência, e vincular a audiência à denúncia correspondente.

[RF08] Atualização do status do acordo
- O sistema deve permitir que apenas o mediador responsável altere o status do acordo, aceitar apenas os status válidos “em andamento”, “fechado” e “cancelado”, registrar a data da atualização e histórico de mudanças, e refletir a mudança de status no histórico da denúncia.

[RF09] Geração de estatísticas das denúncias
- O sistema deve gerar estatísticas das denúncias, incluindo total de denúncias por bairro e ranking das causas mais frequentes, garantir a anonimização dos dados (sem nomes de pessoas), e atualizar automaticamente as estatísticas sempre que uma nova denúncia for registrada.

[RF10] Geração de estatísticas dos acordos
- O sistema deve gerar estatísticas dos acordos, incluindo número total de acordos fechados e relação entre acordos fechados e denúncias totais, garantir a anonimização dos dados (sem mostrar as informações pessoais), e atualizar automaticamente as estatísticas sempre que um acordo for registrado ou atualizado.

# Definição do Problema

Muitos conflitos de convivência ocorrem entre moradores de uma cidade por diversas causas e muitas vezes esses conflitos afetam a dinâmica da coletividade e respeito entre as pessoas, casos que seriam resolvidos de maneira simples são levados a agressões  e processos judiciais com frequência. Para promover a justiça na resolução desses conflitos, a prefeitura pretende ter um controle a partir do mapeamento das principais causas, localidades e modos de resolução desses conflitos. Esse mapeamento precisa ser objetivo, baseado em dados estatísticos de modo a preservar o sigilo das informações pessoais dos moradores. Para realizar essa ação a prefeitura contratou mediadores responsáveis por receber e resolver esses conflitos sem a necessidade de um processo judicial.

Para facilitar esse processo, o grupo 8 do Curso de Engenharia de Software da disciplina de banco de dados propôs o desenvolvimento de um sistema intermediador de conflitos responsável por organizar dados desses conflitos e facilitar a resolução desses e o trabalho dos mediadores. 
O sistema tem como principais funcionalidades: 

Receber denúncias que possuam:  id da denúncia, acusação, id do acusador, nome e telefone do acusado, endereço, causa do conflito e status(em análise, em andamento, resolvida)

Fornecer suporte para a resolução desses problemas por meio de um mediador(funcionário da prefeitura e ator no sistema) que deve ser cadastrado no sistema informando nome, cpf, endereço, telefone e id do mediador. Esse cadastro só poderá ser feito por um membro responsável pela conta da prefeitura, ator que possuirá uma conta de administrador. 

A conta da prefeitura deverá conter informações como: Endereço, CNPJ, id da prefeitura, a identificação dos gestores e o contato, e deverá passar por uma confirmação do gov para realizar esse cadastro.

O cidadão acusador deverá realizar seu cadastro na plataforma informando seu nome, idade, sexo, endereço, telefone e cpf e depois disso poderá cadastrar sua denúncia.

Baseado na localidade informada será destinado um mediador mais próximo para acompanhar o caso. No sistema, o mediador poderá marcar a audiência que reunirá o acusador e o acusado para debater a respeito do conflito. Para fazer esse registro, o mediador deve entrar em contato tanto com o acusador quanto com o acusado para definir uma data para se reunirem no fórum municipal mais próximo. O cadastro da audiência no sistema deve conter as informações de data, hora, id, endereço, denúncia, acusador, acusado e mediador do conflito.
Caso seja necessária a realização de mais de uma Audiência, o mediador também poderá cadastrar essa informação no sistema. 

Após a realização dos processos já apresentados, caso um acordo tenha sido firmado, o mediador adicionará as informações do acordo no sistema que devem ser: data do acordo, solução e id da denúncia  e assim o status da denúncia mudará para resolvida.

Todas as informações de Endereço deverão conter: cidade, cep, bairro, rua, número e complemento.

Além disso, as informações não confidenciais de denúncias e acordos culminarão  na elaboração das estatísticas públicas responsáveis por mapear principais causas de conflitos, tempo médio para resolução, percentual de acordos/denúncias e bairros com maior incidência de conflitos e com base nesses dados a prefeitura poderá analisar as causas e buscar soluções cada vez mais eficazes para manter a justiça e o bem-estar coletivo preservando a privacidade da sua população.

As informações confidenciais como documentos, nome de pessoas, contatos e endereço completo deverão ser privadas e acessadas somente para conferência de veracidade da identidade das pessoas e no caso especificado para a marcação de audiências.

# Histórias de Usuário 

1. Registrar informações do acusador
- Como acusador, eu gostaria de registrar meus dados (Nome, CPF, Endereço,
idade), para formalizar uma denúncia;

2. Registrar informações do acusado
- Como Prefeitura, gostaria de registrar as informações do acusado (Nome,
CPF, idade, Endereço), para que o caso possa ser formalizado;

3. Registrar denúncia
- Como acusador, gostaria de criar uma denúncia, informando o nome do
acusador e a causa do fato, para que o processo de mediação possa ser
iniciado;

4. Registar Endereço
- Como prefeitura, quero registrar cada endereço (Rua, Bairro, Cidade), das
denúncias e acordos, para organizar os dados geograficamente e, gerar
estatísticas

5. Encaminhar a medida para o Mediador
- Como prefeitura, quero atribuir cada denúncia a um Mediador, para que ele
possa acompanhar e gerir o caso;

6. Registar Acordo
- Como Audiência, gostaria de registar um acordo entre o Acusador e o
Acusado em uma audiência, com o objetivo de facilitar um consenso entre as
partes em conflito;

7. Marcar Audiência
- Como mediador, gostaria de marcar uma audiência, com o objetivo de avaliar
os processos;

8. Atualizar os status do Acordo
- Como Audiência, gostaria de atualizar os status do acordo (fechado, em
andamento, cancelado), com o objetivo prosseguir o caso;

9. Receber estatísticas das denúncias
- Como prefeitura, gostaria de receber estatísticas com base nas denúncias e
nos acordos, para organizar os dados;

10. Receber estatísticas dos acordos
- Como prefeitura, quero receber estatísticas dos acordos, com o objetivo de
estruturar as informações;

# Critérios de Aceitação

1. Registar informações do acusador
- O sistema deve permitir inserir nome, idade, endereço e CPF;
- Todos os campos obrigatórios devem ser preenchidos;
- O cadastro só é concluído se todos os dados forem válidos.

2. Registar informações do acusado
- O sistema deve permitir inserir nome, idade, endereço e CPF;
- Todos os campos obrigatórios devem ser preenchidos;
- O cadastro só é concluído se todos os dados forem válidos.

3. Registar denúncia
- O sistema deve permitir selecionar/registrar o acusado e o acusador.
- A denúncia deve incluir: acusação, causa e endereço do fato.

4. Registrar Endereço
- O endereço deve conter obrigatoriamente rua, bairro e cidade;
- O sistema deve permitir reutilizar endereços já cadastrados ou cadastrar um novo;
- Um endereço deve ser associável a acusadores, acusados e denúncias;

5. Encaminhar a medida para o Mediador
- O sistema deve atribuir automaticamente ou manualmente um mediador disponível;
- O vínculo mediador–denúncia deve ser registrado no banco.
- A denúncia deve mudar para o status “em mediação”;

6. Registar Acordo
- Um acordo só pode ser registrado se existir uma denúncia em mediação;
- O acordo deve registrar status e resultado;
- O acordo deve estar vinculado ao acusador, ao acusado e ao mediador;
- Deve ser gerado um ID do acordo automaticamente

7. Marcar Audiência
- Uma audiência só pode ser marcada quando o status da denúncia constar “em Mediação” ;
- A audiência deve estar vinculada a um mediador;

8. Atualizar Status do Acordo
- Apenas o mediador responsável pode alterar o status;
- O sistema deve aceitar somente os status válidos: “em andamento”, “fechado”, “cancelado”;
- A data da atualização deve ser registrada;
- A mudança de status deve refletir no histórico da denúncia;

9. Estatísticas da Denúncia 
- O sistema deve gerar o total de denúncias por bairro;
- O sistema deve gerar as causas mais frequentes;
- Os dados devem ser anonimizados (sem nomes de pessoas);
- A atualização deve ocorrer sempre que uma nova denúncia for registrada;

10. Estatísticas dos Acordos
- O sistema deve gerar o número total de acordos fechados;
- O sistema deve gerar relação entre acordos fechados e denúncias totais;
- Os dados devem ser gerados automaticamente após cada atualização de acordo;
- Os dados devem ser agregados, sem informações pessoais;


# Modelos MER e DER

[Clique aqui para acessar o Modelo Conceitual](https://lucid.app/lucidspark/b70cc641-59a2-40bb-931c-fe3e7eaa2408/edit?viewport_loc=-1382%2C-496%2C4656%2C2213%2C0_0&invitationId=inv_30809952-c4bf-4a87-bb95-0981bc8d1def)

[Clique aqui para acessar o Diagrama Entidade Relacionamento](https://lucid.app/lucidchart/efd61ff3-02be-4ed6-9d89-67cfc7a42c0c/edit?viewport_loc=-64%2C410%2C1839%2C863%2C0_0&invitationId=inv_8327bd62-0403-4cbb-915e-dfe4ebe423df)

[Clique aqui para acessar o Modelo Entidade Relacionamento extendido](https://drive.google.com/file/d/1e1AdAOSJA3Ejn_RfgWzc1QXw4T7juhIS/view?usp=drive_link)

# Tuplas 
[Link para acessar as tuplas](https://escolatrabalhador4-my.sharepoint.com/:x:/g/personal/leticia_365diasgmail_com_escoladotrabalhador40_com_br/IQBMRvCmjCBoRqpJFVDIF9jfAZoY0IGKCmDuzy0b7IW5tnY?e=BsGLnA)

# Commits no liveshare

git commit -m "Co-authored-by: Dorian Dayvid Gomes Feitosa <OtherDinosaur@users.noreply.github.com>"

