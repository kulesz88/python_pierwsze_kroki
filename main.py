#imie = 'Mateusz'
#marka_samochodu = 'Fiat'
#silnik = '1.4 benzyna'
#ilosc_drzwi = 5
#pojemnosc = 1.3
#
#print('Witaj swiecie ' + imie + '!')
#print('Twoje auto to ' + marka_samochodu + ' ma ' + str(ilosc_drzwi) + ' drzwi')
#print('Silnik to ' + silnik)
#print(marka_samochodu.upper())
#print(('Witaj swiecie ' + imie + '!').lower())
#print(silnik.capitalize())
#print(pojemnosc*2)

#imie_psa = 'Rex'
#waga_psa = 50.6
#kolor_psa = 'czarny'

#print(imie + ' ma psa o imieniu ' + imie_psa + ' ktory wazy ' + str(waga_psa))
#print("Kolor psa to " + kolor_psa)

#rowery = ['romet', 'unibike', 'accent']
#ilosc = [5, 6, 14]

#for il in ilosc:
#    print(il)

#print("Dlugosc: {0}".format(len(rowery)))

#for idx in range(len(rowery) ) :
#    print( "idx: " + str(idx) + ": " + rowery[idx])
#    print(rowery[idx] + " jest na stanie " + str(ilosc[idx]) + " sztuk")

#rower = {'marka': "romet",
#         'model': "gazela",
#         'waga': 10}
#
#print(rower['marka'])
#
#for key, value in rower.iteritems():
#    print("{0}:{1}".format(key, value))
#
#for key in rower:
#    print("{0}:{1}".format(key, rower[key]))

#Funkcja

def print_dict(d):
    for key, value in d.iteritems():
        print("{0}:{1}".format(key, value))

if __name__ == "__main__":
    rower = {'marka': "romet",
             'model': "gazela",
             'waga': 10}

print_dict(rower)
print_dict(rower)
print_dict(rower)
