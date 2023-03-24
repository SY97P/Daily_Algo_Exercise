import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 꿀따기 {
    /** answer
     * 57
     * 54
     * 10
     */
    static int n;
    static long[] sum;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\꿀따기.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 3; tc ++) {
            n = Integer.parseInt(br.readLine());

            String[] line = br.readLine().split(" ");
            int[] temp = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                temp[i] = Integer.parseInt(line[i - 1]);
            }

            sum = new long[n + 1];
            sum[1] = temp[1];

            for (int i = 2; i <= n; i++) {
                sum[i] = sum[i - 1] + temp[i];
            }

//        System.out.println(Arrays.toString(sum));

            long result = 0;
            for (int i = 2; i < n; i++) {
                // 1. 벌벌꿀
                result = Math.max(result, (sum[n] - temp[1] - temp[i]) + (sum[n] - sum[i]));
                // 2. 벌꿀벌
                result = Math.max(result, (sum[i] - temp[1]) + (sum[n] - sum[i - 1] - temp[n]));
                // 3. 꿀벌벌
                result = Math.max(result, (sum[i - 1]) + (sum[n] - temp[i] - temp[n]));
            }
            System.out.println(result);
        }
    }
}
