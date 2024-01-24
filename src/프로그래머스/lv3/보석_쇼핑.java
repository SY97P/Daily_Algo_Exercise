package 프로그래머스.lv3;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * 문제요약<br>
 *<br>
 * 진열된 모든 종류 보석을 적어도 1개 이상 포함하는 가장 짧은 구간 찾아서 구매<br>
 * 가장 짧은 구간의 [시작 진열대 번호, 끝 진열대 번호] 반환<br>
 * 여러 개면 시작 진열배 번호가 가장 작은 구간 반환<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= 보석 리스트 길이 <= 10^5<br>
 * 1 <= 보석 이름(알파벳 대문자로만 구성) <= 10<br>
 * 시작번호는 1번 부터 시작<br>
 *<br>
 * 해결전략 (슬라이딩 윈도우)<br>
 *<br>
 * 사전자료형을 하나 준비한다. (보석이름 : 보석개수)<br>
 * 슬라이딩 윈도우로 현재 시작 지점에서 모든 보석을 하나씩 가질 수 있는 끝점을 구한다.<br>
 * 슬라이딩 윈도우를 진행하면서 같은 조건에서 (끝점 - 시작점) 구간이 더 짧은 구간으로 결과를 갱신한다.<br>
 *
 */

public class 보석_쇼핑 {

    private static class Solution {

        public int[] solution(String[] gems) {
            int n = gems.length;

            int[] answer = new int[]{1, n};

            int targetGemCount = Arrays.stream(gems)
                    .collect(Collectors.toSet())
                    .size();

            Map<String, Integer> cart = new HashMap<>();

            int end = 0;
            for (int start = 0; start < n; start ++) {
                while (end < n && cart.keySet().size() < targetGemCount) {
                    cart.put(gems[end], cart.getOrDefault(gems[end ++], 0) + 1);
                }

                if (cart.keySet().size() == targetGemCount && end - (start + 1) < answer[1] - answer[0]) {
                    answer = new int[]{start + 1, end};
                }

                cart.put(gems[start], cart.get(gems[start]) - 1);
                if (cart.get(gems[start]) <= 0) {
                    cart.remove(gems[start]);
                }
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [3, 7]
        int[] solution1 = solution.solution(new String[]{"DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"});
        System.out.println("solutino = " + Arrays.toString(solution1));

        // [1, 3]
        int[] solution2 = solution.solution(new String[]{"AA", "AB", "AC", "AA", "AC"});
        System.out.println("solutino = " + Arrays.toString(solution2));

        // [1, 1]
        int[] solution3 = solution.solution(new String[]{"XYZ", "XYZ", "XYZ"});
        System.out.println("solutino = " + Arrays.toString(solution3));

        // [1, 5]
        int[] solution4 = solution.solution(new String[]{"ZZZ", "YYY", "NNNN", "YYY", "BBB"});
        System.out.println("solutino = " + Arrays.toString(solution4));

    }

}
