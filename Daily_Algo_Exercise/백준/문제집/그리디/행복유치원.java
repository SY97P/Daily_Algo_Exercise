import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 행복유치원 {
    /** answer
     * 3
     */
    static int n;
    static int k;
    static int[] diff;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\행복유치원.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");
        n = Integer.parseInt(line[0]);
        k = Integer.parseInt(line[1]);

        diff = new int[n-1];

        line = br.readLine().split(" ");
        for (int i = 0; i < n-1; i++) {
            diff[i] = Integer.parseInt(line[i+1]) - Integer.parseInt(line[i]);
        }

        Arrays.sort(diff);

        long result = 0;
        for (int i = 0; i < n-k; i++ ){
            result += diff[i];
        }

        System.out.println(result);
    }
}
