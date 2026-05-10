class Minesweeper
{
	// default values used if no parameters provided
	static get SIZE()  { return 15; }
	static get BOMB()  { return "B"; }
	static get EMPTY() { return "E"; }
	
	// -----------------------------
	// Required class properties
	// -----------------------------

	bombs;   // number of bombs placed in the board
	cells;   // 2D array storing all button elements
	rows;    // number of rows
	columns; // number of columns


	constructor(rows = Minesweeper.SIZE, columns = Minesweeper.SIZE, probability_chance = 0.1)
	{
		// store board size
		this.rows = rows;
		this.columns = columns;

		// initialize properties
		this.cells = [];
		this.bombs = 0;

		// --------------------------------
		// Create the grid of buttons
		// --------------------------------

		for (let i = 0; i < this.rows; i++)
		{
			this.cells[i] = [];

			for (let j = 0; j < this.columns; j++)
			{
				// create button using provided helper function
				let btn = create_button();

				// store coordinates inside button dataset
				btn.dataset.x = i;
				btn.dataset.y = j;

				// default state
				btn.dataset.value = Minesweeper.EMPTY;
				btn.dataset.open = "false";
				btn.dataset.flag = "false";

				// randomly place bomb based on probability
				if (Math.random() < probability_chance)
				{
					btn.dataset.value = Minesweeper.BOMB;
					this.bombs++;
				}

				// store button inside 2D array
				this.cells[i][j] = btn;
			}

			// create new line after each row
			create_line_break();
		}

		// after bombs are placed calculate numbers
		this.flood_fill();
	}


	// --------------------------------
	// Reset board state and listeners
	// --------------------------------
	init_board()
	{
		for (let i = 0; i < this.rows; i++)
		{
			for (let j = 0; j < this.columns; j++)
			{
				let btn = this.cells[i][j];

				// clear button display
				btn.innerHTML = "";

				// disable until game starts
				btn.disabled = true;

				btn.dataset.open = "false";
				btn.dataset.flag = "false";

				// left click → open cell
				btn.onclick = () => this._open(i, j);

				// right click → place flag
				btn.oncontextmenu = (e) =>
				{
					e.preventDefault();
					this._flag(i, j);
				};
			}
		}
	}


	// --------------------------------
	// Calculate numbers around bombs
	// --------------------------------
	flood_fill()
	{
		for (let i = 0; i < this.rows; i++)
		{
			for (let j = 0; j < this.columns; j++)
			{
				let btn = this.cells[i][j];

				// skip bombs
				if (btn.dataset.value === Minesweeper.BOMB)
					continue;

				let count = 0;

				// check all 8 neighbors
				for (let dx = -1; dx <= 1; dx++)
				{
					for (let dy = -1; dy <= 1; dy++)
					{
						let x = i + dx;
						let y = j + dy;

						if (x >= 0 && x < this.rows && y >= 0 && y < this.columns)
						{
							if (this.cells[x][y].dataset.value === Minesweeper.BOMB)
								count++;
						}
					}
				}

				// store number of bombs around
				btn.dataset.value = count;
			}
		}
	}


	// --------------------------------
	// Disable all cells (game over)
	// --------------------------------
	lock()
	{
		for (let i = 0; i < this.rows; i++)
		{
			for (let j = 0; j < this.columns; j++)
			{
				this.cells[i][j].disabled = true;
			}
		}
	}


	// --------------------------------
	// Enable all cells (game start)
	// --------------------------------
	unlock()
	{
		for (let i = 0; i < this.rows; i++)
		{
			for (let j = 0; j < this.columns; j++)
			{
				this.cells[i][j].disabled = false;
			}
		}
	}


	// --------------------------------
	// Right click → toggle flag
	// --------------------------------
	_flag(x, y)
	{
		let btn = this.cells[x][y];

		// cannot flag opened cells
		if (btn.dataset.open === "true")
			return;

		if (btn.dataset.flag === "false")
		{
			btn.dataset.flag = "true";
			btn.innerHTML = "🚩";
		}
		else
		{
			btn.dataset.flag = "false";
			btn.innerHTML = "";
		}
	}


	// --------------------------------
	// Left click → open cell
	// --------------------------------
	_open(x, y)
	{
		let btn = this.cells[x][y];

		// ignore already opened or flagged cells
		if (btn.dataset.open === "true" || btn.dataset.flag === "true")
			return;

		btn.dataset.open = "true";

		// if bomb → game over
		if (btn.dataset.value === Minesweeper.BOMB)
		{
			btn.innerHTML = "💣";

			document.getElementById("game_over").innerHTML = "You lost";
			document.getElementById("game_over").style.display = "inline";

			this.lock();
			return;
		}

		// show number
		btn.innerHTML = btn.dataset.value;

		// if zero → explore neighbors
		if (btn.dataset.value == 0)
		{
			this.explore(x, y);
		}

		// check if player won
		if (this.is_winning_choice())
		{
			document.getElementById("game_over").innerHTML = "You won";
			document.getElementById("game_over").style.display = "inline";

			this.lock();
		}
	}


	// --------------------------------
	// Recursive exploration of empty cells
	// --------------------------------
	explore(x, y)
	{
		for (let dx = -1; dx <= 1; dx++)
		{
			for (let dy = -1; dy <= 1; dy++)
			{
				let nx = x + dx;
				let ny = y + dy;

				if (nx >= 0 && nx < this.rows && ny >= 0 && ny < this.columns)
				{
					let btn = this.cells[nx][ny];

					if (btn.dataset.open === "false" && btn.dataset.flag === "false")
					{
						btn.dataset.open = "true";
						btn.innerHTML = btn.dataset.value;

						// continue recursion if cell is zero
						if (btn.dataset.value == 0)
						{
							this.explore(nx, ny);
						}
					}
				}
			}
		}
	}


	// --------------------------------
	// Check if player opened all safe cells
	// --------------------------------
	is_winning_choice()
	{
		let opened = 0;

		for (let i = 0; i < this.rows; i++)
		{
			for (let j = 0; j < this.columns; j++)
			{
				let btn = this.cells[i][j];

				if (btn.dataset.open === "true" && btn.dataset.value !== Minesweeper.BOMB)
					opened++;
			}
		}

		// win condition
		return opened === (this.rows * this.columns - this.bombs);
	}
}