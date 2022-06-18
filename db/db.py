from os import listdir, mkdir, rmdir, path; from json import load, dump; from os import remove as delet
class ValueAlreadyExist(Exception):
  pass
class ValueNotExist(Exception):
  pass
class CategoryAlreadyExist(Exception):
  pass
class CategoryDoesNotExist(Exception):
  pass
current_path = __file__[: -len(__file__.split('/')[-1])]
def search(valuename: str, *, categorie: str = None):
  if not '||' in valuename: return path.isfile(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json')
  for value in valuename.split('||'):
    if not path.isfile(f'{current_path}namedb{"" if not categorie else f"/{categorie}"}/{value}.json'): return False
  return True
async def exist(valuename: str, *, categorie: str = None):
  if not '||' in valuename: return path.isfile(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json')
  for value in valuename.split('||'):
    if not path.isfile(f'{current_path}namedb{"" if not categorie else f"/{categorie}"}/{value}.json'): return False
  return True
def get(valuename: str, *, categorie: str = None):
  if '||' not in valuename:
    file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
    if not path.isfile(file): raise ValueNotExist('Value does not exist')
    return load(open(file, 'r'))['value']
  valuelist: list = []
  for value in valuename.split('||'):
    file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{value}.json'
    if not path.isfile(file): raise ValueNotExist(f'Value {value} does not exist')
    valuelist.append(load(open(file, 'r'))['value'])
  return valuelist
  
async def select(valuename: str, *, categorie: str = None):
  if '||' not in valuename:
    file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
    if not path.isfile(file): raise ValueNotExist('Value does not exist')
    return load(open(file, 'r'))['value']
  valuelist: list = []
  for value in valuename.split('||'):
    file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
    if not path.isfile(file): raise ValueNotExist(f'Value {value} does not exist')
    valuelist.append(load(open(file, 'r'))['value'])
  return valuelist
def add(valuename: str, value: any, *, categorie: str = None):
  file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
  if path.isfile(file): raise ValueNotExist('Value does not exist')
  dump({'value': value}, open(file, 'x'), indent=2)
async def create(valuename: str, value: any, *, categorie: str = None):
  file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
  if path.isfile(file): raise ValueNotExist('Value does not exist')
  dump({'value': value}, open(file, 'x'), indent=2)
def edit(valuename: str, value: any = None, *, create: bool = False, categorie: str = None, add: int = None, minus: int = None, append: any = None, remove: any = None):
  file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
  if not path.isfile(file):
    if create is False: raise ValueNotExist('Value does not exist')
    if value is None: raise ValueError('Value is obligated except when add, minus, remove, append')
    return add(valuename, value) if categorie is None else add(valuename, value, categorie)
  if add is None and minus is None and append is None and remove is None:
    dump({'value': value}, open(file, 'w'), indent=2)
    return True
  fp = open(file, 'r+')
  dat: dict = load(fp); data: dict = {}
  if add != None:
    data['value']: int = dat['value'] + add
  elif minus != None:
    data['value']: int = dat['value'] - minus
  elif append != None:
    listqwe: list = dat['value']; listqwe.append(append); data['value'] = listqwe
  elif remove != None:
    listqwe: list = dat['value']; listqwe.remove(remove); data['value'] = listqwe
  dump(data, fp, indent=2)
  return True
async def replace(valuename: str, value: any = None, *, create: bool = False, categorie: str = None, add: int = None, minus: int = None, append: any = None, remove: any = None):
  file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
  if not path.isfile(file):
    if create is False: raise ValueNotExist('Value does not exist')
    if value is None: raise ValueError('Value is obligated except when add, minus, remove, append')
    return add(valuename, value) if categorie is None else add(valuename, value, categorie)
  if add is None and minus is None and append is None and remove is None:
    dump({'value': value}, open(file, 'w'), indent=2)
    return True
  fp = open(file, 'r+')
  dat: dict = load(fp); data: dict = {}
  if add != None:
    data['value']: int = dat['value'] + add
  elif minus != None:
    data['value']: int = dat['value'] - minus
  elif append != None:
    listqwe: list = dat['value']; listqwe.append(append); data['value'] = listqwe
  elif remove != None:
    listqwe: list = dat['value']; listqwe.remove(remove); data['value'] = listqwe
  dump(data, fp, indent=2)
  return True
def remove(valuename: str, *, cache: bool = False, categorie: str = None):
  if not '||' in valuename:
    file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
    if not path.isfile(file): raise ValueNotExist('Value does not exist')
    if cache is False:
      delet(file)
      return True
    value = get(valuename, categorie=categorie)
    delet(file)
    if path.isfile(file): delet(file)
    dump({'value': value}, open(f'{current_path}namedb/old/{valuename}.json', 'x'), indent=2)
    return True
  if cache is False:
    for valuenamee in valuename.split("||"):
      file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuenamee}.json'
      if not path.isfile(file): raise ValueNotExist('Value does not exist')
      delet(file)
    return True
  for valuenamee in valuename.split("||"):
    file: str = f'{current_path}namedb{"" if not categorie else f"/{categorie}"}/{valuenamee}.json'
    if not path.isfile(file): raise ValueNotExist('Value does not exist')
    delet(file)
    value = get(valuenamee, categorie=categorie)
    file: str = f'{current_path}namedb/old/{valuenamee}.json'
    if path.isfile(file):  delet(f'namedb/old/{valuenamee}.json')
    dump({'value': value}, open(file, 'x'))
  return True
async def delete(valuename: str, *, cache: bool = False, categorie: str = None):
  if not '||' in valuename:
    file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuename}.json'
    if not path.isfile(file): raise ValueNotExist('Value does not exist')
    if cache is False:
      delet(file)
      return True
    value = get(valuename, categorie=categorie)
    delet(file)
    if path.isfile(file): delet(file)
    dump({'value': value}, open(f'{current_path}namedb/old/{valuename}.json', 'x'), indent=2)
    return True
  if cache is False:
    for valuenamee in valuename.split("||"):
      file: str = f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}/{valuenamee}.json'
      if not path.isfile(file): raise ValueNotExist('Value does not exist')
      delet(file)
    return True
  for valuenamee in valuename.split("||"):
    file: str = f'{current_path}namedb{"" if not categorie else f"/{categorie}"}/{valuenamee}.json'
    if not path.isfile(file): raise ValueNotExist('Value does not exist')
    delet(file)
    value = get(valuenamee, categorie=categorie)
    file: str = f'{current_path}namedb/old/{valuenamee}.json'
    if path.isfile(file):  delet(f'namedb/old/{valuenamee}.json')
    dump({'value': value}, open(file, 'x'))
  return True
