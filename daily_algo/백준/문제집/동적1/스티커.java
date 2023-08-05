import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 스티커 {
    /**
     * answer
     * 260
     * 290
     */
    static int t;
    static int n;
    static int[][] matrix;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\스티커.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        t = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < t; tc ++) {
            n = Integer.parseInt(br.readLine());

            matrix = new int[2][n+1];

            for (int i = 0; i < 2; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 1; j <= n; j++) {
                    matrix[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            dp = new int[2][n+1];
            dp[0][1] = matrix[0][1];
            dp[1][1] = matrix[1][1];

            solve();

            System.out.println(Math.max(dp[0][n], dp[1][n]));

//            printDP();
        }
    }

    private static void solve() {
        for (int j = 2; j <= n; j++) {
            for (int i = 0; i < 2; i ++) {
                dp[i][j] = matrix[i][j] + Math.max(dp[i][j-2], Math.max(dp[(i+1)%2][j-1], dp[(i+1)%2][j-2]));
            }
        }
    }

    private static void printDP() {
        for (int[] d : dp) {
            System.out.println(Arrays.toString(d));
        }
    }
}
