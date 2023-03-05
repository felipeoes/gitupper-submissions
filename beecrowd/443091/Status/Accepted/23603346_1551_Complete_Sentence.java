/* * Desafio_3*/
import java.util.*;

public class Main {
    static final String alfabeto = "abcdefghijklmnopqrstuvwxyz";
    static final char[] chars = alfabeto.toCharArray();

    public static String checaFrase(String string) {
        int cont = 0;

        for (int j = 0; j < alfabeto.length(); j++) {
            String alfa = Character.toString(chars[j]);
            if (string.contains(alfa))
                cont++;
        }

        if (cont >= alfabeto.length())
            return ("frase completa");
        else if (cont >= alfabeto.length() / 2 && cont < alfabeto.length())
            return ("frase quase completa");

        return "frase mal elaborada";
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        List<String> results = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String frase = input.nextLine();
            results.add(checaFrase(frase));
        }

        for (String string : results) {
            System.out.println(string);
        }

        input.close();
    }
}