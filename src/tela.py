import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb


class MinhaTela:

    def __init__(
        self,
        janela,
        EmpresasEmpresasDAO,
      
    ):

        self.EmpresasDAO = EmpresasEmpresasDAO
        

        self.janela = janela

       # ==========================================================
        # JANELA PRINCIPAL
        # ==========================================================

        janela.title("Sistema de Gestão de Empresas")

        janela.geometry("1200x700")

        janela.minsize(1000, 600)

        janela.configure(
            bg="#f2f4f7"
        )

     # ==========================================================
        # ESTILO
        # ==========================================================

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "Treeview",
            rowheight=30,
            font=("Segoe UI", 9)
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Segoe UI", 9, "bold")
        )

        estilo.configure(
            "TCombobox",
            padding=5
        )

            # ==========================================================
        # CABEÇALHO
        # ==========================================================

        cabecalho = tk.Frame(
            janela,
            bg="#1f4e78",
            height=50
        )

        cabecalho.pack(
            fill=tk.X
        )

        cabecalho.pack_propagate(False)

        titulo = tk.Label(
            cabecalho,
            text="Sistema de Gestão de Empresas",
            bg="#1f4e78",
            fg="white",
            font=("Segoe UI", 14, "bold")
        )

        titulo.pack(
            side=tk.LEFT,
            padx=20,
            pady=10
        )

        # =======

        # ==========================================================
        # ÁREA PRINCIPAL
        # ==========================================================

        container = tk.Frame(
            janela,
            bg="#f2f4f7"
        )

        container.pack(
            fill=tk.X,
            padx=15,
            pady=5
        )

        # ==========================================================
        # DADOS DA EMPRESA
        # ==========================================================

        dados_empresa = tk.LabelFrame(
            container,
            text=" Dados da Empresa ",
            bg="#f2f4f7",
            fg="#1f4e78",
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=5
        )

        dados_empresa.pack(
            fill=tk.X
        )

        dados_empresa.columnconfigure(1, weight=1)
        dados_empresa.columnconfigure(3, weight=1)

        # ==========================================================
        # CNPJ
        # ==========================================================

        tk.Label(
            dados_empresa,
            text="CNPJ:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.etycnpj = ttk.Entry(
            dados_empresa
        )

        self.etycnpj.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # RAZÃO SOCIAL
        # ==========================================================

        tk.Label(
            dados_empresa,
            text="Razão Social:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=3
        )

        self.etyrazao_social = ttk.Entry(
            dados_empresa
        )

        self.etyrazao_social.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # NOME FANTASIA
        # ==========================================================

        tk.Label(
            dados_empresa,
            text="Nome Fantasia:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=2,
            pady=2
        )

        self.etynome_fantasia = ttk.Entry(
            dados_empresa
        )

        self.etynome_fantasia.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # NATUREZA JURÍDICA
        # ==========================================================

        tk.Label(
            dados_empresa,
            text="Natureza Jurídica:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=3
        )

        self.combobox_natureza = ttk.Combobox(
            dados_empresa,
            state="readonly"
        )

        self.combobox_natureza.grid(
            row=1,
            column=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # PORTE
        # ==========================================================

        tk.Label(
            dados_empresa,
            text="Porte:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=3
        )

        self.combobox_porte = ttk.Combobox(
            dados_empresa,
            state="readonly"
        )

        self.combobox_porte.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # CAPITAL SOCIAL
        # ==========================================================

        tk.Label(
            dados_empresa,
            text="Capital Social:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=2,
            column=2,
            sticky="w",
            padx=5,
            pady=3
        )

        self.etycapital_social = ttk.Entry(
            dados_empresa
        )

        self.etycapital_social.grid(
            row=2,
            column=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # QUALIFICAÇÃO COMERCIAL
        # ==========================================================

        qualificacao = tk.LabelFrame(
            container,
            text=" Qualificação Comercial ",
            bg="#f2f4f7",
            fg="#1f4e78",
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=3
        )

        qualificacao.pack(
            fill=tk.X,
            pady=(10, 0)
        )

        qualificacao.columnconfigure(1, weight=1)
        qualificacao.columnconfigure(3, weight=1)

        # ==========================================================
        # TIPO DE EMPRESA
        # ==========================================================

        tk.Label(
            qualificacao,
            text="Tipo:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=3
        )

        self.combobox_tipo = ttk.Combobox(
            qualificacao,
            state="readonly"
        )

        self.combobox_tipo.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # SEGMENTO
        # ==========================================================

        tk.Label(
            qualificacao,
            text="Segmento:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=3
        )

        self.combobox_segmento = ttk.Combobox(
            qualificacao,
            state="readonly"
        )

        self.combobox_segmento.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # STATUS
        # ==========================================================

        tk.Label(
            qualificacao,
            text="Status:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=3
        )

        self.combobox_status = ttk.Combobox(
            qualificacao,
            state="readonly"
        )

        self.combobox_status.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # CLASSIFICAÇÃO
        # ==========================================================

        tk.Label(
            qualificacao,
            text="Classificação:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=3
        )

        self.combobox_classificacao = ttk.Combobox(
            qualificacao,
            state="readonly"
        )

        self.combobox_classificacao.grid(
            row=1,
            column=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # CONTATO
        # ==========================================================

        contato = tk.LabelFrame(
            container,
            text=" Informações de Contato ",
            bg="#f2f4f7",
            fg="#1f4e78",
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=5
        )

        contato.pack(
            fill=tk.X,
            pady=(10, 0)
        )

        contato.columnconfigure(1, weight=1)
        contato.columnconfigure(3, weight=1)

        # ==========================================================
        # TELEFONE
        # ==========================================================

        tk.Label(
            contato,
            text="Telefone:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=3
        )

        self.etytelefone = ttk.Entry(
            contato
        )

        self.etytelefone.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # CELULAR
        # ==========================================================

        tk.Label(
            contato,
            text="Celular:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=3
        )

        self.etycelular = ttk.Entry(
            contato
        )

        self.etycelular.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # E-MAIL
        # ==========================================================

        tk.Label(
            contato,
            text="E-mail:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=3
        )

        self.etyemail = ttk.Entry(
            contato
        )

        self.etyemail.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # SITE
        # ==========================================================

        tk.Label(
            contato,
            text="Site:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=3
        )

        self.etysite = ttk.Entry(
            contato
        )

        self.etysite.grid(
            row=1,
            column=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # OBSERVAÇÕES
        # ==========================================================

        tk.Label(
            contato,
            text="Observações:",
            bg="#f2f4f7",
            font=("Segoe UI", 9, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="nw",
            padx=5,
            pady=3
        )

        self.txtobservacoes = tk.Text(
            contato,
            height=3,
            font=("Segoe UI", 9),
            relief=tk.SOLID,
            borderwidth=1
        )

        self.txtobservacoes.grid(
            row=2,
            column=1,
            columnspan=3,
            sticky="ew",
            padx=5,
            pady=3
        )

        # ==========================================================
        # BOTÕES
        # ==========================================================

        botoes = tk.Frame(
            janela,
            bg="#f2f4f7"
        )

        botoes.pack(
            fill=tk.X,
            padx=15,
            pady=5
        )

        self.btnInserir = tk.Button(
            botoes,
            text="＋ Novo / Salvar",
            command=self.inserir,
            bg="#198754",
            fg="white",
            activebackground="#157347",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=7,
            cursor="hand2"
        )

        self.btnInserir.pack(
            side=tk.LEFT,
            padx=4
        )

        self.btnAtualizar = tk.Button(
            botoes,
            text="↻ Atualizar",
            command=self.atualizar,
            bg="#0d6efd",
            fg="white",
            activebackground="#0b5ed7",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=7,
            cursor="hand2"
        )

        self.btnAtualizar.pack(
            side=tk.LEFT,
            padx=4
        )

        self.btnDeletar = tk.Button(
            botoes,
            text="✕ Excluir",
            command=self.deletar,
            bg="#dc3545",
            fg="white",
            activebackground="#bb2d3b",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=7,
            cursor="hand2"
        )

        self.btnDeletar.pack(
            side=tk.LEFT,
            padx=4
        )

        self.btnBuscar = tk.Button(
            botoes,
            text="🔎 Buscar",
            command=self.buscar,
            bg="#6c757d",
            fg="white",
            activebackground="#5c636a",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=7,
            cursor="hand2"
        )

        self.btnBuscar.pack(
            side=tk.LEFT,
            padx=4
        )

        self.btnLimpar = tk.Button(
            botoes,
            text="Limpar",
            command=self.limparCampos,
            bg="#495057",
            fg="white",
            activebackground="#343a40",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=7,
            cursor="hand2"
        )

        self.btnLimpar.pack(
            side=tk.LEFT,
            padx=4
        )

        # ==========================================================
        # TABELA
        # ==========================================================

        tabela_frame = tk.LabelFrame(
            janela,
            text=" Empresas Cadastradas ",
            bg="#f2f4f7",
            fg="#1f4e78",
            font=("Segoe UI", 10, "bold")
        )

        tabela_frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=15,
            pady=10
        )

        columns = (
            "id",
            "cnpj",
            "razao_social",
            "nome_fantasia",
            "natureza",
            "porte",
            "capital",
            "tipo",
            "segmento",
            "status",
            "classificacao",
            "telefone",
            "email"
        )

        self.tree = ttk.Treeview(
            tabela_frame,
            columns=columns,
            show="headings"
        )

        # ==========================================================
        # COLUNAS
        # ==========================================================

        larguras = {
            "id": 50,
            "cnpj": 120,
            "razao_social": 220,
            "nome_fantasia": 180,
            "natureza": 180,
            "porte": 150,
            "capital": 120,
            "tipo": 150,
            "segmento": 150,
            "status": 100,
            "classificacao": 100,
            "telefone": 120,
            "email": 200
        }

        for coluna, largura in larguras.items():

            self.tree.column(
                coluna,
                width=largura,
                minwidth=70
            )

        # ==========================================================
        # CABEÇALHOS
        # ==========================================================

        cabecalhos = {
            "id": "ID",
            "cnpj": "CNPJ",
            "razao_social": "Razão Social",
            "nome_fantasia": "Nome Fantasia",
            "natureza": "Natureza Jurídica",
            "porte": "Porte",
            "capital": "Capital Social",
            "tipo": "Tipo",
            "segmento": "Segmento",
            "status": "Status",
            "classificacao": "Classificação",
            "telefone": "Telefone",
            "email": "E-mail"
        }

        for coluna, titulo_coluna in cabecalhos.items():

            self.tree.heading(
                coluna,
                text=titulo_coluna
            )

        # ==========================================================
        # SCROLLBAR VERTICAL
        # ==========================================================

        scrollbar_vertical = ttk.Scrollbar(
            tabela_frame,
            orient=tk.VERTICAL,
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar_vertical.set
        )

        scrollbar_vertical.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        # ==========================================================
        # SCROLLBAR HORIZONTAL
        # ==========================================================

        scrollbar_horizontal = ttk.Scrollbar(
            tabela_frame,
            orient=tk.HORIZONTAL,
            command=self.tree.xview
        )

        self.tree.configure(
            xscrollcommand=scrollbar_horizontal.set
        )

        scrollbar_horizontal.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.tree.pack(
            fill=tk.BOTH,
            expand=True
        )

        # ==========================================================
        # DUPLO CLIQUE
        # ==========================================================

        self.tree.bind(
            "<Double-1>",
            self.selecionarLinha
        )

        # ==========================================================
        # CARREGAR COMBOS
        # ==========================================================

        self.carregarComboboxes()

        # ==========================================================
        # CARREGAR EMPRESAS
        # ==========================================================

        self.atualizarTabela(
            self.EmpresasDAO.buscar()
        )


    # ==============================================================
    # CARREGAR COMBOBOXES
    # ==============================================================

    def carregarComboboxes(self):

        try:

            # ------------------------------------------
            # NATUREZA JURÍDICA
            # ------------------------------------------

            naturezas = self.EmpresasDAO.buscarNaturezas()

            self.naturezas = {}

            valores_natureza = []

            for codigo, descricao in naturezas or []:

                texto = f"{codigo} - {descricao}"

                valores_natureza.append(texto)

                self.naturezas[texto] = codigo

            self.combobox_natureza["values"] = valores_natureza

            # ------------------------------------------
            # PORTE
            # ------------------------------------------

            portes = self.EmpresasDAO.buscarPortes()

            self.portes = {}

            valores_porte = []

            for codigo, descricao in portes or []:

                texto = f"{codigo} - {descricao}"

                valores_porte.append(texto)

                self.portes[texto] = codigo

            self.combobox_porte["values"] = valores_porte

            # ------------------------------------------
            # TIPO
            # ------------------------------------------

            tipos = self.EmpresasDAO.buscarTiposEmpresa()

            self.tipos = {}

            valores_tipo = []

            for codigo, nome in tipos or []:

                valores_tipo.append(nome)

                self.tipos[nome] = codigo

            self.combobox_tipo["values"] = valores_tipo

            # ------------------------------------------
            # SEGMENTO
            # ------------------------------------------

            segmentos = self.EmpresasDAO.buscarSegmentos()

            self.segmentos = {}

            valores_segmento = []

            for codigo, nome in segmentos or []:

                valores_segmento.append(nome)

                self.segmentos[nome] = codigo

            self.combobox_segmento["values"] = valores_segmento

            # ------------------------------------------
            # STATUS
            # ------------------------------------------

            status = self.EmpresasDAO.buscarStatus()

            self.status = {}

            valores_status = []

            for codigo, nome in status or []:

                valores_status.append(nome)

                self.status[nome] = codigo

            self.combobox_status["values"] = valores_status

            # ------------------------------------------
            # CLASSIFICAÇÃO
            # ------------------------------------------

            classificacoes = (
                self.EmpresasDAO.buscarClassificacoes()
            )

            self.classificacoes = {}

            valores_classificacao = []

            for codigo, nome in classificacoes or []:

                valores_classificacao.append(nome)

                self.classificacoes[nome] = codigo

            self.combobox_classificacao["values"] = (
                valores_classificacao
            )

        except Exception as erro:

            print(
                "Erro ao carregar comboboxes:",
                erro
            )


    # ==============================================================
    # ATUALIZAR TABELA
    # ==============================================================

    def atualizarTabela(self, registros):

        for item in self.tree.get_children():

            self.tree.delete(item)

        if not registros:

            return

        for registro in registros:

            valores = (
                registro[0],   # ID
                registro[1],   # CNPJ
                registro[2],   # Razão Social
                registro[3],   # Nome Fantasia
                registro[5],   # Natureza
                registro[7],   # Porte
                registro[8],   # Capital
                registro[10],  # Tipo
                registro[12],  # Segmento
                registro[14],  # Status
                registro[16],  # Classificação
                registro[17],  # Telefone
                registro[19]   # E-mail
            )

            self.tree.insert(
                "",
                tk.END,
                values=valores
            )


    # ==============================================================
    # SELECIONAR EMPRESA
    # ==============================================================

    def selecionarLinha(self, event=None):

        selecao = self.tree.selection()

        if not selecao:

            return

        item = self.tree.item(
            selecao[0]
        )

        valores = item["values"]

        if not valores:

            return

        # CNPJ
        self.etycnpj.delete(0, tk.END)
        self.etycnpj.insert(0, valores[1])

        # Razão Social
        self.etyrazao_social.delete(0, tk.END)
        self.etyrazao_social.insert(0, valores[2])

        # Nome Fantasia
        self.etynome_fantasia.delete(0, tk.END)
        self.etynome_fantasia.insert(0, valores[3])

        # Natureza
        natureza = valores[4]

        for texto, codigo in self.naturezas.items():

            if str(codigo) == str(natureza):

                self.combobox_natureza.set(texto)

                break

        # Porte
        porte = valores[5]

        for texto, codigo in self.portes.items():

            if str(codigo) == str(porte):

                self.combobox_porte.set(texto)

                break

        # Capital
        self.etycapital_social.delete(0, tk.END)
        self.etycapital_social.insert(0, valores[6])

        # Tipo
        self.combobox_tipo.set(
            valores[7]
        )

        # Segmento
        self.combobox_segmento.set(
            valores[8]
        )

        # Status
        self.combobox_status.set(
            valores[9]
        )

        # Classificação
        self.combobox_classificacao.set(
            valores[10]
        )

        # Telefone
        self.etytelefone.delete(0, tk.END)
        self.etytelefone.insert(0, valores[11])

        # E-mail
        self.etyemail.delete(0, tk.END)
        self.etyemail.insert(0, valores[12])


    # ==============================================================
    # PEGAR ID DO COMBO
    # ==============================================================

    def obterIdCombo(
        self,
        dicionario,
        valor
    ):

        return dicionario.get(valor)


    # ==============================================================
    # INSERIR
    # ==============================================================

    def inserir(self, event=None):

        cnpj = self.etycnpj.get().strip()

        razao_social = (
            self.etyrazao_social.get().strip()
        )

        nome_fantasia = (
            self.etynome_fantasia.get().strip()
        )

        if not cnpj or not razao_social:

            mb.showwarning(
                "Atenção",
                "Informe o CNPJ e a Razão Social."
            )

            return

        try:

            cod_natureza = self.naturezas.get(
                self.combobox_natureza.get()
            )

            cod_porte = self.portes.get(
                self.combobox_porte.get()
            )

            tipo_id = self.tipos.get(
                self.combobox_tipo.get()
            )

            segmento_id = self.segmentos.get(
                self.combobox_segmento.get()
            )

            status_id = self.status.get(
                self.combobox_status.get()
            )

            classificacao_id = (
                self.classificacoes.get(
                    self.combobox_classificacao.get()
                )
            )

            capital_social = (
                self.etycapital_social.get()
                .strip()
            )

            if not capital_social:

                capital_social = None

            self.EmpresasDAO.inserir(

                cnpj,
                razao_social,
                nome_fantasia,

                cod_natureza,
                cod_porte,
                capital_social,

                tipo_id,
                segmento_id,
                status_id,
                classificacao_id,

                self.etytelefone.get().strip(),
                self.etycelular.get().strip(),
                self.etyemail.get().strip(),
                self.etysite.get().strip(),
                self.txtobservacoes.get(
                    "1.0",
                    tk.END
                ).strip()
            )

            mb.showinfo(
                "Sucesso",
                "Empresa cadastrada com sucesso!"
            )

            self.atualizarTabela(
                self.EmpresasDAO.buscar()
            )

            self.limparCampos()

        except Exception as erro:

            mb.showerror(
                "Erro",
                f"Não foi possível cadastrar a empresa.\n\n{erro}"
            )


    # ==============================================================
    # ATUALIZAR
    # ==============================================================

    def atualizar(self, event=None):

        cnpj = self.etycnpj.get().strip()

        razao_social = (
            self.etyrazao_social.get().strip()
        )

        if not cnpj or not razao_social:

            mb.showwarning(
                "Atenção",
                "Informe o CNPJ e a Razão Social."
            )

            return

        try:

            cod_natureza = self.naturezas.get(
                self.combobox_natureza.get()
            )

            cod_porte = self.portes.get(
                self.combobox_porte.get()
            )

            tipo_id = self.tipos.get(
                self.combobox_tipo.get()
            )

            segmento_id = self.segmentos.get(
                self.combobox_segmento.get()
            )

            status_id = self.status.get(
                self.combobox_status.get()
            )

            classificacao_id = (
                self.classificacoes.get(
                    self.combobox_classificacao.get()
                )
            )

            capital_social = (
                self.etycapital_social.get()
                .strip()
            )

            if not capital_social:

                capital_social = None

            self.EmpresasDAO.atualizar(

                cnpj,
                razao_social,
                self.etynome_fantasia.get().strip(),

                cod_natureza,
                cod_porte,
                capital_social,

                tipo_id,
                segmento_id,
                status_id,
                classificacao_id,

                self.etytelefone.get().strip(),
                self.etycelular.get().strip(),
                self.etyemail.get().strip(),
                self.etysite.get().strip(),
                self.txtobservacoes.get(
                    "1.0",
                    tk.END
                ).strip()
            )

            mb.showinfo(
                "Sucesso",
                "Empresa atualizada com sucesso!"
            )

            self.atualizarTabela(
                self.EmpresasDAO.buscar()
            )

        except Exception as erro:

            mb.showerror(
                "Erro",
                f"Não foi possível atualizar a empresa.\n\n{erro}"
            )


    # ==============================================================
    # DELETAR
    # ==============================================================

    def deletar(self, event=None):

        cnpj = self.etycnpj.get().strip()

        if not cnpj:

            mb.showwarning(
                "Atenção",
                "Informe o CNPJ da empresa que deseja excluir."
            )

            return

        confirmar = mb.askyesno(
            "Confirmar exclusão",
            f"Deseja realmente excluir a empresa?\n\n"
            f"CNPJ: {cnpj}"
        )

        if not confirmar:

            return

        try:

            resultado = self.EmpresasDAO.deletar(
                cnpj
            )

            if resultado:

                mb.showinfo(
                    "Sucesso",
                    "Empresa excluída com sucesso!"
                )

                self.atualizarTabela(
                    self.EmpresasDAO.buscar()
                )

                self.limparCampos()

            else:

                mb.showwarning(
                    "Atenção",
                    "A empresa não foi encontrada."
                )

        except Exception as erro:

            mb.showerror(
                "Erro",
                f"Não foi possível excluir a empresa.\n\n{erro}"
            )


    # ==============================================================
    # BUSCAR
    # ==============================================================

    def buscar(self, event=None):

        cnpj = self.etycnpj.get().strip()

        razao_social = (
            self.etyrazao_social.get().strip()
        )

        try:

            if cnpj:

                registros = (
                    self.EmpresasDAO.buscarPorCnpj(
                        cnpj
                    )
                )

            elif razao_social:

                registros = (
                    self.EmpresasDAO.buscarPorNome(
                        razao_social
                    )
                )

            else:

                registros = (
                    self.EmpresasDAO.buscar()
                )

            if registros:

                self.atualizarTabela(
                    registros
                )

            else:

                self.atualizarTabela([])

                mb.showinfo(
                    "Pesquisa",
                    "Nenhuma empresa encontrada."
                )

        except Exception as erro:

            mb.showerror(
                "Erro",
                f"Erro ao realizar pesquisa.\n\n{erro}"
            )


    # ==============================================================
    # LIMPAR CAMPOS
    # ==============================================================

    def limparCampos(self):

        self.etycnpj.delete(
            0,
            tk.END
        )

        self.etyrazao_social.delete(
            0,
            tk.END
        )

        self.etynome_fantasia.delete(
            0,
            tk.END
        )

        self.combobox_natureza.set("")

        self.combobox_porte.set("")

        self.etycapital_social.delete(
            0,
            tk.END
        )

        self.combobox_tipo.set("")

        self.combobox_segmento.set("")

        self.combobox_status.set("")

        self.combobox_classificacao.set("")

        self.etytelefone.delete(
            0,
            tk.END
        )

        self.etycelular.delete(
            0,
            tk.END
        )

        self.etyemail.delete(
            0,
            tk.END
        )

        self.etysite.delete(
            0,
            tk.END
        )

        self.txtobservacoes.delete(
            "1.0",
            tk.END
        )