# 🛒 Projeto SmartRetail

O **Projeto SmartRetail** tem como objetivo aplicar os **fundamentos de projeto e modelagem de bancos de dados**, partindo da **abstração do mundo real** até a implementação prática das diferentes camadas de modelagem: **MER (Modelo Entidade-Relacionamento)**, **DER (Diagrama Entidade-Relacionamento)** e **ORM (Object-Relational Mapping)**. 

O projeto foi desenvolvido para **solucionar problemas reais de uma empresa do setor varejista**, abordando de forma estruturada o levantamento de requisitos, a organização das informações e a transformação do modelo conceitual em um banco de dados relacional integrado à linguagem de programação **Python**, por meio do framework **SQLAlchemy**.

Essa abordagem permite garantir **integridade dos dados**, **redução de redundâncias**, **manutenibilidade do sistema** e **base sólida para futuras evoluções**, alinhando conceitos teóricos à prática profissional.

## 🎯 Objetivos do Projeto

O Projeto **SmartRetail** tem como principais objetivos:

- Aplicar os **conceitos fundamentais de modelagem de dados**, desde a abstração do mundo real até a implementação do banco de dados.
- Desenvolver o **Modelo Entidade-Relacionamento (MER)** para representar o domínio do negócio de forma conceitual.
- Construir o **Diagrama Entidade-Relacionamento (DER)**, definindo tabelas, atributos, chaves primárias, chaves estrangeiras e restrições de integridade.
- Implementar o modelo lógico por meio do padrão **ORM (Object-Relational Mapping)**, utilizando **Python e SQLAlchemy**.
- Garantir a **integridade, consistência e normalização dos dados**, reduzindo redundâncias e inconsistências.
- Simular um **cenário real do setor varejista**, contemplando clientes, fornecedores, produtos, pedidos e itens de pedido.
- Criar uma **base de dados escalável e manutenível**, preparada para futuras evoluções do sistema.
- Consolidar conhecimentos teóricos e práticos em **banco de dados relacionais** e **arquitetura de sistemas**.

## Setor Varejista:

O setor de varejo é o segmento da economia responsável pela venda direta de bens ou serviços ao consumidor final, em quantidades geralmente pequenas e para uso pessoal ou familiar. Ele atua como o elo final da cadeia produtiva, conectando fabricantes, distribuidores e atacadistas aos consumidores. Além disso, é responsável pela comercialização direta de produtos e serviços ao consumidor final, sendo essencial para a geração de empregos, arrecadação de impostos e dinamização da economia.

### Problema:

A rede de supermercados opera atualmente com um sistema de gestão (ERP) legado, que não se comunica com as novas demandas do mercado. As informações estão retidas em 'silos de dados', resultando em uma visão parcial da operação. O sistema atual possui uma interface de baixa produtividade, falta de suporte para integração de APIs e processamento de dados em lote (não em tempo real), o que gera latência na tomada de decisão e inconsistências graves entre o estoque físico e o digital.


**A rede de supermercados tem as seguintes regras de negócio:**

Cada produto deve estar obrigatoriamente vinculado a um fornecedor;
Um cliente pode realizar múltiplos podidos ao longo do tempo;
Cada pedido pode conter vários produtos, e um mesmo produto pode ser comprado em diferentes pedidos;
Cada fornecedor pode fornecer múltiplos produtos, mas um produto só pode ter um fornecedor.

## Projeto SmartRetail:
**MER - Modelo Entidade-Relacionamento padrão:**
```
Fornecedor (CNPJ, nome_fantasia, contato, email)
Produto (nome, preço, quantidade_estoque)
Cliente (CPF, nome, email, telefone)
Pedido (data_pedido, valor_total)
Item_Pedido (quantidade, preço_venda_momento)
```
**Relacionamentos:**
```
Fornecedor fornece Produto (1:N)
Cliente realiza Pedido (1:N)
Pedido possui Item_Pedido (1:N)
Produto compõe Item_Pedido (1:N)
```
## Documentação do Modelo de Dados (DER):

Especificação do Diagrama Entidade-Relacionamento para o sistema de gestão de vendas e fornecedores. O esquema foi projetado para garantir a integridade dos dados e a rastreabilidade total dos produtos.

