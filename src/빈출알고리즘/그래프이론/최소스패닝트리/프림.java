package 빈출알고리즘.그래프이론.최소스패닝트리;

import java.io.FileReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.PriorityQueue;
//import java.io.InputStreamReader;


/*
 * Prim 알고리즘
 * - MST (최소 스패닝 트리) 구하는 알고리즘
 * - MST : 그래프의 모든 정점을 잇는 사이클 없는 최소 간선 트리
 *
 * 1. 임의의 정점 하나를 MST에 추가
 * 2. MST에 속한 정점과 아닌 정점 간 간선 중에서 최소인 간선을 찾아 MST에 추가 (우선순위큐)
 * 3. 모든 정점이 MST에 포함될 때까지 반복
 */

public class 프림 {
//public class Main {

    static int v;
    static int e;
    static ArrayList<Pair>[] adj;

    static class Pair implements Comparable<Pair> {
        int cost;
        int node;

        Pair(int cost_num, int node_num) {
            this.cost = cost_num;
            this.node = node_num;
        }
        public void print() {
            System.out.println(this.cost + " " + this.node);
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

        adj = new ArrayList[v+1];

        for (int i = 0; i < v+1; i ++)
            adj[i] = new ArrayList<>();

        for (int i = 0; i < e; i ++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            adj[a].add(new Pair(c, b));
            adj[b].add(new Pair(c, a));
        }

//        for (int i = 0; i < n+1; i ++) {
//            for (Pair p : adj[i]) {
//                System.out.print(i + " : ");
//                p.print();
//            }
//        }

        System.out.println(prim());
    }

    public static int prim() {
        int result = 0;

        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.add(new Pair(0, 1));

        boolean[] visited = new boolean[v+1];

        while(!pq.isEmpty()) {
            Pair p = pq.poll();
            int cost = p.cost;
            int node = p.node;

            if (!visited[node]) {
                visited[node] = true;
                result += cost;

                for (Pair next : adj[node]) {
                    pq.add(new Pair(next.cost, next.node));
                }
            }
        }

        return result;
    }
}
