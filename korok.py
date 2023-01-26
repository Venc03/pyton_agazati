def elso_idos(kor):
    i = 0
    while i < len(kor):
        if i > 70:
            i = i + 1
    return i

def konzolra_ir():
    print(f"II/D, E:\n\tElső idős ember korának helye a listában: {elso_idos(i)}")

def masodik():
    kor = []
    i = 0
    while i < 5:
        evek = int(input("Kére adjon meg 5 kort [0,120]: "))
        kor.append(evek)
        i = i + 1

    i = 1

    print(f"II/A, B, C: \n\t{kor[0]}", end="")

    while i < len(kor):
        print(f" :\n\t{kor[i]}", end="")
        i += 1

    print(f"II/D, E:\n\tElső idős ember korának helye a listában: {elso_idos(i)}")


    elso_idos(kor)
    konzolra_ir()