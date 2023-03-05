//FELIPE OLIVEIRA DO ESPIRITO SANTO / NUSP: 11925242//GUSTAVO FREIRE / NUSP: 11839927
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class filaDeSupermercado {
    public static void main(String[] args) throws IOException {

        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader input = new BufferedReader(ir);

        //armazenando as tres linhas de entrada
        String[] entrada = input.readLine().split(" ");
        int N = Integer.parseInt(entrada[0]);
        int M = Integer.parseInt(entrada[1]);
        int[] velocidades = new int[N];
        int[] qtdeItens = new int[M];
        String[] entrada2 = input.readLine().split(" ");
        String[] entrada3 = input.readLine().split(" ");
        //con    
        for (int i = 0; i < N; i++) {
            velocidades[i] = Integer.parseInt(entrada2[i]);
        }
        for (int i = 0; i < M; i++) {
            qtdeItens[i] = Integer.parseInt(entrada3[i]);
        }
        int[] tempos = new int[N];
        int maiorTempo = 0;

        for (int i = 0; i < M; i++) {
            if (i < N) { // calcula o tempo para os primeiros funcionários até que o número de clientes ultrapasse o de funcionários
                tempos[i] = velocidades[i] * qtdeItens[i];

                if (maiorTempo < tempos[i])
                    maiorTempo = tempos[i];

            } else { // calcula o tempo para atender o restante dos clientes
                int tempoAtual = tempos[0];
                int temp = 0;

                for (int j = 0; j < N; j++) {
                    if (tempoAtual > tempos[j]) {
                        tempoAtual = tempos[j];
                        temp = j;
                    }
                }
                tempos[temp] += (velocidades[temp] * qtdeItens[i]);

                if (maiorTempo < tempos[temp])
                    maiorTempo = tempos[temp];

                temp = 0;
            }
        }
        System.out.println(maiorTempo);
    }
}
