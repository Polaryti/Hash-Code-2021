package src;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Example {

    public void readCompetitionFile() {
        String filePath = "";
        Scanner sc = new Scanner(filePath);

        String line;
        String token; // int token; [...]
        while (sc.hasNextLine()) {
            line = sc.nextLine();
            while (sc.hasNext()) {
                token = sc.next();
                // token = sc.nextInt();
                // token = sc.nextDouble();
                // [...]
                // Procesar cada token como se deba y añadirlo a una estructura de datos u algo
            }
        }

        sc.close();
    }

    public void writeCompetitionFile() throws FileNotFoundException {
        String filePath = "";
        int[][] exampleData = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 } };
        PrintWriter pw = new PrintWriter(filePath);

        String line;
        for (int[] row : exampleData) {
            line = "";
            for (int data : row) {
                line += Integer.toString(data) + " ";
            }
            pw.println(line.trim());
        }

        pw.close();
    }
}
