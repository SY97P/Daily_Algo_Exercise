package 프로그래머스.lv3;

/**
 * 문제요약
 * <p>
 * n * m 격자
 * query(0, dx) : 열 번호 감소
 * query(1, dx) : 열 번호 증가
 * query(2, dx) : 행 번호 감소
 * query(3, dx) : 행 번호 증가
 * 격자 바깥으로 이동하는 공은 이동할 수 있을때까지만 이동
 * 모든 쿼리를 순서대로 실행했을때 목적지에 도달할 수 있는 시작점 개수 구하기
 * <p>
 * 제한사항
 * <p>
 * 1 ≤ n ≤ 109
 * 1 ≤ m ≤ 109
 * 0 ≤ x < n
 * 0 ≤ y < m
 * 1 ≤ queries의 행의 개수 ≤ 200,000
 * 0 ≤ 쿼리 명령어 ≤ 3
 * 1 ≤ 쿼리 변화량 ≤ 109
 * <p>
 * 해결전략
 * <p>
 * 쿼리 역순으로 실행
 * 범위 연산 (왼쪽 위, 오른쪽 아래)
 * 최소범위 혹은 최대범위가 반대편 경계 이상으로 넘어가면 0 (가능성 없음)
 * 점 개수를 구하면 됨.
 *
 */

public class 공_이동_시뮬레이션 {

    private static class Solution {
        public long solution(int n, int m, int x, int y, int[][] queries) {
            long minx = x, maxx = x;
            long miny = y, maxy = y;

            for (int i = queries.length - 1; i >= 0; i --) {
                int[] query = queries[i];
                if (query[0] == 0) {
                    if (miny != 0) {
                        miny += query[1];
                    }
                    maxy = Math.min(maxy + query[1], m - 1);
                } else if (query[0] == 1) {
                    if (maxy != m - 1) {
                        maxy -= query[1];
                    }
                    miny = Math.max(miny - query[1], 0);
                } else if (query[0] == 2) {
                    if (minx != 0) {
                        minx += query[1];
                    }
                    maxx = Math.min(maxx + query[1], n - 1);
                } else {
                    if (maxx != n - 1) {
                        maxx -= query[1];
                    }
                    minx = Math.max(minx - query[1], 0);
                }

                if (minx >= n || maxx < 0 || miny >= m || maxy < 0) {
                    return 0;
                }
            }

            return (maxx - minx + 1) * (maxy - miny + 1);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        long solution1 = solution.solution(2, 2, 0, 0, new int[][]{new int[]{2, 1}, new int[]{0, 1}, new int[]{1, 1}, new int[]{0, 1}, new int[]{2, 1}});
        System.out.println("solution1 = " + solution1);

        // 2
        long solution2 = solution.solution(2, 5, 0, 1, new int[][]{new int[]{3, 1}, new int[]{2, 2}, new int[]{1, 1}, new int[]{2, 3}, new int[]{0, 1}, new int[]{2, 1}});
        System.out.println("solution2 = " + solution2);
        
        // 0
        long solution3 = solution.solution(1000, 1000, 1, 1, new int[][]{new int[]{0, 100001}, new int[]{2, 100001}});
        System.out.println("solution3 = " + solution3);

    }

}
