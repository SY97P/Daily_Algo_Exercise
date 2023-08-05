import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class 알바생강호 {
    /** answer
     * 6
     * 5
     * 30
     * 2
     * 4
     */
    static int n;
    static int[] tips;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\알바생강호.txt"
                )
        );

        for (int tc = 0; tc < 1; tc ++) {
            long result = 0L;

            n = Integer.parseInt(br.readLine());

            tips = new int[n];

            for (int i = 0; i < n; i++) {
                tips[i] = Integer.parseInt(br.readLine());
            }

            Integer[] temp = Arrays.stream(tips).boxed().toArray(Integer[]::new);
            Arrays.sort(temp, Comparator.reverseOrder());

            for (int i = 0; i < n; i++) {
                long benefit = temp[i] - i;
                if (benefit > 0)
                    result += benefit;
//                System.out.printf("%d -> %d = %d - %d -> %d", i, benefit, temp[i], i, result);
//                System.out.println();
            }

            System.out.println(result);
        }
    }
}
