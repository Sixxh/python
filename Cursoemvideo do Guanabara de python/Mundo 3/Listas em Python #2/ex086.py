col1 = [[[], [], []], [[], [], []], [[], [], []]]
c = 0
while True:
    for c, l in enumerate(col1[c]):
        col1[0][c].append(int(input(f'Digite um valor para {c}: ')))
    for c, l in enumerate(col1[c]):
        col1[1][c].append(int(input(f'Digite um valor para {c}: ')))
    for c, l in enumerate(col1[c]):
        col1[2][c].append(int(input(f'Digite um valor para {c}: ')))   
    print(col1[0])
    print(col1[1])
    print(col1[2])
    break