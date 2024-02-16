package 프로그래머스.lv3;

/**
 * 문제요약<br>
 *<br>
 * N개의 아파트 옥상에 있는 4G 기지국을 전달범위가 더 좁은 5G 기지국으로 변경할 때<br>
 * 모든 아파트에 전파 전달학 위해 설치할 기지국 최소 개수 구하기<br>
 * 기지국 양 옆 w 만큼 전파 도달 (2*w + 1 만큼 전파 도달)<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= N <= 2 * 10^8<br>
 * 1 <= 이미 설치된 기지국 수 <= 10^5<br>
 * 이미 설치된 기지국 위치는 오름차순 정렬<br>
 * 1 <= 전파도달 거리 <= 10^4<br>
 *<br>
 * 해결전략<br>
 *<br>
 * 아파트 개수만큼 전파도달 여부 DP 배열 만들기<br>
 * 이미 설치된 기지국으로 인한 전파 범위를 DP 배열에 기록하기<br>
 * 0인덱스부터 시작해서 (현재 인덱스 + 2*w + 1) 만큼 떨어진 공간까지 설치되지 않은 아파트가 있다면 설치<br>
 * 설치 시 현재 인덱스 += 2*w + 1 로 변경<br>
 * 설치 후 현재 인덱스가 이미 설치된 아파트라면, 설치되지 않은 구간까지 이동<br>
 */

public class 기지국_설치 {

    private static class Solution {

        public int solution(int n, int[] stations, int w) {
            int answer = 0;

            int current = 1;

            for (int station : stations) {
                int left = station - w;
                int right = station + w;

                int[] result = setupBase(current, left, right, w);
                current = result[0];
                answer += result[1];
            }

            answer += setupBase(current, n + 1, n + 1, w)[1];

            return answer;
        }

        private int[] setupBase(int current, int left, int right, int w) {
            int count = 0;
            while (current < left) {
                count ++;
                current += 2 * w + 1;
            }
            current = right + 1;

            return new int[]{current, count};
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 3
        int solution1 = solution.solution(11, new int[]{4, 11}, 1);
        System.out.println("solution = " + solution1);

        // 3
        int solution2 = solution.solution(16, new int[]{9}, 2);
        System.out.println("solution = " + solution2);

        // 3
        int solution3 = solution.solution(10, new int[]{4}, 1);
        System.out.println("solution = " + solution3);

    }
}
