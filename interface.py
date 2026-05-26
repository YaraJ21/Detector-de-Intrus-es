# SISTEMA DE DETECÇÃO DE INTRUSÕES
# INTERFACE GRÁFICA
# Biblioteca gráfica
import tkinter as tk

# Data e hora
from datetime import datetime

# Gráficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Importa módulos do projecto
from captura_rede import obter_dados_rede

#25/05/2026: Mudancas feitas para integrar IA a interface
from detector_ia import prever_ataque


# LISTAS DO GRÁFICO


x_dados = []
y_dados = []



# FUNÇÃO PRINCIPAL


def atualizar_dados():

    # Gera dados reais
    dados = obter_dados_rede()

    # Detecta ataque
    #resultado = detectar_ataque(dados)
    resultado= prever_ataque(dados)

    #Mensagens
    if resultado == "BENIGN":
        mensagem = "Actividade Normal"
    
    elif "DoS" in resultado or "DDoS" in resultado:
        mensagem = "Ataque DDoS Detectado"

    elif "PortScan" in resultado:
        mensagem = "Port Scan Detectado"

    elif "Patator" in resultado:
        mensagem = "Ataque de Força Bruta Detectado"

    else:
        mensagem = f"Ataque Detectado: {resultado}"

    
    # CORES DOS ALERTAS
    cor_alerta = "lime"

    if "DDoS" in resultado:
        cor_alerta = "red"

    elif "Port" in resultado:
        cor_alerta = "orange"

    elif "Bot" in resultado:
        cor_alerta = "purple"


    # ACTUALIZA LABELS
    resultado_label.config(
    text=f"Resultado: {mensagem}",
    fg=cor_alerta
)

    duração_label.config(
        text=f"Duração do Fluxo: {dados['duração']}"
    )

    retorno_label.config(
        text=f"Pacotes de Retorno: {dados['pacotes_retorno']}"
    )

    tipo_label.config(
       text=f"Tipo Detectado: {resultado}"
    )

  
    # RELÓGIO
  

    hora_actual = datetime.now().strftime("%H:%M:%S")

    relógio_label.config(
        text=f"Hora: {hora_actual}"
    )

   
    # HISTÓRICO
  

    histórico.insert(
        tk.END,
        f"[{hora_actual}] {resultado}\n"
    )

    histórico.see(tk.END)

    # ACTUALIZA GRÁFICO
   

    x_dados.append(len(x_dados))

    y_dados.append(dados["requisições"])

    if len(x_dados) > 15:

        x_dados.pop(0)

        y_dados.pop(0)

    gráfico.clear()

    gráfico.plot(x_dados, y_dados)

    gráfico.set_title("Tráfego da Rede")

    gráfico.set_ylabel("Pacotes")

    canvas.draw()

    # GUARDA LOGS
    #

    with open("logs.txt", "a", encoding="utf-8") as log:

        log.write(f"[{hora_actual}] {resultado}\n")

    
    # ACTUALIZA NOVAMENTE
   

    janela.after(3000, atualizar_dados)



# CRIA JANELA

janela = tk.Tk()

janela.title("CyberShield AI - IDS")

janela.geometry("900x700")

janela.configure(bg="#0f172a")


# TÍTULO


titulo = tk.Label(
    janela,
    text="CYBERSHIELD AI",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="cyan"
)

titulo.pack(pady=10)

# STATUS

status_label = tk.Label(
    janela,
    text="🟢 SISTEMA ONLINE",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="lime"
)

status_label.pack()



# RELÓGIO


relógio_label = tk.Label(
    janela,
    text="Hora:",
    font=("Arial", 12),
    bg="#0f172a",
    fg="white"
)

relógio_label.pack(pady=5)

# FRAME DOS DADOS

frame_dados = tk.Frame(
    janela,
    bg="#1e293b",
    bd=2,
    relief="ridge"
)

frame_dados.pack(pady=15, padx=20, fill="x")

# LABELS DOS DADOS


requisições_label = tk.Label(
    frame_dados,
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)

requisições_label.pack(pady=5)


duração_label = tk.Label(
    frame_dados,
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)

duração_label.pack(pady=5)


retorno_label = tk.Label(
    frame_dados,
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)

retorno_label.pack(pady=5)


tipo_label = tk.Label(
    frame_dados,
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)

tipo_label.pack(pady=5)

# RESULTADO


resultado_label = tk.Label(
    janela,
    text="",
    font=("Arial", 16, "bold"),
    bg="#0f172a"
)

resultado_label.pack(pady=20)


# HISTÓRICO
#

histórico_titulo = tk.Label(
    janela,
    text="Histórico de Alertas",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="cyan"
)

histórico_titulo.pack()


histórico = tk.Text(
    janela,
    height=8,
    bg="black",
    fg="lime",
    font=("Consolas", 10)
)

histórico.pack(padx=20, pady=10, fill="x")

# GRÁFICO

figura = Figure(figsize=(6, 3), dpi=100)

gráfico = figura.add_subplot(111)

canvas = FigureCanvasTkAgg(figura, master=janela)

canvas.get_tk_widget().pack(pady=10)
figura.patch.set_facecolor("#1e293b")

gráfico.set_facecolor("#1e293b")

gráfico.tick_params(colors="white")

gráfico.spines["bottom"].set_color("white")
gráfico.spines["top"].set_color("white")
gráfico.spines["left"].set_color("white")
gráfico.spines["right"].set_color("white")

gráfico.title.set_color("white")

gráfico.yaxis.label.set_color("white")



# INICIA SISTEMA


atualizar_dados()



# MANTÉM JANELA ABERTA
# 

janela.mainloop()