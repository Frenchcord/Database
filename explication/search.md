Source code :
```py
def search(valuename: str, *, categorie: str = None):
  return path.isfile(f'{f"{categorie}/" if categorie is None else ""}{valuename}.json')
```
# stats
Nombre de variables : 0
<br>
Nombre de if : 1
<br>
Nombre de lignes : 1
<br>
nombre d'arguments : 2
# pourquoi cela?
La fonction isfile de path retourne une variable boolean de si la valeur existe
<br>
Donc autant juste retourner cela
# je veux verifier plusieurs valeures comment faire?
Une boucle for in
```py
for i in valuenames:
  checked.append(db.search(i))
```
