/******************************************************
 Lab Assignment 9

 Name: Christopher Barker
 Course/Semester: Spring 2024
 Class Section: 01
 Lab section: 01
 Sources consulted: drop in tutor from P.L.U
 Comments for grader:  _________
*******************************************************/
/*
 * File: SpellingBee.java
 * ----------------------
 * This program contains the starter file for the SpellingBee application.
 * BE SURE TO CHANGE THIS COMMENT WHEN YOU COMPLETE YOUR SOLUTION.
 */


import java.awt.Color; //all imports needed. color, scanner, IO exception, and file input
import java.util.Scanner;
import java.io.IOException;
import java.io.FileInputStream;
import java.util.*; //mulitple imports from java, Tutor told me to use.

public class SpellingBee {
    private SpellingBeeGraphics sbg;
    private SpellingBeePuzzle puzzle;
    private ArrayList<String> dictionary; //Global var for dictionary

    

    // TODO: Declare other instance variables as described in the assignment

    /** method to run the programs, used to interact with GUI to add to display and interact with button
    @param none */

    public void run() {
        
        sbg = new SpellingBeeGraphics();
        sbg.addField("Puzzle", (s) -> puzzleAction(s));
        sbg.addButton("Solve", (s) -> solveAction());
       
        dictionary = new ArrayList<String>(); //create new arrylist for dictionary in run method
       

            try{
                FileInputStream inStream = new FileInputStream("EnglishWords.txt"); //input file from the EnglishWord file text
                Scanner inScan = new Scanner(inStream); //output from scanner
                 
             while(inScan.hasNext()){ //while loop to keep getting strings from scanner then adds to the dictionary.
                String str = inScan.nextLine();
                dictionary.add(str);
             }
               inStream.close(); //close file


            }
            catch(IOException e){ //exception for error messages
                 sbg.showMessage(e.getMessage(), Color.red);
            }

          
        
        
    }
    
 /** method for the puzzle to know what kind of word and points to be displayed by the GUI.
    @param strings, words and letters to be seen in GUI */
    private void puzzleAction(String s) {
        // TODO: Implement this method
       
        String letters = sbg.getField("Puzzle"); //return name of field with specific name, the puzzle
        try{
           
            puzzle = new SpellingBeePuzzle(letters); //create new object puzzle
            sbg.setBeehiveLetters(letters); //sets the letters made into the GUI.
        }
        catch(SpellingBeePuzzleException e){ //message for error
             sbg.showMessage(e.getMessage(), Color.red);
        }
    
    }

    /** method for the puzzle on what to do
    @param none words and letters will be counted and added up here */

    private void solveAction() {
        int count = 0; //for the number of words
        int totalPoints = 0; //how many points scored
        
        // TODO: Implement this method
        for(int i = 0; i < dictionary.size(); i++){ //going through the dictionary 
            String word = dictionary.get(i); //word stored in var
            int wordPoints = word.length(); //value of points stored by the length of word
            String display = word + " (" + wordPoints + ")"; //display to GUI
            if(word.length() >= 4 && puzzle.wordUsesPuzzleLettersOnly(word) && puzzle.wordUsesCenterLetter(word)){
                count++;
                totalPoints += wordPoints; //if statement for checks on length and if only using words and if special letter is used
                sbg.addWord(display, Color.BLACK);
            }
        }
            
        sbg.showMessage("solveAction not implemented yet", Color.red); //error message

       
         for(int i = 0; i < dictionary.size(); i++){ //going through dictionary
            String word = dictionary.get(i); //store the word
             int wordPoints = word.length(); //add up points


            if(puzzle.wordIsPanagram(word)){ //if word is a panagram bonus points
                    wordPoints += sbg.getField("Puzzle").length(); //adding additional points
                    String display = word + " (" + wordPoints + ")"; //update display 
                   totalPoints += wordPoints;

                
                sbg.addWord(display, Color.BLUE); //color of pangram words
            }
            else{
                String display = word + " (" + wordPoints + ")";
                sbg.addWord(display,Color.BLACK); //if not panagram words are black
            }
        }
            
        sbg.showMessage(count + " words;" + totalPoints + " totalPoints", Color.BLACK); //toal points display to GUI
    }


    public static void main(String[] args) /*throws SpellingBeePuzzleException*/{
        new SpellingBee().run();
    }
}