A partir da **modelagem conceitual (MER)**, foram definidos os atributos e seus respectivos tipos de dados na **modelagem lógica de dados (DER)**.  

No DER ocorrem as validações de:

- Tabelas  
- Colunas  
- Tipos de dados  
- Chaves primárias e estrangeiras (PK/FK)  
- Restrições de integridade  

---

## Entidade: Fornecedor

| Atributo         | Tipo de dado        | Restrições                  |
|------------------|---------------------|------------------------------|
| id_fornecedor    | Números inteiros    | PK, NOT NULL, UNIQUE         |
| nome_fantasia    | Texto variado       | —                            |
| cnpj             | Texto variado*      | UNIQUE                       |
| telefone         | Texto variado*      | —                            |
| email            | Texto variado*      | —                            |

> **Observação:**  
> Dados que possuem apenas números (como CNPJ e telefone) **não devem ser declarados como numéricos**, pois não são utilizados para cálculos, mas sim como **identificadores**.  
> Por boa prática, recomenda-se o uso de **tipos textuais com tamanho definido**.  
> No modelo lógico, não há preocupação com o tipo específico do SGBD.

---

## Entidade: Produto

| Atributo             | Tipo de dado         | Restrições                  |
|----------------------|----------------------|------------------------------|
| id_produtos          | Números inteiros     | PK, NOT NULL, UNIQUE         |
| nome                 | Texto                | —                            |
| categoria            | Texto                | —                            |
| preco                | Números decimais     | —                            |
| quantidade_estoque   | Números inteiros     | —                            |
| id_fornecedor        | Números inteiros     | FK, NOT NULL                 |

---

## Entidade: Clientes

| Atributo       | Tipo de dado     | Restrições                  |
|----------------|------------------|------------------------------|
| id_clientes    | Números inteiros | PK, NOT NULL, UNIQUE         |
| nome           | Texto            | —                            |
| cpf            | Texto variado*   | UNIQUE                       |
| telefone       | Texto variado*   | —                            |
| email          | Texto variado*   | —                            |

> **Observação:**  
> Assim como no CNPJ, o CPF e o telefone devem ser armazenados como **texto**, preservando formatação e evitando perda de zeros à esquerda.

---

## Entidade: Pedidos

| Atributo     | Tipo de dado         | Restrições                   |
|--------------|----------------------|------------------------------|
| id_pedido    | Números inteiros     | PK, NOT NULL, UNIQUE         |
| data_pedido  | Data                 | —                            |
| valor_total  | Números decimais     | —                            |
| id_cliente   | Números inteiros     | FK, NOT NULL                 |

---

## Entidade: Item_Pedido (Entidade Associativa)

| Atributo        | Tipo de dado         | Restrições                   |
|-----------------|----------------------|------------------------------|
| quantidade      | Números inteiros     | —                            |
| preco_unitario  | Números decimais     | —                            |
| id_pedido       | Números inteiros     | FK, NOT NULL                 |
| id_produto      | Números inteiros     | FK, NOT NULL                 |

> **Observação:**  
> A entidade **Item_Pedido** utiliza **chave primária composta**, formada por:
> - `id_pedido`
> - `id_produto`

---

## Considerações sobre o Modelo

O modelo adotado reduz a duplicidade de dados ao vincular o **Produto diretamente ao Fornecedor**, eliminando o risco de cadastrar o mesmo produto múltiplas vezes para fornecedores diferentes.

Além disso, caso um lote de um produto apresente problemas, é possível rastrear no banco de dados:

- **Produto → Fornecedor**
- **Produto → Item_Pedido → Cliente**

A tabela **Item_Pedido** armazena o **preço praticado no momento da venda**, garantindo que, mesmo que o preço do produto seja alterado futuramente, o histórico das vendas permaneça **íntegro e consistente**.

## Integração com Python e SQLAlchemy

A implementação do banco de dados foi realizada por meio da integração com a linguagem de programação **Python**, utilizando o framework **SQLAlchemy**, que adota o padrão **ORM (Object-Relational Mapping)** para a persistência dos dados.

O objetivo dessa integração é **implementar o modelo lógico (DER)** em um formato adequado para um **Sistema Gerenciador de Banco de Dados (SGBD)**, traduzindo as entidades, atributos e relacionamentos definidos na modelagem em **classes Python e tabelas relacionais**.

