import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 최소회의실개수 {
    /** answer
     * 2
     * 1
     */
    static int n;
    static Schedule[] schedules;

    static private class Schedule implements Comparable<Schedule> {
        int start;
        int end;
        Schedule(int s, int e) {
            this.start = s;
            this.end = e;
        }

        @Override
        public int compareTo(Schedule o) {
            return Integer.compare(this.start, o.start) == 0 ? Integer.compare(this.end, o.end) : Integer.compare(this.start, o.start);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\최소회의실개수.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 0; tc < 1; tc ++) {
            n = Integer.parseInt(br.readLine());

            schedules = new Schedule[n];

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                schedules[i] = new Schedule(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }

            Arrays.sort(schedules);

            int count = 0;
            PriorityQueue<Integer> pq = new PriorityQueue<>();

            pq.add(schedules[0].end);

//            for (int i = 0;i < n ;i ++) {
//                System.out.println(schedules[i].start + " " + schedules[i].end);
//            }
//            System.out.println();

            for (int i = 1; i < n; i ++) {
//                System.out.println(pq.peek() + " " + schedules[i].start);
                if (pq.peek() > schedules[i].start) {
                    pq.add(schedules[i].end);
                } else {
                    pq.poll();
                    pq.add(schedules[i].end);
                }
            }

            System.out.println(pq.size());
        }
    }
}
