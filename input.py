
# prove per input

andList = [str(x) for x in input("Tutte queste parole (separale con punto e virgola):\n").split("; ")]
exactStr = input("Questa frase esatta:\n")
orList = [str(x) for x in input("Almeno una di queste parole (separale con punto e virgola):\n").split("; ")]
'''
noList = [str(x) for x in input("Nessuna di queste parole (separale con punto e virgola):\n").split("; ")]
hashtagList = [str(x) for x in input("Tutti questi hashtag (separali con punto e virgola):\n").split("; ")]
language = input("Inserisci la lingua di ricerca (usa codici ISO-691):\n")
fromUsers = [str(x) for x in input("Da questi utenti (separali con punto e virgola):\n").split("; ")]
toUsers = [str(x) for x in input("A questi utenti (separali con punto e virgola):\n").split("; ")]
mentionedUsers = [str(x) for x in input("Tutti questi utenti menzionati (separale con punto e virgola):\n").split("; ")]
place = input("Città e Regione(separale con la virgola):\n")
fromDate = input("Da questa data (AAAA-MM-GG):\n")
toDate = input("A questa data (AAAA-MM-GG):\n")
'''
'''

'''
q=''
for i in orList:
    q = q + " OR " + i
    print(type(i))

print(q)
