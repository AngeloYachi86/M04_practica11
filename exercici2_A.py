def saludar():
    nom = input("Ingresar nom: ")
    nombres_permitidos = ["Albert", "Berta", "Clara", "David", "Eva"]
    if nom in nombres_permitidos:
        if nom == "Albert":
            return "Hola, Albert! Eres una persona molt intel·ligent."
        elif nom == "Berta":
            return "Hola, Berta! Ets una persona molt divertida."
        elif nom == "Clara":
            return "Hola, Clara! Ets una persona molt amable."
        elif nom == "David":
            return "Hola, David! Ets una persona molt valent."
        else:
            return "Hola, Eva! Ets una persona molt encantadora."
    else:
        return "El nom no està a la llista."

