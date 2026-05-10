<html>
	<head>
		<title>Minesweeper</title>
		<script type="text/javascript" src="function.js"></script>
		<script type="text/javascript" src="class.js"></script>
	</head>
	
	<body onload="avoid_image_loading_delay()">
		<button id="start">Start</button>&nbsp;&nbsp;&nbsp;&nbsp;
		<span id="game_over" style="display: none">Game Over</span>
		<br/><br/>
		<script>
		<!-- PLACE YOUR IMPLEMENTATION BELOW -->
			// ------------------------------------
			// Read parameters from URL
			// ------------------------------------
			const params = new URLSearchParams(window.location.search);

			let rows = parseInt(params.get("rows"));
			let cols = parseInt(params.get("cols"));
			let prob = parseFloat(params.get("prob"));

			// validate inputs
			if (!rows || rows <= 0) rows = Minesweeper.SIZE;
			if (!cols || cols <= 0) cols = Minesweeper.SIZE;
			if (!prob || prob < 0 || prob > 1) prob = 0.1;


			// ------------------------------------
			// Create the Minesweeper game
			// ------------------------------------
			let game = new Minesweeper(rows, cols, prob);

			// initialize board
			game.init_board();


			// ------------------------------------
			// Handle Start / Reset button
			// ------------------------------------
			let startButton = document.getElementById("start");

			startButton.onclick = function()
			{
				if (startButton.innerHTML === "Start")
				{
					startButton.innerHTML = "Reset";

					// enable all cells
					game.unlock();

					// hide message
					document.getElementById("game_over").style.display = "none";
				}
				else
				{
					// reload page to reset board
					location.reload();
				}
			};
		<!-- PLACE YOUR IMPLEMENTATION ABOVE -->
		</script>
	</body>
</html>
