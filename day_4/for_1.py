beers = range(99, 0, -1)
#message = '{} beczek piwa na półce stało, jedna spadła {} zostało'
#message = '{beers_before} beczek piwa na półce stało, jedna spadła {beers_after} zostało'
message = '{beers_before} beczek piwa na półce stało, jedna spadła {beers_after} zostało'

for beer in beers:
    #print(message.format(beer, beer - 1))
    #print(message.format(beers_before = beer, beers_after = beer - 1))
    #print(message.format(beers_before = beer, beers_after = beer - 1))
    print(f'{beer} beczek piwa na półce stało, jedna spadła {beer - 1} zostało')