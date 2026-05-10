class SpellingBeePuzzle{
    private String puzzle;
    /** method to boolean check puzzle to know what points to add up, is it using the middle letter, is it a panagram.
    */
    public SpellingBeePuzzle(String puzz)throws SpellingBeePuzzleException{
        if(puzz.length() != 7){ // check to see if puzzle length is 7
            throw new SpellingBeePuzzleException("Error, puzzle must contain exactly 7 letters"); // error message
        }
        for(int i = 0; i < puzz.length(); i++){ 
            if(!(Character.isLetter(puzz.charAt(i)))){ //check to see if the character is a letter of alphabet
                 throw new SpellingBeePuzzleException("Error, every character must be one of the 26 letters");
            
          
            }
            for(int j = i + 1; j < puzz.length(); j++){ //not to equal, prof. Murphy helped with j, i + 1 had to compare first letter and next letter
                if(puzz.charAt(i) == puzz.charAt(j)){ //check to see if a letter was used more then once.
                    throw new SpellingBeePuzzleException("Error, no letter may appear more than once in the puzzle");

                }
            }

           
           
        }
        puzzle = puzz; //Prof Murphy helped moved this I was only checking the first condition, word is 7 letters.
    }
    public boolean wordUsesPuzzleLettersOnly(String word){ //boolean check to see if only using letters from alphabet
        for(int i = 0; i < word.length(); i++){ 
            if(!(puzzle.contains(String.valueOf(word.charAt(i)))) ){ //Drop in tutor helped with string.valueOf, was getting error
           
            return false;
        }
       
        }
        return true;
        
    }
    public boolean wordUsesCenterLetter(String word){ //boolean check to see if using center letter, Yellow letter in puzzle.
        if(word.contains(String.valueOf(puzzle.charAt(0)))){ //Drop in tutor helped with String.ValueOf was getting error.
             
            return true;
        }
        return false;
        
      }

    public boolean wordIsPanagram(String word){ //boolean check to see if word is panagram.
        for(int i = 0; i < puzzle.length(); i++){
            if(!word.contains(String.valueOf(puzzle.charAt(0)))){ //drop in tutor helped with String.ValueOf was getting error.
             
                return false;
            }
        
        }
       
        return true;

       
    }
}