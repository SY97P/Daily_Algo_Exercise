package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/**
 * ** 문제 요약 **
 * <p>
 * 점수 = {근태점수, 동평점수}
 * 1. 다른 사원보다 두 점수 모두 낮은 경우가 있다면 인센티브 미지급
 * 2. 그렇지 않은 사원들은 두 점수 합을 기준으로 인센티브 차등 지급
 * 3. 같은 점수로 인한 동석차 인정 & 동석차 만큼 다음 석차 밀림
 * 4. 점수 배열의 첫 원소인 완호의 점수로 얻어지는 인센티브 석차 반환
 * <p></p>
 *
 * **해결전략**
 * <p>
 * 1. 완호 점수 추출
 * 2. (근태점수 DESC > 동평점수 ASC) 정렬
 * 3. 인센티브 지급
 *  3-0. 인센티브 리스트에 (근태점수, 동평점수) 저장
 *  3-1. 최대 동평점수 >  동평점수 -> 인센티브 미지급(인센티브 리스트에 추가 X)
 *  3-2. 최대 동평점수 <= 동평점수 -> 인센티브 지급 (인센티브 리스트에 추가)
 * 4. 인센티브 리스트 정렬 (sum(근태점수, 동평점수) DESC)
 * 5. 인센티브 리스트에서 완호 점수 찾기
 *
 */

public class 인사고과 {

    private static class Solution {

        public int solution(int[][] scores) {
            int[] target = scores[0];

            Arrays.sort(scores, (a, b) -> {
                if (a[0] == b[0]) {
                    return a[1] - b[1];
                }
                return b[0] - a[0];
            });

            PriorityQueue<int[]> incentiveQueue = new PriorityQueue<>((a, b) -> {
                if (a[0] + a[1] == b[0] + b[1]) {
                    return b[0] - a[0];
                }

                return (b[0] + b[1]) - (a[0] + a[1]);
            });

            int maxAttitudeScore = scores[0][1];
            for (int[] score : scores) {
                if (maxAttitudeScore > score[1]) {
                    if (score == target) {
                        return -1;
                    }
                    continue;
                }

                maxAttitudeScore = score[1];
                incentiveQueue.add(score);
            }

            int answer = 1;
            while (!incentiveQueue.isEmpty()) {
                int[] incentive = incentiveQueue.poll();

                if (incentive[0] == target[0] && incentive[1] == target[1]) {
                    return answer;
                }

                answer++;
            }
            return -1;
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
//        int[][] case1 = {{2, 2}, {1, 4}, {3, 2}, {3, 2}, {2, 1}};
//        int solution1 = solution.solution(case1);
//        System.out.println("solution1 = " + solution1);

        // 3
//        int[][] case2 = {{4, 0}, {2, 3}, {4, 4}, {2, 6}};
//        int solution2 = solution.solution(case2);
//        System.out.println("solution2 = " + solution2);

        // 3
        int[][] case3 = {{2, 2}, {2, 2}, {2, 3}, {3, 2}};
        int solution3 = solution.solution(case3);
        System.out.println("solution3 = " + solution3);
    }

}