def searchcat(catname: str):
  pathe = path.join(f'{current_path}namedb/', catname)
  if path.isdir(pathe): return True
  return False
async def asearchcat(catname: str):
  pathe = path.join(f'{current_path}namedb/', catname)
  if path.isdir(pathe): return True
  return False
def createcat(catname: str):
  pathe = path.join(f'{current_path}namedb/', catname)
  if path.isdir(pathe): raise CategoryAlreadyExist('Category already exist')
  mkdir(pathe); return True
async def acreatecat(catname: str):
  pathe = path.join(f'{current_path}namedb/', catname)
  if path.isdir(pathe): raise CategoryAlreadyExist('Category already exist')
  mkdir(pathe); return True
def deletecat(catname: str):
  pathe = path.join(f'{current_path}namedb/', catname)
  if not path.isdir(pathe): raise CategoryDoesNotExist('Category doesn\'t exist')
  rmdir(pathe); return True
async def adeletecat(catname: str):
  pathe = path.join(f'{current_path}namedb/', catname)
  if not path.isdir(pathe): raise CategoryDoesNotExist('Category doesn\'t exist')
  rmdir(pathe); return True
def listcat(catname: str, type: str):
  qwe: list = []
  if type == 'name':
    for file in listdir(f'{current_path}namedb/{catname}'): qwe.append(file[: -5])
    return qwe
  elif type == 'name':
    for file in listdir(f'{current_path}namedb/{catname}'): data = load(open(f'{current_path}namedb/{catname}/{file}', 'r')); qwe.append(data['value'])
    return qwe
  raise ValueError('Not a valid type\nTypes : "name", "value"')
