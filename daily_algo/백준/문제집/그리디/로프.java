import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 로프 {
    /** answer
     * 20
     */
    static int n;
    static int[] ropes;
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\로프.txt"
                )
        );

        n = Integer.parseInt(br.readLine());

        ropes = new int[n];

        for (int i = 0;i < n; i++) {
            ropes[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(ropes);

        for (int i = 0; i < n; i ++) {
            result = Math.max(result, (n-i)*ropes[i]);
        }

        System.out.println(result);
    }
}
