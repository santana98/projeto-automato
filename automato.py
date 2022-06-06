abc = [
    "a","b","c","d","e","f","g","h","i",
    "j","k","l","m","n","o","p","q","r",
    "s","t","u","v","w","x","y","z"
    ]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


palavra = input('Digite a palavra que deseja validar: ')

step = 1

for value in palavra:
#step 1 = inicio identificador
    if step == 1:
        if value in abc:
            step = 2
        else:
            step = 0
#step 2 = loop caracteres identificador            
    elif step == 2:
        if value in abc or value in numbers or value == '_':
            step = 2
        elif value == " ":
            step = 2   
        elif value == "=":
            step = 3
        else:
            step = 0
#step 3 = op_atrib
    elif step == 3:
        if value == " ":
            step = 3
        elif value in abc:
            step = 4
        elif value in numbers:
            step = 5
        else:
            step = 0
#step 4 = segundo loop identificador
    elif step == 4:
        if value in abc or value in numbers or value == '_':
            step = 4
        elif value == ";":
            step = 7
        else:
            step = 0
#step 5 = loop numeros
    elif step == 5:
        if value == ".":
            step = 6
            decimal = False
        elif value in numbers:
            step = 5
        elif value == ";":
            step = 7
        else:
            step = 0
#step 6 = decimal
    elif step == 6:
        if value in numbers:
            step = 6
            decimal = True
        elif value == ";":
            if decimal:
                step = 7
            else:
              step = 0
        else:
              step = 0
#step 7 = aceitação
    elif step == 7:
        if value != " ":
            step = 0
#step 0 = Fora da linguagem            
    elif step == 0:
        break
            
print('\nPalavra processada')

if step == 7:
    print('\nResultado: Palavra aceita na linguagem')

else:
    print('Resultado: Palavra recusada')
