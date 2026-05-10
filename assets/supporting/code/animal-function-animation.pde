void pikachu(int x, int y, color c) {
  //PIKACHU STARTS HERE
  fill(#FAD61D);//Yellow color 
  noStroke();
  ellipse(100 +x, 100 +y, 65, 50); //big circle
  triangle(75+x, 90+y, 85+x, 50+y, 100+x, 90+y); //left ear
  triangle(75+25+x, 90+y, 85+25+x, 50+y, 100+25+x, 90+y); //right ear
  fill(0);
  triangle(81+x, 65+y, 85+x, 50+y, 89+x, 65+y); //black left filling of ear
  triangle(81+25+x, 65+y, 85+25+x, 50+y, 89+25+x, 65+y); //black right filling of ear
  ellipse(90+x, 89+y, 10, 10); // left eye
  ellipse(90+20+x, 89+y, 10, 10); //right eye
  fill(255);
  ellipse(90+2+x, 88+y, 4, 4); //left pupil
  ellipse(90+18+x, 88+y, 4, 4); //right pupil
  fill(color(random(255),random(255),random(255)));
  ellipse(85+x, 105+y, 10, 10); //left cheek
  ellipse(90+25+x, 105+y, 10, 10); //right cheek
  fill(#F791D4); //color of mouth

  triangle(100+x, 105+y, 95+x, 110+y, 105+x, 110+y);// mouth
}
void setup() {
  size(900, 800); //background size
}

void row(int x, int y,color main, color odd) {
  pikachu(x, y, main); //base for the pikachu
  pikachu(x+ 100, y, main); //plus 100 for another pikachu left direction, 
  pikachu(x+200, y, main); // another 100 for another pikachu left direction
  pikachu(x+300, y, main);// another 100 for another pikachu left direction
  pikachu(x+400, y, main);// another 100 for another pikachu left direction
  pikachu(x+500, y, main);// another 100 for another pikachu left direction
  pikachu(x+600, y, odd);// another 100 for another pikachu left direction, this one is the different color hence odd
}
void grid(int x, int y){
  row(x,y+100,color(#F62D14),color(#0DFFFD)); //add another row
  row(x,y+200,color(#F62D14),color(0,0,255));//add another row
  row(x,y+300,color(#F62D14),color(#2FE320));//add another row
  row(x,y+400,color(#F62D14),color(#2FE320));//add another row
  row(x,y+500,color(#F62D14),color(#2FE320));//add another row
  
  //pikachu(x,y+100,color(#F62D14));
  //pikachu(x,y+200,color(#F62D14));
  //pikachu(x,y+300,color(#F62D14)); 
}

void draw() {
  row(50, 50, #F62D14,color(0,255,0)); //base row
  grid(50, 50); //base grid
  //row(50, 150, #F62D14,color(0,0,255));

  //pikachu(0,0,color(#F62D14));
  //pikachu(100, 0, color(255,0,0));
  //pikachu(200, 0, color(0,255,0));
  //pikachu(300, 0, color(0,0,255)); 
}
