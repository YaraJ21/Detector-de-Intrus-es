import tkinter as tk
from tkinter import ttk
from datetime import datetime

# ============================================================

# CONFIGURAÇÃO DOS NÓS SIMULADOS

# ============================================================

nos = {
"NODE 01": {
"ip": "192.168.1.10",
"estado": "ACTIVO"
},
"NODE 02": {
"ip": "192.168.1.11",
"estado": "ACTIVO"
},
"NODE 03": {
"ip": "192.168.1.12",
"estado": "ACTIVO"
}
}

# ============================================================

# VARIÁVEIS DO SISTEMA

# ============================================================

monitorizacao_ativa = False
total_alertas = 0
total_pacotes = 0

# ============================================================

# CORES

# ============================================================

BG_PRINCIPAL = "#0f172a"
BG_CARD = "#1e293b"
BG_CARD_2 = "#172033"

CYAN = "#00ffff"
BRANCO = "#ffffff"
VERDE = "#00ff66"
VERMELHO = "#ff3333"
LARANJA = "#ff9800"
AMARELO = "#ffff00"
CINZENTO = "#94a3b8"

# ============================================================

# ACTUALIZAR NÓS

# ============================================================

def actualizar_nos():


    for widget in frame_nos.winfo_children():
        widget.destroy()

    for nome, dados in nos.items():

        estado = dados["estado"]

        if estado == "ACTIVO":
            simbolo = "🟢"
            cor = VERDE

        elif estado == "SOB ATAQUE":
            simbolo = "🟠"
            cor = LARANJA

        else:
            simbolo = "🔴"
            cor = VERMELHO

        card = tk.Frame(
            frame_nos,
            bg=BG_CARD_2,
            bd=2,
            relief="ridge"
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=6,
            pady=5
        )

        tk.Label(
            card,
            text=nome,
            font=("Arial", 13, "bold"),
            bg=BG_CARD_2,
            fg=CYAN
        ).pack(pady=(10, 5))

        tk.Label(
            card,
            text=dados["ip"],
            font=("Consolas", 10),
            bg=BG_CARD_2,
            fg=BRANCO
        ).pack()

        tk.Label(
            card,
            text=f"{simbolo} {estado}",
            font=("Arial", 11, "bold"),
            bg=BG_CARD_2,
            fg=cor
        ).pack(pady=10)


# ============================================================

# ACTUALIZAR ESTADO DO NÓ

# ============================================================

def actualizar_estado_no(nome_no, estado):


    if nome_no in nos:
        nos[nome_no]["estado"] = estado

    actualizar_nos()
    actualizar_contador_nos()


# ============================================================

# ACTUALIZAR CONTADOR DE NÓS

# ============================================================

def actualizar_contador_nos():

    nos_ativos = 0

    for dados in nos.values():

        if dados["estado"] == "ACTIVO":
            nos_ativos += 1

    nos_label.config(
        text=f"NÓS ACTIVOS: {nos_ativos}"
    )


# ============================================================

# MOSTRAR ALERTA

# ============================================================

def mostrar_alerta(resultado):
    tipo = resultado["tipo_ataque"]
    origem = resultado["ip_origem"]
    destino = resultado["ip_destino"]
    no_afectado = resultado["no_afectado"]
    confianca = resultado["confianca"]

    if resultado["classificacao"] == "MALICIOSO":

        alerta_titulo.config(
            text="⚠ ATAQUE DETECTADO",
            fg=VERMELHO
        )

    alerta_tipo.config(
        text=f"Tipo: {tipo}"
    )

    alerta_origem.config(
        text=f"Origem: {origem}"
    )

    alerta_destino.config(
        text=f"Destino: {destino}"
    )

    alerta_no.config(
        text=f"Nó afectado: {no_afectado}"
    )

    alerta_classificacao.config(
        text="Classificação: MALICIOSO",
        fg=VERMELHO
    )

    alerta_confianca.config(
        text=f"Confiança: {confianca * 100:.0f}%"
    )

    actualizar_estado_no(
        no_afectado,
        "SOB ATAQUE"
    )


    # ============================================================

    # INICIAR MONITORIZAÇÃO

    # ============================================================

def iniciar_monitorizacao():


    global monitorizacao_ativa

    monitorizacao_ativa = True

    status_sistema.config(
        text="🟢 SISTEMA ONLINE",
        fg=VERDE
    )

    status_operacao.config(
        text="🟢 MONITORIZAÇÃO ACTIVA",
        fg=VERDE
    )


# ============================================================

