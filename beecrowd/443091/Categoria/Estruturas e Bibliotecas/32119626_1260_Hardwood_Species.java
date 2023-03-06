import java.util.*;import java.io.*;

public class Desafio_3 {
    public static void main(String[] args) {
        try (Scanner s = new Scanner(System.in)) {
            int testCases = s.nextInt();
            s.nextLine();
            s.nextLine();

            Map<String, Integer> trees = new TreeMap<>();
            int totalTrees;
            StringBuilder resultsOutput = new StringBuilder();
            int aux = 0;

            for (int i = 0; i < testCases; i++) {
                totalTrees = 0;
                String currLine = s.nextLine();
                while (!currLine.isEmpty()) {
                    trees.put(currLine, trees.getOrDefault(currLine, 0) + 1);
                    totalTrees++;

                    if (s.hasNextLine()) {
                        currLine = s.nextLine();
                    } else {
                        break;
                    }
                }

                Object[] arrayEntry = trees.entrySet().toArray();
                for (Map.Entry<String, Integer> e : trees.entrySet()) {
                    double percentage = ((double) e.getValue() * 100) / totalTrees;
                    resultsOutput.append(e.getKey() + " " + String.format("%.4f", percentage));
                    if (!e.equals(arrayEntry[arrayEntry.length - 1])) {
                        resultsOutput.append("\n");
                    }
                }

                if (aux == 0) {
                    resultsOutput.append("\n");
                    aux++;
                }
                if (i != (testCases - 1)) {
                    resultsOutput.append("\n");
                }
            }

            String linha = "\n";
            String finalString = linha + resultsOutput.toString().replace(",", ".");
            resultsOutput.setLength(resultsOutput.length() - 1);
            System.out.println(finalString);
        }
    }
}
