package 프로그래머스.lv3;

/* 문제조건

- 탑승 중 항상 t1 ~ t2 유지

- 전원 on  : 희망온도 방향 1도 / 1분
- 전원 off : 실외온도 방향 1도 / 1분

- 실내온도 != 희망온도 -> a 전력 소비
- 실내온도 == 희망온도 -> b 전력 소비
- 전원 off : 0 전력 소비

- 승객 탑승 중 실내온도 t1 ~ t2 유지할때의 최소 소비전력 구하기
*/

/* 해결전략 (DP)
- dp[time][temperature] : time 분에 실내온도가 temparature 도로 만들때의 소비 전력
- dp[onboard.length-1][n] 의 최소값 구하기

- dp[time][temp] = min(dp[time-1][temp-1]+å, dp[time-1][temp]+ß, dp[time][temp+1]+ç)
- time : 현재 시간
- temp : 현재 온도
1. 현재온도+1
    - 실내온도 < 실외온도 : 0 전력
    - 실내온도 = 실외온도 : a 전력
    - 실내온도 > 실외온도 : a 전력
2. 현재온도-1
    - 실내온도 < 실외온도 : a 전력
    - 실내온도 = 실외온도 : a 전력
    - 실내온도 > 실외온도 : 0 전력
3. 현재온도
    - 실내온도 < 실외온도 : a 전력
    - 실내온도 = 실외온도 : b 전력
    - 실내온도 > 실외온도 : a 전력

1. 0 전력 소비
    - 현재온도 = 실외온도 -> 현재온도
    - 현재온도 < 실외온도 -> 현재온도 + 1
    - 현재온도 > 실외온도 -> 현재온도 - 1
2. a 전력 소비
    - 현재온도 = 실외온도 -> 현재온도 + 1 and 현재온도 - 1
    - 현재온도 < 실외온도 -> 현재온도 - 1
    - 현재온도 > 실외온도 -> 현재온도 + 1
3. b 전력 소비

1. 기탑승 -> t1 ~ t2 사이 온도만 가능해야함.
2. 미탑승 -> 모든 온도 가능해야함.
*/

public class 에어컨 {

    static class Solution {

        public int solution(int temperature, int t1, int t2, int a, int b, int[] onboard) {
            int lowestTemperature = 10;
            int highestTemperature = 50;

            temperature += lowestTemperature;
            t1 += lowestTemperature;
            t2 += lowestTemperature;

            int[][] dp = new int[onboard.length + 1][highestTemperature + 1];

            for (int time = onboard.length - 1; time >= 0; time--) {
                for (int temp = 0; temp <= highestTemperature; temp++) {
                    dp[time][temp] = Integer.MAX_VALUE - Math.max(a, b);

                    if (onboard[time] == 1 && (temp < t1 || temp > t2)) {
                        continue;
                    }

                    if (temp == temperature) {
                        dp[time][temp] = Math.min(dp[time][temp], dp[time + 1][temp]);
                    } else if (temp < 50 && temp < temperature) {
                        dp[time][temp] = Math.min(dp[time][temp], dp[time + 1][temp + 1]);
                    } else if (temp > 0 && temp > temperature) {
                        dp[time][temp] = Math.min(dp[time][temp], dp[time + 1][temp - 1]);
                    }

                    if (temp < 50) {
                        dp[time][temp] = Math.min(dp[time][temp], dp[time + 1][temp + 1] + a);
                    }
                    if (temp > 0) {
                        dp[time][temp] = Math.min(dp[time][temp], dp[time + 1][temp - 1] + a);
                    }
                    dp[time][temp] = Math.min(dp[time][temp], dp[time + 1][temp] + b);
                }
            }

            return dp[0][temperature];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 40
        int solution1 = solution.solution(28, 18, 26, 10, 8, new int[]{0, 0, 1, 1, 1, 1, 1});
        // 25
        int solution2 = solution.solution(-10, -5, 5, 5, 1, new int[]{0, 0, 0, 0, 0, 1, 0});
        // 20
        int solution3 = solution.solution(11, 8, 10, 10, 1, new int[]{0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1});
        // 60
        int solution4 = solution.solution(11, 8, 10, 10, 100, new int[]{0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1});

        System.out.println("solution1 = " + solution1);
        System.out.println("solution2 = " + solution2);
        System.out.println("solution3 = " + solution3);
        System.out.println("solution4 = " + solution4);
    }

}
