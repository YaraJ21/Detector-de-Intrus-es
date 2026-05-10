import random
import time


# Função responsável por gerar dados fictícios da rede
def gerar_dados():

    # Criação de um dicionário com informações simuladas
    dados = {

        # Simula número de tentativas de login
        "tentativas_login": random.randint(1, 50),

        # Simula quantidade de requisições na rede
        "requisições": random.randint(100, 5000),

        # Simula acessos/modificações em arquivos
        "acesso_arquivos": random.randint(1, 200),

        # Simula quantidade de IPs suspeitos detectados
        "ips_suspeitos": random.randint(0, 20),

        # Simula quantidade de links de phishing encontrados
        "links_phishing": random.randint(0, 10)
    }

    # Retorna os dados gerados
    return dados


# Função principal de monitoramento da rede
def monitorar_rede():

    # Loop infinito para manter o sistema funcionando em tempo real
    while True:

        # Chama a função que gera os dados simulados
        dados = gerar_dados()

        # Exibe título da secção no terminal
        print("\n===== DADOS DA REDE =====")

        # Mostra os dados simulados
        print(f"Tentativas de Login: {dados['tentativas_login']}")
        print(f"Requisições: {dados['requisições']}")
        print(f"Acesso a Arquivos: {dados['acesso_arquivos']}")
        print(f"IPs Suspeitos: {dados['ips_suspeitos']}")
        print(f"Links de Phishing: {dados['links_phishing']}")

        # Pausa de 3 segundos antes da próxima análise
        time.sleep(3)


# Verifica se o arquivo está sendo executado directamente
if __name__ == "__main__":

    # Inicia o monitoramento da rede
    monitorar_rede()