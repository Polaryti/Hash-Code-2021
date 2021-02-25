package src;

import java.io.FileNotFoundException;
import java.io.IOException;
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
}
