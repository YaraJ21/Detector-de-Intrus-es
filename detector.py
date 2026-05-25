
# DETECTOR DE ATAQUES


def detectar_ataque(dados):

    ataque = dados["label"]

    # TRÁFEGO NORMAL
  

    if ataque == "BENIGN":

        return "✔ Actividade Normal"

  
    # DDOS
   

    elif "DoS" in ataque or "DDoS" in ataque:

        return "⚠ Ataque DDoS Detectado"

    
    # PORTSCAN
   

    elif "PortScan" in ataque:

        return "⚠ Port Scan Detectado"

    
    # BOTNET
    # 

    elif "Bot" in ataque:

        return "⚠ Botnet Detectada"

    # OUTROS ATAQUES
    

    else:

        return f"⚠ Ataque Detectado: {ataque}"