# PARAR MONITORIZAÇÃO

# ============================================================

def parar_monitorizacao():


    global monitorizacao_ativa

    monitorizacao_ativa = False

    status_operacao.config(
        text="🔴 MONITORIZAÇÃO PARADA",
        fg=VERMELHO
    )


    # ============================================================

    # LIMPAR ALERTAS

    # ============================================================

def limpar_resultados():


    global total_alertas
    global total_pacotes


    total_alertas = 0
    total_pacotes = 0

    for nome in nos:
        nos[nome]["estado"] = "ACTIVO"

    alertas_label.config(
        text="AMEAÇAS: 0"
    )

    pacotes_label.config(
        text="PACOTES: 0"
    )

    nos_label.config(
        text="NÓS ACTIVOS: 3"
    )

    alerta_titulo.config(
        text="AGUARDANDO DETECÇÃO",
        fg=CYAN
    )

    alerta_tipo.config(
        text="Tipo: -"
    )

    alerta_origem.config(
        text="Origem: -"
    )

    alerta_destino.config(
        text="Destino: -"
    )

    alerta_no.config(
        text="Nó afectado: -"
    )

    alerta_classificacao.config(
        text="Classificação: -",
        fg=BRANCO
    )

    alerta_confianca.config(
        text="Confiança: -"
    )

    historico.delete(
        "1.0",
        tk.END
    )

    if monitorizacao_ativa:

        status_operacao.config(
            text="🟢 MONITORIZAÇÃO ACTIVA",
            fg=VERDE
        )

    else:

        status_operacao.config(
            text="🔴 MONITORIZAÇÃO PARADA",
            fg=VERMELHO
        )

    actualizar_nos()


# ============================================================

# CRIAR JANELA

# ============================================================

