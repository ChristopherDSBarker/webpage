/* christopher Barker
 Professor Martin Hock
 CS 120
 elli assignment */

/* this code is a catipillar that goes to the right and then eventually diagnal. 
 The catipillar also changes color to a lighter color using the blue value of RGB*/

int faceSum = 20; //for the face made to move 20 each time
int forElliY = 100;  //initialized for Y arrary
color blueValue = 200; //color set variable for blue value of RGB
color redValue = 50;
color greenValue = 50;
int sum = 20; // adding 20 each time for the array and circle
int [] elliY = new int [7]; // step 3 setting an array size of 100
int[] elliX = new int [7]; // given
color [] c = new color[7]; //for the color array
color [] f = new color[7]; //attempt for color change for face


void setup() {
  size(500, 500); //canvas size
  frameRate(8); //frame rate to 8
  for (int i=0; i < 7; i++) { // for loop, same size as all arrays, setup for sum and y cord for elli
    elliX[i] = sum;   // set elliX array to sum 
    elliY[i] = forElliY; //set elliY array to forElliY which is for the Y direction
    c[i] = color(redValue, greenValue, blueValue); //prof note: "color();"
    f[i] = color(255, 0, 0);
    sum = sum + 20; //sum adds 20 each time
  }
}

void elli() { //the figure elli the catipillar
  for (int i=0; i < 7; i++) { //for loop for the actual circle body of the catipillar
    //set the color index to i

    fill(c[i]); //fill the ellipse 

    c[i] = color(50, 50, blueValue - 50);
    blueValue = blueValue - 2;
    ellipse(elliX[i], elliY[i], 40, 40);
  }
}


void draw() {
  background(0); //background to black
  elli(); //calls the elli method to draw 
  for (int i=0; i < 6; i++) { 
    elliX[i] = elliX[i+1];     // put this inside a loop
    elliY[i] = elliY[i+1];
  }
  elliX[6] = elliX[6] + 20;  //this apart of the last index
  elliY[6] = elliY[6] +20;
  elliFace();
}

void elliFace() {


  for (int i=0; i < 7; i++) {
    fill(f[i]);
    rect(elliX[6]-15, elliY[6]-30, 10, 10); //right eye
    rect(elliX[6]-30, elliY[6]-30, 10, 10); //left eye
    ellipse(elliX[6]-15, elliY[6]-10, 10, 10); // mouth
  }
}
