/******************************************************
 Lab Assignment 7

 Name: Christopher Barker
 Course/Semester: Spring 2024
 Class Section: 07
 Lab section: 07
 Sources consulted: drop in tutor from P.L.U
 Comments for grader:  _________
*******************************************************/
import java.util.Scanner; //used for scanner
import java.io.FileInputStream; //used for reading a file to a file
import java.io.IOException; // used for reading a file

import java.io.FileOutputStream; //used for outputing to file
import java.io.PrintWriter; //used to output to a file

public class ImageModify{
    /*this program asked the user what kind of edit to do with a ppm file. 4 types of edits
    negate, quantize, gray scale, flip horizontal */
    static Scanner scan = new Scanner(System.in);

    static int height, width; // height and width values that are global

    enum Modification{ //given in class lab
        NEGATE, QUANTIZE, GRAY_SCALE, FLIP_HORIZONTAL
    }

    public static void main(String[] args)throws IOException{

        FileInputStream fileStream = null;
        Scanner scnr = null;
        
        //open a file
        System.out.print("Input file: ");//prompt to user
        String input = scan.nextLine();  //used to store a line from user
        fileStream = new FileInputStream(input); //needed for files and variable input from user
        scnr = new Scanner(fileStream); // scanner to the file

        //output file
        System.out.print("Output file: "); //prompt user
        String output = scan.nextLine(); //store output
        FileOutputStream fileOutStream = new FileOutputStream(output); //file output using a variable 
        PrintWriter outFS = new PrintWriter(fileOutStream); //needed for output files

        //method calls
        processHeader(scnr, outFS);

        char charTyped = scan.next().charAt(0); // used char input used for if  statement checks

        //if statements for which mod to use for the ppm file
        if(charTyped == 'a'){
             processBody(scnr, outFS, Modification.NEGATE); 
        }
        else if(charTyped == 'b'){
          processBody(scnr, outFS, Modification.QUANTIZE);
        }
        else if(charTyped == 'c'){
              processBody(scnr, outFS, Modification.GRAY_SCALE);
        }
        else if(charTyped == 'd'){
             processBody(scnr, outFS, Modification.FLIP_HORIZONTAL);
        }
       
    //  close file 
        fileStream.close();
        outFS.close();
    }

    /* Method to ask user which modification to use, scans in and saves value of the first couple of values
    from the file like width height and color and then outputs those values into the new or existing file
    @param is the scanner to files and printwriter for output to the file*/


    public static void processHeader(Scanner scnr, PrintWriter outFS){
        String str = scnr.nextLine();
        width = scnr.nextInt();
        height = scnr.nextInt();
        int color = scnr.nextInt();
        outFS.println(str);
        outFS.println(width + " " + height);
        outFS.println(color);
     
        System.out.println("Select modification: ");
        System.out.println("      (a) negate");
        System.out.println("      (b) quantize");
        System.out.println("      (c) gray scale");
        System.out.println("      (d) flip horizontal");

    }

    
    /* method to take the modifications from the enum method and to then 
    used to send the modded picture to the new file
    @param is scanner to the file, printwriter is used for the output files, and the modification method 
    for what to do to the file */
    public static void processBody(Scanner scnr, PrintWriter outFS, Modification mod){
        //if statements to tell which modification to set for values and to then use to call from scanner and 
        //output files
        if(mod == Modification.NEGATE){
            negatePic(scnr, outFS);
        }
        else if(mod == Modification.QUANTIZE){
            quantizePic(scnr,outFS);
        }
        else if(mod == Modification.GRAY_SCALE){
             grayPic(scnr, outFS);
        }
        else if(mod == Modification.FLIP_HORIZONTAL){
            flipPic(scnr, outFS);
        }

    }

    /* method to make the ppm file negated, type of edit for the picture
    @param scanner from file and the output to the file*/
    public static void negatePic(Scanner scnr, PrintWriter outFS){
        //go through the file in a 2d array to store the values of red green and blue.
        for(int i = 0; i < width; i++){
            for(int j = 0; j < height; j++){
                int r = Math.abs(scnr.nextInt() - 255); //red 
                int g = Math.abs(scnr.nextInt() - 255); //green    
                int b = Math.abs(scnr.nextInt() - 255); //blue
                outFS.print(r + " " + g + " " + b + " "); //send those values to new file
        
            }
          outFS.println(); 
        }
    }
    /* method to edit the ppm file picture to a quantize version
    @param is from the scanner to the file and sending the file ouput with printwriter*/
    public static void quantizePic(Scanner scnr, PrintWriter outFS){
        //goes through the 2d array in file and saves the value in terms of color
        for(int i = 0; i < width; i++){
            for(int j = 0; j < height; j++){
            
                int r = scnr.nextInt(); 
                int g = scnr.nextInt(); 
                int b = scnr.nextInt(); 
                //if statmeents to check value set to either black or white
                if(r > 127){
                    r = 255;
                }
                else{
                    r = 0;
                }
                   if(g > 127){
                    g = 255;
                }
                else{
                    g = 0;
                }
                   if(b > 127){
                    b = 255;
                }
                else{
                    b = 0;
                }
                 outFS.print(r + " " + g + " " + b + " ");

            }
             outFS.println();
        }
    }
    
    /* method that takes the picture and makes it gray
    @param is scanner to file and printwriter file to output*/
    public static void grayPic(Scanner scnr, PrintWriter outFS){
        //2d array to save the values in terms of rgb 
        
        for(int i = 0; i < height; i++){
           
            for(int j = 0; j < width; j++){
                int r = scnr.nextInt(); 
                int g = scnr.nextInt(); 
                int b = scnr.nextInt(); 
                int average = (r + g + b) / 3;//calc for the average
                outFS.print(average  + " " + average + " " + average + " ");//print to file

            
            }
            outFS.println();
        }
    }
    
    /* method to flip the picture ppm horizontally
    @parm is from the scanner to file and the printwrite to the output file*/
    public static void flipPic(Scanner scnr, PrintWriter outFS){
    //arrays for the color values
    int[] reds = new int[width];
    int[] greens = new int[width];
    int[] blues = new int[width];
    //going through the 2d array and storying values 
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                  reds[j] = scnr.nextInt();
                  greens[j] = scnr.nextInt();
                  blues[j] = scnr.nextInt();
            }
        //methods to reverse the colors in array
        reverseVals(reds);
        reverseVals(greens);
        reverseVals(blues);
            //going through width of array to set the colors
            for(int j = 0; j < width; j++){
                int r = reds[j];
                int g =  greens[j];
                int b = blues[j];
               
                outFS.print(r  + " " + g + " " + b + " "); //send colors styled to output file
            }
            outFS.println();
        }
    }
    
    /* method to reverse values in an array
    parm is the array made with stored values*/
    public static void reverseVals(int[] arrVals) {
        int i; // start of index
        int tempValue; //temp value to switch index
        for (i = 0; i < (arrVals.length / 2); ++i) {
            tempValue = arrVals[i]; // Do swap
            arrVals[i] = arrVals[arrVals.length - 1 - i];
            arrVals[arrVals.length - 1 - i] = tempValue;
        } 
        
    }
}