package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * 문제요약<br>
 *<br>
 * 매칭점수가 가장 높은 페이지의 인덱스 구하기 (여러개면 번호가 가장 적은 페이지 인덱스 구하기)<br>
 * 웹페이지 점수 = [기본점수, 외부링크 수, 링크점수, 매칭점수]<br>
 * 기본점수 : 검색어 등장 수 (대소문자 무시)<br>
 * 외부링크 수 : 다른 외부페이지로 연결된 링크 개수<br>
 * 링크점수 : 링크 걸린 다른 웹페이지 기본점수 / 외부링크 수<br>
 * 매칭점수 : 기본점수 + 링크점수<br>
 *<br>
 * 제한사항<br>
 *<br>
 * 1 <= 페이지 수 <= 20<br>
 * 1 <= 웹페이지 문자열 길이 <= 1_500<br>
 * 웹페이지 인덱스는 0부터 시작<br>
 * 웹페이지 태그 : <meta property="og:url" content="웹페이지" /><br>
 * 외부링크 태그 : <a href="외부링크"><br>
 * 모든 url 은 https:// 로 시작<br>
 * 1 <= 검색어(한 개의 영단어, 대소문자 무시) <= 12<br>
 * 검색어는 완전히 일치하는 경우에만 기본점수에 반영<br>
 *  aba -> abab (안 됨) / aba@aba aba (3개 일치)<br>
 * 매칭점수가 높은 페이지가 여러개면 그 중 최소 인덱스 번호를 반환<br>
 *<br>
 * 해결전략<br>
 *<br>
 * 검색어, 페이지 소문자 변환<br>
 * 페이지 별 기반점수 구하기 (순회, 정규식)<br>
 *  기본점수 구하기<br>
 *  외부링크 수 구하기<br>
 * 페이지 별 의존점수 구하기<br>
 *  링크점수 구하기<br>
 *  매칭점수 구하기<br>
 * (매칭점수 DESC, 인덱스 ASC) 정렬<br>
 * 최상단 페이지 인덱스 반환<br>
 *<br>
 * 신경쓸거<br>
 *<br>
 * 링크점수는 현재 페이지가 링크로 등록된 페이지의 기본 점수를 가져오는것.<br>
 *
 */

public class 매칭_점수 {

    private static class Solution {

        public int solution(String word, String[] pages) {
            Map<String, PageInfo> pageInfoMap = new HashMap<>();

            renderPages(word, pages, pageInfoMap);
            calculateLinkScore(pageInfoMap);

            return pageInfoMap.values().stream()
                    .sorted((p1, p2) -> {
                        if (Double.compare(p1.matchingScore, p2.matchingScore) == 0) {
                            return Integer.compare(p1.pageIndex, p2.pageIndex);
                        }
                        return Double.compare(p2.matchingScore, p1.matchingScore);
                    })
                    .map(pageInfo -> pageInfo.pageIndex)
                    .findFirst()
                    .orElse(0);
        }

        private void calculateLinkScore(Map<String, PageInfo> pageInfoMap) {
            Set<String> urlSet = pageInfoMap.keySet();
            for (String url : urlSet) {
                for (String linkTo : pageInfoMap.get(url).externalLinks) {
                    if (!urlSet.contains(linkTo)) {
                        continue;
                    }
                    double currentLinkScore = (double) pageInfoMap.get(url).basicScore / pageInfoMap.get(url).externalLinks.size();
                    pageInfoMap.get(linkTo).linkScore += currentLinkScore;
                    pageInfoMap.get(linkTo).matchingScore += currentLinkScore;
                }
            }
        }

        private void renderPages(String word, String[] pages, Map<String, PageInfo> pageInfoMap) {
            word = word.toLowerCase();
            for (int i = 0; i < pages.length; i ++) {
                String page = pages[i].toLowerCase()
                        .replace("\n", " ");

                String url = getUrl(page);
                int wordCount = getWordCount(word, page);
                List<String> linkedPageUrl = getLinkPageUrl(page);

                pageInfoMap.put(url, new PageInfo(i, wordCount, linkedPageUrl));
            }
        }

        private List<String> getLinkPageUrl(String page) {
            Pattern pattern = Pattern.compile("<a href=\"(.+?)\">");
            Matcher matcher = pattern.matcher(page);

            List<String> urls = new ArrayList<>();

            while (matcher.find()) {
                urls.add(matcher.group(1));
            }

            return urls;
        }

        private int getWordCount(String word, String page) {
            int count = 0;
            String[] tokens = page.split("[^a-z]");
            for (String token : tokens) {
                if (Objects.equals(token, word)) {
                    count ++;
                }
            }
            return count;
        }

        private String getUrl(String page) {
            Pattern pattern = Pattern.compile("<meta property=\"og:url\" content=\"(.+?)\"/>");
            Matcher matcher = pattern.matcher(page);
            matcher.find();
            return matcher.group(1);
        }

        private static class PageInfo {
            int pageIndex;
            int basicScore;
            List<String> externalLinks;
            double linkScore;
            double matchingScore;

            PageInfo(int pageIndex, int basicScore, List<String> externalLinks) {
                this.pageIndex = pageIndex;
                this.basicScore = basicScore;
                this.externalLinks = externalLinks;
                this.linkScore = 0;
                this.matchingScore = basicScore;
            }
        }

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 0
        int solution1 = solution.solution("blind", new String[]{
                "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
                "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
                "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"});
        System.out.println("solution1 = " + solution1);

        // 1
        int solution2 = solution.solution("Muzi", new String[]{
                "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
                "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"});
        System.out.println("solution2 = " + solution2);

    }

}
