// ----------------------------------------------------
// Create a line break element and add it to the page
// Used to move the next row of buttons to a new line
// ----------------------------------------------------
function create_line_break()
{
    // create a <br> element
    const br = document.createElement("br");

    // add the line break to the body of the document
    document.body.appendChild(br);
}


// ----------------------------------------------------
// Create a button element and add it to the page
// This represents one cell in the Minesweeper board
// ----------------------------------------------------
function create_button()
{
	// create a new button element
	const btn = document.createElement("button");

	// set fixed size so the grid stays square
	btn.style.width = "30px";
	btn.style.height = "30px";

	// remove default padding so numbers stay centered
	btn.style.padding = "0";

	// small margin to create spacing between cells
	btn.style.margin = "1px";

	// add the button to the webpage body
	document.body.appendChild(btn);

	// return the button so the class can store it in the 2D array
	return btn;
}


// ----------------------------------------------------
// Preload images so they appear instantly during gameplay
// This prevents delay when bomb/flag images are first shown
// ----------------------------------------------------
function avoid_image_loading_delay()
{
    // list of all images used by the game
    const images = [
        "bomb.png",
        "flag.png",
        "0.png",
        "1.png",
        "2.png",
        "3.png",
        "4.png",
        "5.png",
        "6.png",
        "7.png",
        "8.png"
    ];

    // loop through each image name
    for (let i = 0; i < images.length; i++)
    {
        // create a new image object
        const img = new Image();

        // load the image into the browser cache
        img.src = images[i];
    }
}