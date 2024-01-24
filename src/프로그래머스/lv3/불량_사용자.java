package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * 문제요약 <br>
 *<br>
 * '*' 문자로 이름 일부가 가려진 불량사용자를 활용<br>
 * 유저 중에서 불량사용자로 유추 가능한 제재 아디이 목록 경우의 수 구하기<br>
 *<br>
 * 제한사항 <br>
 *<br>
 * 1 <= 유저 목록, 불량사용자 목록 <= 8<br>
 * 1 <= 유저 이름(알파벳 소문자), 불량사용자 목록(알파벳 소문자 + *) 길이 <= 8<br>
 * 유저 이름은 중복되지 않음<br>
 * 불량 사용자 이름에는 '*' 문자가 하나 이상 반드시 들어감<br>
 * 제재 목록에 중복 유저 불가<br>
 * 제재 목록 이름의 순서는 관계 없음<br>
 *<br>
 * 해결전략 <br>
 *<br>
 * 1번 방법. 정규식 활용<br>
 * 불량 사용자 목록을 정규식으로 변환<br>
 * 불량 사용자 목록에 매핑되는 유저 목록을 구함<br>
 * 유저 목록에서 순열 구함<br>
 * 조건에 맞지 않는 제재 목록 제거<br>
 *  중복되는 이름이 있거나<br>
 *  정렬했을때 이미 제재 목록에 있거나<br>
 *<br>
 * 2번 방법. 문자열 비교<br>
 * 각 불량 사용자와 매핑되는 유저 목록을 구함<br>
 * 유저목록에서 순열 구함<br>
 * 조건에 맞지 않는 제재 목록 제거<br>
 *  중복되는 이름이 있거나<br>
 *  정렬했을때 이미 제재 목록에 있거나<br>
 */

public class 불량_사용자 {

    private static class Solution {

        private int n;
        private Set<String> allSanctionLists;
        private List<Set<String>> sanctionedUsers;

        public int solution(String[] user_id, String[] banned_id) {
            n = banned_id.length;
            allSanctionLists = new HashSet<>();
            sanctionedUsers = new ArrayList<>();

            for (String banned: banned_id) {
                Set<String> currentSanctionedUsers = new HashSet<>();

                String regex = banned.replace("*", ".");

                Pattern pattern = Pattern.compile(regex);

                for (String user : user_id) {
                    Matcher matcher = pattern.matcher(user);
                    if (matcher.matches()) {
                        currentSanctionedUsers.add(user);
                    }
                }

                sanctionedUsers.add(currentSanctionedUsers);
            }

            combinations(0, new ArrayList<>());

            return allSanctionLists.size();
        }

        private void combinations(int index, List<String> sanctionList) {
            if (index >= n) {
                if (sanctionList.size() == n) {
                    List<String> copy = new ArrayList<>(sanctionList);
                    copy.sort(String::compareTo);
                    String result = String.join("", copy);
                    allSanctionLists.add(result);
                }
                return;
            }

            for (String sanctionedUser : sanctionedUsers.get(index)) {
                if (sanctionList.contains(sanctionedUser)) {
                    continue;
                }
                sanctionList.add(sanctionedUser);
                combinations(index + 1, sanctionList);
                sanctionList.remove(sanctionList.size() - 1);
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 2
        int solution1 = solution.solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"fr*d*", "abc1**"});
        System.out.println("solution = " + solution1);

        // 2
        int solution2 = solution.solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"*rodo", "*rodo", "******"});
        System.out.println("solution = " + solution2);

        // 3
        int solution3 = solution.solution(new String[]{"frodo", "fradi", "crodo", "abc123", "frodoc"}, new String[]{"fr*d*", "*rodo", "******", "******"});
        System.out.println("solution = " + solution3);

    }

}
