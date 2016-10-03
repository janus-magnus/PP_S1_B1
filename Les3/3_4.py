
password = 'DesuDesuDesuDesuDesuDesuDesuDesuDesuDesuDesuDesuDesu'
nums = [0,1,2,3,4,5,6,7,8,9]

def new_pass(oldPass, newPass):
    if oldPass == password:
        if oldPass != newPass:
            if len(newPass) >= 6:
                if any(char.isdigit() for char in newPass):#controleert of newPass een getal bevat
                    return True
                return 'je wachtword bevat geen cijfer'
            return 'je wachtword is niet lang genoeg'
        return 'je wachtword mag niet gelijk zijn aan het oude wachtwoord'
    return 'het ingevoerde wachtword komt niet overeen met het huidige wachtwoord'


oldPassIn = input('voer je oude wachtwoord in: ')
print('je wachtwoord moet minstend 6 charcters lang zijn en minimaal in cijfer bevaten')
newPassIn = input('voer je nieuwe wachtwoord in: ')



if new_pass(oldPassIn,newPassIn) == True:
    password=newPassIn
else:
    print(new_pass(oldPassIn, newPassIn))

print(password)
