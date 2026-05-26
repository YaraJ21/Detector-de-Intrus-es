#26/05/2026
# Regras de deteção de ataques

def detectar_por_regras(dados):

    requisicoes = dados["requisições"]
    duracao = dados["duração"]
    retorno = dados["pacotes_retorno"]

    # DDoS
    if requisicoes > 100:
        return "DDoS"

    # Força Bruta
    elif requisicoes < 10 and duracao > 10:
        return "Força Bruta"

    # Phishing
    elif requisicoes > 20 and retorno < 2:
        return "Phishing"

    # Ransomware
    elif requisicoes > 150 and duracao < 3:
        return "Ransomware"

    # Nenhuma regra encontrada
    return None