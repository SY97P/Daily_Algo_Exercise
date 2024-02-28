package 프로그래머스.lv3;

import java.util.PriorityQueue;

/**
 * 문제요약
 *
 * 야근 피로도 = sum((남은 일의 작업량)^2)
 * N 시간 동안 야근피로도가 최소화되도록 작업
 * 1시간 동안 1의 작업량 완료 가능
 * N 시간 동안 남은 작업 works에 대한 야근 피로도가 최소가 되도록 할 때의 야근 피로도 값 구하기
 *
 * 제한사항
 *
 * 1 <= works <= 2 * 10^4
 * 1 <= 남은 작업량 <= 5 * 10^4
 * 1 <= n <= 10^6
 *
 * 해결전략
 *
 * 최대한 남은 작업량이 골고루 남도록 작업해야 함.
 * 최대힙을 이용해서 N 번 큰 값을 줄여가기
 * 남은 작업량이 0이 되면 제거하기
 * 남은 작업량을 제곱하여 모두 더하기
 *
 * 문제해결
 *
 * Q. 12번 오답
 * 큐에 있는 작업을 빼는 행위 자체로도 이미 작업을 한 것이나 다름없음
 * 근데 나는 이미 작업한 것을 넣어줄 때 작업 횟수를 갱신했기 때문에 정합성 오류가 발생함.
 */

public class 야근지수 {

    private static class Solution {
        public long solution(int n, int[] works) {
            PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);

            for (int work : works) {
                pq.add(work);
            }

            int count = n;
            while (!pq.isEmpty() && count > 0) {
                count --;
                int work = pq.poll() - 1;
                if (work > 0) {
                    pq.add(work);
                }
            }

            long answer = 0;
            while (!pq.isEmpty()) {
                answer += (long) Math.pow(pq.poll(), 2);
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // 12
        long answer1 = s.solution(4, new int[]{4, 3, 3});
        System.out.println("answer = " + answer1);

        // 6
        long answer2 = s.solution(1, new int[]{2, 1, 2});
        System.out.println("answer = " + answer2);

        // 0
        long answer3 = s.solution(3, new int[]{1, 1});
        System.out.println("answer = " + answer3);

    }

}
