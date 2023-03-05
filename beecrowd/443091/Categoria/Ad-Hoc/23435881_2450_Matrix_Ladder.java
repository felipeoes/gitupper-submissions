import java.io.IOException;import java.util.Scanner;

/*
 Uma matriz está na forma escada quando, para cada linha, as condições a seguir forem satisfeitas:

* Se a linha só possuir zeros, então todas as linhas abaixo desta também só possuem zeros. (CONDICAO 1)

* Caso contrário, seja X o elemento diferente de zero mais à esquerda da linha; então, para todas as linhas 
    abaixo da linha de X, todos os elementos nas colunas à esquerda de X e na coluna de X são iguais a zero.
    (CONDICAO 2)
 */
public class Main {

    // funcao auxiliar que verifica se uma linha da matriz só possui zeros
    static boolean verificaZeros(int[][] matriz, int i, int nColunas) {

        for (int j = 0; j < nColunas; j++) {
            if (matriz[i][j] != 0)
                return false;
        }

        return true;
    }

    // funcao auxiliar que retorna o indice da coluna do elemento diferente de zero
    // mais à esquerda da linha
    static int pegaMaiorESquerda(int[][] matriz, int i, int nColunas) {
        int coluna = 0;

        for (int j = 0; j < nColunas; j++) {
            int elem = matriz[i][j];
            if (elem != 0) {
                coluna = j;
                break;
            }
        }

        return coluna;
    }

    static boolean ehMatrizEscada(int[][] matriz, int nLinhas, int nColunas) {
        boolean condicao1 = false;
        // boolean condicao2 = false;

        // para cada linha
        for (int i = 0; i < nLinhas; i++) {
            condicao1 = verificaZeros(matriz, i, nColunas); // começo verificando se é uma linha de zeros

            // a linha só possui zeros
            if (condicao1) {
                // vamos verificar para todas linhas abaixo
                for (int linha = i + 1; linha < nLinhas; linha++) {
                    condicao1 = verificaZeros(matriz, linha, nColunas);
                    if (!condicao1)
                        return false; // uma linha não possui só zeros: não é matriz escada
                }

                if (condicao1)
                    return true; // é matriz escada pois todas as linhas abaixo sao de zeros
            }

            // não é uma linha só de zeros: condicao 2 precisa ser verificada
            else {
                // pegando o indice da coluna de X (elemento diferente de zero mais à esquerda
                // da linha)
                int col = pegaMaiorESquerda(matriz, i, nColunas);

                if (col == 0)
                    continue;

                for (int j = 0; j <= col && i < nLinhas - 1; j++) {
                    if (matriz[i + 1][j] != 0)
                        return false;
                }
            }

        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int nLin = sc.nextInt();
        int nCol = sc.nextInt();
        int[][] matriz = new int[nLin][nCol];
        sc.nextLine();

        for (int i = 0; i < nLin; i++) {
            String linha = sc.nextLine();
            String[] valores = linha.split(" ");

            for (int j = 0; j < nCol; j++) {
                matriz[i][j] = Integer.parseInt(valores[j]);
            }
        }

        boolean verifica = ehMatrizEscada(matriz, nLin, nCol);
        if (verifica)
            System.out.println("S");
        else
            System.out.println("N");

        sc.close();
    }

}