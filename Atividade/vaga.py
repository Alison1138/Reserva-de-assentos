import os

# Configurações do Avião
FILEIRAS = 10
COLUNAS = ['A', 'B', 'C', 'D']
# Criamos o mapa usando um dicionário para facilitar a visualização
# Ex: {0: ['0', '0', '0', '0'], 1: [...]}
aviao = {i: ["0"] * len(COLUNAS) for i in range(FILEIRAS)}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_mapa():
    limpar_tela()
    print("      === SISTEMA DE RESERVAS GOL-MINI ===")
    print(f"        {'   '.join(COLUNAS)}") # Cabeçalho A B C D
    
    for fileira, assentos in aviao.items():
        # Formata o número da fileira com 2 dígitos para alinhar
        status = "   ".join(assentos)
        print(f"Row {fileira:02} | {status} |")
    
    print("-" * 40)
    print("Legenda: [ 0 ] Livre  |  [ X ] Ocupado")

def reservar():
    try:
        exibir_mapa()
        f = int(input("\nDigite o número da fileira (0-9): "))
        c_letra = input("Digite a letra do assento (A-D): ").upper()
        
        if c_letra not in COLUNAS:
            print("❌ Coluna inválida!")
            return

        c_index = COLUNAS.index(c_letra)

        if aviao[f][c_index] == "0":
            aviao[f][c_index] = "X"
            print(f"\n✅ Sucesso! Assento {f}{c_letra} reservado.")
        else:
            print(f"\n⚠️ O assento {f}{c_letra} já está ocupado!")
            
    except (ValueError, KeyError):
        print("\n⚠️ Entrada inválida. Use números para fileiras.")
    
    input("\nPressione Enter para continuar...")

def menu_principal():
    while True:
        exibir_mapa()
        print("1. Reservar Assento")
        print("2. Ver Taxa de Ocupação")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            reservar()
        elif opcao == "2":
            total = FILEIRAS * len(COLUNAS)
            ocupados = sum(fileira.count("X") for fileira in aviao.values())
            print(f"\n📊 Ocupação atual: {ocupados}/{total} ({(ocupados/total)*100:.1f}%)")
            input("\nPressione Enter para voltar...")
        elif opcao == "3":
            print("Encerrando... Tenha um ótimo voo!")
            break

if __name__ == "__main__":
    menu_principal()