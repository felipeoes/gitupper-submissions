import java.io.IOException; 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
        int[] numbers = [7,14,106];
        int maior = numbers[0];
        
        for int number in numbers {
            if(number > maior)
            maior = number;
        }
        
        System.out.println(maior + " eh o maior")
    }
 
}