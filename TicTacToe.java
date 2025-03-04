import java.util.Scanner;

public class TicTacToe {
    static char input(Scanner obj, String prompt) {
        System.out.print(prompt);
        String inp = obj.next();
        char ch = inp.charAt(0);
        return ch;
    }

    static void printGrid(char[][] grid) {
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                System.out.print("|" + grid[row][col] + "|");
            }
            System.out.println();
        }
    }

    static boolean isWinner(char[][] grid) {
        // Check rows
        for (int row = 0; row < grid.length; row++) {
            if (grid[row][0] == grid[row][1] && grid[row][1] == grid[row][2]) {
                if (grid[row][0] == 'x' || grid[row][0] == 'o')
                    return true;
            }
        }

        // Check columns
        for (int col = 0; col < grid[0].length; col++) {
            if (grid[0][col] == grid[1][col] && grid[1][col] == grid[2][col]) {
                if (grid[0][col] == 'x' || grid[0][col] == 'o')
                    return true;
            }
        }

        // Check diagonals
        if ((grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2]) ||
                (grid[0][2] == grid[1][1] && grid[1][1] == grid[2][0])) {
            if (grid[1][1] == 'x' || grid[1][1] == 'o')
                return true;
        }

        return false;
    }

    static boolean isValidMove(char[][] grid, int row, int col) {
        return grid[row][col] != 'x' && grid[row][col] != 'o';
    }

    static void makeMove(char[][] grid, int row, int col, char symbol) {
        grid[row][col] = symbol;
    }

    public static void main(String[] args) {
        char[][] grid = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                grid[i][j] = '-';
            }
        }

        Scanner object = new Scanner(System.in);
        System.out.println("Tic Tac Toe Game: ");
        printGrid(grid);
        char currentPlayer = 'x';

        while (true) {
            System.out.println("Player " + currentPlayer + "'s turn.");
            System.out.print("Enter row (1-3): ");
            int row = object.nextInt() - 1; // Adjust for 0-based indexing
            System.out.print("Enter column (1-3): ");
            int col = object.nextInt() - 1; // Adjust for 0-based indexing

            if (row < 0 || row >= 3 || col < 0 || col >= 3) {
                System.out.println("Invalid position. Please try again.");
                continue;
            }

            if (!isValidMove(grid, row, col)) {
                System.out.println("Position already occupied. Please try again.");
                continue;
            }

            makeMove(grid, row, col, currentPlayer);
            printGrid(grid);

            if (isWinner(grid)) {
                System.out.println("Player " + currentPlayer + " wins!");
                break;
            }

            // Switch player
            currentPlayer = (currentPlayer == 'x') ? 'o' : 'x';
        }

        object.close(); // Close the Scanner to prevent resource leak
    }
}
