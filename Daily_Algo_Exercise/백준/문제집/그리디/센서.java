import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 센서 {
    /** answer
     * 5
     * 7
     */
    static int n;
    static int k;
    static long[] sensors;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\센서.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        sensors = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        Arrays.sort(sensors);

//        System.out.println(Arrays.toString(sensors));

        long[] diff = new long[n-1];

        for (int i = 0; i < n-1; i ++) {
            diff[i] = sensors[i+1] - sensors[i];
        }

        Arrays.sort(diff);

        long result = 0;
        for (int i = 0; i < n-k; i++) {
            result += diff[i];
        }
        System.out.println(result);
    }
}
