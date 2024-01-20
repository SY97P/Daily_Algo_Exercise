package 프로그래머스.lv3;

/**
 * 문제요약
 * <p>
 * 금 a, 은 b 를 모아 도시를 지을것!<br>
 * i번 도시 -> 금 g[i], 은 s[i], 트럭편도이동시간 t[i], 트럭최대수용량 w[i]<br>
 * 도시를 만들 수 있는 가장 빠른시간 구하기                                   <br>
 * <p>
 * 제한사항
 * <p>
 * 0 ≤ a, b ≤ 10^9<br>
 * 1 ≤ g의 길이 = s의 길이 = w의 길이 = t의 길이 = 도시 개수 ≤ 10^5<br>
 * 0 ≤ g[i], s[i] ≤ 10^9<br>
 * 1 ≤ w[i] ≤ 10^2<br>
 * 1 ≤ t[i] ≤ 10^5<br>
 * a ≤ g의 모든 수의 합<br>
 * b ≤ s의 모든 수의 합<br>
 * <p>
 * 해결전략 (이분탐색)
 * <p>
 * mid : 도시 건설 시 예상 최단시간 추정치
 *
 */

public class 금과_은_운반하기 {

    private static class Solution {

        int n;
        int a, b;
        int[] g, s, w, t;

        public long solution(int _a, int _b, int[] _g, int[] _s, int[] _w, int[] _t) {
            n = _g.length;
            a = _a; b = _b;
            g = _g; s = _s; w = _w; t = _t;

            long answer = -1;

            long l = 0;
            long r = (long) 1e15;

            while (l <= r) {
                long m = (l + r) / 2;

                if (possible(m)) {
                    answer = m;
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }

            return answer;
        }

        private boolean possible(long estimateTime) {
            long total = 0;
            long gold = 0;
            long silver = 0;

            for (int i = 0; i < n; i ++) {
                long count = estimateTime / (t[i] * 2L);
                if (estimateTime >= count * (t[i] * 2L) + t[i]) {
                    count ++;
                }

                long amount = Math.min(w[i] * count, g[i] + s[i]);
                total += amount;
                gold += Math.min(amount, g[i]);
                silver += Math.min(amount, s[i]);

                if (total >= a + b && gold >= a && silver >= b) {
                    return true;
                }
            }
            return false;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 50
        long solution1 = solution.solution(10, 10, new int[]{100}, new int[]{100}, new int[]{7}, new int[]{10});
        System.out.println("solution1 = " + solution1);

        // 499
        long solution2 = solution.solution(90, 500, new int[]{70, 70, 0}, new int[]{0, 0, 500}, new int[]{100, 100, 2}, new int[]{4, 8, 1});
        System.out.println("solution2 = " + solution2);

    }

}
