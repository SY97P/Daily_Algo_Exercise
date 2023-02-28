import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.FieldPosition;

public class 문자열집합 {
    static int n;
    static int m;
    static Trie trie;
    static int count;

    public static class TrieNode {
        char token;
        String data;
        TrieNode[] children;

        TrieNode() {
            this.token = '\u0000';
            this.data = null;
            this.children = new TrieNode[26];
            init();
        }

        TrieNode(char val) {
            this.token = val;
            this.data = null;
            this.children = new TrieNode[26];
            init();
        }

        private void init() {
            for (int i = 0; i < 26; i ++) {
                this.children[i] = null;
            }
        }
    }

    public static class Trie {
        TrieNode root;

        Trie() {
            this.root = new TrieNode();
        }

        void insert(String token) {
            TrieNode curr = this.root;

            for (int i=0; i < token.length(); i++) {
                char t = token.charAt(i);
                if (curr.children[t-'a'] == null) {
                    curr.children[t-'a'] = new TrieNode(t);
                }
                curr = curr.children[t-'a'];
            }
            curr.data = token;
        }

        boolean find(String token) {
            TrieNode curr = this.root;

            for (int i = 0; i < token.length(); i ++) {
                char t = token.charAt(i);
                if (curr.children[t-'a'] == null) {
                    return false;
                } else {
                    curr = curr.children[t-'a'];
                }
            }

            return curr.data != null;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new FileReader(
                        "C:\\Users\\onetu\\IdeaProjects\\Daily_Algo_Exercise\\백준\\단계별\\문자열알고리즘1\\문자열집합.txt"
                )
        );
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");

        count = 0;

        n = Integer.parseInt(line[0]);
        m = Integer.parseInt(line[1]);

        trie = new Trie();

        for (int i =0; i < n; i ++) {
            String token = br.readLine().strip();
            trie.insert(token);
        }

        for (int i = 0; i < m; i ++) {
            String token = br.readLine().strip();
            if (trie.find(token)) {
                count += 1;
//                System.out.println(token);
            }
        }

        System.out.println(count);
    }
}
