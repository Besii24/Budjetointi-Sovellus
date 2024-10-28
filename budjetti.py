vuokra = int(input("Vuokra: "))
valuutukset = int(input("Vakuutukset: "))
kouluruokailu = int(input("Kouluruokailu: "))
sähkö = int(input("Sähkö: "))
liikkuminen = int(input("Liikkuminen: "))
uusiN = input("Anna uusi kuluerän nimi: ")
uusiS = int(input("Anna siihen budjetoitu summa: "))

while True:
    muokkaus = input('Jos haluat muokata jotain budjettikohdetta, kirjoita "1". Jos haluat mennä eteenpäin kirjoita "0".')
    if muokkaus == 0:
        break
    elif muokkaus == 1:
        valitse = input("Kirjoita budjettikohde, jota haluat muokata: ")
        
        

sk = {"vuokra": vuokra,
"valuutukset": valuutukset,
"kouluruokailu": kouluruokailu,
"sähkö": sähkö, 
"liikkuminen": liikkuminen,
uusiN: uusiS}

print(sk)
