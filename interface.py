# Importa a biblioteca gráfica tkinter
import tkinter as tk

# Importa funções do projecto
from colector import gerar_dados
from detector import detectar_ataque


# Função responsável por atualizar os dados na interface
def atualizar_dados():

    # Gera novos dados da rede
    dados = gerar_dados()

    # Detecta possíveis ataques
    resultado = detectar_ataque(dados)

    # Actualiza os textos da interface
    login_label.config(
        text=f"Tentativas de Login: {dados['tentativas_login']}"
    )

    requisições_label.config(
        text=f"Requisições: {dados['requisições']}"
    )

    arquivos_label.config(
        text=f"Acesso a Arquivos: {dados['acesso_arquivos']}"
    )

    ips_label.config(
        text=f"IPs Suspeitos: {dados['ips_suspeitos']}"
    )

    phishing_label.config(
        text=f"Links de Phishing: {dados['links_phishing']}"
    )

    resultado_label.config(
        text=f"Resultado: {resultado}"
    )

    # Atualiza os dados novamente após 3 segundos
    janela.after(3000, atualizar_dados)


# Cria a janela principal
janela = tk.Tk()

# Define título da janela
janela.title("Sistema de Detecção de Intrusões")

# Define tamanho da janela
janela.geometry("500x400")

# Cor de fundo
janela.configure(bg="#1e1e1e")


# Título principal
titulo = tk.Label(
    janela,
    text="Sistema Inteligente IDS",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)

titulo.pack(pady=15)


# Labels para mostrar os dados
login_label = tk.Label(janela, font=("Arial", 12), bg="#1e1e1e", fg="white")
login_label.pack(pady=5)

requisições_label = tk.Label(janela, font=("Arial", 12), bg="#1e1e1e", fg="white")
requisições_label.pack(pady=5)

arquivos_label = tk.Label(janela, font=("Arial", 12), bg="#1e1e1e", fg="white")
arquivos_label.pack(pady=5)

ips_label = tk.Label(janela, font=("Arial", 12), bg="#1e1e1e", fg="white")
ips_label.pack(pady=5)

phishing_label = tk.Label(janela, font=("Arial", 12), bg="#1e1e1e", fg="white")
phishing_label.pack(pady=5)

resultado_label = tk.Label(
    janela,
    font=("times new roman", 14, "bold"),
    bg="#1e1e1e",
    fg="red"
)

resultado_label.pack(pady=20)


# Inicia atualização automática
atualizar_dados()

# Mantém a interface aberta
janela.mainloop()