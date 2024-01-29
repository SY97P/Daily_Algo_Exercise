package 빈출알고리즘.문자열탐색.크모프;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class kmp {
    static int m;
    static String[] t;
    static int l;
    static String[] p;
    static int[] pi;

    static int count;
    static ArrayList<Integer> loc;

    // Answer
    // 2
    // 1 8
    // 2
    // 1 5
    // 1
    // 16

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(
           "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\문자열알고리즘1\\찾기.txt"
        ));

        t = br.readLine().split("");
        p = br.readLine().split("");

        m = t.length;
        l = p.length;

        pi = new int[l];
        loc = new ArrayList<>();

        failureFunc();

        System.out.println(Arrays.toString(pi));

        kmp();

        System.out.println(count);
        System.out.println(Arrays.toString(loc.toArray()));
    }

    private static void failureFunc() {
        int j = 0;
        for (int i = 1; i < l; i ++) {
            while (j > 0 && !p[i].equals(p[j]))
                j = pi[j-1];
            if (p[i].equals(p[j])) {
                j += 1;
                pi[i] = j;
            }
        }
    }

    private static void kmp() {
        int j = 0;
        for (int i = 0; i < m; i ++) {
            while (j > 0 && !t[i].equals(p[j]))
                j = pi[j-1];
            if (t[i].equals(p[j])) {
                j += 1;
                if (j == l) {
                    count += 1;
                    loc.add(i-l+2);
                    j = pi[j-1];
                }
            }
        }
    }
}
