package 프로그래머스.lv3;

/**
 * 문제요약
 * <p>
 * 이진트리 돌아다니면 양, 늑대가 모임
 * 늑대 >= 양 -> 양 주금 ㅠㅠ
 * 양이 늑대에게 잡아먹히지 않으면서 모을 수 있는 최대 양 수 구하기
 * 루트에는 항상 양 존재
 * <p>
 * 제한사항
 * <p>
 * 2 <= 노드 수 <= 17
 * 노드 원소 = 0(양) / 1(늑대)
 * 연결관계 길이 = 노드 수 - 1
 * 연결관계 = [부모 노드, 자식 노드]
 * 중복 간선 없음
 * 항상 답을 구할 수 있는 이진트리 형태
 * 루트 = 0번 노드
 * <p>
 * 해결전략 (MST & DFS)
 * <p>
 * 방문 배열 만들기
 * 방문한 노드이면서 연결관계에서 자신의 자식노드는 미방문 노드인 모든 자식노드로 DFS
 * 늑대 >= 양 이라면 return 0
 * 그외엔 return 양
 */

public class 양과_늑대 {

    private static class Solution {

        private int n;
        private int[] info;
        private int[][] edges;
        private boolean[] visited;

        public int solution(int[] info_, int[][] edges_) {
            n = info_.length;
            info = info_;
            edges = edges_;
            visited = new boolean[n];
            visited[0] = true;

            return dfs(0, 1, 0);
        }

        private int dfs(int node, int sheepCount, int wolfCount) {
            if (wolfCount >= sheepCount) {
                return 0;
            }

            int count = sheepCount;
            for (int[] edge : edges) {
                if (visited[edge[0]] && !visited[edge[1]]) {
                    visited[edge[1]] = true;
                    if (info[edge[1]] == 0) {
                        count = Math.max(count, dfs(edge[1], sheepCount + 1, wolfCount));
                    } else {
                        count = Math.max(count, dfs(edge[1], sheepCount, wolfCount + 1));
                    }
                    visited[edge[1]] = false;
                }
            }

            return count;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 5
        int solution1 = solution.solution(new int[]{0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1}, new int[][]{new int[]{0, 1}, new int[]{1, 2}, new int[]{1, 4}, new int[]{0, 8}, new int[]{8, 7}, new int[]{9, 10}, new int[]{9, 11}, new int[]{4, 3}, new int[]{6, 5}, new int[]{4, 6}, new int[]{8, 9}});
        System.out.println("solution1 = " + solution1);

        //5
        int solution2 = solution.solution(new int[]{0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0}, new int[][]{new int[]{0, 1}, new int[]{0, 2}, new int[]{1, 3}, new int[]{1, 4}, new int[]{2, 5}, new int[]{2, 6}, new int[]{3, 7}, new int[]{4, 8}, new int[]{6, 9}, new int[]{9, 10}});
        System.out.println("solution2 = " + solution2);

    }

}
