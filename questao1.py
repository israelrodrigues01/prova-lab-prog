inteiro = int(input("Digite um número número inteiro: "))

palavras = ['FizzBuzzPop', 'FizzBuzz', 'FizzPop', 'BuzzPop', 'Fizz', 'Buzz', 'Pop']

if(inteiro % 3 == 0 and inteiro % 5 == 0 and inteiro % 7 == 0):
    print(palavras[0])
else:
    if(inteiro % 3 == 0 and inteiro % 5 == 0):
        print(palavras[1])
    elif(inteiro % 3 == 0 and inteiro % 7 == 0):
        print(palavras[2])
    elif(inteiro % 5 == 0 and inteiro % 7 == 0):
        print(palavras[3])
    elif(inteiro % 3 == 0):
        print(palavras[4])
    elif(inteiro % 5 == 0):
        print(palavras[5])
    elif(inteiro % 7 == 0):
        print(palavras[6])
    else:
        print("Número:", inteiro)
        
    