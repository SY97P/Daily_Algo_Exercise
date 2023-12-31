import java.io.FileReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.InputStreamReader;

public class 전력난 {
    static int m;
    static int n;
    static ArrayList<Edges> edges;
    static int[] parent;
    static int maxCost;

    static class Edges {
        int cost;
        int a;
        int b;

        Edges(int a_num, int b_num, int cost_num) {
            this.a = a_num;
            this.b = b_num;
            this.cost = cost_num;
        }

        public void print() {
            System.out.println(this.cost+ " " + this.a + " " + this.b);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\최소신장트리\\전력난.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());

            if (m == 0 && n == 0)
                break;

            edges = new ArrayList<>();
            maxCost = 0;

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                edges.add(new Edges(
                        Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken()),
                        Integer.parseInt(st.nextToken())
                ));
                maxCost += edges.get(edges.size() - 1).cost;
            }
            edges.sort(new Comparator<Edges>() {
                @Override
                public int compare(Edges o1, Edges o2) {
                    return Integer.compare(o1.cost, o2.cost);
                }
            });

            parent = new int[m];
            for (int i = 0; i < m; i++) {
                parent[i] = i;
            }

            System.out.println(maxCost - kruskal());
        }
    }

    public static int kruskal() {
        int result = 0;

        for (Edges e : edges) {
            int fa = find(e.a);
            int fb = find(e.b);

            if (fa == fb)
                continue;
            else if (fa < fb)
                union(e.b, fa);
            else
                union(e.a, fb);
            result += e.cost;
//            System.out.printf("%d %d %d\n", e.cost, e.a, e.b);
        }

        return result;
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
}
