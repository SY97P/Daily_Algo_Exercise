package 프로그래머스.lv3;

/**
 * 문제요약<br>
 *<br>
 * [동영상 시작시간, 동영상 종료시간)<br>
 * 누적 재생시간이 가장 많이 나오는 곳에 공익광고 삽입<br>
 * 누적 재생시간이 많은 곳이 여러곳이라면 그 중 가장 빠른 시작 시간 반환<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 00:00:01 <= 시간형식 = HH:MM:SS <= 99:59:59<br>
 * 광고시간 <= 동영상시간<br>
 * 1 <= 전체 재생기록 <= 3 * 10^5<br>
 * 재생기록 형식 = H1:M1:S1-H2:M2:S2<br>
 *<br>
 * 해결전략 (슬라이딩윈도우)<br>
 *<br>
 * 시간형식 <-> 초단위 숫자 메소드 구현<br>
 * 동영상시간 만큼의 DP 배열 만들기<br>
 * 시작시간을 기준으로 슬라이딩 윈도우<br>
 *  누적횟수 += [시작시간 + 광고시간]<br>
 *  누적횟수 -= [시작시간]<br>
 *  시작시간 ++<br>
 * 전체 시간에서 재생횟수가 가장 큰 시작시간 구하기<br>
 * 해당 시작시간을 시간형식으로 변환해 반환<br>
 *
 */

public class 광고_삽입 {

    private static class Solution {

        public String solution(String play_time, String adv_time, String[] logs) {
            int playTime = convertTimeToSec(play_time);
            int advTime = convertTimeToSec(adv_time);

            long[] dp = new long[playTime + 1];

            for (String log : logs) {
                String[] split = log.split("-");
                int startTime = convertTimeToSec(split[0]);
                int endTime = convertTimeToSec(split[1]);

                dp[startTime] ++;
                dp[endTime] --;
            }

            for (int i = 0; i < playTime; i ++) {
                dp[i + 1] += dp[i];
            }

            int startTime = 0;
            int answer = startTime;
            long count = 0;
            long maxCount = count;
            while (startTime + advTime <= playTime) {
                if (count > maxCount) {
                    maxCount = count;
                    answer = startTime;
                }

                count -= dp[startTime];
                count += dp[startTime + advTime];

                startTime ++;
            }

            return convertSecToTime(answer);
        }

        private int convertTimeToSec(String time) {
            String[] split = time.split(":");
            int hour = Integer.parseInt(split[0]) * 3600;
            int minute = Integer.parseInt(split[1]) * 60;
            int second = Integer.parseInt(split[2]);
            return hour + minute + second;
        }

        private String convertSecToTime(int time) {
            String hour = String.format("%02d", time / 3600);
            String minute = String.format("%02d", (time % 3600) / 60);
            String second = String.format("%02d", time % 60);
            return hour + ":" + minute + ":" + second;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // "01:30:59"
        String solution1 = solution.solution("02:03:55", "00:14:15", new String[]{"01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"});
        System.out.println("solution = " + solution1);

        // "01:00:00"
        String solution2 = solution.solution("99:59:59", "25:00:00", new String[]{"69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"});
        System.out.println("solution = " + solution2);

        // "00:00:00"
        String solution3 = solution.solution("50:00:00", "50:00:00", new String[]{"15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"});
        System.out.println("solution = " + solution3);

    }

}
