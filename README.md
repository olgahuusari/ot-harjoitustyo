# Asteroidit
Asteroidit on peli, jossa pelaaja ohjaa näytön keskellä olevaa avaruusalusta ja ampuu sitä kohti lentäviä asteroideja. Avaruusalus pyörii nuolinäppäimiä painamalla ja ampuu lasereita välilyöntiä painamalla. Pelin häviää, jos asteroidi osuu alukseen. 

[Release 1](https://github.com/olgahuusari/ot-harjoitustyo/releases/tag/viikko5)


### Dokumentaatio
[vaatimusmäärittely](https://github.com/olgahuusari/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/olgahuusari/ot-harjoitustyo/tree/main/dokumentaatio/työaikakirjanpito.md)

[changelog](https://github.com/olgahuusari/ot-harjoitustyo/tree/main/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/olgahuusari/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

### Asennus
Asenna riippuvuudet komennolla
```bash
poetry install
```

Käynnistä peli komennolla
```bash
poetry run invoke start
```

### Komentorivitoiminnot
#### Ohjelman suorittaminen
Pelin voi käynnistää komennolla
```bash
poetry run invoke start
```

#### Testaus
Testit voi suorittaa komennolla
```bash
poetry run invoke test
```

#### Testikattavuus
Testikattavuusraportin saa komennolla
```bash
poetry run invoke coverage-report
```

#### Pylint
Tiedoston pylint.rc määrittelemät tarkistukset voi suorittaa komennolla
```bash
poetry run invoke lint
```