def iniciar_sistema():


    global janela
    global frame_nos
    global status_sistema
    global status_operacao
    global alertas_label
    global pacotes_label
    global nos_label
    global alerta_titulo
    global alerta_tipo
    global alerta_origem
    global alerta_destino
    global alerta_no
    global alerta_classificacao
    global alerta_confianca
    global historico
    global ataque_var
    global no_var

    janela = tk.Tk()

    janela.title(
        "CyberShield AI - IDS"
    )

    janela.geometry(
        "1100x950"
    )

    janela.configure(
        bg=BG_PRINCIPAL
    )

    # ========================================================
    # CABEÇALHO
    # ========================================================

    titulo = tk.Label(
        janela,
        text="CYBERSHIELD AI",
        font=("Times New Roman", 25, "bold"),
        bg=BG_PRINCIPAL,
        fg=CYAN
    )

    titulo.pack(
        pady=(12, 2)
    )

    subtitulo = tk.Label(
        janela,
        text="SISTEMA DE DETECÇÃO DE INTRUSÕES",
        font=("Times New Roman", 10),
        bg=BG_PRINCIPAL,
        fg=CINZENTO
    )

    subtitulo.pack(
        pady=(0, 10)
    )

    # ========================================================
    # STATUS
    # ========================================================

    frame_status = tk.Frame(
        janela,
        bg=BG_PRINCIPAL
    )

    frame_status.pack(
        fill="x",
        padx=20
    )

    status_sistema = tk.Label(
        frame_status,
        text="🟢 SISTEMA ONLINE",
        font=("Times New Roman", 11, "bold"),
        bg=BG_CARD,
        fg=VERDE,
        bd=2,
        relief="ridge",
        padx=15,
        pady=10
    )

    status_sistema.pack(
        side="left",
        expand=True,
        fill="x",
        padx=4
    )

    status_operacao = tk.Label(
        frame_status,
        text="🔴 MONITORIZAÇÃO PARADA",
        font=("Times New Roman", 11, "bold"),
        bg=BG_CARD,
        fg=VERMELHO,
        bd=2,
        relief="ridge",
        padx=15,
        pady=10
    )

    status_operacao.pack(
        side="left",
        expand=True,
        fill="x",
        padx=4
    )

    nos_label = tk.Label(
        frame_status,
        text="NÓS ACTIVOS: 3",
        font=("Times New Roman", 11, "bold"),
        bg=BG_CARD,
        fg=CYAN,
        bd=2,
        relief="ridge",
        padx=15,
        pady=10
    )

    nos_label.pack(
        side="left",
        expand=True,
        fill="x",
        padx=4
    )

    alertas_label = tk.Label(
        frame_status,
        text="AMEAÇAS: 0",
        font=("Times New Roman", 11, "bold"),
        bg=BG_CARD,
        fg=VERMELHO,
        bd=2,
        relief="ridge",
        padx=15,
        pady=10
    )

    alertas_label.pack(
        side="left",
        expand=True,
        fill="x",
        padx=4
    )

    pacotes_label = tk.Label(
        frame_status,
        text="PACOTES: 0",
        font=("Times New Roman", 11, "bold"),
        bg=BG_CARD,
        fg=BRANCO,
        bd=2,
        relief="ridge",
        padx=15,
        pady=10
    )

    pacotes_label.pack(
        side="left",
        expand=True,
        fill="x",
        padx=4
    )

    # ========================================================
    # NÓS DA REDE
    # ========================================================

    tk.Label(
        janela,
        text="NÓS DA REDE",
        font=("Times New Roman", 14, "bold"),
        bg=BG_PRINCIPAL,
        fg=CYAN
    ).pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )

    frame_nos = tk.Frame(
        janela,
        bg=BG_PRINCIPAL
    )

    frame_nos.pack(
        fill="x",
        padx=20
    )

    actualizar_nos()

    # ========================================================
    # ALERTA
    # ========================================================

    frame_alerta = tk.Frame(
        janela,
        bg=BG_CARD,
        bd=2,
        relief="ridge"
    )

    frame_alerta.pack(
        fill="x",
        padx=20,
        pady=15
    )

    tk.Label(
        frame_alerta,
        text="ALERTA DE SEGURANÇA",
        font=("Times New Roman", 13, "bold"),
        bg=BG_CARD,
        fg=CYAN
    ).pack(
        anchor="w",
        padx=15,
        pady=(10, 5)
    )

    alerta_titulo = tk.Label(
        frame_alerta,
        text="AGUARDANDO DETECÇÃO",
        font=("Times New Roman", 13, "bold"),
        bg=BG_CARD,
        fg=CYAN
    )

    alerta_titulo.pack(
        anchor="w",
        padx=15,
        pady=5
    )

    alerta_tipo = tk.Label(
        frame_alerta,
        text="Tipo: -",
        font=("Times New Roman", 10),
        bg=BG_CARD,
        fg=BRANCO
    )

    alerta_tipo.pack(
        anchor="w",
        padx=15
    )

    alerta_origem = tk.Label(
        frame_alerta,
        text="Origem: -",
        font=("Times New Roman", 10),
        bg=BG_CARD,
        fg=BRANCO
    )

    alerta_origem.pack(
        anchor="w",
        padx=15
    )

    alerta_destino = tk.Label(
        frame_alerta,
        text="Destino: -",
        font=("Times New Roman", 10),
        bg=BG_CARD,
        fg=BRANCO
    )

    alerta_destino.pack(
        anchor="w",
        padx=15
    )

    alerta_no = tk.Label(
        frame_alerta,
        text="Nó afectado: -",
        font=("Times New Roman", 10),
        bg=BG_CARD,
        fg=BRANCO
    )

    alerta_no.pack(
        anchor="w",
        padx=15
    )

    alerta_classificacao = tk.Label(
        frame_alerta,
        text="Classificação: -",
        font=("Times New Roman", 10, "bold"),
        bg=BG_CARD,
        fg=BRANCO
    )

    alerta_classificacao.pack(
        anchor="w",
        padx=15
    )

    alerta_confianca = tk.Label(
        frame_alerta,
        text="Confiança: -",
        font=("Times New Roman", 10),
        bg=BG_CARD,
        fg=BRANCO
    )

    alerta_confianca.pack(
        anchor="w",
        padx=15,
        pady=(0, 10)
    )

    # ========================================================
    # PARTE INFERIOR
    # ========================================================

    frame_inferior = tk.Frame(
        janela,
        bg=BG_PRINCIPAL
    )

    frame_inferior.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 10)
    )

    # ========================================================
    # HISTÓRICO
    # ========================================================

    frame_historico = tk.Frame(
        frame_inferior,
        bg=BG_CARD,
        bd=2,
        relief="ridge"
    )

    frame_historico.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 5)
    )

    tk.Label(
        frame_historico,
        text="HISTÓRICO DE ALERTAS",
        font=("Times New Roman", 12, "bold"),
        bg=BG_CARD,
        fg=CYAN
    ).pack(
        anchor="w",
        padx=10,
        pady=8
    )

    historico = tk.Text(
        frame_historico,
        bg="#000000",
        fg=VERDE,
        font=("Consolas", 9),
        height=8,
        relief="flat"
    )

    historico.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=(0, 10)
    )

    # ========================================================
    # CONTROLO DA SIMULAÇÃO
    # ========================================================

    frame_controlos = tk.Frame(
        frame_inferior,
        bg=BG_CARD,
        bd=2,
        relief="ridge",
        width=500
    )

    frame_controlos.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(5, 0)
    )
    frame_controlos.pack_propagate(False)

    tk.Label(
        frame_controlos,
        text="CONTROLO DA SIMULAÇÃO",
        font=("Times New Roman", 12, "bold"),
        bg=BG_CARD,
        fg=CYAN
    ).pack(
        pady=(8, 5)
    )

    # ========================================================
    # SELECÇÃO
    # ========================================================
    

    frame_seleccao = tk.Frame(
        frame_controlos,
        bg=BG_CARD
    )

    frame_seleccao.pack(
        fill="x",
        padx=15
    )

