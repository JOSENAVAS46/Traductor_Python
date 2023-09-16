from googletrans import Translator, LANGUAGES

def print_menu():
    print("Idiomas disponibles:")
    for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
        print(f"{idx}. {lang} ({code})")
    print("0. Salir")

def main():
    translator = Translator()

    while True:
        print_menu()
        choice = input("Selecciona el idioma de origen (0 para salir): ")
        
        if choice == '0':
            break

        try:
            choice = int(choice)
            if choice < 0 or choice > len(LANGUAGES):
                print("Selecciona una opción válida.")
                continue
            
            source_language = list(LANGUAGES.keys())[choice - 1]
            text = input(f"Ingrese el texto en {LANGUAGES[source_language]}: ")
            
            print_menu()
            choice = input("Selecciona el idioma de destino (0 para salir): ")
            
            if choice == '0':
                break

            try:
                choice = int(choice)
                if choice < 0 or choice > len(LANGUAGES):
                    print("Selecciona una opción válida.")
                    continue
                
                target_language = list(LANGUAGES.keys())[choice - 1]
                
                translation = translator.translate(text, src=source_language, dest=target_language)
                print(f"Texto traducido a {LANGUAGES[target_language]}: {translation.text}\n")
                
            except ValueError:
                print("Selecciona una opción válida.")
        except ValueError:
            print("Selecciona una opción válida.")

if __name__ == "__main__":
    main()
