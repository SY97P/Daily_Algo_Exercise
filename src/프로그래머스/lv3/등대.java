package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;

/**
 * 문제요약
 * <p>
 * - n개의 등대, n-1개의 항로
 * - 한 뱃길의 양쪽 끝 등대 중 적어도 하나는 켜져 있게 함
 * - 켜 두어야 하는 등대 최소 개수 구하기
 * - 2 <= n <= 100,000
 * - [a, b] : a번 등대와 b번 등대를 연결하는 항로
 * <p>
 * 해결전략 (백트래킹)
 * <p>
 * 1. 어느 노드에서 시작하던지 결과는 같음
 * 2. 현재 노드의 자식노드를 탐색하면서 (on: 내가 켜졌을때 서브트리 켜진 수, off: 내가 꺼졌을때 서브트리 켜진 수) 구하기
 *  2-1. on = min(현재노드 on + 자식노드 off, 현재노드 on + 자식노드 on)
 *  2-2. off = 현재노드 off + 자식노드 on
 * 3. 루트 노드에서 on, off 중 작은 값을 리턴
 */

public class 등대 {

    private static class Solution {

        private List<List<Integer>> adj;
        private boolean[] visited;

        public int solution(int n, int[][] lighthouse) {
            adj = initAdj(n, lighthouse);
            visited = new boolean[n + 1];

            int root = 1;
            visited[root] = true;
            int[] result = dfs(root);

            return Math.min(result[0], result[1]);
        }

        private int[] dfs(int node) {
            int on = 1;
            int off = 0;

            for (int child : adj.get(node)) {
                if (!visited[child]) {
                    visited[child] = true;
                    int[] subResult = dfs(child);
                    on += Math.min(subResult[0], subResult[1]);
                    off += subResult[0];
                }
            }

            return new int[]{on, off};
        }

        private List<List<Integer>> initAdj(int n, int[][] lighthouse) {
            List<List<Integer>> adj = new ArrayList<>();
            for (int i = 0; i <= n; i ++) {
                adj.add(new ArrayList<>());
            }

            for (int[] route : lighthouse) {
                int a = route[0];
                int b = route[1];

                adj.get(a).add(b);
                adj.get(b).add(a);
            }

            return adj;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 2
        int[][] lighthouse1 = {{1, 2}, {1, 3}, {1, 4}, {1, 5}, {5, 6}, {5, 7}, {5, 8}};
        int solution1 = s.solution(8, lighthouse1);
        System.out.println("solution1 = " + solution1);

        // 3
        int[][] lighthouse2 = {{4, 1}, {5, 1}, {5, 6}, {7, 6}, {1, 2}, {1, 3}, {6, 8}, {2, 9}, {9, 10}};
        int solution2 = s.solution(10, lighthouse2);
        System.out.println("solution2 = " + solution2);

    }

}