# ---------------- ATAQUE ----------------

    tk.Label(
        frame_seleccao,
        text="Tipo de ataque:",
        font=("Times New Roman", 9, "bold"),
        bg=BG_CARD,
        fg=BRANCO
    ).grid(
        row=0,
        column=0,
        padx=5,
        pady=4,
        sticky="w"
    )

    ataque_var = tk.StringVar(
        value="DDoS"
    )

    ataque_combo = ttk.Combobox(
        frame_seleccao,
        textvariable=ataque_var,
        values=[
            "DDoS",
            "Brute Force",
            "Phishing",
            "Ransomware"
        ],
        state="readonly",
        width=18
    )

    ataque_combo.grid(
        row=0,
        column=1,
        padx=5,
        pady=4
    )

    # ---------------- NÓ ALVO ----------------

    tk.Label(
        frame_seleccao,
        text="Nó alvo:",
        font=("Times New Roman", 9, "bold"),
        bg=BG_CARD,
        fg=BRANCO
    ).grid(
        row=1,
        column=0,
        padx=5,
        pady=4,
        sticky="w"
    )

    no_var = tk.StringVar(
        value="NODE 03"
    )

    no_combo = ttk.Combobox(
        frame_seleccao,
        textvariable=no_var,
        values=list(nos.keys()),
        state="readonly",
        width=18
    )

    no_combo.grid(
        row=1,
        column=1,
        padx=5,
        pady=4
    )

    # ========================================================
    # BOTÃO INICIAR MONITORIZAÇÃO
    # ========================================================

    

    frame_botoes = tk.Frame(
        frame_controlos,
        bg=BG_CARD
    )

    frame_botoes.pack(
        fill="x",
        padx=20,
        pady=8
    )

    botao_iniciar = tk.Button(
        frame_botoes,
        text="▶ INICIAR MONITORIZAÇÃO",
        command=iniciar_monitorizacao,
        bg="#166534",
        fg=BRANCO,
        font=("Arial", 9, "bold"),
        relief="flat",
        height=2
    )

    botao_iniciar.grid(
        row=0,
        column=0,
        padx=5,
        pady=5,
        sticky="ew"
    )

    botao_ataque = tk.Button(
        frame_botoes,
        text="⚔ INICIAR ATAQUE",
        bg="#991b1b",
        fg=BRANCO,
        font=("Arial", 9, "bold"),
        relief="flat",
        height=2
    )

    botao_ataque.grid(
        row=0,
        column=1,
        padx=5,
        pady=5,
        sticky="ew"
    )

    botao_parar = tk.Button(
        frame_botoes,
        text="■ PARAR MONITORIZAÇÃO",
        command=parar_monitorizacao,
        bg="#7f1d1d",
        fg=BRANCO,
        font=("Arial", 9, "bold"),
        relief="flat",
        height=2
    )

    botao_parar.grid(
        row=1,
        column=0,
        padx=5,
        pady=5,
        sticky="ew"
    )

    botao_limpar = tk.Button(
        frame_botoes,
        text="🗑 LIMPAR ALERTAS",
        command=limpar_resultados,
        bg="#334155",
        fg=BRANCO,
        font=("Arial", 9, "bold"),
        relief="flat",
        height=2
    )

    botao_limpar.grid(
        row=1,
        column=1,
        padx=5,
        pady=5,
        sticky="ew"
    )

    frame_botoes.columnconfigure(0, weight=1)
    frame_botoes.columnconfigure(1, weight=1)
    # ========================================================
    # EXECUTAR SISTEMA
    # ========================================================

    janela.mainloop()


    # ============================================================

    # INICIAR A APLICAÇÃO

    # ============================================================

iniciar_sistema()
