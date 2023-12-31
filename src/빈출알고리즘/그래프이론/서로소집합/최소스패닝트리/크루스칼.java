package 빈출알고리즘.그래프이론.서로소집합.최소스패닝트리;

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.InputStreamReader;


/*
 * Kruskal 알고리즘
 * - MST(최소신장트리) 구하는 알고리즘
 * - MST : 가중치 합이 최소인 모든 정점이 연결된 사이클 없는 트리
 *
 * 1. 모든 간선을 가중치 기준 오름차순 정렬
 * 2. MST에 속한 다른 정점들과 사이클이 발생하지 않는 선에서 최소 가중치 간선을 선택해 MST에 추가
 * 3. 모든 정점이 MST에 포함되도록 반복
 *
 * * 사이클 발생 확인
 * - 유니온-파인드
 */
public class 크루스칼 {

    static int v;
    static int e;
    static Pair[] edges;
    static int[] parent;

    static class Pair implements Comparable<Pair> {
        int cost;
        int start;
        int end;

        Pair(int cost_num, int start_num, int end_num) {
            super();
            this.cost = cost_num;
            this.start = start_num;
            this.end = end_num;
        }

        public void printPair() {
            System.out.println(this.cost + " " + this.start + " " + this.end);
        }

        @Override
        public int compareTo(Pair o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\최소신장트리\\최소스패닝트리.txt"
                )
        );

//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        edges = new Pair[e];

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            edges[i] = new Pair(cost, start, end);
        }

        Arrays.sort(edges);

//        for (Pair p : edges)
//            p.printPair();

        System.out.println(kruskal());
    }

    public static int find(int num) {
        if (parent[num] == num)
            return num;
        return find(parent[num]);
    }

    public static void union(int num, int set_num) {
        if (parent[num] == num) {
            parent[num] = set_num;
            return;
        }
        union(parent[num], set_num);
    }

    public static int kruskal() {
        int result = 0;

        parent = new int[v + 1];
        for (int i = 0; i < v + 1; i++) {
            parent[i] = i;
        }

        for (Pair p : edges) {
            int a = p.start;
            int b = p.end;

            int fa = find(a);
            int fb = find(b);

            // 두 정점의 대표정점이 같다 = 합치면 사이클이 발생한다.
            if (fa == fb)
                continue;
            else if (fa < fb)
                union(b, fa);
            else
                union(a, fb);
            result += p.cost;
        }

        return result;
    }
}
