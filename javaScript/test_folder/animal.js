class Animal {
    // the x and the y are postions 
    constructor(x,y) {
        this.x = x
        this.y = y
        this.color = {
            r: 0,
            g: 255,
            b: 0
        }
    }

    move() {
        const directions = [-1, 0, 1]

        const randomIndexX = Math.round(Math.random() * 2)
        const randomIndexY = Math.round(Math.random() * 2)

        function wrapCoord(n) {
            // is n less than 0 if that is true wrap it with gridresulion -
            // otherwise is : is n grater than gridresulion then wrap to 0
            // otherwise it is not either and it just equals n
            return n < 0 ? GRID_RESOLUTION-1 : n > GRID_RESOLUTION ? 0 : n
        }
        // this makes it so it will not wrap off the end it will bring it back around
        this.x = wrapCoord(this.x +directions[randomIndexX])
        this.y = wrapCoord(this.y +directions[randomIndexY])
    }
}

class Preditor extends Animal {
    constructor(x,y) {
        super(x,y)
        this.color = {
            r: 255,
            g: 0,
            b: 0
        }
    }
    move(animals) {
        super.move()

        animals.forEach(function(animal, i) {
            // && is saying and 
            if(animal && animal.constructor.name !== Preditor.name){
                if (this.x === animal.x && this.y === animal.y) {
                    animals.splice(i, 1)
                }
            }
        }.bind(this))
    }
}