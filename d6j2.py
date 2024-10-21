def triangle(a) :
    for i in range(1,a+1) :
        if i < a :
            print(" " * (a+1-(i)) + "/" + " "*((i-1)*2) + "\\")
        else :
            print(" " * (a+1-(i)) + "/" + "_"*((i-1)*2) + "\\")

hauteur = int(input("Give me a number : "))

triangle(hauteur)