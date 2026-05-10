import java.awt.Graphics; //import for graphics
import java.awt.Color; //import for color

//program is used to draw the checkerboard picture in the abstract art lab
public class Checkerboard {

	/** The x coordinate of the upper left corner of the checkerboard. */
	private int x;

	/** The y coordinate of the upper left corner of the checkerboard. */
	private int y;

	/** The width (and height) of the square checkerboard. */
	private int width;

	/** The number of squares per side of the checkerboard. */
	private int squaresPerSide;

	/** The color for even squares */
	private Color evenColor;

	/** The color for odd squares */
	private Color oddColor;

	 /* method is used to draw checkerboard with the instance fields x, y, width, squares per side, even color, and odd color
    @Param is x value, y value, width, squares per side, even color, and  odd color of the checkerboard for constructors*/

	public Checkerboard(int xVal, int yVal, int w, int s, Color colorE, Color colorO){
		x = xVal;
		y = yVal;
		width = w;
		squaresPerSide = s;
		evenColor = colorE;
		oddColor = colorO;
	}
	//all accessors
	public int getX(){
        return x;
    }
    public int getY(){
        return y;
    }
    public int getWidth(){
        return width;
    }
	public int getSquaresPerSide(){
		return squaresPerSide;
	}
	public Color getEvenColor(){
		return evenColor;
	}
	public Color getOddColor(){
		return oddColor;
	}

	//all mutators
	public void setX(int newX){
        x = newX;
    }
    
    public void setY(int newY){
        y = newY;
    }
    public void setWidth(int newWidth){
        width = newWidth;
    }

	public void setSquaresPerSide(int newSquaresPerSide){
		squaresPerSide = newSquaresPerSide;
	}
	public void setEvenColor(Color newEvenColor){
		evenColor = newEvenColor;
	}
	public void setOddColor(Color newOddColor){
		oddColor = newOddColor;
	}

	//graphics method to draw the checkerboard
	public void draw(Graphics g){
		int squareWidth = width / squaresPerSide;
		for(int i = 0; i < squaresPerSide; i++){
			for (int j = 0; j < squaresPerSide; j++){ //to loop over the squares
				if((i + j) % 2 == 0){ //the even colors
					g.setColor(evenColor);
				}
				else{ //the odd colors
					g.setColor(oddColor);
				}
				g.fillRect(x + i * squareWidth, y + j * squareWidth, squareWidth, squareWidth); //the colors filled in 
			}
			
		}
	}

	 public String toString(){
        return "x: " + x + " y: " + y + " width " + width + " squares: " + squaresPerSide;
    }




}
