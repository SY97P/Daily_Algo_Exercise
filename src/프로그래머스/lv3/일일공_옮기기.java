package 프로그래머스.lv3;

import java.util.Arrays;
import java.util.Stack;

/**
 * 문제요약<br>
 *
 * 0/1로 이뤄진 문자열 x<br>
 * x에 있는 "110" 뽑아서 사전 순으로 가장 앞에 오도록 임의의 위치에 삽입<br>
 * 모든 110을 조사부러서 사전 순으로 가장 앞에 오는 문자열을 만들어 반환<br>
 *<br>
 * 제한사항<br>
 *
 * 1 <= 문자열 개수 <= 10^6<br>
 * 1 <= 문자열 길이 <= 10^6<br>
 *<br>
 * 해결전략<br>
 *
 * 문자열을 역순으로 탐색하면서 110이 나오면<br>
 *  [현재 인덱스, 현재 인덱스 + 2] 까지 제거<br>
 *  110 카운트를 증가<br>
 * 모든 110을 제거한 문자열을 역순으로 탐색하면서 가장 먼저 0이 나오는 구간 바로 뒤에 모든 110 배치<br>
 * 만약 남은 문자열에 0이 하나도 없는 경우 가장 앞에 모든 110 배치<br>
 *
 */

public class 일일공_옮기기 {

    private static class Solution {
        public String[] solution(String[] strings) {
            String[] answer = new String[strings.length];

            for (int i = 0; i < strings.length; i ++) {
                String string = strings[i];
                int tokenCount = 0;
                Stack<Character> stack = new Stack<>();

                for (char st : string.toCharArray()) {
                    int lastIndex = stack.size() - 1;
                    if (st == '0' && stack.size() >= 2 && stack.get(lastIndex) == '1' && stack.get(lastIndex - 1) == '1') {
                        tokenCount ++;
                        stack.pop();
                        stack.pop();
                        continue;
                    }
                    stack.add(st);
                }

                StringBuilder sb = new StringBuilder();
                while (!stack.isEmpty()) {
                    char token = stack.pop();

                    if (tokenCount > 0 && token == '0') {
                        sb.insert(0, "110".repeat(tokenCount));
                        tokenCount = 0;
                    }
                    sb.insert(0, token);
                }
                if (tokenCount > 0) {
                    sb.insert(0, "110".repeat(tokenCount));
                }

                answer[i] = sb.toString();
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // ["1101", "100110110", "0110110111"]
        String[] solution1 = solution.solution(new String[]{"1110", "100111100", "0111111010"});
        System.out.println("solution1 = " + Arrays.toString(solution1));

    }

}
