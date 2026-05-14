import java.util.Scanner;

public class BattleShipsGame {

    static final int SIZE_OF_PLAYFIELD = 10;
    static final int STARTING_MISSILES = 35;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("=================================");
        System.out.println("         BATTLESHIPS");
        System.out.println("=================================");

        System.out.print("Enter player name: ");
        String playerName = scanner.nextLine();

        int[][] playfield = new int[SIZE_OF_PLAYFIELD][SIZE_OF_PLAYFIELD];

        selectGameBoard(playfield);

        boolean gameOver = false;
        int missiles = STARTING_MISSILES;

        while (!gameOver) {

            gameBoard(playfield, playerName, missiles);

            shipsSunk(playfield);

            int row = -1;
            int col = -1;

            boolean validMove = false;

            while (!validMove) {

                System.out.print("\nEnter letter coordinate (A-J): ");
                col = checkColumn(scanner);

                System.out.print("Enter number coordinate (1-10): ");
                row = checkRow(scanner);

                if (playfield[row][col] >= 10) {
                    System.out.println("You already fired at that coordinate.");
                } else {
                    validMove = true;
                }
            }

            playfield[row][col] += 10;
            missiles--;

            boolean won = winner(playfield);

            if (won) {
                gameBoard(playfield, playerName, missiles);

                System.out.println("\nYou've vanquished our enemies Captain "
                        + playerName + "!");
                System.out.println("You deserve a medal!");

                gameOver = true;
            }

            if (missiles == 0 && !won) {
                gameBoard(playfield, playerName, missiles);

                System.out.println("\nWe have lost the war.");

                gameOver = true;
            }
        }

        scanner.close();
    }

    public static void selectGameBoard(int[][] board) {

        int destroyer = 2;
        int cruiser = 3;
        int battleship = 4;
        int carrier = 5;

        int presets = 5;

        int randomNum = (int) ((Math.random() * presets) + 1);

        // PRESET 1
        if (randomNum == 1) {

            board[2][4] = board[2][5] = destroyer;

            board[1][0] = board[2][0] = board[3][0] = cruiser;

            board[4][5] = board[4][6] =
            board[4][7] = board[4][8] = battleship;

            board[1][2] = board[2][2] =
            board[3][2] = board[4][2] =
            board[5][2] = carrier;
        }

        // PRESET 2
        else if (randomNum == 2) {

            board[7][1] = board[7][2] = destroyer;

            board[0][5] = board[1][5] = board[2][5] = cruiser;

            board[5][3] = board[5][4] =
            board[5][5] = board[5][6] = battleship;

            board[2][8] = board[3][8] =
            board[4][8] = board[5][8] =
            board[6][8] = carrier;
        }

        // PRESET 3
        else if (randomNum == 3) {

            board[0][0] = board[1][0] = destroyer;

            board[8][3] = board[8][4] = board[8][5] = cruiser;

            board[3][6] = board[4][6] =
            board[5][6] = board[6][6] = battleship;

            board[9][1] = board[9][2] =
            board[9][3] = board[9][4] =
            board[9][5] = carrier;
        }

        // PRESET 4
        else if (randomNum == 4) {

            board[5][0] = board[5][1] = destroyer;

            board[2][7] = board[3][7] = board[4][7] = cruiser;

            board[7][4] = board[7][5] =
            board[7][6] = board[7][7] = battleship;

            board[0][9] = board[1][9] =
            board[2][9] = board[3][9] =
            board[4][9] = carrier;
        }

        // PRESET 5
        else {

            board[9][7] = board[9][8] = destroyer;

            board[4][1] = board[4][2] = board[4][3] = cruiser;

            board[1][4] = board[2][4] =
            board[3][4] = board[4][4] = battleship;

            board[6][0] = board[6][1] =
            board[6][2] = board[6][3] =
            board[6][4] = carrier;
        }
    }

    public static void gameBoard(int[][] playfield,
                                 String name,
                                 int missiles) {

        System.out.println("\n=================================");
        System.out.println("Captain: " + name);
        System.out.println("Missiles Remaining: " + missiles);
        System.out.println("=================================");

        String gridX = "    A  B  C  D  E  F  G  H  I  J";

        String[] gridY = {
                "1 ", "2 ", "3 ", "4 ", "5 ",
                "6 ", "7 ", "8 ", "9 ", "10"
        };

        System.out.println(gridX);

        for (int i = 0; i < playfield.length; i++) {

            String row = "";

            for (int j = 0; j < playfield[i].length; j++) {

                if (playfield[i][j] > 10) {
                    row += "*  ";
                }

                else if (playfield[i][j] == 10) {
                    row += "!  ";
                }

                else {
                    row += "   ";
                }
            }

            System.out.println(gridY[i] + " " + row);
        }
    }

    public static void shipsSunk(int[][] playfield) {

        int carrierCounter = 0;
        int battleshipCounter = 0;
        int cruiserCounter = 0;
        int destroyerCounter = 0;

        for (int i = 0; i < playfield.length; i++) {

            for (int j = 0; j < playfield[i].length; j++) {

                if (playfield[i][j] == 5) {
                    carrierCounter++;
                }

                if (playfield[i][j] == 4) {
                    battleshipCounter++;
                }

                if (playfield[i][j] == 3) {
                    cruiserCounter++;
                }

                if (playfield[i][j] == 2) {
                    destroyerCounter++;
                }
            }
        }

        String sunkShips = "";

        if (carrierCounter == 0) {
            sunkShips += "Carrier ";
        }

        if (battleshipCounter == 0) {
            sunkShips += "Battleship ";
        }

        if (cruiserCounter == 0) {
            sunkShips += "Cruiser ";
        }

        if (destroyerCounter == 0) {
            sunkShips += "Destroyer ";
        }

        System.out.println("\nShips sunk:");

        if (sunkShips.equals("")) {
            System.out.println("None.");
        } else {
            System.out.println(sunkShips);
        }
    }

    public static boolean winner(int[][] playfield) {

        for (int i = 0; i < playfield.length; i++) {

            for (int j = 0; j < playfield[i].length; j++) {

                if (playfield[i][j] == 2 ||
                    playfield[i][j] == 3 ||
                    playfield[i][j] == 4 ||
                    playfield[i][j] == 5) {

                    return false;
                }
            }
        }

        return true;
    }

    public static int checkColumn(Scanner scanner) {

        while (true) {

            String input = scanner.nextLine().trim().toUpperCase();

            if (input.length() != 1) {
                System.out.println("Please enter one letter.");
                continue;
            }

            char letter = input.charAt(0);

            if (letter >= 'A' && letter <= 'J') {
                return letter - 'A';
            }

            System.out.println("Invalid column. Use A-J.");
        }
    }

    public static int checkRow(Scanner scanner) {

        while (true) {

            String input = scanner.nextLine().trim();

            try {

                int row = Integer.parseInt(input);

                if (row >= 1 && row <= 10) {
                    return row - 1;
                }

            } catch (NumberFormatException e) {
            }

            System.out.println("Invalid row. Use 1-10.");
        }
    }
}