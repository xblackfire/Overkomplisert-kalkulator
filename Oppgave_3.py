print("""Velkommen til min mini kalkulator! \n""")
def multiplikasjon(x,y):
    return x * y
def divisjon(x,y):
    return x / y
def  summasjon(x,y):
    return x+y
def subtraksjon(x,y):
    return x-y
def modulo(x,y):
    return x%y
def opphøye(x,y):
    return x**y
def nedrunning(x,y):
    return x//y
#I linje 2-15 definerer jeg de ulike aritmetiske operatorene.

tall_1 = float(input("Oppgi et hvilket som helst tall: "))
tall_2 = float(input("Oppgi enda et hvilket som helst tall: "))
#I linje 18-19 ber jeg brukeren oppgi to tall, og jeg lagrer de oppgitte tallene i to variabler: tall_1 og tall_2

aritmetiske_operatorer = input(f''' 
skriv '1' hvis du vil multiplisere (*) tallene
skriv '2' hvis du vil dele (/) tallene
skriv '3' hvis du vil summere (+) tallene
skriv '4' hvis du vil subtrahere (-) tallene
skriv '5' hvis du vil finne resten (%) av tallene
skriv '6' hvis du vil opphøye {tall_1} i {tall_2}
skriv '7' hvis du vil dele tallene med nedrunding 
: ''')
#Jeg lager enda en ny input, der brukeren velger hvilken aritmetisk operator som skal bli brukt på tallene.

if aritmetiske_operatorer == '1':
    print(f"{tall_1} * {tall_2} = {multiplikasjon(tall_1,tall_2)}")

elif aritmetiske_operatorer == '2':
    print(f"{tall_1}/{tall_2} = {divisjon(tall_1,tall_2)}")

elif aritmetiske_operatorer == '3':
    print(f"{tall_1} + {tall_2} = {summasjon(tall_1,tall_2)}")

elif aritmetiske_operatorer == '4':
    print(f"{tall_1} - {tall_2} = {subtraksjon(tall_1,tall_2)}")

elif aritmetiske_operatorer == '5':
    print(f"{tall_1} % {tall_2} = {modulo(tall_1,tall_2)}")

elif aritmetiske_operatorer == '6':
    print(f"{tall_1}^{tall_2} = {opphøye(tall_1,tall_2)} ")

elif aritmetiske_operatorer == '7':
    print(f"{tall_1}//{tall_2} = {nedrunning(tall_1,tall_2)}")
else:
    print("Feil input. Kjør koden på nytt! ")
#I linje 33-52 har jeg brukt de aritmetiske operatorene jeg definerte i starten.
#Jeg bruker også if, elif og else for å

