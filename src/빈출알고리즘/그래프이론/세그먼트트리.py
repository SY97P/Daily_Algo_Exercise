def main():
  n, m, k = map(int, input().rstrip().split())

  l = []
  tree = [0] * 3*(10**6)

  for _ in range(n):
    l.append(int(input().rstrip()))

  init(1, 0, n-1)

  for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
      b = b - 1
      diff = c - l[b]
      l[b] = c
      update(1, 0, n-1, b, diff)
    elif a == 2:
      print(sub_sum(1, 0, n-1, b-1, c-1))


# 세그먼트 트리 생성
# node가 담당하는 구간 [start, end]
def init(node, start, end):
	# node가 leaf 노드인 경우 배열의 원소값을 반환
	# node가 leaf 노드인 경우, leaf는 배열의 원소를 가져야 함.
	# 따라서 tree[node] = a[start]
	if start == end:
		tree[node] = l[start]
		return tree[node]
	else:
		# 재귀함수를 이용해 왼쪽 자식과 오른쪽 자식 트리를 만들고 합 저장.
		tree[node] = init(node*2, start, (start+end)//2)
			+ init(node*2+1, (start+end)//2+1, end)
		return tree[node]


# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야 하는 구간 [left, right]
def sub_sum(node, start, end, left, right):

	# 겹치지 않음.
	# 더이상 탐색을 이어갈 필요 없음
	if left > end or right < start:
		return 0

	# 구해야 하는 합의 범위는 [left, right]
	# [start, end] 구간이 포함되고, 해당 node의 자식도 모두 포함
	# 따라서 더이상 탐색할 필요 없이 값 반환
	if left <= start and end <= right:
		return tree[node]

	# 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색
	# 왼쪽 자식 = node * 2
	# 오른쪽 자식 = node * 2 + 1
	# 현재 node가 담당하는 부분 [start, end] 라면,
	# 왼쪽 자식 = [start, (start+end)//2]
	# 오른쪽 자식 = [(start+end)//2+1, end]
	return sub_sum(node*2, start, (start+end)//2, left, right)
		+ sub_sum(node*2+1, (start+end)//2+1, end, left, right)


def update(node, start, end, index, diff):
	if index < start or index > end:
		return

	tree[node] += diff

	# leaf가 아닌 경우, 자식도 변경해줘야 함.
	if start != end:
		update(node*2, start, (start+end)//2, index, diff)
		update(node*2+1, (start+end)//2+1, end, index, diff)


if __name__ == '__main__':
  main()