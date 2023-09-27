import Fc_ahorcado

# Archivo principal del juego
secret_word = Fc_ahorcado.select_word()
tries = 6  # Número de intentos permitidos
letter_guesseds = []

print("¡Bienvenido al Juego del Ahorcado!")

while tries > 0:
    board = Fc_ahorcado.show_board(secret_word, letter_guesseds)
    print(f"\nPalabra secreta: {board}")
    letter = input("Adivina una letra: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        Fc_ahorcado.show_letters(letter_guesseds)
        print("Por favor, ingresa una sola letra válida.")
        continue

    if letter in letter_guesseds:
        Fc_ahorcado.show_letters(letter_guesseds)
        print("Ya adivinaste esa letra antes.")
        continue

    letter_guesseds.append(letter)

    if letter in secret_word:
        Fc_ahorcado.show_letters(letter_guesseds)
        print("¡Adivinaste una letra!")
    else:
        tries -= 1
        Fc_ahorcado.show_letters(letter_guesseds)
        print(f"Letra incorrecta. Te quedan {tries} intentos.")

    if "_" not in Fc_ahorcado.show_board(secret_word, letter_guesseds):
        print(f"\n¡Felicidades! ¡Has adivinado la palabra secreta: '{secret_word}'!")
        break

if tries == 0:
    print(f"\n¡Has perdido! La palabra secreta era '{secret_word}'.")