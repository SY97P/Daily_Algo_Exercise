import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 호텔 {
    /** answer
     * 8
     * 4
     * 10
     * 45
     */
    static int c;
    static int n;
    static int[] cost;
    static int[] man;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\호텔.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        c = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        cost = new int[n+1];
        man = new int[n+1];

        dp = new int[n+1][c+1];

        for (int i = 1; i <= n; i ++) {
            st = new StringTokenizer(br.readLine());
            cost[i] = Integer.parseInt(st.nextToken());
            man[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= c; j++) {
                dp[i][j] = ((j-1) / man[i] + 1) * cost[i];
            }
        }
        for (int i = 0; i <= c; i++){
            dp[0][i] = Integer.MAX_VALUE;
        }
        for (int i = 0; i <= n; i++) {
            dp[i][0] = Integer.MAX_VALUE;
        }

        solve();

        System.out.println(dp[n][c]);

//        for (int[] d : dp)
//            System.out.println(Arrays.toString(d));
    }

    private static void solve() {
        for (int j = 1; j <= c; j ++) {
            for (int i = 1; i <= n; i++) {
                if (j - man[i] >= 0 && dp[i-1][j-man[i]] != Integer.MAX_VALUE)
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j-man[i]] + cost[i]);
                if (dp[i][j] < dp[i-1][j])
                    dp[i-1][j] = dp[i][j];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
    }
}
