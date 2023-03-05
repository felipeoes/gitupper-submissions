import java.util.Scanner;import java.util.TreeMap;
import java.util.LinkedList;
import java.util.Map;

public class URI1522 {
	static Map<String, Integer> mapa = new TreeMap<String, Integer>(); // mapa para guardar os caminhos visitados
	static int n;

	// metodo de entrada EOF modificado para o problema
	public static LinkedList<String> lerEntrada() {
		LinkedList<String> linhas = new LinkedList<String>();
		Scanner input = new Scanner(System.in);

		while (true) {
			String linha = input.nextLine();

			if (linha.length() == 1) {
				int n = Integer.parseInt(linha);
				if (n == 0)
					break; // quando encontra o 0 para o loop
			}
			linhas.add(linha);
		}
		input.close();
		return linhas;
	}

	// aux
	public static boolean ehMultiploDeTres(int n) {
		if ((n % 3) == 0)
			return (true);
		return (false);
	}

	public static boolean dfs(int topo1, int topo2, int topo3, int[] pilha1, int[] pilha2, int[] pilha3) {
		String string = "";
		int visitado;
		string += (topo1);
		string += (topo2);
		string += (topo3);

		if (topo1 == topo2 && topo2 == topo3 && topo3 == n) {
			mapa.put(string, 1);
			return true;
		}

		if (mapa.containsKey(string)) { // marcando a chave como visitada
			visitado = mapa.get(string);
		} else
			visitado = -1;

		if (visitado > 0) // verifica se a chave já foi visitado para evitar recursões desnecessárias
			return (visitado == 1 ? true : false);

		if (topo1 < n && ehMultiploDeTres(pilha1[topo1]) && dfs(topo1 + 1, topo2, topo3, pilha1, pilha2, pilha3)) {
			mapa.put(string, 1);
			return true;
		}
		if (topo2 < n && ehMultiploDeTres(pilha2[topo2]) && dfs(topo1, topo2 + 1, topo3, pilha1, pilha2, pilha3)) {
			mapa.put(string, 1);
			return true;
		}
		if (topo3 < n && ehMultiploDeTres(pilha3[topo3]) && dfs(topo1, topo2, topo3 + 1, pilha1, pilha2, pilha3)) {
			mapa.put(string, 1);
			return true;
		}
		if (topo1 < n && topo2 < n && ehMultiploDeTres(pilha1[topo1] + pilha2[topo2])
				&& dfs(topo1 + 1, topo2 + 1, topo3, pilha1, pilha2, pilha3)) {
			mapa.put(string, 1);
			return true;
		}
		if (topo1 < n && topo3 < n && ehMultiploDeTres(pilha1[topo1] + pilha3[topo3])
				&& dfs(topo1 + 1, topo2, topo3 + 1, pilha1, pilha2, pilha3)) {
			mapa.put(string, 1);
			return true;
		}
		if (topo2 < n && topo3 < n && ehMultiploDeTres(pilha2[topo2] + pilha3[topo3])
				&& dfs(topo1, topo2 + 1, topo3 + 1, pilha1, pilha2, pilha3)) {
			mapa.put(string, 1);
			return true;
		}
		if (topo1 < n && topo2 < n && topo3 < n && ehMultiploDeTres(pilha1[topo1] + pilha2[topo2] + pilha3[topo3])
				&& dfs(topo1 + 1, topo2 + 1, topo3 + 1, pilha1, pilha2, pilha3)) {
			mapa.put(string, 1);
			return true;
		}

		mapa.put(string, 2);
		return false;
	}

	public static void main(String[] args) {
		LinkedList<String> linhas = lerEntrada();
		Object[] linhasArray = linhas.toArray();

		int i = 0;
		// a ideia é que esse while faça cada caso de teste
		while (i < linhasArray.length) {
			String linha = String.valueOf(linhasArray[i]); // linha atual

			/*
			 * cada caso de teste sempre vai começar com o inteiro N (que identifica o
			 * número de cartas em cada pilha)
			 */
			n = Integer.parseInt(linha);

			// tres pilhas inicializadas (cada uma com N cartas)
			int[] pilha1 = new int[n];
			int[] pilha2 = new int[n];
			int[] pilha3 = new int[n];

			// formando as tres pilhas
			int indice = i;
			for (int j = n - 1; j >= 0; j--) {
				indice++;
				// armazenando a linha que contem os tre inteiros das tres pilhas
				String valoresString = String.valueOf(linhasArray[indice]);
				String[] valores = valoresString.split(" ");
				// salvando do topo para o fundo (da mesma forma que a entrada nos da os valores
				// das pilhas)
				pilha1[j] = Integer.parseInt(valores[0]);
				pilha2[j] = Integer.parseInt(valores[1]);
				pilha3[j] = Integer.parseInt(valores[2]);

			}

			// LOGICA DO JOGO COMEÇA AQUI
			if (dfs(0, 0, 0, pilha1, pilha2, pilha3))
				System.out.println(1);
			else
				System.out.println(0);

			mapa.clear();

			i = i + n + 1; // alterando o i para que ele começe na primeira linha do proximo caso de teste
		}
	}
}