def handvalue(lista):
    
    count = 0
    flags = []
    values = []
    for x in lista:
        values.append(x.hival())
    while sum(values) > 21 and 11 in values:
        #values.sort()
        index = values.index(11)
        values[index] = 1

    
    return int(sum(values))

import card
x = card.card('two','spades')
