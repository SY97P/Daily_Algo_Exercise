package 프로그래머스.lv3;

/**
 * 문제요약
 *
 * CPU 동작
 * CPU 코어 별로 작업 처리 시간 상이
 * 작업이 없는 코어는 바로 다음 작업 수행
 * 2개 이상의 코어가 남는 경우 앞의 코어부터 작업 수행
 *
 * 처리해야 할 작업 n 개와 코어 별 처리시간 cores 가 주어질 때, 마지막 작업 처리하는 코어 번호 구하기
 *
 * 제한사항
 *
 * 2 <= 코어 수 <= 10^4
 * 0 <= 코어 처리시간 <= 10^4
 * 0 <= 처리할 작업 수 <= 5 * 10^4
 *
 * 해결전략 (이분탐색)
 *
 * 맨 처음엔 모든 코어에 작업이 각각 할당
 * 따라서 n 이 코어 개수보다 작거나 같으면 n 에 해당하는 코어 번호 반환
 * 이분탐색으로 모든 코어가 한 번씩 작업하면서 n 을 넘지 않는 횟수를 구하기
 * 해당 횟수에 처리한 작업과 n 의 차이만큼 코어에서 다시 작업
 */

public class 선입_선출_스케줄링 {

    private static class Solution {
        public int solution(int n, int[] cores) {
            if (n <= cores.length) {
                return n;
            }

            n -= cores.length;

            int hour = getHour(n, cores);

            for (int core : cores) {
                n -= (hour - 1) / core;
            }

            for (int i = 0; i < cores.length; i ++) {
                if (hour % cores[i] == 0 && -- n <= 0) {
                    return i + 1;
                }
            }

            return 0;
        }

        private int getHour(int n, int[] cores) {
            int hour = 0;

            int l = 0;
            int r = getMax(cores) * n + 1;
            while (l <= r) {
                int m = (l + r) / 2;
                int cnt = getPossibleWork(m, cores);
                if (cnt < n) {
                    l = m + 1;
                } else {
                    r = m - 1;
                    hour = m;
                }
            }

            return hour;
        }

        private int getMax(int[] cores) {
            int maxValue = 0;
            for (int core : cores) {
                maxValue = Math.max(maxValue, core);
            }
            return maxValue;
        }

        private int getPossibleWork(int hour, int[] cores) {
            int count = 0;
            for (int core : cores) {
                count += hour / core;
            }
            return count;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 2
        int answer1 = s.solution(6, new int[]{1, 2, 3});
        System.out.println("answer = " + answer1);

        // 3
        int answer2 = s.solution(3, new int[]{1, 3, 4, 5, 6});
        System.out.println("answer2 = " + answer2);
    }

}
