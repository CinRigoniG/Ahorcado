import random

'''ARCHIVO DE FUNCIONES'''

# Función para seleccionar una palabra al azar
def select_word():
    # Lista de palabras para adivinar
    words = ["python", "programacion", "computadora", "desarrollo", "inteligencia"]
    return random.choice(words)

# Función para mostrar el tablero
def show_board(word, letter_guesseds):
    board = ""
    for letter in word:
        if letter in letter_guesseds:
            board += letter
        else:
            board += "_ "
    return board

# Funcion para mostrar las letras ingresadas
def show_letters(letter_guesseds):
    print('\nLetras ingresadas:',end=' ')
    for i in letter_guesseds:
        print(i,end='-')
    print()