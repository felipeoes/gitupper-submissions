import java.util.Scanner;import java.util.LinkedList;

public class Main {
  public static LinkedList<String> readFromStdin() {
    LinkedList<String> total = new LinkedList<String>();

    Scanner sc = new Scanner(System.in);
    while (sc.hasNextLine()) {
      total.add(sc.nextLine());
    }
    sc.close();

    return total;
  }

  static boolean calculaPrimo(int num) {
    if(num == 0 || num == 1) return false;
    
    for (int i = 2; i < num; i++) {
      if ((num % i) == 0) {
        return false;
      }
    }
    return true;
  }

  static boolean calculaPrimoAux(int num) {
    if (num > 10) {

      String strNum = Integer.toString(num);
      int[] algarismos = new int[strNum.length()];
      for (int i = 0; i < strNum.length(); i++) {
        algarismos[i] = Character.getNumericValue(strNum.charAt(i));
      }
      for (int i = 0; i < algarismos.length; i++) {
        if (!calculaPrimo(algarismos[i]) || algarismos[i] == 0 || algarismos[i] == 1)
          return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    LinkedList<String> linhas = readFromStdin();
    int num = 0;
    for (String l : linhas) {
      num = Integer.parseInt(l);
      if (calculaPrimo(num)) {
        if (calculaPrimoAux(num)) {
          System.out.println("Super");
          continue;
        }
        System.out.println("Primo");
        continue;
      }
      System.out.println("Nada");
    }
  }

}