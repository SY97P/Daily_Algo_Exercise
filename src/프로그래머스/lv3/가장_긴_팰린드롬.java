package 프로그래머스.lv3;

/**
 * 문제요약
 *
 * 팰린드롬 : 앞뒤를 뒤집어도 똑같은 문자열
 * 주어진 문자열의 부분 문자열 중 가장 긴 길이의 팰린드롬 길이 구하기
 *
 * 제한사항
 *
 * 1 <= 문자열 길이 <= 2_500
 * 문자열은 알파벳 소문자로만 구성
 *
 * 해결전략
 *
 * Java는 DFS로 풀려고 하면 시간초과가 발생 (trunning을 해도 소용 없음)
 * 반복문으로 풀어야 함.
 * 길이를 하나씩 줄여가면서 각 길이에 해당하는 문자열을 추출하고, 그 문자열이 팰린드롬인지 여부 검사
 * 팰린드롬이면 그 당시의 길이를 반환
 *
 * 문제해결
 *
 * Q. 효율성 1번 시간초과
 * String.substring() 메소드를 사용해서 시간초과
 * start, end 인덱스를 기준으로 자릿값을 연산하여 해결
 */

public class 가장_긴_팰린드롬 {

    private static class Solution {

        public int solution(String s) {
            for (int len = s.length(); len > 1; len --) {
                for (int start = 0; start + len <= s.length(); start ++) {
                    int end = start + len;
                    if (isPalindrome(s, len, start, end)) {
                        return len;
                    }
                }
            }

            return 1;
        }

        private boolean isPalindrome(String s, int len, int start, int end) {
            for (int i = 0; i < len; i ++) {
                if (s.charAt(start + i) != s.charAt(end - 1 - i)) {
                    return false;
                }
            }
            return true;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 7
        int answer1 = s.solution("abcdcba");
        System.out.println("answer1 = " + answer1);

        // 3
        int answer2 = s.solution("abacde");
        System.out.println("answer2 = " + answer2);

    }

}
