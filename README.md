# 🏢 Sistema de Gestão de Empresas

Aplicação desktop em Python para cadastrar, consultar, atualizar e excluir empresas, com interface gráfica em Tkinter e banco de dados relacional PostgreSQL.

O sistema organiza os dados de empresas parceiras (fornecedores, clientes, distribuidores e outros) em um banco normalizado, com busca por CNPJ e por razão social ou nome fantasia.

---

## 📸 Tela

![Tela principal](imagens/tela.png)

---

## 🚀 Funcionalidades

- **Cadastro, edição e exclusão** de empresas (CRUD completo)
- **Busca por CNPJ** ou por **razão social / nome fantasia** (busca parcial, sem diferenciar maiúsculas de minúsculas)
- **Listagem em tabela** com todas as empresas, ordenadas por razão social
- **Campos de seleção alimentados pelo banco:** natureza jurídica, porte, tipo de empresa, segmento, status e classificação
- **Validação de campos obrigatórios** (CNPJ e razão social) e mensagens de aviso, sucesso e erro
- **Confirmação antes de excluir** um registro
- **Tratamento de erros de conexão** com o banco, sem travar a aplicação

---

## 🛠️ Tecnologias

| Categoria | Tecnologias |
|---|---|
| Linguagem | Python |
| Interface gráfica | Tkinter (ttk) |
| Banco de dados | PostgreSQL |
| Acesso ao banco | psycopg2 |
| Configuração | python-dotenv (variáveis de ambiente) |
| Ferramentas | Git, GitHub |

---

## 🧱 Arquitetura

O projeto separa interface, acesso a dados e criação do banco, seguindo o padrão **DAO (Data Access Object)**:

```
sistema-gestao-empresas/
├── src/
│   ├── main.py            # Ponto de entrada: abre a janela
│   ├── tela.py            # Interface gráfica (Tkinter)
│   ├── empresasDAO.py     # Acesso ao banco: consultas, inserção, atualização, exclusão
│   └── bancodedado.py     # Script que cria as tabelas e os dados iniciais
├── imagens/
│   └── tela.png
├── .env.example           # Modelo das variáveis de ambiente
├── .gitignore
├── requirements.txt
└── README.md
```

- A tela **não escreve SQL**: ela chama métodos do `EmpresasDAO`.
- Todas as consultas usam **parâmetros** (`%s`), o que protege contra SQL injection.
- As credenciais do banco ficam no arquivo `.env`, que **não vai para o GitHub**.

---

## 🗄️ Modelo de dados

O banco tem 7 tabelas. A tabela principal, `empresas`, se relaciona por chave estrangeira com 6 tabelas de apoio:

| Tabela | Função |
|---|---|
| `empresas` | Dados da empresa (CNPJ único, razão social, contatos, capital social etc.) |
| `natureza_juridica` | Natureza jurídica (Ltda., S.A., cooperativa etc.) |
| `porte` | Porte da empresa (microempresa, pequeno porte etc.) |
| `tipos_empresa` | Fornecedor, distribuidor, cliente, parceiro etc. |
| `segmentos` | Segmento de atuação (tecnologia, saúde, indústria etc.) |
| `status_empresa` | Ativa, inativa, bloqueada, em análise |
| `classificacoes` | Pequena, média, grande empresa etc. |

Há índices em `cnpj`, `razao_social` e `nome_fantasia` para acelerar as buscas.

---

## ⚙️ Como executar

**Pré-requisitos:** Python 3.10+ (com Tkinter), PostgreSQL e Git.
No Linux, se o Tkinter não estiver instalado: `sudo apt install python3-tk`.

### 1. Clonar o repositório

```bash
git clone https://github.com/Marydev23/sistema-gestao-empresas.git
cd sistema-gestao-empresas
```

### 2. Instalar as dependências

```bash
python -m venv venv
source venv/bin/activate        # no Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Criar o banco no PostgreSQL

Crie um banco vazio (pelo pgAdmin ou pelo terminal):

```sql
CREATE DATABASE gestao_empresas;
```

### 4. Configurar as variáveis de ambiente

Copie o arquivo de exemplo e preencha com os seus dados:

```bash
cp .env.example .env            # no Windows: copy .env.example .env
```

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=gestao_empresas
DB_USER=postgres
DB_PASSWORD=sua_senha
```

### 5. Criar as tabelas

```bash
python src/bancodedado.py
```

Execute **uma única vez**. O script cria as tabelas e insere os dados iniciais (naturezas jurídicas, portes, tipos, segmentos, status e classificações). Se rodar de novo, ele avisa que as tabelas já existem.

### 6. Iniciar a aplicação

```bash
python src/main.py
```

---

## 💡 Como usar

- **Cadastrar:** preencha os campos e clique em **Novo / Salvar**.
- **Editar:** clique em uma empresa na tabela, altere os dados e clique em **Atualizar**.
- **Excluir:** selecione a empresa e clique em **Excluir** (o sistema pede confirmação).
- **Buscar:** informe o CNPJ ou parte da razão social e clique em **Buscar**. Com os campos vazios, a busca lista todas as empresas.
- **Limpar:** esvazia os campos do formulário.

> Digite o CNPJ apenas com números (14 dígitos).

---

## 🚧 Próximos passos

- Validação dos dígitos verificadores do CNPJ e máscara de formatação
- Testes automatizados
- Reaproveitar a consulta principal, que hoje se repete em três métodos do DAO
- Empacotar como executável para Windows

---

## 👩‍💻 Autora

**Marilza de Souza Santos**
[LinkedIn](https://www.linkedin.com/in/marilzadesouza) · [GitHub](https://github.com/Marydev23)

Projeto sob licença MIT.
