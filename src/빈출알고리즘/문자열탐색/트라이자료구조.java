package 빈출알고리즘.문자열탐색;

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class 트라이자료구조 {
	static int t;
	static int n;
	static Trie trie;

	static class TrieNode {
		char node;
		String data = null;
		Map<Character, TrieNode> children;
		
		TrieNode(char num, String data) {
			this.node = num;
			this.data = data;
			this.children = new HashMap<>();
		}
	}

	private static class Trie {
		TrieNode root;

		Trie() {
			this.root = new TrieNode('\u0000', null);
		}

		public void insert(String digits) {
			TrieNode curr = this.root;

			for (int i=0; i < digits.length(); i ++) {
				char digit = digits.charAt(i);
				// 현재 노드의 자식이랑 현재 문자가 일치하면 현재 위치를 자식노드로 이동.
				if (!curr.children.containsKey(digit))
					curr.children.put(digit, new TrieNode(digit, null));
				curr = curr.children.get(digit);
			}		
			curr.data = digits;
		}

		public boolean find(String digits) {
			TrieNode curr = this.root;

			for (int i = 0; i < digits.length(); i ++) {
				char digit = digits.charAt(i);
				if (!curr.children.containsKey(digit)) 
					return false;
				else
					curr = curr.children.get(digit);
			}

			if (curr.data != null)
				return true;
			return false;
		}

		public void print() {
			dfs(this.root, 0);
		}

		private void dfs(TrieNode node, int depth) {
			for (char child : node.children.keySet()) {
				System.out.print("--".repeat(depth));
				System.out.println(child);
				dfs(node.children.get(child), depth+1);
			}
		}
	}



	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("./백준/단계별/문자열알고리즘1/전화번호목록.txt"));

		t = Integer.parseInt(br.readLine());

		for (int tc = 0; tc < t; tc ++) {
			System.out.println("TC : " + tc);
			
			n = Integer.parseInt(br.readLine());

			trie = new Trie();

			for (int k=0; k < n; k ++) {
				String digits = br.readLine().strip();
				System.out.print(digits);

				if (trie.find(digits))
					System.out.println("is in trie");
				else {
					System.out.println("is not in trie. So, I add it");
					trie.insert(digits);
				}
			}

			// Test
			System.out.println("TEST");
			System.out.println("911 is in trie " + trie.find("911"));
			System.out.println("1 is in trie " + trie.find("1"));

			// 트라이 구조 출력
			trie.print();

			System.out.println();
		}
	}
}