/******************************************************
 Lab Assignment 6

 Name: Christopher Barker
 Course/Semester: Spring 2024
 Class Section: 06
 Lab section: 06
 Sources consulted: drop in tutor
 Comments for grader:  _________
*******************************************************/
import java.awt.Color; // needed for color
import java.awt.Graphics; //needed for graphics
import java.util.Random; //needed for random

public class MountainPaths {
    //This program uses other files to draw a map. Then with arrays finds a path through the map which is a mountain pass. With 
    //data from another file as elevation. There is some calculations to find Min and maximum elevations. 
    // Also finds the lowest elevation path and draws a red line through the path of elevations.

    private static final long RAND_SEED = 1234L;
    private static Random randGen = new Random( RAND_SEED );
    
    public static void main(String[] args) throws Exception{
        final int WIDTH = 840;
        final int HEIGHT = 480;
        final String INPUT_FILE = "Colorado_840x480.dat";
      
        // Construct the DrawingPanel, and get its Graphics context
        DrawingCanvas panel = new DrawingCanvas(WIDTH, HEIGHT);
        Graphics g = panel.getGraphics();
        
        // Load elevation data from INPUT_FILE
        int[][] grid = ElevationData.load(INPUT_FILE, WIDTH, HEIGHT);
        
        // TODO: Implement your solution here
        //-------------------------------------------------------------------------------------------------------

        // Part 1 to find min and max elevations
        int min = grid[0][0]; //set the double array
        int max = 0; //store value of max
        
        for(int i = 0; i < grid.length; i++){ //go through one array row
            for(int j = 0; j < grid[i].length; j++){ //go through 2d array col
                if(grid[i][j] > max){ // check for values in array if bigger then max 
                    max = grid[i][j]; //store vlaue
                }
                if(grid[i][j] < min){ //check for min in the array
                    min = grid[i][j]; //store value
                }
                
            }
        }
        System.out.println("Min value in map: " + min ); //print
        System.out.println("Max value in map: " + max );

        //part 2 to draw the map
        for(int i = 0; i < grid.length; i++){
           
            for(int j = 0; j < grid[i].length; j++){
                double r = (grid[i][j] - min) / (double)(max - min); //value between min and max, 
                int c = (int) (r  * 255); //grayscale value
                g.setColor( new Color(c,c,c)); //given code for pictures and color
                g.fillRect(j,i,1,1);  
            
            }
        }
       
        //part 3 to find row with minimum elevation in col 0

        int j; 
        int min2 = grid[0][0]; //another 2d array for min
        int minIndex = 0; //store index from array
        for (j = 0; j < grid.length; j++) {  //go through the row
            if (grid[j][0] < min2) { //iterate through col
                min2 = grid[j][0]; //store value 
                minIndex = j; //store exact value
            }
        }
        System.out.println("Row with the lowest val in col 0: " + minIndex);//print

        //part 4 find and draw lowest elevation path
        int totalChange = 0; 
        int i = minIndex;
        
       

        for(j = 0; j < grid[0].length - 1; j++){   
            int val = grid[i][j]; //drop in tutor helped, was getting a total change in elevation to high, this starts at correct location
            int upVal = 0; 
            int downVal = 0;
            int moveFor = 0;
            
            if(j + 1 < grid[0].length){  //checks to move forward, up, and down through the 2d array. 
                moveFor = grid[i][j + 1];

                if(i + 1 < grid.length){
                    upVal = grid[i + 1][j + 1];
                }
                if(i - 1 >= 0 ){
                    downVal = grid[i - 1][j + 1]; //Student Pheonix and drop in tutor double checked i array incorrectly put i + 1
                }
            }

            //changes to positive sign for elevation distance. 
            int diffUp = Math.abs(val - upVal);
            int diffDown = Math.abs(val - downVal);
            int diffFor = Math.abs(val - moveFor);

            //drop in tutor helped with logic of checking  and adding up the total change.
            //if statements that are for moving, the greedy walk logic.
            if(diffFor <= diffUp && diffFor <= diffDown){
                i = i;
                totalChange += diffFor;
             
            }
            else if(diffUp < diffDown){
                i = i + 1;
                totalChange += diffUp;
                
            }
            else if(diffDown < diffUp){
                i = i - 1;
                totalChange += diffDown;
                
            }
            else{
                if(randGen.nextInt(2) == 0){ //given code for random the flick a coin option.
                    //...
                    i = i + 1;
                    totalChange += diffUp;
                   
                }else{
                    //...
                    i = i - 1;
                    totalChange += diffDown;
                   
                }
           
                
            }
           
            
            g.setColor(new Color(255, 0, 0)); //set color to red
            g.fillRect(j,i,1,1);
        }
       

      System.out.println("Lowest-Elevation-Change Path starting at row " + minIndex + " give total change of: " + (totalChange)); 
      //print the index and total change.
       
    }
    
}
