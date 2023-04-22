def serie():
    valor = int (input("Introduce numero a calcular: "))
    resultado = fibonacci (valor)
    print ("Su resultado en la serie de Fibonacci es: " + str (resultado))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        for i in range (1,n): 
            return (fibonacci(n-1) + fibonacci(n-2))


if __name__ == "__main__":
    serie ()
    
