import java.util.*;
public class Problema_1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int count = 0;
            String resp = "";
            String line = input.nextLine();
            char[] c = line.toCharArray();
            for (char cc : c) {
                if (cc == ' ') continue;
                    if (cc=='G' || cc=='Q' || cc=='a' || cc=='k' || cc=='u') {
                        resp += '0';
                    }
                    if (cc=='I' || cc=='S' || cc=='b' || cc=='l' || cc=='v') {
                        resp += '1';
                    }if (cc=='E' || cc=='O' || cc=='Y' || cc=='c' || cc=='m' || cc=='w') {
                        resp += '2';
                    }if (cc=='F' || cc=='P' || cc=='Z' || cc=='d' || cc=='n' || cc=='x') {
                        resp += '3';
                    }if (cc=='J' || cc=='T' || cc=='e' || cc=='o' || cc=='y') {
                        resp += '4';
                    }if (cc=='D' || cc=='N' || cc=='X' || cc=='f' || cc=='p' || cc=='z') {
                        resp += '5';
                    }if (cc=='A' || cc=='K' || cc=='U' || cc=='g' || cc=='q') {
                        resp += '6';
                    }if (cc=='C' || cc=='M' || cc=='Y' || cc=='r' || cc=='h') {
                        resp += '7';
                    }if (cc=='B' || cc=='L' || cc=='V' || cc=='i' || cc=='s') {
                        resp += '8';
                    }if (cc=='H' || cc=='R' || cc=='j' || cc=='t') {
                        resp += '9';
                    }
                    count++;
                    
                    if (count == 12) {
                        result.add(resp);
                        break;
                    }
            }
            
        }
        for (String string : result) {
            System.out.println(string);
        }

        input.close();

    }
}