import java.text.DecimalFormat;import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int testCases = s.nextInt();
		s.nextLine();

		Map<String, Integer> trees = new TreeMap<>();
		int totalTrees;
		StringBuilder resultsOutput = new StringBuilder();
		DecimalFormat df = new DecimalFormat();
		df.setMaximumFractionDigits(4);

		for (int i = 0; i < testCases; i++) {
			totalTrees = 0;
			String currLine = s.nextLine();
			while (!currLine.equals("")) {
				trees.put(currLine, trees.getOrDefault(currLine, 0) + 1);
				totalTrees++;

				currLine = s.nextLine();
			}
			for (Map.Entry<String, Integer> e : trees.entrySet()) {
				double percentage = ((double) e.getValue() * 100) / totalTrees;
				resultsOutput.append(e.getKey() + " " + String.format("%.4f", percentage) + "\n");
			}
			resultsOutput.append("\n");
			trees.clear();
		}
		s.close();
		String finalString = resultsOutput.toString().replace(",", ".");
		System.out.println(finalString);
	}
}