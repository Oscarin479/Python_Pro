meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "Juicioso": "Persona que es juiciosa",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
# ¿Qué debemos hacer si se encuentra la palabra?
if word in meme_dict.keys():
    print(meme_dict[word])
    # ¿Qué hacer si no se encuentra la palabra?
else:
    print("No esta en nuestro diccionario")
