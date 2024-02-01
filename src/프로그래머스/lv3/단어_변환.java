package 프로그래머스.lv3;

import java.util.Objects;

/**
 * 문제요약
 *
 * 문자의 시작 begin
 * 문자의 끝 target
 * 문자의 경유지 words
 *
 * 시작에서 끝으로 경유지를 거치면서 변환
 * 한 번에 한 개의 알파벳만 변환 가능
 * words 에 있는 단어로만 변환 가능
 * 변환에 필요한 최소 개수 구하기
 *
 * 제한사항
 *
 * 각 단어는 알파벳 소문자로만 구성
 * 3 <= 단어 길이 <= 10
 * 모든 단어 길이는 동일
 * 3 <= 경유지 개수 <= 50
 * 중복되는 경유지 단어는 없음
 * begin != target
 * 변환할 수 없는 경우에는 0 반환
 *
 * 해결전략 (DFS)
 *
 * 가장 처음으로 target 이 되는 경로가 최단경로
 *
 */

public class 단어_변환 {

    private static class Solution {
        public int solution(String begin, String target, String[] words) {
            int answer = dfs(begin, target, words, new boolean[words.length], 0);
            return answer == Integer.MAX_VALUE ? 0 : answer;
        }

        private int dfs(String token, String target, String[] words, boolean[] used, int count) {
            if (Objects.equals(token, target)) {
                return count;
            }

            int result = Integer.MAX_VALUE;
            for (int i = 0; i < words.length; i ++) {
                String word = words[i];
                if (!used[i] && oneDiff(token, word)) {
                    used[i] = true;
                    int rtnCount = dfs(word, target, words, used, count + 1);
                    result = Math.min(result, rtnCount);
                    used[i] = false;
                }
            }

            return result;
        }

        private boolean oneDiff(String token, String word) {
            int count = 0;
            for (int i = 0; i < token.length(); i ++) {
                if (token.charAt(i) != word.charAt(i)) {
                    count ++;
                    if (count > 1) {
                        return false;
                    }
                }
            }
            return count == 1;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        int solution1 = solution.solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log", "cog"});
        System.out.println("solution1 = " + solution1);

        // 0
        int solution2 = solution.solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log"});
        System.out.println("solution2 = " + solution2);

    }

}
