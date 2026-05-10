import java.awt.Graphics;
import java.awt.Color;

//program is used to draw the stars used in abstract art lab
public class Star {

	/** The x coordinate of the upper left corner of the star. */
	private int x;

	/** The y coordinate of the upper left corner of the star. */
	private int y;

	/** The width of the star. */
	private int width;

	/** The number of spokes that make up the star. */
	private int numSpokes;

	/** The color of the star */
	private Color color;

     /* method is used to draw stars with the instance fields x, y, width, numSquares, and color
    @Param is x value, y value, width, and number of spokes of the star for constructors*/

	public Star(int xVal, int yVal, int w, int s, Color c){
        x = xVal;
        y = yVal;
        width = w;
        numSpokes = s;
		color = c;
       
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
    public int getSpokes(){
        return numSpokes;
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
    public void setNumSpokes(int newNumSpokes){
        numSpokes = newNumSpokes;
    }

	public void setColor(Color newColor){
		color = newColor;
	}

    //graphics method to draw the star
	public void draw(Graphics g){
       int radius = width / 2;
    	int centerX = x + radius;
     	int centerY = y + radius;
       	double delta = (2.0 * Math.PI) / numSpokes;
        g.setColor(color);
        
        
        for(int spoke = 0; spoke < numSpokes; spoke++){
            
            int spokeX = (int) ( Math.cos(spoke * delta) * radius + centerX ) ;
            int spokeY = (int) ( Math.sin(spoke * delta) * radius + centerY ) ;
            g.drawLine(centerX, centerY, spokeX, spokeY);
           
        }
     
    }

    public String toString(){
        return "x: " + x + " y: " + y + " width " + width + " spokes: " + numSpokes;
    }
  


}
