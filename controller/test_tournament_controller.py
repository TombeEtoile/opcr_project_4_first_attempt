import json


def player_printer():

    players = [
      {
        "Nom": "AA",
        "Prenom": "aa",
        "Date de naissance": "1/1/1",
        "ID": "7259Ser5046"
      },
      {
        "Nom": "ZZ",
        "Prenom": "zz",
        "Date de naissance": "2/2/2",
        "ID": "6856yUs2921"
      }
    ]
    return players


p = 1
for player in player_printer():
    print({cle: valeur for cle, valeur in zip(str(p), player)})
    p += 1

# print(player_printer())

# objectif :
# {1: {'Nom': 'AA', 'Prenom': 'aa', 'Date de naissance': '1/1/1', 'ID': '7259Ser5046'}, 2: {'Nom': 'ZZ', 'Prenom': 'zz', 'Date de naissance': '2/2/2', 'ID': '6856yUs2921'}}