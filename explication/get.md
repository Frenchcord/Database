source code :
```py
def get(valuename: str, *, categorie = None):
  e = f'{f"{categorie}/" if categorie is None else ""}{valuename}'
  if path.isfile(e) is False: raise ValueDoesNotExist(f'{valuename}{f" dans la categorie {categorie}" if categorie is not None else ""} n\'éxiste pas')
  with open(f'./{e}', 'r') as f:
    return load(f)['value']
```
# stats
Nombre de variables : 1
<br>
Nombre de if : 2
<br>
Nombre de lignes : 4
<br>
Nombre d'arguments : 2
# pourquoi cela
La variable e va stocker la variable de fichier qui nous evite de faire un if de plus et donc perdre de la vitesse
<br>
Pour voir si la valeure existe nous avons un if qui va raise "valueDoesNotExist"
<br>
nous ouvrons le fichier en mode read et retournons la 'value' du dict que nous loadons avec "load"
# je veux prendre plusieurs valeurs comment faire?
Une boucle for in
```py
for i in items:
  get.append(db.get(i))
```
