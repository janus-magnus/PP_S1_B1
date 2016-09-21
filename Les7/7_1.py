def calc(aantalPers):
    costPP = 0
    try:
        if aantalPers >= 0:

                costPP = 4356 / aantalPers

        else:
            print('Het aantal persoonen mag niet negatief zijn')

    except ZeroDivisionError:
        print('delen door 0 niet toegenstaan')

    except TypeError:
        print('gebruik alleen cijfers')

    except:
        print('Incorecte invoer')
    print(costPP)


calc(0)
calc(6)
calc(-10)
calc('zeven')
