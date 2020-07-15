## Laboratorium nr 7

1. Zaimplementuj algorytm wyszukiwania wyrażeń regularnych. Wyrażenie może zawierać:
    - litery, cyfry i spacje - traktować literalnie (sine qua non)
    - kropki - reprezentuje dowolny znak (1 pkt)
    - operatory: gwiazdkę - 0 lub więcej powtórzeń poprzedniego symbolu, plus - 1 lub więcej powtórzeń, pytajnik - 0 lub 1 powtórzenie (1.5 pkt)
    - nawiasy - na potrzeby operatorów gwiazdki, plusa i pytajnika zawartość nawiasów jest pojedynczym symbolem; nawiasy mogą być zagnieżdżone; nawiasy po których nie występuje żaden z wymienionych operatorów nie mają skutku (1 pkt)
    - klasy znaków (albo dowolna liczba znaków wymieniona w nawiasach kwadratowych, albo oznaczenie klasy, typu \d) (1.5 pkt)

Możesz założyć, że wprowadzone wyrażenie jest poprawne.

Sugerowany algorytm: automat skończony.   
Nie można używać modułów re/regex lub im podobnych.

