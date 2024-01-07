package 프로그래머스.lv3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 해결전략
 *
 * 1. 주어진 숫자 이진수로 변환
 * 2. 포화 트리가 되도록 이진수 앞에 0 붙이기
 *  - 2^k - 1 = 2진수 k개로 이루어진 포화 이진트리
 * 3. 해당 수가 이진트리가 맞는지 확인하기
 *  - 서브트리의 루트가 0일 때는 모든 자식노드가 0일 때 뿐만임. (자식노드 중에 1이 하나라도 있다면 이진트리가 아님)
 */

public class 표현_가능한_이진트리 {

    private static class Solution {

        private int[] perfectBinaryTreeSizes;

        public int[] solution(long[] numbers) {
            List<Integer> answer = new ArrayList<>();

            perfectBinaryTreeSizes = initPerfectBinaryTreeSizes();

            for (long number : numbers) {
                String binaryString = Long.toBinaryString(number);
                int length = binaryString.length();
                int treeSize = getPerfectBinaryTreeSize(length);

                String perfectBinaryString = makePerfectBinaryString(binaryString, treeSize);

                answer.add(isBinaryTree(perfectBinaryString));
            }

            return answer.stream()
                    .mapToInt(Integer::intValue)
                    .toArray();
        }

        private int isBinaryTree(String binary) {
            int midium = binary.length() / 2;
            if (binary.length() == 1) {
                return 1;
            }

            char root = binary.charAt(midium);
            String leftChild = binary.substring(0, midium);
            String rightChild = binary.substring(midium + 1);

            if (root == '0' && (leftChild.contains("1") || rightChild.contains("1"))) {
                return 0;
            }

            return isBinaryTree(leftChild) * isBinaryTree(rightChild);
        }

        private String makePerfectBinaryString(String binaryString, int treeSize) {
            return "0".repeat(treeSize - binaryString.length()) + binaryString;
        }

        private int getPerfectBinaryTreeSize(int length) {
            int size = 0;

            for (int perfectBinaryTreeSize : perfectBinaryTreeSizes) {
                if (size >= length) {
                    return size;
                }
                size = perfectBinaryTreeSize;
            }

            return perfectBinaryTreeSizes[perfectBinaryTreeSizes.length - 1];
        }

        private int[] initPerfectBinaryTreeSizes() {
            int[] treeSizes = new int[51];

            for (int i = 1; i <= 50; i ++) {
                treeSizes[i] = (int) Math.pow(2, i) - 1;
            }

            return treeSizes;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [1, 1, 0]
        int[] solution1 = solution.solution(new long[]{7, 42, 5});
        System.out.println("solution1 = " + Arrays.toString(solution1));

        // [1, 1, 0]
        int[] solution2 = solution.solution(new long[]{63, 111, 95});
        System.out.println("solution2 = " + Arrays.toString(solution2));
    }

}