Por meio do SQLAlchemy, cada entidade do modelo lógico é representada como uma classe, enquanto seus atributos tornam-se colunas da tabela correspondente. Os relacionamentos entre as entidades são implementados por meio de chaves primárias e estrangeiras, garantindo a **integridade referencial**, a **consistência dos dados** e a **aderência às regras de negócio**.

### Benefícios da utilização do SQLAlchemy

* Implementação direta do modelo lógico no banco de dados
* Mapeamento objeto-relacional entre Python e SGBD
* Garantia de integridade e consistência dos dados
* Facilidade de manutenção e evolução do sistema
* Maior produtividade no desenvolvimento da aplicação

### Tecnologias Utilizadas:

- **Python**: Linguagem de programação utilizada no desenvolvimento da aplicação e na integração com o banco de dados.
- **SQLAlchemy**: Framework ORM responsável pelo mapeamento objeto-relacional, permitindo a implementação do modelo lógico no SGBD e a persistência dos dados.
- **SQL**: Linguagem utilizada para consultas, manipulação e definição de dados no banco.
- **Git e GitHub**: Ferramentas utilizadas para controle de versão e hospedagem do repositório do projeto.
- **DuckDB** é um banco de dados relacional analítico (OLAP) embutido, rápido, sem servidor, ideal para análise de dados e integração com Python.
📌**Nota:** Ele funciona como um arquivo (.duckdb), parecido com SQLite, porém orientado a análise.
- **VS Code** (Ambiente de desenvolvimento)
- **PowerShell** (Execução dos comandos no Windows)
- **DB Designer** (Modelagem do MER)

### Arquitetura do Projeto (MER → DER → ORM):

A arquitetura do projeto foi estruturada seguindo boas práticas de modelagem de dados e desenvolvimento de software, respeitando as etapas de abstração e implementação.

### Estrutura do projeto:

```
├── src/
│ ├── models/
| | ├── init.py
│ │ ├── cliente.py
│ │ ├── fornecedor.py
│ │ ├── produto.py
│ │ ├── pedido.py
│ │ └── item_pedido.py
│ │
│ ├── database/
│ │ ├── init.py
│ │ ├── connection.py
│ │ └── base.py
│ │
│ ├── main.py
│ ├── init.py
│ 
│
├── docs/
│ ├── DER_simplificado.dbml
│ └── DER.png
│ └── DER.dbml
│
├── requirements.txt
├── README.md
└── .gitignore
```


## Possíveis Evoluções do Sistema

O projeto foi desenvolvido de forma modular, permitindo futuras expansões e melhorias, tais como:

- Implementação de **CRUD completo** para todas as entidades  
- Criação de uma **API REST** utilizando frameworks como Flask ou FastAPI  
- Integração com **interfaces gráficas ou aplicações web**  
- Inclusão de **rotinas de validação** (CPF, CNPJ, e-mail)  
- Implementação de **controle de usuários e autenticação**  
- Criação de **relatórios gerenciais** e dashboards analíticos  
- Evolução para um ambiente **OLAP/BI**, com rotinas **ETL**  
- Implementação de **testes automatizados** para validação das regras de negócio  

Essas evoluções tornam o sistema mais **robusto**, **escalável** e **aderente a cenários reais de mercado**.

## 👤 Autor do Projeto:

**Daniel Martins França**

Projeto desenvolvido com foco em **modelagem de dados**, **bancos de dados relacionais** e **integração com Python**, aplicando boas práticas desde a fase conceitual até a implementação utilizando ORM.

### 📬 Contato:

- 📧 Email: [f.daniel.m@gmail.com](mailto:f.daniel.m@gmail.com)  
- 💼 LinkedIn: [www.linkedin.com/in/danixdev](https://www.linkedin.com/in/danixdev)  
- 📁 Trabalhos: [wwww.danixdev.blogspot.com/2026/01/projeto-de-banco-de-dados-para.html](https://danixdev.blogspot.com/2026/01/projeto-de-banco-de-dados-para.html)


**Execução:**

Abra o terminal na pasta project_varejo e rode:

```python -m src.main```

**Atenção**:

Caso tenha problemas com a engine do Duckdb, execute no terminal a instalação do mesmo:

```pip install duckdb duckdb-engine sqlalchemy```