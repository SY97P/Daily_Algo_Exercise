package 프로그래머스.lv3;

/**
 * 문제요약<br>
 *<br>
 * 징검다리를 건너서 개울을 건널 수 있는 최대 인원 구하기<br>
 * 디딤돌마다 숫자가 있고, 밟을때마다 1씩 줄어듬<br>
 * 디딤돌 숫자가 0이 되면 밟을 수 없음<br>
 * 한 번에 여러 0인 디딤돌을 건너 뛸 수 있음<br>
 * 단, 여러 칸 중에서 가장 가까운 디딤돌로만 건너뛸 수 있음<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 인원 제한 없음<br>
 * 1 <= 디딤돌 개수 <= 2 * 10^5<br>
 * 1 <= 디딤돌 숫자 <= 2 * 10^8<br>
 * 1 <= 한 번에 건너뛸 수 있는 디딤돌 수 <= 디딤돌 개수<br>
 *<br>
 * 해결전략 (이분탐색)<br>
 *<br>
 * m = 건널 수 있는 인원 최대 예상 추정치<br>
 * m 인원 징검다리를 건너기 가능 여부 판단<br>
 *  건널 수 없으면 인원 줄여서 다시<br>
 *      0 인 구간으로 뛰어넘으려고 하는데가 k 값보다 크면 실패<br>
 *  건널 수 있으면 인원 늘려서 다시 + 정답 갱신<br>
 *<br>
 *  신경쓸거<br>
 *<br>
 *  k 칸 이상을 건너뛰게 되면 못 건너는거<br>
 *<br>
 */

public class 징검다리_건너기 {

    private static class Solution {

        public int solution(int[] stones, int k) {

            int answer = 0;

            int l = 0;
            int r = 2 * (int) 1e8 + 1;

            while (l <= r) {
                int m = (l + r) / 2;

                if (possible(m, k, stones)) {
                    answer = m;
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }

            return answer;
        }

        private boolean possible(int m, int k, int[] stones) {
            int jumpCount = 0;
            for (int stone : stones) {
                if (stone - m < 0) {
                    if (++ jumpCount >= k) {
                        return false;
                    }
                } else {
                    jumpCount = 0;
                }
            }
            return true;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 3
        int solution1 = solution.solution(new int[]{2, 4, 5, 3, 2, 1, 4, 2, 5, 1}, 3);
        System.out.println("solution1 = " + solution1);
    }

}
