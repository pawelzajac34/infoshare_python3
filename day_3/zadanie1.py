ADMIN_USERNAME = "Piotr"
name = input("Podaj imię: ")
name_capitalized = name.lower().capitalize()
if name_capitalized == ADMIN_USERNAME:
    print("Cześć",name_capitalized)
else:
    print("Hey Poklikash?")
# TODO: some comment