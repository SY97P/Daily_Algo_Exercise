package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

/**
 * 문제요약<br>
 *<br>
 * 항상 "ICN" 공항에서 출발해서 주어진 항공권을 모두 이용하는 여행경로 구하기<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 모든 공항은 알파벳 대문자 3자.<br>
 * 3 <= 공항 수 <= 10^4<br>
 * tickets : [a, b] : a -> b 항공권<br>
 * 주어진 항공권을 모두 써야 함<br>
 * 가능한 경로가 2개 이상인 경우 알파벳 순서상 앞에 있는 경로를 반환<br>
 * 모든 도시를 방문할 수 없는 경우는 주어지지 않음<br>
 *<br>
 * 해결전략 (DFS)<br>
 *<br>
 * 모든 티켓을 알파벳 순으로 정렬<br>
 * DFS 를 하면서 만들어진 경로가 생기면 나머지 연산 결과 trunning<br>
 *
 */

public class 여행_경로 {

    private static class Solution {

        private List<List<String>> answer;

        public String[] solution(String[][] tickets) {
            answer = new ArrayList<>();

            for (int i = 0; i < tickets.length; i++) {
                if (Objects.equals(tickets[i][0], "ICN")) {
                    boolean[] used = new boolean[tickets.length];
                    List<String> path = new ArrayList<>();
                    used[i] = true;
                    path.add(tickets[i][0]);
                    path.add(tickets[i][1]);
                    findPath(tickets, used, path);
                    used[i] = false;
                }
            }

            answer.sort((a, b) -> {
                for (int i = 0; i < a.size(); i ++) {
                    if (a.get(i).compareTo(b.get(i)) == 0) {
                        continue;
                    }
                    return a.get(i).compareTo(b.get(i));
                }
                return 0;
            });

            return answer.get(0).toArray(String[]::new);
        }

        private void findPath(String[][] tickets, boolean[] used, List<String> path) {
            if (path.size() == tickets.length + 1) {
                answer.add(List.copyOf(path));
                return;
            }

            for (int i = 0; i < tickets.length; i ++) {
                if (!used[i] && Objects.equals(tickets[i][0], path.get(path.size() - 1))) {
                    used[i] = true;
                    path.add(tickets[i][1]);
                    findPath(tickets, used, path);
                    used[i] = false;
                    path.remove(path.size() - 1);
                }
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [ICN, JFK, HND, IAD]
        String[][] tickets = {{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}};
        String[] solution1 = solution.solution(tickets);
        System.out.println("solution1 = " + Arrays.toString(solution1));

        // [ICN, ATL, ICN, SFO, ATL, SFO]
        String[][] tickets2 = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL", "SFO"}};
        String[] solution2 = solution.solution(tickets2);
        System.out.println("solution2 = " + Arrays.toString(solution2));

    }

}
