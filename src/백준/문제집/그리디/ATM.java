import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class ATM {
    /** answer
     *  32
     */
    static int n;
    static int[] p;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\ATM.txt"
                )
        );

        n = Integer.parseInt(br.readLine());

        p = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(p);

//        System.out.println(Arrays.toString(p));

        int time = 0;
        int result = 0;
        for (int i = 0; i < n; i ++) {
//            System.out.printf("%d + %d = %d -> ", time, p[i], time + p[i]);
            time = time + p[i];
            result += time;
//            System.out.println(time);
        }
        System.out.println(result);
    }
}
