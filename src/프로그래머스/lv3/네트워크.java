package 프로그래머스.lv3;

import java.util.Arrays;
import java.util.stream.Collectors;

/**
 * 문제요약
 *
 * A <-> B <-> C 로 각각 연결됨
 * A, B, C 는 하나의 네트워크에 존재하는 것
 * 연결 정보가 주어졌을때 네트워크의 개수 구하기
 *
 * 제한사항
 *
 * 1 <= 컴퓨터 개수 <= 200
 * 0 <= 컴퓨터 번호 < n
 * computer[i][j] : i, j 컴퓨터 서로 연결 (1)
 *
 * 해결전략
 *
 * 모든 i, j 쌍에 대해서 연결된 경우 네트워크 번호를 두 컴퓨터 모두에 기록
 * 최종적으로 구해지는 네트워크 최고 번호 반환
 */

public class 네트워크 {

    private static class Solution {

        private int[] parent;

        public int solution(int n, int[][] computers) {
            parent = new int[n];
            for (int i = 0; i < n; i ++) {
                parent[i] = i;
            }

            for (int i = 0; i < n; i ++) {
                for (int j = 0; j < n; j ++) {
                    if (computers[i][j] == 1) {
                        union(i, j);
                    }
                }
            }

            return Arrays.stream(parent)
                    .map(this::find)
                    .boxed()
                    .collect(Collectors.toSet())
                    .size();
        }

        private void union(int a, int b) {
            int fa = find(a);
            int fb = find(b);

            if (fa < fb) {
                parent[fb] = fa;
            } else if (fa > fb) {
                parent[fa] = fb;
            }
        }

        private int find(int num) {
            if (parent[num] != num) {
                parent[num] = find(parent[num]);
            }
            return parent[num];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 2
        int solution1 = solution.solution(3, new int[][]{new int[]{1, 1, 0}, new int[]{1, 1, 0}, new int[]{0, 0, 1}});
        System.out.println("solution = " + solution1);

        // 1
        int solution2 = solution.solution(3, new int[][]{new int[]{1, 1, 0}, new int[]{1, 1, 1}, new int[]{0, 1, 1}});
        System.out.println("solution = " + solution2);

        // 5
        int solution3 = solution.solution(5,
                new int[][]{
                        new int[]{1, 1, 0, 0, 0},
                        new int[]{0, 1, 1, 0, 0},
                        new int[]{0, 0, 1, 1, 0},
                        new int[]{0, 0, 0, 1, 1},
                        new int[]{0, 0, 0, 0, 1}});
        System.out.println("solution3 = " + solution3);

    }

}
