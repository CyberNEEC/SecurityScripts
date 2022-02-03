import socket
# Com este import conseguiremos utilizar expressões regulares que assegurarão que o input do user estará bem formatado
import re

# Aqui vamos criar um padrão para os endereços IPV4 - 192.168.1.12 como exemplo
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# E aqui para o intervalo das portas que pretendemos dar scan que deve ser algo do género 20-80
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Variáveis de controlo para a primeira e ultima porta possíveis de dar scan
port_min = 0
port_max = 65535

#DISCLAIMER
# Este script usa a Socket API para ver se é possível conectar a um conjunto de portas de um endereço especifico
# Este script não faz a comparação entre portas fechadas e filtradas
# Apenas dará open quando a conexão à porta for feita com sucesso

print("Este port scanner foi feito pelo CyberNEEC para uso experimental.\n\n")

# Lista que irá armazenar as portas que foi possível conectar
open_ports = []

# Pedir ao user o IP que deseja efetuar o scan
while True:
    ip_add_entered = input("\nIntroduza o IP que deseja efetuar o scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"\n{ip_add_entered} é um endereço válido")
        break
    else:
        print("\nPor favor insira um endereço válido.")

while True:
    # Mais tarde irá ser feito um script com multithreading para ser possível o scan de todas as portas
    print("\nIntervalo de ports que pretende dar scan no seguinte formato: X-Y")
    port_range = input("Insira o intervalo: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
    try:
        # Criar um socket object da mesma forma que se abre um ficheiro
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 0.5 é o limite máximo de tempo que damos para fazer a conexão a uma port
            s.settimeout(0.5)
            #Usamos o objeto criado para fazer connect ao ip:port
            s.connect((ip_add_entered, port))
            # Se deu tudo certo adiciona à lista
            open_ports.append(port)

    except:
        # Tratamento de ports fechadas
        pass

for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")