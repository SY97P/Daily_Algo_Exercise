package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;

/**
 * 문제요약
 *
 * 초당 최대 처리량 = 1_000ms 간 처리하는 요청의 최대 개수
 * 작년 추석 (2016-09-15) 초당 최대 처리량 구하기
 *
 * 제한사항
 *
 * 1 <= 요청 정보(문자열) <= 2_000
 * 요청정보 : "응답완료시간 처리시간"
 * 응답 완료 시간 : "2016-09-15 hh:mm:ss.sss"
 * 처리시간 : "x.xxx s" (소수점 아래 세자리)
 * 처리시간은 시작시간과 끝시간 포함 (33.010 ~ 33.020 = 0.011초)
 * 0.001 <= 처리시간 <= 3.000
 * 요청정보는 응답완료시간을 기준으로 오름차순 정렬
 *
 * 해결전략
 *
 * 각 요청 별로 1_000 ms 내에 겹치는 다른 요청의 개수 구하기
 * 그 중에서 최대값 구하기
 */

public class 추석_트래픽 {

    private static class Solution {

        private static final double TIME_UNIT = 0.001F;
        private static final double TIME_DIFFER = 1;

        public int solution(String[] lines) {
            int answer = 1;

            List<Request> requests = regulateRequestLines(lines);

            for (int i = 0; i < requests.size(); i ++) {
                int maxTraffic = 1;
                for (int j = i + 1; j < requests.size(); j ++) {
                    if (isConcurrent(requests.get(i), requests.get(j))) {
                        maxTraffic ++;
                    }
                }
                answer = Math.max(answer, maxTraffic);
            }

            return answer;
        }

        private boolean isConcurrent(Request requestA, Request requestB) {
            return requestB.requsetTime - requestA.responseTime < TIME_DIFFER;
        }

        private List<Request> regulateRequestLines(String[] lines) {
            List<Request> requests = new ArrayList<>();
            for (String line : lines) {
                String[] split = line.split(" ");
                double responseTime = regulateResponseTime(split[1]);
                double durationTime = regulateDurationTime(split[2]);
                Request request = new Request(responseTime - durationTime + TIME_UNIT, responseTime);
                requests.add(request);
            }
            return requests;
        }

        private double regulateDurationTime(String time) {
            return Double.parseDouble(time.replace("s", ""));
        }

        private double regulateResponseTime(String time) {
            String[] split = time.split(":");
            double hour = Double.parseDouble(split[0]) * 3600;
            double minute = Double.parseDouble(split[1]) * 60;
            double second = Double.parseDouble(split[2]);
            return hour + minute + second;
        }

        private static class Request {
            double requsetTime;
            double responseTime;

            Request (double requestTime, double responseTime) {
                this.requsetTime = requestTime;
                this.responseTime = responseTime;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 1
        int solution1 = solution.solution(new String[]{"2016-09-15 00:00:00.000 3s"});
        System.out.println("solution = " + solution1);

        // 1
        int solution2 = solution.solution(new String[]{"2016-09-15 23:59:59.999 0.001s"});
        System.out.println("solution = " + solution2);

        // 1
        int solution3 = solution.solution(new String[]{"2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"});
        System.out.println("solution = " + solution3);

        // 2
        int solution4 = solution.solution(new String[]{"2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"});
        System.out.println("solution = " + solution4);

        // 7
        int solution5 = solution.solution(new String[]{"2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"});
        System.out.println("solution = " + solution5);

        // 1
        int solution6 = solution.solution(new String[]{"2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"});
        System.out.println("solution = " + solution6);

    }

}
