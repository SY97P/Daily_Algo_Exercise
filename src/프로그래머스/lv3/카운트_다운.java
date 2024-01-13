package 프로그래머스.lv3;

import java.util.Arrays;

/**
 * 문제요약
 * <p>
 * - 주어진 점수에서 타트 점수를 얻어 더도말고 덜도말고 정확하게 0점을 만드는게 목표 - 더 빨리 0점을 만들거나 싱글 또는 불을 더 많이 던지도록 할 때 [던질 다트 수, 싱글 + 불 횟수] 구하기 - 싱글
 * : 해당 수 * 1 점 - 더블 : 해당 수 * 2 점 - 트리플: 해당 수 * 3 점 - 불 : 50 점 - 1 <= target <= 10 ^ 5
 * <p>
 * 해결전략 (DP)
 * <p>
 * 1. target 점수부터 시작해서 가능한 모든 점수 연산을 DP에 기록 1-1. 가능한 모든 점수 = (1 ~ 20) * (1싱글, 2더블, 3트리플), 50(불) 1-2. target - 점수 > 0 인
 * 것만 연산 2. DP 갱신은 [던질 다트 수, 싱글 + 불 횟수] 가 큰 값으로 2-1. 1차 우선순위 : 던질 다트 수가 작은 것 2-2. 2차 우선순위 : 싱글 + 불 횟수가 큰 것 3. DP[0] 반환
 */

public class 카운트_다운 {

    private static class Solution {

        private int[][] dp;

        public int[] solution(int target) {
            dp = new int[target + 1][2];
            for (int i = 0; i < target; i++) {
                dp[i] = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
            }

            for (int score = target; score >= 0; score--) {
                int dartScore = 50;
                if (score - dartScore >= 0) {
                    update(score, dartScore, true);
                }
                for (int i = 1; i <= 20; i++) {
                    for (int k = 1; k <= 3; k++) {
                        dartScore = i * k;
                        if (score - dartScore < 0) {
                            continue;
                        }
                        update(score, dartScore, k == 1);
                    }
                }
            }

            return dp[0];
        }

        private void update(int originScore, int dartScore, boolean isSingleOrBull) {
            int targetScore = originScore - dartScore;
            int[] nextScore = new int[]{dp[originScore][0] + 1, dp[originScore][1] + (isSingleOrBull ? 1 : 0)};
            if (dp[targetScore][0] > nextScore[0] || (dp[targetScore][0] == nextScore[0]
                    && dp[targetScore][1] < nextScore[1])) {
                dp[targetScore] = nextScore;
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [1, 0]
//        int[] solution1 = solution.solution(21);
//        System.out.println("solution1 = " + Arrays.toString(solution1));

        // [2, 2]
        int[] solution2 = solution.solution(58);
        System.out.println("solution2 = " + Arrays.toString(solution2));

    }
}
