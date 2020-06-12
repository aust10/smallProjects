// var lat1 = 45.5289;
// var lon1 = -122.4582;
// var lat2 = 45.615849;
// var lon2 = -122.4932303;

// var y = Math.sin(lon2-lon1) * Math.cos(lat2);
// var x = Math.cos(lat1)*Math.sin(lat2) - Math.sin(lat1)*Math.cos(lat2)*Math.cos(lon2-lon1);
// var brng = Math.atan2(y, x);
// var deg = brng * (180 / Math.PI)
// console.log(deg, "this is brng")

// heading = (231 + brng) % 360;

// console.log(heading, "this is heading")
// the above text is a test that i was running.

// this is const because we are never re asigning it 
const canvas = document.getElementById('canvas');
let go = document.getElementById("go");
let stopit = document.getElementById('stop');
// this is the way canvas works thats why it is what it is 
const ctx = canvas.getContext('2d');

//grid resolution makes the boxes smaller
const GRID_RESOLUTION = 50
const CELL_SIZE = canvas.width / GRID_RESOLUTION
//the interval will make it go slower if you increase and faster if you lower the number
const INTERVAL = 100
// this is the fill color of the box
// ctx.fillStyle = `rgb(0,0,0)`
// this fillRect is how big it will be with x y and w h
// ctx.fillRect(10,10,10,10)
function run() {

    function getRandomCoord(){
        return Math.round(Math.random() * GRID_RESOLUTION)
    }
    
    const animals = []
    // below is the animal green
    for (let i = 0; i < 200; i++) {
        animals.push(new Animal(getRandomCoord(), getRandomCoord()))
    }
    // the one below is the preditor red
    for (let i = 0; i < 50; i++) {
        animals.push(new Preditor(getRandomCoord(), getRandomCoord()))
    }
    
    
    function draw(animals){
        ctx.clearRect(0,0, canvas.width, canvas.height)
        animals.forEach(function(animal) {
            ctx.fillStyle = `rgb(${animal.color.r}, ${animal.color.g}, ${animal.color.b})`
            ctx.fillRect(animal.x*CELL_SIZE, animal.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        })
    }
    
    // the below sets how fast it pops up it is like the speed at witch it moves
    const interval = setInterval(function(){
        draw(animals)
    
        animals.forEach(function(animal){
            animal.move(animals)
        })
    
    }, INTERVAL)
}

go.addEventListener('click', run);

