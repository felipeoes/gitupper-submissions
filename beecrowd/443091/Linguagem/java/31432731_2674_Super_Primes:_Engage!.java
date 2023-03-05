import java.util.Scanner;import java.util.LinkedList;

public class Main {
  public static LinkedList<Integer> readFromStdin() {
    LinkedList<Integer> numbers = new LinkedList<Integer>();

    Scanner sc = new Scanner(System.in);
    while (sc.hasNextLine()) {
      String line = sc.nextLine();
      if (line.equals("")) {
        break;
      }
      try {
        int num = Integer.parseInt(line);
        numbers.add(num);
      } catch (NumberFormatException e) {
        // ignore invalid input
      }
    }
    sc.close();

    return numbers;
  }

  static boolean isPrime(int num) {
    if (num < 2) {
      return false;
    }
    for (int i = 2; i <= Math.sqrt(num); i++) {
      if ((num % i) == 0) {
        return false;
      }
    }
    return true;
  }

  static boolean isSuperPrime(int num) {
    if (!isPrime(num)) {
      return false;
    }
    while (num > 0) {
      int digit = num % 10;
      if (!isPrime(digit)) {
        return false;
      }
      num /= 10;
    }
    return true;
  }

  public static void main(String[] args) {
    LinkedList<Integer> numbers = readFromStdin();
    for (int num : numbers) {
      if (isSuperPrime(num)) {
        System.out.println("Super");
      } else if (isPrime(num)) {
        System.out.println("Primo");
      } else {
        System.out.println("Nada");
      }
    }
  }
}
