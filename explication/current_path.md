source code :
```py
current_path = __file__[: -len(__file__.split('/')[-1])]
```
# pourquoi cela?
Nous avons le fichier avec sa path mais je veux acceder a la database (le dossier) et donc je vais faire une liste des elements et enlever la taille <br>
du dernier fichier donc le main.py
