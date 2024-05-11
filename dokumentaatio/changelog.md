## Viikko 3
- Lisätty luokka "Game", joka käynnistää pelin ja pyörittää sitä
- Lisätty luokka "SpaceShip", jossa avaruusalukselle määritetään parametrit
- Käyttäjä voi avata peli-ikkunan
- Käyttäjä voi pyörittää avaruusalusta nuolinäppäimillä

## Viikko 4
- Lisätty luokat Laser, Asteroid, UI ja Events
- Laserit lähtevät liikkumaan ruudulla samaan suuntaan kuin mihin avaruusalus osoittaa ja niitä voi ampua välilyöntiä painamalla
- Asteroidit liikkuvat ruudun reunoilta ruudun keskipistettä kohti
- Testejä lisätty

## Viikko 5 
- Lisätty luokka Collide, joka laskee osuuko laser asteroidiin tai asteroidi alukseen
- Lisätty luokka Level, joka on vielä vähän vaiheessa, nimi saattaa muuttua. Tällä hetkellä se luo listan asteroideja
- Laserin osuessa asteroidiin molemmat häviävät ruudulta ja pelaaja saa yhden pisteen
- Asteroidin osuessa alukseen pelin häviää, minkä jälkeen voi aloittaa uuden pelin
- Testien haarautumakattavuutta nostettu

## Viikko 6
- Poistettu luokka Level, koska se tuntui turhalta
- Pelissä voi nyt päästä eri tasoille, kun saa tarpeeksi pisteitä. Viitostasolle asti uudelle tasolle päästessä käytettäväksi saa eri näköisen avaruusaluksen. Lisäksi pelin vauhti kiihtyy.
- Pelin voi pistää pauselle
- Docstring-dokumentaatio lisätty koodiin

## Viikko 7
- Uutta toiminnallisuutta: käyttäjä voi tallentaa pelin, ja tallennettu data ladataan, kun peli aukaistaan seuraavan kerran, tai jos pelin häviää
- Tallennusta varten uudet luokat Repository ja SaveFile
- Testejä lisätty

