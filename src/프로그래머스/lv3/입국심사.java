package 프로그래머스.lv3;

/**
 * 문제요약
 *
 * 심사대에서는 동시에 한 명만 심사 가능
 * 가장 앞에 서 있는 사람은 비어있는 심사대로 가서 더 빨리 심사받기 가능
 * 모든 사람이 심사 받는데 걸리는 최소 시간 구하기
 *
 * 제한사항
 *
 * 1 <= 사람 <= 10^9
 * 1 <= 심사 시간 < =10^9
 * 1 <= 심사관 <= 10^5
 *
 * 해결전략 (이분탐색)
 *
 * mid : 모든 사람이 심사 받는데 걸리는 최소 시간 추정치
 * 해당 시간 추정치로 모든 사람을 심사할 수 있으면 추정치 낮추기
 * 모든 사람 심사 불가면 추정치 높히기
 */

public class 입국심사 {

    private static class Solution {
        public long solution(int n, int[] times) {
            long answer = 0;

            long l = 1;
            long r = (long) 1e18;

            while (l <= r) {
                long m = (l + r) / 2;
                long count = getCount(m, times);
                if (count >= n) {
                    answer = m;
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }

            return answer;
        }

        private long getCount(long m, int[] times) {
            long count = 0;
            for (int time : times) {
                count += m / (long) time;
            }
            return count;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 28
//        long solution1 = solution.solution(6, new int[]{7, 10});
//        System.out.println("solution1 = " + solution1);
//
//        // 21
//        long solution2 = solution.solution(6, new int[]{7, 10, 12});
//        System.out.println("solution2 = " + solution2);

//        long solution3 = solution.solution((int) 1e9, new int[]{(int) 1e9});
//        System.out.println("solution3 = " + solution3);

        long solution4 = solution.solution(59, new int[]{1, 1});
        System.out.println("solution4 = " + solution4);

    }

}
