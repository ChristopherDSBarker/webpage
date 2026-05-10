/*Christopher Barker
Raka 
CS 120
Proffessor Hock
this project is for the birthday visualization project;
with the hovering of the mouse that shows the ranking number.*/
//step 1 setting up array
String[] temp;
int elements = 366;
int[] month;  //returns the month Jan 1 - Dec 12
int[] day; // returns day of the month 1-31
int[] rank; // returns the frequence ordering
//most common birthday = 1, least common birthday = 366
 

//step 2 for blocks
int blockW = 38;
int blockH = 18;
int xstart = 28;
int ystart = 20;

void setup() {
  size(1000, 1000);
 
  //step 1 extra part, for string use; using files
  temp = loadStrings("month.csv");  // read file data into array of Strings
  month = int(split(temp[0], ','));  // convert 1st line of file (temp[0]) into integer array
  temp = loadStrings("day.csv"); //copied syntax from temp and month as dictated in step 1
  day = int(split(temp[0], ','));//copied syntax from temp and month as dictated in step 1
  temp = loadStrings("rank.csv");//copied syntax from temp and month as dictated in step 1
  rank = int(split(temp[0], ','));//copied syntax from temp and month as dictated in step 1

}

void draw() {
   //step 2 for blocks
    int m0;
    int m1;
    int x = xstart;
    int y = ystart;
    int iRank;
    int z;
   
    m0=month[0];
    background(255,255,255);
   
    fill(0);
    text("     Jan     Feb      Mar      Apr    May     Jun     Jul      Aug      Sep       Oct     Nov     Dec ",20, 15);
   
    z = 16;
    for (int i = 0; i < 31; i++){
      z = z + 18;
      fill(0,0,0);
      text(i+1,10,z);
    }
   
    for (int i=0; i<=month.length-1; i++) {
           m1=month[i];
           if(m0==m1){
              iRank = rank[i];
              z = 160 - (iRank * 160 / 366);
              fill (255-z , 247-z, 197-z);
              rect(x,y,blockW,blockH);
              y=y+blockH;
           }else{
             x= x+blockW;
             y=ystart;
             rect(x,y,blockW,blockH);
             y=y+blockH;
           }
           m0=m1;    
    }
   
    fill(0,0,0);
    text("Less Common", xstart, 620);
    for (int i = 0; i <160 ; i++){
      stroke(255-i,247-i,197-i);
      line(xstart+90+i, 600, xstart+90+i, 600+30);
    }
    fill(0,0,0);
    text("More Common", xstart+260, 620);  
    display_value();
}


void display_value(){
  int m_index;
  int d_index;
  int r_index;

  int[] dayTotal = {0, 31, 60,91, 121, 152,182,213,244,274,305,335,366};  
 
  m_index = (mouseX - xstart) / blockW;
  d_index = (mouseY - ystart) / blockH;
 
  if ( ((mouseX >= xstart) && (mouseX <=((xstart-2+(12*blockW))))) && ((mouseY >= ystart) && (mouseY <= (ystart + (blockH * (dayTotal[m_index+1] - dayTotal[m_index]) )))) && (mouseY <= 1000 && mouseX <=1000) ){ // on range  
    r_index = dayTotal[m_index] + d_index;
    fill(0,0,0);
    text(rank[r_index], xstart+10+(m_index * blockW),ystart+15+(d_index * blockH));
   
  }
 
}
