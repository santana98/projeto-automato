from automato import automato

if __name__ == '__main__':
    print("\nAUTOMATO FINITO\n")
    palavra = None
    while palavra != "exit":
        palavra = input("Digite a palvra que desaja validar: ")
        if palavra != "exit":
            automato(palavra)
        else: 
            print("PROGRAMA ENCERRADO")