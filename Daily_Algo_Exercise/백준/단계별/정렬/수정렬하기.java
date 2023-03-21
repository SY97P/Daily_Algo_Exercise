import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 수정렬하기 {
    final static boolean isInsertSort = true;

    static int n;
    static int[] list;
    static int lastIdx = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\정렬\\수정렬하기.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        list = new int[n];

        for (int i = 0; i < n; i++) {
            list[i] = Integer.MAX_VALUE;
        }

        for (int i=0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            if (isInsertSort)
                insertSort(num);
            else
                list[i] = num;
        }

        if (!isInsertSort) {
            bubbleSort();
        }

        for (int l : list) {
            System.out.println(l);
        }
    }

    private static void insertSort(int num) {
//        System.out.println("삽입정렬");
        for (int i=0; i < n; i++) {
            if (list[i] == Integer.MAX_VALUE) {
                list[i] = num;
                break;
            } else if (num < list[i]) {
                for (int j = lastIdx; j > i; j--) {
                    list[j] = list[j-1];
                }
                list[i] = num;
                break;
            }
        }
        lastIdx ++;
    }

    private static void bubbleSort() {
//        System.out.println("거품정렬");
        for (int i =0; i < n-1; i ++) {
            for (int j=i+1; j < n; j++) {
                if (list[i] > list[j]) {
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }
    }
}
