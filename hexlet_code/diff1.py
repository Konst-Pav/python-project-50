file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

file2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}


def diff():
    all_keys = set()
    all_keys.update(file1.keys())
    all_keys.update(file2.keys())
    all_keys = list(all_keys)
    all_keys.sort()
    for key in all_keys:
        print(compare(key, file1, file2))


def compare(key, file1, file2):
    x = file1.get(key)
    y = file2.get(key)
    if (x is not None) and (y is None):
        return f'- {key}: {x}'
    if (x is None) and (y is not None):
        return f'+ {key}: {y}'
    if x == y:
        return f'  {key}: {x}'
    if x != y:
        return f'- {key}: {x}\n+ {key}: {y}'


diff()
