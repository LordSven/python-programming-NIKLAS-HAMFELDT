# uppgift 1
tal = input('Välj ett tal: ')
if float(tal) == 0:
    print('Ditt tal är 0.')
elif float(tal) < 0:
    print('Ditt tal är negativt.')
else:
    print('Ditt tal är positivt.')
# alternativt
tal = input('Välj ett tal: ')
if float(tal) == 0:
    print(f'Talet {tal} som du valde är 0.')
elif float(tal) < 0:
    print(f'Talet {tal} som du valde är negativt.')
else:
    print(f'Talet {tal} som du valde är positivt.')

# uppgift 2
tal1 = input('Välj ett tal: ')
tal2 = input('Välj ett till tal: ')
if float(tal1) > float(tal2):
    print(f'Det andra talet {tal2} du valde är mindre än det första talet {tal1}.')
elif float(tal1) < float(tal2):
    print(f'Det första talet {tal1} du valde är mindre än det andra talet {tal2}.')
else:
    print(f'Talen {tal1} och {tal2} du valde är samma tal.')

# uppgift 3
print('Välj tre vinklar i en triangel.')
v1 = float(input('Vinkel 1: '))
v2 = float(input('Vinkel 2: '))
v3 = float(input('Vinkel 3: '))
if sum([v1, v2, v3]) != 180:
    print('Summan av de tre vinklarna i en triangel måste bli 180, annars är det inte en triangel. Vänligen försök igen.')
    v1 = input('Vinkel 1: ')
    v2 = input('Vinkel 2: ')
    v3 = input('Vinkel 3: ')
    if v1 == 90 or v2 == 90 or v3 == 90:
        print('Det är en rätvinklig triangel.')
    else:
        print('Det är inte en rätvinklig triangel.')  
elif v1 == 90 or v2 == 90 or v3 == 90:
        print('Det är en rätvinklig triangel.')
else:
        print('Det är inte en rätvinklig triangel.')

# uppgift 4
å = input('Hur gammal är patienten? ')
v = input('Hur mycket väger patienten? ')
if float(å) > 12 and float(v) > 40:
    print('Patienten ska ta 1-2 piller om dagen.')
elif float(å) >= 7 < 12 and float(v) >= 26 < 40:
    print('Patienten ska ta 0,5-1 piller om dagen.')
elif float(å) >= 3 < 7 and float(v) >= 15 < 26:
    print('Patienten ska ta 0,5 piller om dagen.')
else:
    print('Patienten bör uppsöka läkare snarast möjligt.')

# uppgift 5
nummer = float(input('Välj en siffra: '))
if nummer % 2 != 0 or nummer % 5 == 0:
    if nummer % 5 == 0:
        if nummer % 2 != 0 and nummer % 5 == 0:
            print('Siffran är ojämn och kan delas med 5.')
        else:
            print('Siffran är jämn och kan delas med 5.')
    else:
        print('Siffran är ojämn och kan inte delas med 5.')
else:
    print('Siffran är jämn och kan inte delas med 5.')

# uppgift 6
vi = float(input('Hur mycket väger bagaget i kg? '))
if vi > 8:
    print('Bagaget är för tungt.')
else:
    lä = float(input('Hur långt är bagaget i cm? '))
    if lä > 55:
        print('Bagaget är för långt.')
    else:
        br = float(input('Hur brett är bagaget i cm? '))
        if br > 40 < 55 and lä < 40:
            print('Bagaget är för brett, men du kan ju bara vrida på bagaget dumfan.')
            dj = float(input('Hur djupt är bagaget i cm? '))
            if dj > 23:
                print('Bagaget är för tjockt.')
            else:
                print('Bagaget faller inom ramen för tillåten vikt och tillåtna dimensioner förutsatt att du lägger det ned.')
        elif br > 40:
            print('Bagaget är för brett.')
        else:
            dj = float(input('Hur djupt är bagaget i cm? '))
            if dj > 23:
                print('Bagaget är för tjockt.')
            else:
                print('Bagaget faller inom ramen för tillåtna dimensioner och tillåten vikt.')