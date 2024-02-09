package 프로그래머스.lv3;

import java.util.Arrays;
import java.util.Objects;
import java.util.PriorityQueue;

/**
 * 문제요약
 *
 * 필요 연산
 * I 숫자 : 큐에 숫자 삽입
 * D 1   : 큐 최댓값 삭제
 * D -1  : 큐 최솟값 삭제
 *
 * 모든 연산을 수행했을때 큐가 비어있으면 [0, 0] 반환
 * 비어있지 않으면 [최댓값, 최솟값] 구하기
 *
 * 제한사항
 *
 * 1 <= 명령문 수 <= 10^6
 * 최댓값, 최솟값이 두 개 이상인 경우, 그 중 하나만 제거
 * 빈 큐에 삭제연산 발생 시 해당 연산은 무시
 *
 * 해결전략
 *
 * 최대힙큐와 최소힙큐 두 개 만들기
 * 삽입 연산은 두 큐 모두 넣어주기
 * 최댓값 제거 연산은 최대힙큐에서 poll() 로 찾은 다음 최소힙큐에서 remove() 로 제거
 * 최솟값 제거 연산은 최소힙큐에서 poll() 로 찾은 다음 최대힙큐에서 remove() 로 제거
 *
 */

public class 이중우선순위큐 {

    private static class Solution {
        public int[] solution(String[] operations) {
            PriorityQueue<Integer> maxQ = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
            PriorityQueue<Integer> minQ = new PriorityQueue<>();

            for (String operation : operations) {
                String[] split = operation.split(" ");
                String command = split[0];
                int operand = Integer.parseInt(split[1]);

                if (Objects.equals(command, "I")) {
                    maxQ.add(operand);
                    minQ.add(operand);
                } else {
                    if (maxQ.isEmpty() || minQ.isEmpty()) {
                        continue;
                    }

                    if (operand == 1) {
                        int maxValue = maxQ.poll();
                        minQ.remove(maxValue);
                    } else {
                        int minValue = minQ.poll();
                        maxQ.remove(minValue);
                    }
                }
            }

            if (minQ.isEmpty() || maxQ.isEmpty()) {
                return new int[]{0, 0};
            }
            return new int[]{maxQ.poll(), minQ.poll()};
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [0, 0]
        int[] solution1 = solution.solution(new String[]{"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"});
        System.out.println("solution = " + Arrays.toString(solution1));

        // [333, -45]
        int[] solution2 = solution.solution(new String[]{"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"});
        System.out.println("solution = " + Arrays.toString(solution2));

    }

}
