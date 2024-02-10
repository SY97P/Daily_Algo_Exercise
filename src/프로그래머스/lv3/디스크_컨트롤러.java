package 프로그래머스.lv3;

import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * 문제요약
 *
 * 작업 요청부터 종료까지 걸린 시간 평균을 가장 크게 줄이는 방법으로 처리할 때의 평균 시간 구하기
 * 단, 소수점 이하 수는 버리기
 *
 * 제한사항
 *
 * 1 <= 작업 수 <= 500
 * 작업 : [작업 요청 시점, 작업 소요 시간]
 * 0 <= 작업 요청 시간 <= 10^3
 * 1 <= 작업 소요 시간 <= 10^3
 * 하드디스크가 유휴상태일때는 먼저 요청이 들어온 작업부터 처리
 *
 * 해결전략
 *
 * 현재 시간에 작업 대기 중인 작업 중에서 소요시간이 짧은 것부터 처리
 * 현재 시간 기준 요청시점을 넘은 작업을 우선순위큐에 넣음
 * 소요시간 기준 정렬된 우선순위큐에서 작업 하나를 꺼내 작업
 * 현재 시간은 소요시간 만큼 증가
 * 현재 시간 - 작업 요청 시점을 평균총합에 더함
 * 모든 작업을 완료했을때 구해지는 평균 반환
 */

public class 디스크_컨트롤러 {

    private static class Solution {

        public int solution(int[][] jobs) {
            int answer = 0;

            Arrays.sort(jobs, (a, b) -> Integer.compare(a[0], b[0]));

            PriorityQueue<int[]> waitingQueue = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));

            int index = 0;
            int currentTime = 0;
            int previousTime = currentTime - 1;

            while (index < jobs.length) {
                moveToWaitingQueue(waitingQueue, jobs, previousTime, currentTime);

                if (waitingQueue.isEmpty()) {
                    currentTime ++;
                    continue;
                }

                int[] runningTask = waitingQueue.poll();

                index ++;
                previousTime = currentTime;
                currentTime += runningTask[1];
                answer += currentTime - runningTask[0];
            }

            return answer / jobs.length;
        }

        private void moveToWaitingQueue(
                PriorityQueue<int[]> waitingQueue,
                int[][] jobs,
                int previousTime,
                int currentTime
        ) {
            for (int[] job : jobs) {
                if (job[0] > previousTime && job[0] <= currentTime) {
                    waitingQueue.add(job);
                }
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 9
        int solution1 = solution.solution(new int[][]{new int[]{0, 3}, new int[]{1, 9}, new int[]{2, 6}});
        System.out.println("solution = " + solution1);

        // 9
        int solution2 = solution.solution(new int[][]{new int[]{10, 9}});
        System.out.println("solution = " + solution2);

        // 6
        int solution3 = solution.solution(new int[][]{new int[]{0, 3}, new int[]{2, 1}, new int[]{1, 10}});
        System.out.println("solution = " + solution3);

        // 12
        int solution4 = solution.solution(new int[][]{new int[]{0, 9}, new int[]{1, 6}, new int[]{2, 3}});
        System.out.println("solution = " + solution4);
    }

}
