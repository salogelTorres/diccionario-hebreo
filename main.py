import itertools

# Definimos una tupla con los 22 caracteres del hebreo
hebreo = (
    "א",
    "ב",
    "ג",
    "ד",
    "ה",
    "ו",
    "ז",
    "ח",
    "ט",
    "י",
    "כ",
    "ל",
    "מ",
    "נ",
    "ס",
    "ע",
    "פ",
    "צ",
    "ק",
    "ר",
    "ש",
    "ת",
)

# Definimos un diccionario para las letras finales
letras_finales = {"כ": "ך", "מ": "ם", "נ": "ן", "פ": "ף", "צ": "ץ"}

# Generamos todas las combinaciones de 1, 2 y 3 letras del hebreo
combinaciones = []
for length in range(1, 5):  # Longitudes de 1 a 3
    for combinacion in itertools.product(hebreo, repeat=length):
        if length == 1:
            combinaciones.append(
                "".join(combinacion)[::-1]
            )  # Invertir para derecha a izquierda
        else:
            letra1, *resto = combinacion
            if resto and resto[-1] in letras_finales:
                combinaciones.append(
                    (letra1 + letras_finales[resto[-1]])[::-1]
                )  # Invertir
            else:
                combinaciones.append("".join(combinacion)[::-1])  # Invertir

# Imprimimos las combinaciones
print(combinaciones)
