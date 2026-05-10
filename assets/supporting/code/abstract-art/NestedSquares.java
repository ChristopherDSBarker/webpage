
import java.awt.Graphics; //import needed for graphics
import java.awt.Color; //import needed for color

/* This program is used to draw squares the squares get smaller and smaller similar to the bullseye program used for abstract art method*/

public class NestedSquares {

	/** The x coordinate of the upper left corner of the nested square. */
	private int x;

	/** The y coordinate of the upper left corner of the nested square. */
	private int y;

	/** The width (and height) of the nested square. */
	private int width;

	/** The number of squares that make up the nested square. */
	private int numSquares;

	/** The color of the nested square. */
	private Color color;

    /* method is used to draw squares with the instance fields x, y, width, numSquares, and color
    @Param is x value, y value, width, and color of the square for constructors*/
    
    public NestedSquares(int xVal, int yVal, int w, Color sqrColor){
        x = xVal;
        y = yVal;
        width = w;
        numSquares = 6;
        color = sqrColor;
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

    public int getNumSquares(){
        return numSquares;
    }
    public Color getColor(){
        return color;
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
    public void setNumSquares(int newSqr){
        numSquares = newSqr;
    }
    public void setColor(Color newColor){
        color = newColor;
    }

    //graphics method for the nested squares
    public void draw(Graphics g){
        int diff = width / (numSquares * 2);
        g.setColor(color); //makes the color
        for(int sqr = 0; sqr < numSquares; sqr++){
            int sqrX = x + sqr * diff;
            int sqrY = y + sqr * diff;
            int sqrWidth = width - 2 * sqr * diff;
            g.drawRect(sqrX, sqrY, sqrWidth, sqrWidth);
           
        }
        g.drawLine(x, y, x + width, y + width); //given by drop in tutor for the lines of the square
        g.drawLine(x + width, y, x, y + width);
    }

    public String toString(){
        return "NestedSquares: x = " + x + " y = " + y + " width = " + width 
        + " squares " + numSquares;
    }
}

