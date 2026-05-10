# Função responsável por analisar os dados da rede
# e identificar possíveis ataques cibernéticos
def detectar_ataque(dados):

    # Verifica se existem muitas tentativas de login
    # Pode indicar ataque de força bruta
    if dados["tentativas_login"] > 20:
        return "⚠ Ataque de Força Bruta Detectado"

    # Verifica excesso de requisições na rede
    # Pode indicar ataque DDoS
    elif dados["requisições"] > 3000:
        return "⚠ Ataque DDoS Detectado"

    # Verifica acessos excessivos a arquivos
    # Pode indicar ransomware
    elif dados["acesso_arquivos"] > 150:
        return "⚠ Possível Ransomware Detectado"

    # Verifica muitos links suspeitos
    # Pode indicar phishing
    elif dados["links_phishing"] > 5:
        return "⚠ Possível Ataque de Phishing"

    # Verifica quantidade elevada de IPs suspeitos
    elif dados["ips_suspeitos"] > 10:
        return "⚠ Actividade Suspeita na Rede"

    # Caso nenhuma condição suspeita seja encontrada
    else:
        return "✔ Actividade Normal"