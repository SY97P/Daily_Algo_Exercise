package SWEA.D3;/*

#1 471034 815406 542284 170257 228297 740370 785047 677617 834173 648732 
#2 364373 466241 450661 237978 437060 679163 812457 727955 262600 218437 
#3 562558 606238 599072 901079 648987 991218 138805 551830 793601 911203 
#4 473893 754291 376044 625502 726892 675628 577615 202218 294934 272419 
#5 998955 640601 735077 815674 472787 409220 611754 821736 474544 410783 
#6 477531 707563 112007 366337 887845 148402 850777 298548 383970 952541 
#7 191509 619449 218830 814428 864237 528831 951407 783449 150278 484266 
#8 611841 364298 772115 790896 707995 429462 335725 189113 435637 971472 
#9 885312 812032 639909 338989 672494 421265 383659 140603 174105 605989 
#10 660691 200576 435127 482997 733701 294859 743083 652241 756248 619607 

*/

import java.util.Scanner;
// import java.io.FileInputStream;
import java.util.LinkedList;
import java.util.List;

class 암호문3
{
	static int n;
	static int m;

	static List<Integer> crypt;
	
	public static void main(String args[]) throws Exception
	{
		// Scanner sc = new Scanner(new FileInputStream("./SWEA/D3/암호문3.txt"));
		Scanner sc = new Scanner(System.in);

		for (int tc = 1; tc < 11; tc ++) {
			n = sc.nextInt();
	
			crypt = new LinkedList<Integer>();
			for (int i = 0; i < n; i ++) {
				crypt.add(sc.nextInt());
			}
	
			sc.nextLine();
	
			m = sc.nextInt();
	
			for (int k = 0; k < m; k ++) {
				String oper = sc.next();
	
				if (oper.equals("I")) {
					int x = sc.nextInt();
					int y = sc.nextInt();
	
					for (int i = x; i < x + y; i ++) {
						crypt.add(i, sc.nextInt());
					}
				} else if (oper.equals("D")) {
					int x = sc.nextInt();
					int y = sc.nextInt();
	
					for (int i = 0; i < y; i++) {
						crypt.remove(x);
					}
				} else if (oper.equals("A")) {
					int y = sc.nextInt();
	
					for (int i = 0; i < y; i ++) {
						crypt.add(sc.nextInt());
					}
				}
			}
	
			System.out.printf("#%d ", tc);
			for (int i = 0; i < 10; i ++) {
				System.out.print(crypt.get(i) + " ");
			}
			System.out.println();
			
		}
	}
}