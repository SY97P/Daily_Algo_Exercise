package 프로그래머스.lv3;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

/**
 *
 * 문제요약 <br>
 *
 * center = root<br>
 * 자신에게 발생한 이익의 10%를 추천인에게 배분, 나머지는 자기가 가짐<br>
 * 10% 계산 시 원 단위에서 절사 (10% 금액이 1원인 경우 0원 배분)<br>
 * 칫솔 가격 = 100원 / 1개<br>
 * 각 판매원이 얻은 이익금 총합을 반환<br>
 *<br>
 * 제한사항<br>
 *
 * 1 <= 판매원 수, 추천인 수 <= 10^4<br>
 * 추천인[i] = 판매원[i]를 악의 수렁텅이로 끌고 들어간 사람 (10% 줘야하는 사람)<br>
 * 최고 빌런은 추천인에 '-' 로 되어있음<br>
 * 1 <= 판매내역 <= 10^6<br>
 * 판매내역에는 중복된 이름 가능<br>
 * 1 <= 판매량 <= 10^2<br>
 * 모든 조직원 이름은 10자 이내 영문 알파벳 소문자<br>
 *<br>
 * 해결전략<br>
 *
 * DFS<br>
 * 각 판매내역 별로 자신의 수익금 계산<br>
 * 10% 제외하고 자신의 이득에 추가<br>
 * 10%를 추천인에게 전달 (DFS)<br>
 * 10% 금액이 1 미만이거나, 더이상 추천인이 없을때까지 DFS<br>
 * 조직원 순서대로 자신의 이익금을 배열에 담아 반환<br>
 *
 */

public class 다단계_칫솔_판매 {

    private static class Solution {

        private static final int PRICE = 100;

        private int n;
        private int m;
        private Map<String, String> pedigree;
        private Map<String, Integer> profit;

        public int[] solution(String[] enrolls, String[] referrals, String[] sellers, int[] amounts) {
            n = enrolls.length;
            m = sellers.length;
            int[] answer = new int[n];
            pedigree = new HashMap<>();
            profit = new HashMap<>();

            for (int i = 0; i < n; i ++) {
                pedigree.put(enrolls[i], referrals[i]);
                profit.put(enrolls[i], 0);
            }

            for (int i = 0; i < m; i ++) {
                dfs(sellers[i], PRICE * amounts[i]);
            }

            for (int i = 0; i < n; i ++) {
                answer[i] = profit.get(enrolls[i]);
            }

            return answer;
        }

        private void dfs(String seller, int gain) {
            int dept = getDept(gain);
            profit.put(seller, profit.get(seller) + (gain - dept));
            if (dept <= 0 || Objects.equals(pedigree.get(seller), "-")) {
                return;
            }
            dfs(pedigree.get(seller), dept);
        }

        private int getDept(int gain) {
            return gain * 0.1 < 1 ? 0 : (int) (gain * 0.1);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [360, 958, 108, 0, 450, 18, 180, 1080]
        int[] solution1 = solution.solution(
                new String[]{"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"},
                new String[]{"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"},
                new String[]{"young", "john", "tod", "emily", "mary"}, new int[]{12, 4, 2, 5, 10});
        System.out.println("solution1 = " + Arrays.toString(solution1));

        // [0, 110, 378, 180, 270, 450, 0, 0]
        int[] solution2 = solution.solution(
                new String[]{"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"},
                new String[]{"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"},
                new String[]{"sam", "emily", "jaimie", "edward"}, new int[]{2, 3, 5, 4});
        System.out.println("solution2 = " + Arrays.toString(solution2));
    }

}
