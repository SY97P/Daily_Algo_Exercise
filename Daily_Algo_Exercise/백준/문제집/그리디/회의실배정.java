import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

public class 회의실배정 {
    /**
     * answer
     * 4
     */

    static int n;
    static Schedule[] schedules;

    static class Schedule implements Comparable<Schedule> {
        int start;
        int end;

        Schedule(int s, int e) {
            this.start = s;
            this.end = e;
        }

        @Override
        public int compareTo(Schedule o) {
            return Integer.compare(this.end, o.end) == 0 ? Integer.compare(this.start, o.start) : Integer.compare(this.end, o.end);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "D:\\git\\IdeaProjects\\Daily_Algo_Exercise\\백준\\문제집\\그리디\\회의실배정.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        schedules = new Schedule[n];

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            schedules[i] = new Schedule(Integer.parseInt(line[0]), Integer.parseInt(line[1]));
        }

        Arrays.sort(schedules);

//        for (int i = 0; i < n; i ++) {
//            System.out.println(schedules[i].start + " " + schedules[i].end);
//        }

        int time = 0;
        int count = 0;
        for (int i = 0; i < n; i ++) {
            if (time <= schedules[i].start) {
                time = schedules[i].end;
                count ++;
            }
        }
        System.out.println(count);
    }
}
