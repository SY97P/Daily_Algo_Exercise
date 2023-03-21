import java.io.BufferedReader;
// import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class 행렬곱셈순서 {

	static int n;
	static int[][] dp;
	static int[][] mat;
	
	public static void main(String[] args) throws Exception {
		// BufferedReader br = new BufferedReader(new FileReader("./백준/dp/lv2/행렬곱셈순서.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(br.readLine());
		mat = new int[n][2];

		for (int i = 0; i < n; i ++) {
			String[] line = br.readLine().split(" ");
			mat[i][0] = Integer.parseInt(line[0]);
			mat[i][1] = Integer.parseInt(line[1]);

			// System.out.println(mat[i][0] + " " + mat[i][1]);
		}

		dp = new int[n][n];

		System.out.println(solve());
	}

	public static int solve() {
		for (int d = 1; d < n; d ++) {
			for (int i = 0; i < n - d; i++) {
				int j = i + d;
				ArrayList<Integer> temp = new ArrayList<>();
				for (int k = i; k < j; k ++) {
					temp.add(dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k][1] * mat[j][1]);
				}
				dp[i][j] = Collections.min(temp);
			}
		}
		return dp[0][n-1];
	}
}