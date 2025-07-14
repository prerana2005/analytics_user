# complex FUNc
def risky_math(x, y, z):
    if x > 10:
        if y < 5:
            print("Case A")
        elif y > 100:
            if z % 2 == 0:
                print("Case B")
            else:
                if x + y > z:
                    print("Case C")
                else:
                    print("Case D")
        else:
            for i in range(10):
                if i % 3 == 0:
                    print(i)
    elif x < 0:
        print("Negative X")
        if x == -1:
            print("Special case -1")
        elif x == -100:
            print("Special case -100")
        else:
            print("Generic negative")
    else:
        print("Neutral")
