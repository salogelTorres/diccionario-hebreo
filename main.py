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

# Generamos todas las combinaciones de dos letras del hebreo
combinaciones = list(itertools.product(hebreo, repeat=2))

# Convertimos las combinaciones de tuplas a strings, considerando las letras finales
combinaciones_str = []
for combinacion in combinaciones:
    letra1, letra2 = combinacion
    if letra2 in letras_finales:
        combinaciones_str.append(letra1 + letras_finales[letra2])
    else:
        combinaciones_str.append(letra1 + letra2)

# Imprimimos las combinaciones
print(combinaciones_str)
