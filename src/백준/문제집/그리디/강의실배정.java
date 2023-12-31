import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.PriorityQueue;

public class 강의실배정 {
    /** answer
     * 2
     */
    static int n;
    static Schedule[] schedules;
    static PriorityQueue<Long> room;

    private static class Schedule implements Comparable<Schedule> {
        long start;
        long end;
        Schedule(long s, long e) {
            this.start = s;
            this.end = e;
        }

        @Override
        public int compareTo(Schedule o) {
            return Long.compare(this.start, o.start) == 0 ? Long.compare(this.end, o.end) : Long.compare(this.start, o.start);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\강의실배정.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        schedules = new Schedule[n];

        for (int i = 0; i < n; i ++) {
            String[] line = br.readLine().split(" ");
            schedules[i] = new Schedule(Long.parseLong(line[0]), Long.parseLong(line[1]));
        }

        Arrays.sort(schedules);

        room = new PriorityQueue<>();
        room.add(schedules[0].end);

        for (int i = 1; i < n; i ++) {
            if (schedules[i].start < room.peek()) {
                room.add(schedules[i].end);
            } else {
                room.poll();
                room.add(schedules[i].end);
            }
        }

        System.out.println(room.size());
    }
}