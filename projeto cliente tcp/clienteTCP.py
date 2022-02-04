import socket
#biblioteca fornece acesso a variaveis e funções
# e tem forte interação com o interpretador que é o python
import sys  

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Falha na conecção!")
        print("Erro: {}".format(e))
        sys.exit()
    print("\nSocket criado com sucesso.")

    HostAlvo = input("\nDigite o Host ou Ip a ser conectado: ")
    PortaAlvo = input("\nDigite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no Host {} - Porta {}".format(HostAlvo,PortaAlvo))

        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no Host {} - Porta {}".format(HostAlvo,PortaAlvo))
        print("Error: {}".format(e))
        sys.exit()

if __name__ == '__main__':
    main()
