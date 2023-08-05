package SWEA.D3;

import java.util.ArrayList;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class Knapsack01 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("./SWEA/D3/Knapsack01.txt"));

		int t = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= t; tc++) {
			String[] line = br.readLine().split(" ");
			// System.out.println(Arrays.toString(line));
			int n = Integer.parseInt(line[0]); 
			int k = Integer.parseInt(line[1]);
			// System.out.println(n + " " + k);

		 	ArrayList<float[]> things = new ArrayList<>(n);

			for (int h = 0; h < n; h ++) {
				line = br.readLine().split(" ");
				int v = Integer.parseInt(line[0]);
				int c = Integer.parseInt(line[1]);
				things.add(new float[]{c/v, v, c});
			}
		}

		br.close();
	}
}