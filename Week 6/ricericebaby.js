var acc, vel, xpos, ypos;
var mul= [];

function setup() 
{
  createCanvas(2000, 2000);
  background(0);
    // rice rice baby
}
      
  function draw() {
    background(0);
    for(i=0;i<mul.length;i++){
        mul[i].move();
        mul[i].displ();
            
 }
}
    
    function mouseDragged(){
    mul.push(new Flower(mouseX,mouseY));
     };
    
function Flower(x,y){
    this.x = x;
    this.y = y;
    this.speed = 1;
    this.diameter = random(5, 20);
        this.move = function() {
    this.x += random(-this.speed, this.speed);
    this.y += random(-this.speed, this.speed);
  };
   this.displ= function()
     {    
         // translate(50, 40);
  noStroke();
  for (var i = 0; i < 10; i ++) {
        fill(random(0,255),random(0,255),random(0,255));
    ellipse(this.x, this.y, 5, 20);
    rotate(PI/5);
        
       
 }
   }
     }
