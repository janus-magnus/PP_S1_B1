studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for stu in studentencijfers:
        antw.append(sum(stu)/len(stu))
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    secList = []
    for stu in studentencijfers:
        for c in stu:
            secList.append(c)
    antw = sum(secList)/len(secList)
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
