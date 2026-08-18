import os
import psycopg2
from dotenv import load_dotenv


# ==========================================
# CONFIGURAÇÃO
# ==========================================

load_dotenv(encoding="latin-1")


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


conexao = None
cursor = None


try:

    # ==========================================
    # CONECTAR AO POSTGRESQL
    # ==========================================

    conexao = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = conexao.cursor()

    print("PostgreSQL conectado!")


    # ==========================================
    # APAGAR BANCO ANTIGO
    # ==========================================
    #
    # ATENÇÃO:
    # Isso apaga TODAS as tabelas deste sistema.
    #
    # ==========================================

   


    # ==========================================
    # NATUREZA JURÍDICA
    # ==========================================

    cursor.execute("""
        CREATE TABLE natureza_juridica (

            cod_natureza VARCHAR(20) PRIMARY KEY,

            descricao_natureza VARCHAR(200) NOT NULL

        );
    """)


    # ==========================================
    # NATUREZAS BÁSICAS
    # ==========================================

    naturezas = [

        ("1015", "Órgão Público do Poder Executivo Federal"),
        ("1023", "Órgão Público do Poder Executivo Estadual"),
        ("1031", "Órgão Público do Poder Executivo Municipal"),
        ("2011", "Empresa Pública"),
        ("2038", "Sociedade de Economia Mista"),
        ("2046", "Sociedade Empresária Limitada"),
        ("2054", "Sociedade Anônima Fechada"),
        ("2062", "Sociedade Empresária Limitada"),
        ("2070", "Sociedade Anônima Aberta"),
        ("2135", "Empresário"),
        ("2143", "Cooperativa"),
        ("2151", "Consórcio de Sociedades"),
        ("2160", "Grupo de Sociedades"),
        ("2305", "Organização Religiosa"),
        ("2313", "Associação Privada"),
        ("2321", "Fundação Privada")

    ]


    for natureza in naturezas:

        cursor.execute("""
            INSERT INTO natureza_juridica (
                cod_natureza,
                descricao_natureza
            )
            VALUES (%s, %s)
            ON CONFLICT (cod_natureza) DO NOTHING;
        """, natureza)


    # ==========================================
    # PORTE
    # ==========================================

    cursor.execute("""
        CREATE TABLE porte (

            cod_porte VARCHAR(10) PRIMARY KEY,

            descricao_porte VARCHAR(100) NOT NULL

        );
    """)


    portes = [

        ("00", "Porte não informado"),
        ("01", "Microempresa"),
        ("03", "Empresa de Pequeno Porte"),
        ("05", "Demais")

    ]


    for porte in portes:

        cursor.execute("""
            INSERT INTO porte (
                cod_porte,
                descricao_porte
            )
            VALUES (%s, %s);
        """, porte)


    # ==========================================
    # TIPOS DE EMPRESA
    # ==========================================

    cursor.execute("""
        CREATE TABLE tipos_empresa (

            id SERIAL PRIMARY KEY,

            nome VARCHAR(100) NOT NULL UNIQUE

        );
    """)


    tipos_empresa = [

        "Fornecedor",
        "Distribuidor",
        "Fabricante",
        "Prestador de Serviços",
        "Cliente",
        "Parceiro"

    ]


    for tipo in tipos_empresa:

        cursor.execute("""
            INSERT INTO tipos_empresa (nome)
            VALUES (%s);
        """, (tipo,))


    # ==========================================
    # SEGMENTOS
    # ==========================================

    cursor.execute("""
        CREATE TABLE segmentos (

            id SERIAL PRIMARY KEY,

            nome VARCHAR(100) NOT NULL UNIQUE

        );
    """)


    segmentos = [

        "Alimentação",
        "Construção",
        "Tecnologia",
        "Saúde",
        "Educação",
        "Comércio",
        "Indústria",
        "Serviços",
        "Transporte",
        "Logística",
        "Distribuição",
        "Outros"

    ]


    for segmento in segmentos:

        cursor.execute("""
            INSERT INTO segmentos (nome)
            VALUES (%s);
        """, (segmento,))


    # ==========================================
    # STATUS DA EMPRESA
    # ==========================================

    cursor.execute("""
        CREATE TABLE status_empresa (

            id SERIAL PRIMARY KEY,

            nome VARCHAR(50) NOT NULL UNIQUE

        );
    """)


    status = [

        "Ativa",
        "Inativa",
        "Bloqueada",
        "Em análise"

    ]


    for item in status:

        cursor.execute("""
            INSERT INTO status_empresa (nome)
            VALUES (%s);
        """, (item,))


    # ==========================================
    # CLASSIFICAÇÕES
    # ==========================================

    cursor.execute("""
        CREATE TABLE classificacoes (

            id SERIAL PRIMARY KEY,

            nome VARCHAR(100) NOT NULL UNIQUE

        );
    """)


    classificacoes = [

        "Pequena Empresa",
        "Média Empresa",
        "Grande Empresa",
        "Multinacional",
        "Microempresa"

    ]


    for classificacao in classificacoes:

        cursor.execute("""
            INSERT INTO classificacoes (nome)
            VALUES (%s);
        """, (classificacao,))


    # ==========================================
    # EMPRESAS
    # ==========================================

    cursor.execute("""
        CREATE TABLE empresas (

            id SERIAL PRIMARY KEY,

            cnpj VARCHAR(14) NOT NULL UNIQUE,

            razao_social VARCHAR(200) NOT NULL,

            nome_fantasia VARCHAR(200),

            cod_natureza VARCHAR(20),

            cod_porte VARCHAR(10),

            capital_social NUMERIC(18, 2),

            tipo_empresa_id INTEGER NOT NULL,

            segmento_id INTEGER,

            status_id INTEGER NOT NULL,

            classificacao_id INTEGER,

            telefone VARCHAR(20),

            celular VARCHAR(20),

            email VARCHAR(150),

            site VARCHAR(200),

            observacoes TEXT,

            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


            CONSTRAINT fk_empresa_natureza

                FOREIGN KEY (cod_natureza)

                REFERENCES natureza_juridica(cod_natureza),


            CONSTRAINT fk_empresa_porte

                FOREIGN KEY (cod_porte)

                REFERENCES porte(cod_porte),


            CONSTRAINT fk_empresa_tipo

                FOREIGN KEY (tipo_empresa_id)

                REFERENCES tipos_empresa(id),


            CONSTRAINT fk_empresa_segmento

                FOREIGN KEY (segmento_id)

                REFERENCES segmentos(id),


            CONSTRAINT fk_empresa_status

                FOREIGN KEY (status_id)

                REFERENCES status_empresa(id),


            CONSTRAINT fk_empresa_classificacao

                FOREIGN KEY (classificacao_id)

                REFERENCES classificacoes(id)

        );
    """)


    # ==========================================
    # ÍNDICES
    # ==========================================

    cursor.execute("""
        CREATE INDEX idx_empresas_razao_social
        ON empresas(razao_social);
    """)


    cursor.execute("""
        CREATE INDEX idx_empresas_nome_fantasia
        ON empresas(nome_fantasia);
    """)


    cursor.execute("""
        CREATE INDEX idx_empresas_cnpj
        ON empresas(cnpj);
    """)


    # ==========================================
    # SALVAR
    # ==========================================

    conexao.commit()


   


except psycopg2.Error as erro:

    if conexao:
        conexao.rollback()

    print("")
    print("ERRO NO POSTGRESQL:")
    print(erro)


except Exception as erro:

    if conexao:
        conexao.rollback()

    print("")
    print("ERRO:")
    print(erro)


finally:

    if cursor:
        cursor.close()

    if conexao:
        conexao.close()