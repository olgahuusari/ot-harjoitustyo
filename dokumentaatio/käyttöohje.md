# Käyttöohje

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, lataa poetry riippuvuudet terminaalissa komennolla
```bash
poetry install
```
Tämän jälkeen ohjelman voi käynnistää komennolla
```bash
poetry run invoke start
```

## Ohjelman toiminta
Keskellä näyttöä on avaruusalus, jota voi pyörittää oikealla ja vasemmalla nuolinäppäimellä. Pelin tavoitteena on estää asteroidien osuminen alukseen. Tämä onnistuu välilyöntiä painamalla, jolloin alus ampuu laserin joka osuessaan asteroidiin tuhoaa sen.

Jokaisesta tuhotusta asteroidista saa pisteen. Kun pisteitä on kerääntynyt tarpeeksi, pääsee uudelle tasolle, jolloin pelin vauhti kiihtyy. 

Avaruusaluksia on useanlaisia, ja niitä pääse valitsemaan painamalla Ships-nappia näytöllä. Aluksi niitä on vain yksi, mutta päästessä uusille tasoille, niitä saa käyttöön enemmän.

Pelin saa keskeytettyä väliaikaisesti painamalla P-näppäintä.

Pelin saa tallennettua painamalla S-näppäintä, ja aiemmin tallennetun pelin saa ladattua painamalla näytöllä Load game -nappia.
