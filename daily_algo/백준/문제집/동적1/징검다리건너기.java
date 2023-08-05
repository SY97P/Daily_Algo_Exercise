import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 징검다리건너기 {
    static int n;
    static int[] small;
    static int[] big;
    static int k;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\징검다리건너기.txt"
                )
        );

        n = Integer.parseInt(br.readLine());

        small = new int[n-1];
        big = new int[n-1];

        dp = new int[2][n];

        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[1][i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            small[i] = Integer.parseInt(st.nextToken());
            big[i] = Integer.parseInt(st.nextToken());
        }

        k = Integer.parseInt(br.readLine());

        solve();

        System.out.println(Math.min(dp[0][n-1], dp[1][n-1]));

//        for (int[] d: dp)
//            System.out.println(Arrays.toString(d));

//        System.out.println(Arrays.toString(small));
//        System.out.println(Arrays.toString(big));
    }

    private static void solve() {
        for (int i = 0 ; i < n-1; i ++) {
            if (i + 1 < n) {
                dp[0][i+1] = Math.min(dp[0][i+1], dp[0][i] + small[i]);
                dp[1][i+1] = Math.min(dp[1][i+1], small[i] + Math.min(dp[1][i], dp[0][i]));
            }
            if (i + 2 < n) {
                dp[0][i+2] = Math.min(dp[0][i+2], dp[0][i] + big[i]);
                dp[1][i+2] = Math.min(dp[1][i+2], big[i] + Math.min(dp[1][i], dp[0][i]));
            }
            if (i + 3 < n) {
                dp[1][i + 3] = Math.min(dp[1][i + 3], dp[0][i] + k);
            }
        }
    }
}
