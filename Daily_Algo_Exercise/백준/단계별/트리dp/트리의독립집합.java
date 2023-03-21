import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class 트리의독립집합 {
    static boolean LOG = false;
    static int INIT_VALUE = 1;

    static int n;
    static int[] weights;
    static ArrayList<Integer>[] adj;
    static int[][] dp;
    static int visited;
    static ArrayList<Integer> track;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\트리dp\\트리의독립집합.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        weights = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++)
            weights[i] = Integer.parseInt(st.nextToken());

        adj = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            adj[i] = new ArrayList<>();
        }

        String input = "";
        while (true) {
            input = br.readLine();
            if (input == null || input.equals(""))
                break;
            String[] data = input.split(" ");
            int u = Integer.parseInt(data[0]);
            int v = Integer.parseInt(data[1]);
            adj[u].add(v);
            adj[v].add(u);
        }

        if (LOG) {
            System.out.println("Adj print");
            for (ArrayList ar : adj)
                System.out.println(ar);
            System.out.println();
        }

        dp = new int[n + 1][3];

        visited = INIT_VALUE;
        solve(INIT_VALUE);
        System.out.println(dp[1][2]);

        if (LOG) {
            System.out.println("DP print");
            for (int[] temp : dp)
                System.out.println(Arrays.toString(temp));
            System.out.println();
        }

        visited = INIT_VALUE;
        track = new ArrayList<>();
        trace(INIT_VALUE, dp[1][2]);
        track.sort(Comparator.naturalOrder());

        for (int t : track)
            System.out.print(t + " ");
        System.out.println();

        if (LOG)
            System.out.println();
    }

    private static void trace(int node, int value) {
        boolean selected = false;

        if (value <= 0)
            return;

        int temp = 0;
        for (int next_node : adj[node]) {
            if ((visited & 1 << (next_node - 1)) == 0) {
                temp += dp[next_node][0];
            }
        }

        if (value - weights[node] == temp) {
            track.add(node);
            selected = true;
        }

        for (int next_node : adj[node]) {
            if ((visited & 1 << (next_node - 1)) == 0) {
                visited |= 1 << (next_node - 1);
                if (selected) {
                    trace(next_node, value - weights[node]);
                } else {
                    trace(next_node, dp[next_node][2]);
                }
            }
        }
    }

    private static void solve(int node) {
        for (int next_node : adj[node]) {
            if ((visited & 1 << next_node - 1) == 0) {
                visited |= 1 << next_node - 1;
                solve(next_node);
                dp[node][0] += dp[next_node][2];
                dp[node][1] += dp[next_node][0];
            }
        }
        dp[node][1] += weights[node];

        if (dp[node][0] < dp[node][1] || (dp[node][0] == 0 && dp[node][1] == 0))
            dp[node][2] = dp[node][1];
        else
            dp[node][2] = dp[node][0];
    }
}
