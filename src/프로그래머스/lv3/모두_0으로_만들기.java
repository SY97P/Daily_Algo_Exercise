package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;

/**
 * 문제요약<br>
 *
 * 각 노드에 가중치 있는 트리<br>
 * 모든 점의 가중치를 0으로 만들때 드는 최소 연산횟수 구하기<br>
 * 직접 연결된 두 점 중에서 한쪽은 1증가, 다른 한쪽은 1 감소<br>
 * 만약 모두 0으로 만드는 것이 불가하면 -1 반환<br>
 *<br>
 * 제한사항<br>
 *
 * 2 <= 노드 개수 <= 3 * 10^6<br>
 * -10^6 <= 가중치 <= 10^6<br>
 * 연결정보 : [u, v]<br>
 *<br>
 * 해결전략<br>
 *
 * 어느 노드에서 시작해도 결과 얻는데에는 영향 X<br>
 * 자식노드를 0으로 만들기<br>
 * 노드 별로 [현재 노드 가중치 값, 연산횟수] 필요<br>
 * 현재 노드 가중치 값 = 자식노드 0으로 만들고 자신이 얻은 값 + 원래 자신의 가중치 값<br>
 * 연산 횟수 = |자식노드 0으로 만들기 위해 얻은 값|<br>
 * 시작노드(루트)노드로 최종적으로 백트래킹된 결과 중<br>
 *  `현재 노드 가중치 값`이 0이 아니면 -1 반환.<br>
 *  0이면 해당 값 반환<br>
 *<br>
 *  신경쓸것<br>
 *
 *  연산과정에서 탐색하는 노드가 너무 많아 스택오버플로우가 발생한다.<br>
 *  그래서 6, 7번 문제에 런타임 에러로 문제 통과가 어렵다.<br>
 *  해결방법은 향상for문을 일반for문으로 변경하는것.<br>
 *  성능상의 차이는 없다고 하는데, 미세한 차이가 있는 것으로 보인다.<br>
 *  실무에서는 이정도 미세한 차이보다는 가독성이 중요하므로 향상 for 문을 쓰는게 좋아보인다.<br>
 *
 */

public class 모두_0으로_만들기 {

    private static class Solution {

        private int n;
        private int[] a;
        private List<List<Integer>> adj;
        private boolean[] visited;

        public long solution(int[] _a, int[][] edges) {
            a = _a;
            n = _a.length;
            visited = new boolean[n];
            initAdj(n, edges);

            visited[0] = true;
            long[] answer = dfs(0);

            return answer[0] == 0 ? answer[1] : -1;
        }

        private long[] dfs(int node) {
            long currentValue = a[node];
            long operateCount = 0;

            for (int i = 0; i < adj.get(node).size(); i ++) {
                int child = adj.get(node).get(i);
                if (visited[child]) {
                    continue;
                }
                visited[child] = true;
                long[] result = dfs(child);
                currentValue += result[0];
                operateCount += Math.abs(result[0]) + result[1];
            }

            return new long[]{currentValue, operateCount};
        }

        private void initAdj(int n, int[][] edges) {
            adj = new ArrayList<>();
            for (int i = 0; i < n; i ++) {
                adj.add(new ArrayList<>());
            }

            for (int[] edge : edges) {
                int u = edge[0];
                int v = edge[1];
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 9
        long solution1 = solution.solution(new int[]{-5, 0, 2, 1, 2}, new int[][]{new int[]{0, 1}, new int[]{3, 4}, new int[]{2, 3}, new int[]{0, 3}});
        System.out.println("solution1 = " + solution1);

        // -1
        long solution2 = solution.solution(new int[]{0, 1, 0}, new int[][]{new int[]{0, 1}, new int[]{1, 2}});
        System.out.println("solution2 = " + solution2);

        // 1
        long solution3 = solution.solution(new int[]{-1, 1}, new int[][]{new int[]{0, 1}});
        System.out.println("solution3 = " + solution3);

    }

}
