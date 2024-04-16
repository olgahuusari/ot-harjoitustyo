```mermaid
    classDiagram
    class Game{
        window
        lasers
    }
    class SpaceShip{
        image
        rect
        degree
    }
    class Laser{
        image
        degree
        x
        y
    }
    class Events{
        rotate_r
        rotate_l
        quit
        laser
    }
    class UI{
        window
        lasers
        asteroids
        font
        instructions
    }
    class Asteroid{
        image
        degree
        x
        y
    }
    Game "1" -- "1" SpaceShip
    Game "1" -- "0..1000" Laser
    Game "1" --"1" Events
    Game "1" --"10" Asteroid
    Game "1" --"1" UI

```
