package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * 문제요약
 *
 * 셔틀버스 규칙
 *  09:00 부터 n 회 t 분 간격으로 역에 도착
 *  한 셔틀에 최대 m 명의 승객 탑승 가능
 *  셔틀 도착시간가지 포함한 시간에 역에 존재하는 크루 순서대로 태우고 바로 출발 (09:00 도착 -> 바로 탑승 가능)
 *  모든 크루는 23:59에 집에 들어가서 어떤 크루도 다음날 셔틀을 타는 일 없음
 * 콘이 셔틀을 타고 사무실로 갈 수 있는 가장 늦은 시간 구하기
 *
 * 제한사항
 *
 * 0 < 셔틀 운행 횟수 n <= 10
 * 0 < 셔틀 운행 간격 t <= 60
 * 0 < 셔틀 탑승 가능 최대 크루 수 m <= 45
 * 1 <= 크루 도착 정보 수 <+ 2_000
 * 00:01 <= 크루 도착 시간 <= 23:59
 *
 * 해결전략
 *
 * 시간문자열 <-> 분단위 정수 변환 함수 선언
 * timetables 정렬
 * 00:00 ~ 24:00 DP에 각 timetable 누적합을 구함
 * 셔틀 운행 시간마다 dp 값과 비교해서 정답구하기
 *  dp < m 이면 -> 운행 시간에 도착해도 됨
 *  dp >= m 이면 -> 방금전에 dp 값을 m 으로 만든 크루보다 1분 먼저 역에 도착해야 함
 */

public class 셔틀버스 {

    private static class Solution {
        public String solution(int n, int t, int m, String[] timetable) {
            int answer = 0;

            List<Integer> arrivalTime = convertToArrivalTime(timetable);

            int index = 0;
            int count = 0;
            int busTime = convertToTime("09:00");

            for (int iter = 0; iter < n; iter ++) {
                while (index < arrivalTime.size() && arrivalTime.get(index) <= busTime) {
                    count ++;
                    index ++;
                    if (count >= m) {
                        answer = arrivalTime.get(index - 1) - 1;
                        break;
                    }
                }

                if (count < m) {
                    answer = busTime;
                }

                count = 0;
                busTime += t;
            }

            return convertToTime(answer);
        }

        private List<Integer> convertToArrivalTime(String[] timetable) {
            List<Integer> arrivalTime = new ArrayList<>();
            for (String time : timetable) {
                arrivalTime.add(convertToTime(time));
            }
            arrivalTime.sort(Integer::compareTo);
            return arrivalTime;
        }

        private int convertToTime(String time) {
            String[] split = time.split(":");
            return Integer.parseInt(split[0]) * 60 + Integer.parseInt(split[1]);
        }

        private String convertToTime(int time) {
            return String.format("%02d:%02d", time / 60, time % 60);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // "09:00"
        String solution1 = solution.solution(1, 1, 5, new String[]{"08:00", "08:01", "08:02", "08:03"});
        if (!Objects.equals(solution1, "09:00")) {
            System.out.println("solution1 = " + solution1);
        }

        // "09:09"
        String solution2 = solution.solution(2, 10, 2, new String[]{"09:10", "09:09", "08:00"});
        if (!Objects.equals(solution2, "09:09")) {
            System.out.println("solution2 = " + solution2);
        }

        // "08:59"
        String solution3 = solution.solution(2, 1, 2, new String[]{"09:00", "09:00", "09:00", "09:00"});
        if (!Objects.equals(solution3, "08:59")) {
            System.out.println("solution3 = " + solution3);
        }

        // "00:00"
        String solution4 = solution.solution(1, 1, 5, new String[]{"00:01", "00:01", "00:01", "00:01", "00:01"});
        if (!Objects.equals(solution4, "00:00")) {
            System.out.println("solution4 = " + solution4);
        }

        // "09:00"
        String solution5 = solution.solution(1, 1, 1, new String[]{"23:59"});
        if (!Objects.equals(solution5, "09:00")) {
            System.out.println("solution5 = " + solution5);
        }

        // "18:00"
        String solution6 = solution.solution(10, 60, 45, new String[]{"23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"});
        if (!Objects.equals(solution6, "18:00")) {
            System.out.println("solution6 = " + solution6);
        }

        // "10:29"
        String solution7 = solution.solution(10, 25, 1, new String[]{"09:00", "09:10", "09:20", "09:30", "09:40", "09:50", "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"});
        if (!Objects.equals(solution7, "10:29")) {
            System.out.println("solution7 = " + solution7);
        }

        // "09:08"
        String solution8 = solution.solution(2, 10, 2, new String[]{"09:10", "09:09", "08:00", "09:09"});
        if (!Objects.equals(solution8, "09:08")) {
            System.out.println("solution8 = " + solution8);
        }

        // "09:10"
       String solution9 = solution.solution( 2, 10, 3, new String[]{"09:05", "09:09", "09:13"});
        if (!Objects.equals(solution9, "09:10")) {
            System.out.println("solution9 = " + solution9);
        }

        // "00:04"
        String solutionA = solution.solution(1, 1, 5, new String[]{"00:01", "00:02", "00:03", "00:04", "00:05", "00:06"});
        if (!Objects.equals(solutionA, "00:04")) {
            System.out.println("solutionA = " + solutionA);
        }

    }

}
