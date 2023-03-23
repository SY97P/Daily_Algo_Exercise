import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 블로그2 {
    /**
     * answer
     * 4
     * 1
     */
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\블로그2.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        for (int tc = 0; tc < 3; tc ++) {
            n = Integer.parseInt(br.readLine());

            String line = br.readLine();

            int result = 1;

            int count_b = 0;
            int count_r = 0;

            char prev = line.charAt(0);
            if (prev == 'B')
                count_b ++;
            else
                count_r ++;
            for (int i = 1; i < n; i ++) {
                if (prev != line.charAt(i)) {
                    if (line.charAt(i) == 'B')
                        count_b ++;
                    else
                        count_r ++;
                    prev = line.charAt(i);
                }
            }

            if (line.charAt(0) != line.charAt(n-1))
                System.out.println(Math.max(count_b, count_r) + 1);
            else
                System.out.println(Math.max(count_b, count_r));
        }
    }
}
