/******************************************************
 Lab Assignment 8

 Name: Christopher Barker
 Course/Semester: Spring 2024
 Class Section: 08
 Lab section: 08
 Sources consulted: drop in tutor from P.L.U
 Comments for grader:  _________ 
*******************************************************/
import java.awt.Graphics;
import java.awt.Color;
import java.util.Random;
public class AbstractArtTest{
    public static void main(String[] args){
        DrawingCanvas canvas = new DrawingCanvas();
        Graphics g = canvas.getGraphics();
        
        Random rand = new Random();
   
      
        for(int i = 0; i < 10; i++){
        int width = rand.nextInt(101) + 50;
         int y = rand.nextInt( canvas.getHeight() - width);
         int x = rand.nextInt( canvas.getWidth() - width); 
         int starSize = rand.nextInt(100) + 15;
         int starLegs = rand.nextInt(12) + 5;
         int checkSize = rand.nextInt(12) + 5;
        
         Color randomColor = new Color(rand.nextInt(256), rand.nextInt(256), rand.nextInt(256));
       
           int shapeType = rand.nextInt(5);
                if(shapeType == 0){
                    Star s1 = new Star(x, y, starSize , starLegs, randomColor);
                    s1.draw(g);
                }
                else if(shapeType == 1){
                    NestedSquares s2 = new NestedSquares(x, y, width, randomColor);
                    s2.draw(g);
                }
                else{
                    Checkerboard s3 = new Checkerboard(x, y, width, checkSize, randomColor, Color.BLUE);
                    s3.draw(g);
                }
            }

        }
    
     

        

    

    }
