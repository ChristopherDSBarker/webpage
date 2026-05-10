// Christopher Barker
//Xavier
//Class: CS 120, 9:30 
//Instructor: Prof. Martin Hock
//Creative assignment

//Draw shapes at random points across screen

int shapeCount = 10; 
float[] x = new float[shapeCount]; // arrary for the x cord, using the same size as array shapeCount
float[] y = new float[shapeCount];  // arrary for the x cord, using the same size as array shapeCount
color[] c = new color[shapeCount];  // arrary for the x cord, using the same size as array shapeCount
int[] shapeType = new int[shapeCount];//helps to keep everything alligned, bassic array to determine shape type
int shapeSize = 75; //Shape size to make them controlled and easy to change



void setup() {
  size (500, 500); //size of the canvas
  keyPressed(); //keyPressed method to make the shapes start with multiple shapes instead of just the one
}

void draw() {
  background(0); //color to black
  // if there is a moving shape, move it
  if (movingShape >= 0) { //if statement for moving shape check
    // Move x and y coordinates of moving shape
    x[movingShape] += mouseX - pmouseX; // x array for moving by mouse
    y[movingShape] += mouseY - pmouseY; // y arrary for moving by mouse
     vibratingShape();
  }


  shapeTime();
  
 // vibratingShape();
}

void shapeTime() {
  for (int i=0; i<shapeCount; i++) {  //for loop to change shapes 


    float topPointY = y[i];
    float topPointX = x[i]; //random points that become set every time we run through them
    fill(c[i]); //set color related to an array for color
    if (shapeType[i] == 0) { // if statement related to the number 0 change to ellipse
      ellipse(topPointX, topPointY, shapeSize, shapeSize);
    } else if (shapeType[i] == 1) {
      triangle(topPointX, topPointY, topPointX-(shapeSize/2), topPointY+shapeSize, topPointX+(shapeSize/2), topPointY+shapeSize); // if statement for triangles related to number 1
    } else if (shapeType[i] == 2) {
      rect(topPointX, topPointY, shapeSize, shapeSize); //if statement for rect associated with number 2
    } else if (shapeType[i] == 3) {
    }
    //y[i] = y[i] + random(-1, 1); // shape moves a little...
    //x[i] = x[i] + random(-1, 1);
  }
}


void keyPressed() { //method for pressing a key
  background(0); //refesh the background to black again


  for (int i=0; i<shapeCount; i++) { //for loop for array for x, y and color
    y[i] = random(height);
    x[i] = random(width);
    c[i] = color(random(255), random(255), random(255));
    if (shapeType[i] == 0) {
      shapeType[i] = 1; //if statements to change the number in array to another variable for shapes
    } else if (shapeType[i] == 1) {
      shapeType[i] = 2;
    } else if (shapeType[i] == 2) {
      shapeType[i] = 0;
    }
  }
}

void mouseClicked() {
  int pixel= get(mouseX, mouseY); // ability to mouse click on location and obtain the pixel at that point
  for (int i = 0; i < shapeCount; i++) {
    if (pixel == c[i]) { //for loop to store the color of the pixel inside the color array
      // we clicked on shape i

      y[i] = random(height); //changed the position on click to another location and color
      x[i] = random(width);
      c[i] = color(random(255), random(255), random(255)); //changes color as well
    }
  }
}

int movingShape = -1; // no moving shape variable

void mousePressed() {
  int pixel= get(mouseX, mouseY); // click on location and obtain pixel at mouse point
  for (int i = 0; i < shapeCount; i++) {
    if (pixel == c[i]) {
      movingShape = i; //note: instead of moving shape +1  moving shape is instead i. movingShape set to be bigger than 0.
     
    }
  }
}

void mouseReleased() {

  movingShape = -1; // no moving shape
}
void vibratingShape() {
  for (int i=0; i<shapeCount; i++) {  //for loop to change shapes 

    y[i] = y[i] + random(-1, 1); // shape moves a little...
    x[i] = x[i] + random(-1, 1);
  }
}
