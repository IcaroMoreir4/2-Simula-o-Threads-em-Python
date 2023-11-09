import threading
import time

# Função para imprimir uma sequência de números
def print_numbers():
    for i in range(1, 6):
        print(f"Number {i}")
        time.sleep(1)  # Aguarda 1 segundo entre as impressões

# Função para imprimir uma sequência de letras
def print_letters():
    for letter in 'ABCDE':
        print(f"Letter {letter}")
        time.sleep(1)  # Aguarda 1 segundo entre as impressões

# Cria duas threads para executar as funções
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Inicia as threads
thread1.start()
thread2.start()

# Aguarda até que ambas as threads terminem
thread1.join()
thread2.join()

print("Programa concluído!")
