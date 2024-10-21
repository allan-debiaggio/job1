def rectangle (height,width) :
    for j in range(1,3) :
        print("|" + "-" * (width-2) + "|")
        if j < 2 :
            for i in range(1, height-1) :
                print("|" + " " * (width-2) + "|")
        else :
            break

h = int(input("Give me a number for height : "))
w = int(input("Give me a number for width : "))

rectangle(h,w)