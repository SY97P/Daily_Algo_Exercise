import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 점프 {
    /**
     * answer
     * 3
     */
    static int n;
    static int[][] matrix;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\점프.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        matrix = new int[n][n];

        for (int i = 0; i < n ;i ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j ++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp = new int[n][n];

        dp[0][0] = 1;

        solve();

        System.out.println(Integer.MAX_VALUE == (int) Math.pow(2, 64));

        System.out.println(dp[n-1][n-1]);

        printDP();
    }

    private static void solve() {
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] != 0 && dp[i][j] != 0) {
                    // 오른쪽
                    if (j + matrix[i][j] < n)
                        dp[i][j+matrix[i][j]] += dp[i][j];
                    // 아래쪽
                    if (i + matrix[i][j] < n)
                        dp[i+matrix[i][j]][j] += dp[i][j];
                }
            }
        }
    }

    private static void printDP() {
        for (int[] d : dp) {
            System.out.println(Arrays.toString(d));
        }
    }
}
