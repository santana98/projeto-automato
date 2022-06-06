def automato(palavra):
    abc = [
        "a","b","c","d","e","f","g","h","i",
        "j","k","l","m","n","o","p","q","r",
        "s","t","u","v","w","x","y","z"
        ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    step = 1
    space = 0

    for value in palavra:
    #[ Step 1 ] = inicio identificador
        if step == 1:
            print("[ Step 1 ] - Validando o inicio do identificador [a-z]")
            print(value)
            if value in abc:
                step = 2
            else:
                step = 0
    #[ Step 2 ] = loop caracteres identificador            
        elif step == 2 and space == 0:
            print("[ Step 2 ] - Validando o loop de caracteres [a-z] | [0-9] | _")
            print(value)
            if value in abc or value in numbers or value == '_':
                continue
            elif value == " ":
                space = 1   
            elif value == "=":
                print("op_atrib '=' encontrado")
                step = 3
            else:
                print("Fora do padrão definido!!")
                step = 0
        elif step == 2 and space == 1:
            print("[ Step 2 ] - Validando o loop de caracteres [a-z] | [0-9] | _")
            print(value)
            if value == " ":
                continue
            elif value == "=":
                print("op_atrib '=' encontrado")
                step = 3
                space = 0
            else:
                print("Fora do padrão definido!!")
                step = 0
    #[ Step 3 ] = op_atrib
        elif step == 3:
            print("[ Step 3 ] - Validando seguimentação identificador|número")
            print(value)
            if value == " ":
                continue
            elif value in abc:
                print("Ramo indetificador ativado")
                step = 4
            elif value in numbers:
                print("Ramo número ativado")
                step = 5
            else:
                print("Fora do padrão definido!!")
                step = 0
    #[ Step 4 ] = segundo loop identificador
        elif step == 4 and space == 0:
            print("[ Step 4 ] - Validando loop de caracteres do identificador")
            print(value)
            if value in abc or value in numbers or value == '_':
                continue
            elif value ==" ":
                step == 4
                space == 1
            elif value == ";":
                print("'pv' (;) encontrado!")
                step = 7
            else:
                print("Fora do padrão definido!!")
                step = 0
        elif step == 4 and space == 1:
            print("[ Step 4 ] - Validando loop de caracteres do identificador")
            print(value)
            if value == " ":
                continue
            elif value == ";":
                print("'pv' (;) encontrado!")
                step = 7
            else:
                print("Fora do padrão definido!!")
                step = 0
    #[ Step 5 ] = loop numeros
        elif step == 5:
            print("[ Step 5 ] - Validando loop de números")
            print(value)
            if value == ".":
                print("Número decimal")
                step = 6
                decimal = False
            elif value in numbers:
                continue
            elif value == ";":
                print("'pv' (;) encontrado!")
                step = 7
            elif value == " ":
                step = 6
                space = 1
            else:
                print("Fora do padrão definido!!")
                step = 0
    #[ Step 6 ] = decimal
        elif step == 6 and space == 0 :
            print("[ Step 6 ] - Validando número decimal")
            print(value)
            if value in numbers:
                step = 6
                decimal = True
            elif value == " " and decimal == True:
                space = 1
            elif value == ";":
                print("'pv' (;) encontrado!")
                if decimal:
                    step = 7
                else:
                    print("Fora do padrão definido!!")
                    step = 0
            else:
                print("Fora do padrão definido!!")
                step = 0
        elif step == 6 and space == 1:
            if value == " ":
                continue
            elif value == ";":
                print("'pv' (;) encontrado!")
                step = 7
            else:
                print("Fora do padrão definido!!")
                step = 0
    #[ Step 7 ] = aceitação
        elif step == 7:
            print("[ Step 7 ] - Requisitos atendidos até aqui... ")
            print(value)
            if value != " ":
                print("Fora do padrão definido!!")
                step = 0
    #step 0 = Fora da linguagem            
        elif step == 0:
            break
                
    print('\nPalavra processada')

    if step == 7:
        return print('\nResultado: Palavra aceita na linguagem\n')
    else:
        return print("\nResultado: Palavra recusada, fora do padrão da linguagem\n")
