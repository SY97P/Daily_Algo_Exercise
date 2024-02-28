package 프로그래머스.lv3;

/**
 * 문제요약
 *
 * 거슬러 줘야 하는 금액 n 과 현재 보유하고 있는 돈 종류 money 가 주어짐
 * 거슬러 줄 수 있는 방법의 수 구하기
 *
 * 제한사항
 *
 * 1 <= n <= 10^5
 * 1 <= 화폐 단위 종류 <= 100
 * 모든 화폐는 무한히 존재
 * 정답을 1_000_000_007로 나눈 나머지 구하기
 *
 * 해결전략 (DP)
 *
 * 1원부터 n원까지 각 원마다 가지고 있는 화폐 단위를 더한 인덱스에 방법 + 1 갱신하기
 */

public class 거스름돈 {

    private static class Solution {

        public int solution(int n, int[] money) {
            int[] dp = new int[n + 1];

            for (int m : money) {
                dp[m] ++;
                for (int i = 0; i < n; i ++) {
                    if (dp[i] != 0 && i + m <= n) {
                        dp[i + m] += dp[i];
                    }
                }
            }

            return dp[n];
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 4
        int answer1 = s.solution(5, new int[]{1, 2, 5});
        System.out.println("answer1 = " + answer1);
    }

}
