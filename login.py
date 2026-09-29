import tkinter as tk
from tkinter import messagebox

BG = "#0f172a"
BG_CARD = "#1e293b"
CYAN = "#22d3ee"
BRANCO = "#f8fafc"
CINZA = "#94a3b8"
VERDE = "#22c55e"
VERMELHO = "#ef4444"

def abrir_painel():
    utilizador = entrada_utilizador.get().strip()
    senha = entrada_senha.get()

    if utilizador == "" or senha == "":
        messagebox.showwarning(
            "Campos obrigatórios",
            "Preencha o utilizador e a palavra-passe."
        )
        return

    if utilizador == "admin" and senha == "1234":
        janela.destroy()

        import interface
        interface.iniciar_sistema()

    else:
        messagebox.showerror(
            "Acesso negado",
            "Utilizador ou palavra-passe incorrectos."
        )

janela = tk.Tk()
janela.title("CyberShield AI - Login")
janela.geometry("1100x950")
janela.configure(bg=BG)
janela.resizable(True, True)

frame_principal = tk.Frame(
    janela,
    bg=BG
)
frame_principal.pack(
    fill="both",
    expand=True
)

tk.Label(
    frame_principal,
    text="CYBERSHIELD AI",
    font=("Times New Roman", 25, "bold"),
    bg=BG,
    fg=CYAN
).pack(pady=(50, 5))

tk.Label(
    frame_principal,
    text="Sistema de Detecção de Intrusões",
    font=("Times New Roman", 11),
    bg=BG,
    fg=CINZA
).pack(pady=(0, 40))

frame_login = tk.Frame(
    frame_principal,
    bg=BG_CARD,
    bd=2,
    relief="ridge",
    width=450,
    height=400
)

frame_login.pack(
    padx=50,
    pady=10
)

frame_login.pack_propagate(False)
tk.Label(
    frame_login,
    text="AUTENTICAÇÃO",
    font=("Times New Roman", 15, "bold"),
    bg=BG_CARD,
    fg=BRANCO
).pack(pady=(25, 25))

tk.Label(
    frame_login,
    text="Utilizador",
    font=("Times New Roman", 10, "bold"),
    bg=BG_CARD,
    fg=CINZA
).pack(
    anchor="w",
    padx=15
)

entrada_utilizador = tk.Entry(
    frame_login,
    font=("Times New Roman", 11),
    bg="#334155",
    fg=BRANCO,
    insertbackground=BRANCO,
    relief="flat"
)
entrada_utilizador.pack(
    padx=15,
    pady=(8, 15),
    fill="x",
    ipady=8
)

tk.Label(
    frame_login,
    text="Palavra-passe",
    font=("Times New Roman", 10, "bold"),
    bg=BG_CARD,
    fg=CINZA
).pack(
    anchor="w",
    padx=35
)

entrada_senha = tk.Entry(
    frame_login,
    font=("Times New Roman", 11),
    bg="#334155",
    fg=BRANCO,
    insertbackground=BRANCO,
    relief="flat",
    show="*"
)
entrada_senha.pack(
    padx=15,
    pady=(8, 15),
    fill="x",
    ipady=8
)

botao_entrar = tk.Button(
    frame_login,
    text="ENTRAR",
    command=abrir_painel,
    font=("Times New Roman", 11, "bold"),
    bg=CYAN,
    fg=BG,
    activebackground=CYAN,
    activeforeground=BG,
    relief="flat",
    cursor="hand2",
    height=2
)
botao_entrar.pack(
    padx=15,
    pady=(0, 15),
    fill="x"
)

tk.Label(
    frame_principal,
    text="CyberShield AI • Segurança de Sistemas",
    font=("Times New Roman", 9),
    bg=BG,
    fg=CINZA
).pack(
    side="bottom",
    pady=25
)

entrada_utilizador.focus()

janela.bind(
    "<Return>",
    lambda event: abrir_painel()
)

janela.mainloop()