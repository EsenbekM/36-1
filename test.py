

def sum(a, b):
    return a + b


dct = {
    'a': 1,
    'b': 2,
}

print(sum(**dct))  # sum(a=1, b=2)