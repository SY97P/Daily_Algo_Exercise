package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 문제요약
 * <p>
 * 문제를 풀기 위해서는 알고력, 코딩력 필요
 * 1. 알고력 1 증가 / 1 시간
 * 2. 코딩력 1 증가 / 1 시간
 * 3. 문제 풀이 시 해당 문제의 알고증가량, 코딩증가량 만큼 증가 / 문제 풀이 시간
 * 모든 문제를 풀 수 있는 수준까지 도달하는 최단시간 구하기
 * 0 <= 초기 알고력, 초기 코딩력 <= 150
 * 1 <= 문제 수 <= 100
 * 문제 = [필요 알고력, 필요 코딩력, 알고증가량, 코딩증가량, 풀이 시간]
 * <p>
 * 해결전략 (DP)
 * - DP[알고력][코딩력] : 알고력, 코딩력을 만드는데 걸린 최단시간
 * 1. 초기 알고, 코딩력의 DP값을 0으로 시작.
 * 2. 알고, 코딩력을 각각 올리는 경우를 풀어야 하는 문제에 추가 ([필요알고=0,  필요코딩=0, 증가알고=1, 증가코딩=1, 시간=1])
 * 3. 현재 풀 수 있는 문제를 풀고 증가하는 알고코딩력에 해당하는 DP값을 최소값으로 갱신
 * 4. 문제 중 최대 알고력, 최대 코딩력에 해당하는 DP값 반환
 *
 */

public class 코딩_테스트_공부 {

    private static class Solution {

        public int solution(int alp, int cop, int[][] problems) {
            List<ProblemInfo> problemInfos = initProblemInfos(problems);
            int targetAlgorithm = alp;
            int targetCoding = cop;

            for (int[] problem : problems) {
                if (targetAlgorithm < problem[0]) {
                    targetAlgorithm = problem[0];
                }
                if (targetCoding < problem[1]) {
                    targetCoding = problem[1];
                }
            }

            if (alp >= targetAlgorithm && cop >= targetCoding) {
                return 0;
            }

            int[][] dp = initDp(alp, cop, targetAlgorithm, targetCoding);

            solve(alp, cop, targetAlgorithm, targetCoding, dp, problemInfos);

            return dp[targetAlgorithm][targetCoding];
        }

        private void solve(int alp, int cop, int targetAlgorithm, int targetCoding, int[][] dp, List<ProblemInfo> problemInfos) {
            for (int i = alp; i <= targetAlgorithm; i ++) {
                for (int j = cop; j <= targetCoding; j ++) {
                    if (dp[i][j] == Integer.MAX_VALUE) {
                        continue;
                    }

                    for (ProblemInfo problemInfo : problemInfos) {
                        if (i < problemInfo.requestedAlgorithm || j < problemInfo.requestedCoding) {
                            continue;
                        }

                        int nextAlgorithm = Math.min(i + problemInfo.augmentAlgorithm, targetAlgorithm);
                        int nextCoding = Math.min(j + problemInfo.augmentCoding, targetCoding);

                        dp[nextAlgorithm][nextCoding] = Math.min(dp[nextAlgorithm][nextCoding], dp[i][j] + problemInfo.timeCost);
                    }
                }
            }
        }

        private int[][] initDp(int algorithm, int coding, int targetAlgorithm, int targetCoding) {
            int[][] dp = new int[targetAlgorithm + 1][targetCoding + 1];

            for (int i = 0; i <= targetAlgorithm; i ++) {
                for (int j = 0; j <= targetCoding; j ++) {
                    dp[i][j] = Integer.MAX_VALUE;
                }
            }

            dp[algorithm][coding] = 0;
            return dp;
        }

        private List<ProblemInfo> initProblemInfos(int[][] problems) {
            List<ProblemInfo> probs = new ArrayList<>();
            probs.add(new ProblemInfo(0, 0, 1, 0, 1));
            probs.add(new ProblemInfo(0, 0, 0, 1, 1));
            for (int[] problem : problems) {
                probs.add(new ProblemInfo(problem[0], problem[1], problem[2], problem[3], problem[4]));
            }
            return probs;
        }

        private class ProblemInfo {
            int requestedAlgorithm;
            int requestedCoding;
            int augmentAlgorithm;
            int augmentCoding;
            int timeCost;

            ProblemInfo(int requestedAlgorithm, int requestedCoding, int augmentAlgorithm, int augmentCoding, int timeCost) {
                this.requestedAlgorithm = requestedAlgorithm;
                this.requestedCoding = requestedCoding;
                this.augmentAlgorithm = augmentAlgorithm;
                this.augmentCoding = augmentCoding;
                this.timeCost = timeCost;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 15
        int solution1 = solution.solution(10, 10, new int[][]{new int[]{10, 15, 2, 1, 2}, new int[]{20, 20, 3, 3, 4}});
        System.out.println("solution1 = " + solution1);

        // 13
        int solution2 = solution.solution(0, 0,
                new int[][]{new int[]{0, 0, 2, 1, 2}, new int[]{4, 5, 3, 1, 2}, new int[]{4, 11, 4, 0, 2},
                        new int[]{10, 4, 0, 4, 2}});
        System.out.println("solution2 = " + solution2);
    }

}
