import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.Objects;
import java.util.StringTokenizer;
import java.io.IOException;

public class 광고 {
    static int n;
    static String[] text;
    static int[] pi;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(
           "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\문자열알고리즘1\\광고.txt"
        ));

        n = Integer.parseInt(br.readLine());
        text = br.readLine().split("");

        pi = new int[n];

        failureFunc();

        System.out.println(n - pi[n-1]);
    }

    private static void failureFunc() {
        int j = 0;
        for (int i = 1; i < n; i ++) {
            while (j > 0 && !Objects.equals(text[i], text[j]))
                j = pi[j-1];
            if (Objects.equals(text[i], text[j])) {
                j += 1;
                pi[i] = j;
            }
        }
    }
}
