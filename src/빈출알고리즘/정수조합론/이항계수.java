package 빈출알고리즘.정수조합론;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileReader;

public class 이항계수 {
    final static long P = 100000007L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\분할정복\\이항계수3.txt"
                )
        );

        String[] line = br.readLine().split(" ");

        int n = Integer.parseInt(line[0]);
        int k = Integer.parseInt(line[1]);

        long numerator = factorial(n);
        long denominater = pow(factorial(k) * factorial(n-k), P-2);

        System.out.println(numerator * denominater % P);
    }

    private static long factorial(int n) {
        long result = 1L;
        while (n > 1){
            result = (result * n) % P;
            n --;
        }
        return result;
    }

    private static long pow(long a, long b) {
        if (b <= 1)
            return a % P;

        long result = pow(a, b/2);
        if (b % 2 != 0)
            return (result * result % P) * (a % P);
        return result * result % P;
    }
}