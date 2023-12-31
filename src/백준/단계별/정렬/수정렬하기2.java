import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.PriorityQueue;

public class 수정렬하기2 {
    final static boolean isMergeSort = false;

    static int n;
    static int[] alist;
    static int[] sorted;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\정렬\\수정렬하기.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        alist = new int[n];
        sorted = new int[n];

        for (int i = 0; i < n; i++) {
            alist[i] = Integer.parseInt(br.readLine());
        }

        if (isMergeSort) {
//            System.out.println("병합정렬");
            mergeSort(0, n - 1);
        } else {
//            System.out.println("힙정렬");
            heapSort();
        }

        for (int s : sorted)
            System.out.println(s);
    }

    private static void mergeSort(int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            mergeSort(start, mid);
            mergeSort(mid + 1, end);

            int p = start;
            int q = mid + 1;
            int idx = start;

            while (p <= mid || q <= end) {
                if (q > end || (p <= mid && alist[p] <= alist[q])) {
                    sorted[idx++] = alist[p++];
                } else if (p > mid || (q <= end && alist[p] > alist[q])) {
                    sorted[idx++] = alist[q++];
                }
            }

            for (int i = start; i <= end; i++) {
                alist[i] = sorted[i];
            }

//            for (int s: sorted)
//                System.out.print(s);
//            System.out.println();
        }
    }

    private static void heapSort() {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i ++) {
            pq.add(alist[i]);
        }

        int idx = 0;
        while (!pq.isEmpty()) {
            sorted[idx++] = pq.poll();
        }
    }
}
