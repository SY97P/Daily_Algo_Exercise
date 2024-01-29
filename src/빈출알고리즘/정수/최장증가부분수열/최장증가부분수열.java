package 빈출알고리즘.정수.최장증가부분수열;

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class 최장증가부분수열 {
    static int n;
    static int[] a;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\동적1\\가장긴증가하는부분수열.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        a = new int[n+1];
        dp = new int[n+1];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i =1 ; i <= n; i ++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        lis();

        int maxValue = 0;
        for (int i = 1; i <= n; i++) {
            if (maxValue < dp[i])
                maxValue = dp[i];
        }
        System.out.println(maxValue);
//        printDP();
    }

    private static void lis() {
        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (a[j] < a[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
    }

    private static void printDP() {
        for (int al: a) {
            System.out.print(al + " ");
        }
        System.out.println();
        for (int d: dp) {
            System.out.print(d + "  ");
        }
    }
}