async def alistcat(catname: str, type: str):
  qwe: list = []
  if type == 'name':
    for file in listdir(f'{current_path}namedb/{catname}'): qwe.append(file[: -5])
    return qwe
  elif type == 'name':
    for file in listdir(f'{current_path}namedb/{catname}'): data = load(open(f'{current_path}namedb/{catname}/{file}', 'r')); qwe.append(data['value'])
    return qwe
  raise ValueError('Not a valid type\nTypes : "name", "value"')
def prefix(type: str, prefix: str, *, categorie: str = None):
  list: list = []
  if type == 'value':
    for file in listdir(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}'):
      if file.startswith(prefix):
        data: dict = load(open(f'{current_path}namedb/{"" if categorie is None else f"{categorie}/"}{file}', 'r')); list.append(data['value'])
    return list
  elif type == 'name':
    for file in listdir(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}'):
      if file.startswith(prefix):
        list.append(file[: -5])
    return list
  raise ValueError('Not a valid type\nTypes : "name", "value"')
async def aprefix(type: str, prefix: str, *, categorie: str = None):
  list: list = []
  if type == 'value':
    for file in listdir(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}'):
      if file.startswith(prefix):
        data: dict = load(open(f'{current_path}namedb/{"" if categorie is None else f"{categorie}/"}{file}', 'r')); list.append(data['value'])
    return list
  elif type == 'name':
    for file in listdir(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}'):
      if file.startswith(prefix):
        list.append(file[: -5])
    return list
  raise ValueError('Not a valid type\nTypes : "name", "value"')
def clearprefix(prefix: str, *, cache: bool = False, categorie: str = None):
  for file in listdir(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}'):
    if file.startswith(prefix): remove(file[: -5], cache=cache, categorie=categorie)
  return True
async def cleanprefix(prefix: str, *, cache: bool = False, categorie: str = None):
  for file in listdir(f'{current_path}namedb{"" if categorie is None else f"/{categorie}"}'):
    if file.startswith(prefix): remove(file[: -5], cache=cache, categorie=categorie)
  return True
def restore(valuename: str, *, categorie: str = None):
  file: str = f'{current_path}namedb/old/{valuename}.json'
  if not path.isfile(file): raise ValueNotExist('value does not exist')
  data: dict = load(open(file, 'r'))
  delet(file)
  add(valuename, data['value']) if not categorie else add(valuename, data['value'], categorie=categorie)
  return data['value']
async def arestore(valuename: str, *, categorie: str = None):
  file: str = f'{current_path}namedb/old/{valuename}.json'
  if not path.isfile(file): raise ValueNotExist('value does not exist')
  data: dict = load(open(file, 'r'))
  delet(file)
  add(valuename, data['value']) if not categorie else add(valuename, data['value'], categorie=categorie)
  return data['value']
def clearcache():
  for file in listdir(f'{current_path}namedb/old'): delet(f'{current_path}namedb/old/{file}')
  return True
async def cleancache():
  for file in listdir(f'{current_path}namedb/old'): delet(f'{current_path}namedb/old/{file}')
  return True
def transferjson(data: dict, *, categorie: str = None):
  for valuename in data: add(valuename, data[valuename], categorie=categorie)
  return True
async def atransferjson(data: dict, *, categorie: str = None):
  for valuename in data: add(valuename, data[valuename], categorie=categorie)
  return True
