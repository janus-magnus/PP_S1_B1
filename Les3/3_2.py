gList = [1, 0, 58 , 69 ,87 ,-99]test

def f(getallenLijst):
    if type(getallenLijst) == list:
        getal = 0

        for i in range(len(getallenLijst)):
            getal+= getallenLijst[i]
          #  print(getal)
    return getal

print(f(gList))