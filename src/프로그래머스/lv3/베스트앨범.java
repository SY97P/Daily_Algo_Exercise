package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

/**
 * 문제요약
 *
 * 노래수록 기준에 맞춰 베스트앨범을 제작할 때 해당 앨범에 들어갈 노래 고유번호 순서대로 구하기
 * 각 장르별로 최대 2곡만 수록
 * 노래수록 기준
 *  1순위 : 많이 재생된 장르 먼저
 *  2순위 : 많이 재생된 노래 먼저
 *  3순위 : 고유번호 낮은 노래 먼저
 *
 * 제한사항
 *
 * 1 <= 장르목록 길이 == 재생횟수 길이 <= 10^4
 * 장르 종류 < 100
 * 장르에 속한 곡이 하나면, 해당 곡 하나만 앨범 수록
 * 모든 장르의 재생횟수 다름
 *
 * 해결전략 (우선순위큐)
 *
 * 각 장르별로 (총 재생횟수 합, 각 노래 최적힙(재생횟수 DESC, 고유번호 ASC)) 최대힙에 모으기
 * 장르별 최대힙이 모두 빌 때까지 각 장르를 하나씩 뽑아서 1 ~ 2곡 수록
 * 곡 수록시 각 노래 최적힙에서 뽑아서 수록
 * 수록 시 각 노래의 고유번호를 반환
 */

public class 베스트앨범 {

    private static class Solution {
        public int[] solution(String[] genres, int[] plays) {
            List<Integer> answer = new ArrayList<>();

            Map<String, PriorityQueue<Song>> map = getAllSongInfos(genres, plays);

            includeSongsIntoAlbum(map, answer);

            return answer.stream().mapToInt(Integer::intValue).toArray();
        }

        private void includeSongsIntoAlbum(Map<String, PriorityQueue<Song>> map, List<Integer> answer) {
            for (String genre : getGenresOrder(map)) {
                PriorityQueue<Song> songs = map.get(genre);
                int includeCount = 2;
                while (!songs.isEmpty() && includeCount > 0) {
                    Song song = songs.poll();
                    answer.add(song.index);
                    includeCount --;
                }
            }
        }

        private Map<String, PriorityQueue<Song>> getAllSongInfos(String[] genres, int[] plays) {
            Map<String, PriorityQueue<Song>> map = new HashMap<>();

            for (int i = 0; i < genres.length; i ++) {
                PriorityQueue<Song> songs = map.getOrDefault(genres[i], new PriorityQueue<>());
                songs.add(new Song(i, plays[i]));
                map.put(genres[i], songs);
            }
            return map;
        }

        private List<String> getGenresOrder(Map<String, PriorityQueue<Song>> map) {
            return map.entrySet()
                    .stream()
                    .sorted((entry1, entry2) -> {
                        PriorityQueue<Song> songs1 = entry1.getValue();
                        PriorityQueue<Song> songs2 = entry2.getValue();
                        int totalPlayCount1 = songs1.stream()
                                .map(song -> song.playCount)
                                .mapToInt(Integer::intValue)
                                .sum();
                        int totalPlayCount2 = songs2.stream()
                                .map(song -> song.playCount)
                                .mapToInt(Integer::intValue)
                                .sum();
                        return totalPlayCount2 - totalPlayCount1;
                    })
                    .map(Entry::getKey)
                    .collect(Collectors.toList());
        }

        private static class Song implements Comparable<Song> {
            int index;
            int playCount;

            Song(int index, int playCount) {
                this.index = index;
                this.playCount = playCount;
            }

            @Override
            public int compareTo(Song o) {
                if (playCount == o.playCount) {
                    return index - o.index;
                }
                return o.playCount - playCount;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [4, 1, 3, 0]
        int[] solution1 = solution.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500});
        System.out.println("solution = " + Arrays.toString(solution1));

        // [4, 1, 0, 2]
        int[] solution2 = solution.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{200, 600, 200, 200, 2500});
        System.out.println("solution = " + Arrays.toString(solution2));

    }

}
