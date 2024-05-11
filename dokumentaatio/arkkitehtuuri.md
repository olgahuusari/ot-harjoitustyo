# Arkkitehtuuri

## Koodin rakenne
Pelin koodi koostuu moduuleista ja luokista eri toiminnoille. Alla oleva luokkakaavio havainnollistaa moduulien välisiä yhteyksiä. Game-moduuli pyörittää peliä, ja kutsuu tarvittaessa muita moduuleja. Spaceship, Asteroid ja Laser luokat luovat ja käsittelevät ruudulla näytettäviä kuvakkeita. Events-luokka käy läpi pelissä tapahtuvat toiminnot ja niiden perusteella moduulit Game ja UI muuttavat pelin kulkua. UI moduuli on vastuussa käyttöliittymästä. Sen kautta myös luodaan asteroidit ja tarkastetaan, onko laser osunut asteroidiin, tai asteroidi avaruusalukseen Collide-luokan avulla. Kaikkia attribuutteja ei ole joissain luokissa merkitty kaavioon selkeyden vuoksi

## Luokkakaavio

```mermaid
    classDiagram
    class Game{
        clock
        tick
    }
    class SpaceShip{
        image
        rect
        degree
        x, y
    }
    class Laser{
        image
        degree
        x, y
    }
    class Events{
        rotate
        quit
        laser
        instructions
        game_over
        pause
        button
        event_pos
        save
    }
    class UI{
        window
        lasers
        asteroids
        ships
        font
        game_over
        points
        level
        choose_ship
    }
    class Asteroid{
        image
        degree
        x, y
        direction
    }
    class Collide{
        laser_asteroid
        asteroid_ship
    }
    class Repository{
        file path
        loaded file
    }
    class SaveFile{
        score
        level
        ship
        tick
    }

    UI "1" -- "1" Collide
    Game "1" -- "1" SpaceShip
    Game "1" -- "0..1000" Laser
    Game "1" --"1" Events
    UI "1" --"0..100" Asteroid
    Game "1" --"1" UI
    Game "1" --"1" Repository
    Repository "1" --"1" SaveFile
    Game "1" --".." SaveFile

```
## Sekvenssikaavio pelisilmukasta
Alla sekvenssikaavio, joka näyttää pelisilmukan toiminnan yhden silmukan aikana. Kaavio on yksinkertaistettu havainnollisuuden parantamiseksi, eli funktioiden tulokset tai attribuutit on valittu niin, että silmukka olisi mahdollisimman yksinkertainen.

```mermaid
sequenceDiagram
    actor User
    participant Game
    participant UI
    participant Collide
    participant Laser
    participant Asteroid
    participant Events
    participant SpaceShip
    User ->> Game : game_loop()
    Game ->> UI : setup()
    activate UI
    UI ->> UI : get_asteroids([], 10)
    UI ->> UI : get_ships()
    UI -->> Game : 
    deactivate UI
    Game ->> Events : event_handler(event)
    Game ->> Game : examine_event_module()
    Game ->> Events : quit, rotate_l, rotate_r, laser, instructions, button
    activate Events
    Events -->> Game : everything False
    deactivate Events
    Game ->> UI : choose_ship
    activate UI
    UI -->> Game : 1
    deactivate UI
    Game ->> SpaceShip : get_img(1)
    Game ->> UI : draw_window(spaceship)
    activate UI
    UI ->> UI : window.fill((0, 0, 0))
    UI ->> UI : window.blit(points)
    UI ->> UI : window.blit(level)
    UI ->> UI : window.blit(pause_text)
    UI ->> UI : window.blit(ship_text)
    UI ->> UI : examine_attributes()
    UI ->> UI : examine_lasers()
    UI ->> Collide : laser_hit_asteroid(laser, asteroid)
    UI ->> Collide : laser_asteroid
    deactivate UI
    activate Collide
    Collide -->> UI : False
    deactivate Collide
    activate UI
    UI ->> Laser : move()
    UI ->> SpaceShip : rotate()
    UI ->> UI : window.blit(spaceship)
    UI ->> UI : examine_asteroids(spaceship)
    UI ->> Collide : asteroid_hit_ship(asteroid, spaceship)
    UI ->> Collide : asteroid_ship
    deactivate UI
    activate Collide
    Collide ->> UI : False
    deactivate Collide
    activate UI
    UI ->> Asteroid : move()
    UI -->> Game : 
    deactivate UI
    Game ->> Game : pygame.display.flip()
    Game ->> Game : clock.tick(tick)
```

## Sekvenssikaavio laserin osumisesta asteroidiin
Tarkempi kuvaus oikeilla arvoilla siitä, miten peli laskee laserin osumisen asteroidiin, ja miten se toimii sen jälkeen. 

```mermaid
sequenceDiagram
    participant Game
    participant UI
    participant Collide
    participant Laser
    participant Asteroid
    Game ->> UI : draw.window(spaceship)
    UI ->> Laser : laser in lasers
    UI ->> Asteroid : asteroid in asteroids
    UI ->> Collide : asteroid_hit_ship(laser, asteroid)
    activate Collide
    Collide ->> Asteroid : x
    Asteroid -->> Collide : 233.11
    Collide ->> Laser : img.get_width()
    Laser -->> Collide : 10
    Collide ->> Laser : x
    Laser -->> Collide : 260.15
    Collide ->> Asteroid : img.get_width()
    Asteroid -->> Collide : 30
    Collide ->> Asteroid : y
    Asteroid -->> Collide : 62.85
    Collide ->> Laser : img.get_height()
    Laser -->> Collide : 18
    Collide ->> Laser : y
    Laser -->> Collide : 81.93
    Collide ->> Asteroid : img.get_height()
    Asteroid -->> Collide : 20
    Collide ->> Collide : laser_asteroid = True
    deactivate Collide
    Collide -->> UI : 
    UI ->> Collide : laser_asteroid
    activate UI
    Collide -->> UI : True
    deactivate UI
    UI ->> UI : points +=1
    UI ->> Collide : laser_asteroid = False
    UI ->> UI : asteroids.remove(asteroid)
    UI ->> Asteroid : new_asteroid
    UI ->> UI : asteroids.append(new_asteroid)
    UI ->> UI : lasers.remove(laser)
    
    
    


