# Importa a biblioteca time
# usada para criar pausas no sistema
import time

# Importa a função gerar_dados do arquivo collector.py
from collector import gerar_dados # type: ignore

# Importa a função detectar_ataque do arquivo detector.py
from detector import detectar_ataque


# Loop infinito para manter o sistema funcionando continuamente
while True:

    # Chama a função que gera os dados simulados da rede
    dados = gerar_dados()

    # Envia os dados para o detector analisar
    resultado = detectar_ataque(dados)

    # Exibe título do monitoramento
    print("\n========== MONITORAMENTO ==========")

    # Mostra os dados capturados
    print(f"Tentativas de Login: {dados['tentativas_login']}")
    print(f"Requisições: {dados['requisições']}")
    print(f"Acesso a Arquivos: {dados['acesso_arquivos']}")
    print(f"IPs Suspeitos: {dados['ips_suspeitos']}")
    print(f"Links de Phishing: {dados['links_phishing']}")

    # Exibe o resultado da análise
    print(f"\nResultado da Análise: {resultado}")

    # Guarda o resultado no arquivo logs.txt
    with open("logs.txt", "a", encoding="utf-8") as log:

        # Escreve o resultado no arquivo de logs
        log.write(resultado + "\n")

    # Pausa de 3 segundos antes da próxima análise
    time.sleep(3)