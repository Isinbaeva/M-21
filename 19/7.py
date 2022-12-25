def same_by(characteristic, objects):
    a = filter(characteristic, objects)
    b = [elem for elem in a]
    if len(b) == len(objects):
        return True
    else:
        return False


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
