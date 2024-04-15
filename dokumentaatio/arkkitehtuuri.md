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
    Game "1" -- "1" SpaceShip
    Game "1" -- "0..1000" Laser
    Game "1" --"1" Events

```