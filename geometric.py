if __name__ == "__main__" :
    a = float(input("Enter first term of GP \n"))
    r = float(input("Enter common ratio of GP \n"))
    i = 1
    print(a)
    print("\n")
    while i < 10 :
        a = a * r
        print(a)
        print("\n")
        i = i + 1
