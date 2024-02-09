package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

/**
 * 문제요약<br>
 * <br>
 * n 개 섬 사이에 다리 건설 비용 costs 주어질때 최소 비용으로 모든 섬 통행가능토록 할때 필요한 최소 비용 구하기<br>
 * 다리를 여러번 건너도 도달할 수만 있으면 통행 가능<br>
 * <br>
 * 제한사항<br>
 * <br>
 * 1 <= 섬 개수 <= 100<br>
 * costs : [u, v, 비용]<br>
 * 중복 연결 주어지지 않음<br>
 * 양방향 그래프<br>
 * 연결할 수 없는 섬은 입력으로 주어지지 않음<br>
 * <br>
 * 해결전략 (MST - 프림)<br>
 * <br>
 * MST 집합을 만들기<br>
 * 모든 노드가 MST에 존재하도록 연산<br>
 * 현재 MST에 있는 노드와 연결된 모든 비MST 노드 중에서 가장 연결비용이 작은 것을 선택<br>
 *  costs 를 비용기준 오름차순 정렬해야 함.<br>
 * 모든 노드가 MST 에 있게 되면 현재까지 모든 비용을 더해서 반환<br>
 *
 * Prim 알고리즘
 *
 * O(ElogV) -> V < E 면 이득
 * 우선순위 큐 활용 알고리즘
 *
 */

public class 섬_연결하기_prim {

    private static class Solution {
        public int solution(int n, int[][] costs) {
            List<List<int[]>> adj = initAdj(n, costs);
            boolean[] mst = new boolean[n];
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

            int rootNode = 0;

            pq.add(new int[]{0, rootNode});
            mst[rootNode] = true;

            int answer = 0;

            while (!pq.isEmpty()) {
                int[] node = pq.poll();

                if (!mst[node[1]]) {
                    answer += node[0];
                    mst[node[1]] = true;
                }

                for (int[] next : adj.get(node[1])) {
                    if (mst[next[1]]) {
                        continue;
                    }

                    pq.add(next);
                }
            }

            return answer;
        }

        private List<List<int[]>> initAdj(int n, int[][] costs) {
            List<List<int[]>> adj = new ArrayList<>();
            for (int i = 0; i < n; i ++) {
                adj.add(new ArrayList<>());
            }

            for (int[] cost : costs) {
                int u = cost[0];
                int v = cost[1];
                int c = cost[2];

                adj.get(u).add(new int[]{c, v});
                adj.get(v).add(new int[]{c, u});
            }

            return adj;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        int solution1 = solution.solution(4, new int[][]{new int[]{0, 1, 1}, new int[]{0, 2, 2}, new int[]{1, 2, 5}, new int[]{1, 3, 1}, new int[]{2, 3, 8}});
        System.out.println("solution1 = " + solution1);

        // 15
        int solution2 = solution.solution(5, new int[][]{new int[]{0, 1, 5}, new int[]{1, 2, 3}, new int[]{2, 3, 3}, new int[]{3, 1, 2}, new int[]{3, 0, 4}, new int[]{2, 4, 6}, new int[]{4, 0, 7}});
        System.out.println("solution2 = " + solution2);

    }

}
