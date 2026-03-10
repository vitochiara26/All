def num_primo(num):
        if num < 2:
            print(f"El numero {num} no es un numero primo")
            return

        es_primo = True
        tercer_divisor = 0

        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                tercer_divisor = i
                break
            
        if es_primo:
            print(f"El numero {num} si es un numero primo")
        else:
            print(f"El numero {num} no es un numero primo")
            print(f"Ya que ademas de ser divisible entre 1 y el mismo({num}),")
            print(f"Es divisible tambien entre {tercer_divisor}: {num/tercer_divisor}")

try: 
    numero = int(input("Ingrese un numero entre 0 y 100: "))
    if numero < 0:
        print("Debe ingresar un valor mayor a 0 y menor 100")
    elif numero > 100:
        print("Debe ingresar un valor mayor a 0 y menor 100")
    else :
        num_primo(numero)
except Exception:
        print("Ingreso un numero no valido")
