source code :
```py
def get(valuename: str, *, categorie = None):
  e = f'{f"{categorie}/" if categorie is None else ""}{valuename}'
  if path.isfile(e) is False: raise ValueDoesNotExist(f'{valuename}{f" dans la categorie {categorie}" if categorie is not None else ""} n\'éxiste pas')
  with open(f'./{e}', 'r') as f:
    return load(f)['value']
```
# stats
variables : 1
<br>
nombre de if : 2
