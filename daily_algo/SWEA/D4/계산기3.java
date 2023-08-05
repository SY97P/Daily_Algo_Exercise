/*
#1 672676
#2 1974171
#3 12654
#4 38756
#5 4035
#6 155304
#7 6964
#8 2819
#9 24711
#10 208785
*/

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 계산기3 {
// class solution {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("./SWEA/D4/계산기3.txt"));
		// BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int tc = 1; tc < 11; tc++) {
			int length = Integer.parseInt((br.readLine()));
			String[] line = br.readLine().split("");

			// if (tc != 2)
			// 	continue;

			Stack<String> digit = new Stack<>();
			Stack<String> opera = new Stack<>();

			// 후위 표기하는 부분
			for (String li : line) {
				if (Character.isDigit(li.charAt(0))) {
					digit.push(li);
				}
				else if (li.equals(")")) {
					while (!opera.isEmpty() && !opera.peek().equals("(")) {
						digit.push(opera.pop());
					}
					if (opera.peek().equals("(")) {
						opera.pop();
					}
				} else {
					while (!opera.isEmpty() && li.equals("+") && !opera.peek().equals("(")) {
						digit.push(opera.pop());
					}
					opera.push(li);
				}
					
				// Object[] digit_temp = digit.toArray();
				// Object[] opera_temp = opera.toArray();
	
				// System.out.println(Arrays.toString(digit_temp));
				// System.out.println(Arrays.toString(opera_temp));
				// System.out.println();

				// if (digit_temp.length > 40) 
				// 	break;
			}

			while (!opera.isEmpty()) {
				digit.push(opera.pop());
			}
			
			// Object[] digit_temp = digit.toArray();
			// Object[] opera_temp = opera.toArray();

			// System.out.println(Arrays.toString(digit_temp));
			// System.out.println(Arrays.toString(opera_temp));

			Stack<Integer> stack = new Stack<>();
			while (!digit.isEmpty()) {
				opera.push(digit.pop());
			}

			// 후위 표기한 거 이용해서 계산하는 부분
			while (!opera.isEmpty()) {
				String curr = opera.pop();
				if (Character.isDigit(curr.charAt(0))) {
					stack.push(Integer.parseInt(curr));
				}
				else if (curr.equals("+")){
					stack.push(stack.pop() + stack.pop());
				} else {
					stack.push(stack.pop() * stack.pop());
				}

				// Object[] digit_temp = opera.toArray();
				// Object[] stack_temp = stack.toArray();

				// System.out.println(Arrays.toString(digit_temp));
				// System.out.println(Arrays.toString(stack_temp));
			}

			System.out.printf("#%d %d\n", tc, stack.pop());
		}
	}
}