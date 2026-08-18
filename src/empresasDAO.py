import os
import psycopg2
from dotenv import load_dotenv


# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

load_dotenv(encoding="latin-1")


class EmpresasDAO:

    # ==========================================================
    # CONEXÃO
    # ==========================================================

    def abrirConexao(self):

        try:

            self.conexao = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )

            self.cursor = self.conexao.cursor()

            return True

        except psycopg2.Error as erro:

            print("Erro na conexão com PostgreSQL:", erro)

            return False

    # ==========================================================
    # FECHAR CONEXÃO
    # ==========================================================

    def fecharConexao(self):

        if hasattr(self, "cursor") and self.cursor:

            try:
                self.cursor.close()
            except Exception:
                pass

        if hasattr(self, "conexao") and self.conexao:

            try:
                self.conexao.close()
            except Exception:
                pass

    # ==========================================================
    # BUSCAR TODAS AS EMPRESAS
    # ==========================================================

    def buscar(self):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    e.id,
                    e.cnpj,
                    e.razao_social,
                    e.nome_fantasia,

                    e.cod_natureza,
                    nj.descricao_natureza,

                    e.cod_porte,
                    p.descricao_porte,

                    e.capital_social,

                    e.tipo_empresa_id,
                    te.nome AS tipo_empresa,

                    e.segmento_id,
                    s.nome AS segmento,

                    e.status_id,
                    se.nome AS status,

                    e.classificacao_id,
                    c.nome AS classificacao,

                    e.telefone,
                    e.celular,
                    e.email,
                    e.site,
                    e.observacoes,
                    e.data_cadastro

                FROM empresas e

                LEFT JOIN natureza_juridica nj
                    ON e.cod_natureza = nj.cod_natureza

                LEFT JOIN porte p
                    ON e.cod_porte = p.cod_porte

                LEFT JOIN tipos_empresa te
                    ON e.tipo_empresa_id = te.id

                LEFT JOIN segmentos s
                    ON e.segmento_id = s.id

                LEFT JOIN status_empresa se
                    ON e.status_id = se.id

                LEFT JOIN classificacoes c
                    ON e.classificacao_id = c.id

                ORDER BY e.razao_social
            """)

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar empresas:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR POR CNPJ
    # ==========================================================

    def buscarPorCnpj(self, cnpj):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    e.id,
                    e.cnpj,
                    e.razao_social,
                    e.nome_fantasia,

                    e.cod_natureza,
                    nj.descricao_natureza,

                    e.cod_porte,
                    p.descricao_porte,

                    e.capital_social,

                    e.tipo_empresa_id,
                    te.nome AS tipo_empresa,

                    e.segmento_id,
                    s.nome AS segmento,

                    e.status_id,
                    se.nome AS status,

                    e.classificacao_id,
                    c.nome AS classificacao,

                    e.telefone,
                    e.celular,
                    e.email,
                    e.site,
                    e.observacoes,
                    e.data_cadastro

                FROM empresas e

                LEFT JOIN natureza_juridica nj
                    ON e.cod_natureza = nj.cod_natureza

                LEFT JOIN porte p
                    ON e.cod_porte = p.cod_porte

                LEFT JOIN tipos_empresa te
                    ON e.tipo_empresa_id = te.id

                LEFT JOIN segmentos s
                    ON e.segmento_id = s.id

                LEFT JOIN status_empresa se
                    ON e.status_id = se.id

                LEFT JOIN classificacoes c
                    ON e.classificacao_id = c.id

                WHERE e.cnpj = %s
            """, (cnpj,))

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar CNPJ:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR POR NOME
    # ==========================================================

    def buscarPorNome(self, nome):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    e.id,
                    e.cnpj,
                    e.razao_social,
                    e.nome_fantasia,

                    e.cod_natureza,
                    nj.descricao_natureza,

                    e.cod_porte,
                    p.descricao_porte,

                    e.capital_social,

                    e.tipo_empresa_id,
                    te.nome AS tipo_empresa,

                    e.segmento_id,
                    s.nome AS segmento,

                    e.status_id,
                    se.nome AS status,

                    e.classificacao_id,
                    c.nome AS classificacao,

                    e.telefone,
                    e.celular,
                    e.email,
                    e.site,
                    e.observacoes,
                    e.data_cadastro

                FROM empresas e

                LEFT JOIN natureza_juridica nj
                    ON e.cod_natureza = nj.cod_natureza

                LEFT JOIN porte p
                    ON e.cod_porte = p.cod_porte

                LEFT JOIN tipos_empresa te
                    ON e.tipo_empresa_id = te.id

                LEFT JOIN segmentos s
                    ON e.segmento_id = s.id

                LEFT JOIN status_empresa se
                    ON e.status_id = se.id

                LEFT JOIN classificacoes c
                    ON e.classificacao_id = c.id

                WHERE
                    e.razao_social ILIKE %s
                    OR e.nome_fantasia ILIKE %s

                ORDER BY e.razao_social
            """, (
                f"%{nome}%",
                f"%{nome}%"
            ))

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar empresa:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR NATUREZAS JURÍDICAS
    # ==========================================================

    def buscarNaturezas(self):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    cod_natureza,
                    descricao_natureza

                FROM natureza_juridica

                ORDER BY cod_natureza
            """)

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar naturezas jurídicas:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR PORTES
    # ==========================================================

    def buscarPortes(self):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    cod_porte,
                    descricao_porte

                FROM porte

                ORDER BY cod_porte
            """)

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar portes:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR TIPOS DE EMPRESA
    # ==========================================================

    def buscarTiposEmpresa(self):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    id,
                    nome

                FROM tipos_empresa

                ORDER BY nome
            """)

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar tipos de empresa:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR SEGMENTOS
    # ==========================================================

    def buscarSegmentos(self):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    id,
                    nome

                FROM segmentos

                ORDER BY nome
            """)

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar segmentos:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR STATUS
    # ==========================================================

    def buscarStatus(self):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    id,
                    nome

                FROM status_empresa

                ORDER BY nome
            """)

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar status:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # BUSCAR CLASSIFICAÇÕES
    # ==========================================================

    def buscarClassificacoes(self):

        if not self.abrirConexao():
            return None

        try:

            self.cursor.execute("""
                SELECT
                    id,
                    nome

                FROM classificacoes

                ORDER BY nome
            """)

            return self.cursor.fetchall()

        except psycopg2.Error as erro:

            print("Erro ao buscar classificações:", erro)

            return None

        finally:

            self.fecharConexao()

    # ==========================================================
    # INSERIR EMPRESA
    # ==========================================================

    def inserir(
        self,
        cnpj,
        razao_social,
        nome_fantasia,
        natureza_juridica,
        porte,
        capital_social,
        tipo_empresa_id,
        segmento_id,
        status_id,
        classificacao_id,
        telefone,
        celular,
        email,
        site,
        observacoes
    ):

        if not self.abrirConexao():
            return False

        try:

            self.cursor.execute("""
                INSERT INTO empresas (
                    cnpj,
                    razao_social,
                    nome_fantasia,
                    cod_natureza,
                    cod_porte,
                    capital_social,
                    tipo_empresa_id,
                    segmento_id,
                    status_id,
                    classificacao_id,
                    telefone,
                    celular,
                    email,
                    site,
                    observacoes
                )

                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
            """, (
                cnpj,
                razao_social,
                nome_fantasia,
                natureza_juridica,
                porte,
                capital_social,
                tipo_empresa_id,
                segmento_id,
                status_id,
                classificacao_id,
                telefone,
                celular,
                email,
                site,
                observacoes
            ))

            self.conexao.commit()

            print("Empresa inserida com sucesso!")

            return True

        except psycopg2.Error as erro:

            self.conexao.rollback()

            print("Erro ao inserir empresa:", erro)

            return False

        finally:

            self.fecharConexao()

    # ==========================================================
    # ATUALIZAR EMPRESA
    # ==========================================================

    def atualizar(
        self,
        cnpj,
        razao_social,
        nome_fantasia,
        natureza_juridica,
        porte,
        capital_social,
        tipo_empresa_id,
        segmento_id,
        status_id,
        classificacao_id,
        telefone,
        celular,
        email,
        site,
        observacoes
    ):

        if not self.abrirConexao():
            return False

        try:

            self.cursor.execute("""
                UPDATE empresas

                SET
                    razao_social = %s,
                    nome_fantasia = %s,
                    cod_natureza = %s,
                    cod_porte = %s,
                    capital_social = %s,
                    tipo_empresa_id = %s,
                    segmento_id = %s,
                    status_id = %s,
                    classificacao_id = %s,
                    telefone = %s,
                    celular = %s,
                    email = %s,
                    site = %s,
                    observacoes = %s

                WHERE cnpj = %s
            """, (
                razao_social,
                nome_fantasia,
                natureza_juridica,
                porte,
                capital_social,
                tipo_empresa_id,
                segmento_id,
                status_id,
                classificacao_id,
                telefone,
                celular,
                email,
                site,
                observacoes,
                cnpj
            ))

            self.conexao.commit()

            print("Empresa atualizada com sucesso!")

            return True

        except psycopg2.Error as erro:

            self.conexao.rollback()

            print("Erro ao atualizar empresa:", erro)

            return False

        finally:

            self.fecharConexao()

    # ==========================================================
    # DELETAR EMPRESA
    # ==========================================================

    def deletar(self, cnpj):

        if not self.abrirConexao():
            return False

        try:

            self.cursor.execute("""
                DELETE FROM empresas
                WHERE cnpj = %s
            """, (cnpj,))

            empresa_excluida = self.cursor.rowcount > 0

            self.conexao.commit()

            if empresa_excluida:
                print("Empresa deletada com sucesso!")
            else:
                print("Empresa não encontrada.")

            return empresa_excluida

        except psycopg2.Error as erro:

            self.conexao.rollback()

            print("Erro ao deletar empresa:", erro)

            return False

        finally:

            self.fecharConexao()

    # ==========================================================
    # INSERIR SEGMENTO
    # ==========================================================

    def inserirSegmento(self, nome):

        if not self.abrirConexao():
            return False

        try:

            self.cursor.execute("""
                INSERT INTO segmentos (nome)
                VALUES (%s)

                ON CONFLICT (nome)
                DO NOTHING
            """, (nome,))

            self.conexao.commit()

            return True

        except psycopg2.Error as erro:

            self.conexao.rollback()

            print("Erro ao inserir segmento:", erro)

            return False

        finally:

            self.fecharConexao()