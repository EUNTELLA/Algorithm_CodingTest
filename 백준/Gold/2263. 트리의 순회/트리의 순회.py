import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



def build(in_left , in_right, post_left, post_right):
    if in_left > in_right:
        return
    
    root = postorder[post_right]
    print(root,end=" ")
    
    root_idx = in_order_idx[root]
    offset = root_idx - in_left
    
    build(in_left,root_idx-1, post_left, post_left + offset -1)
    build(root_idx + 1 , in_right, post_left + offset, post_right-1)
    
    
n = int(input())  # 노드 개수 
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

in_order_idx = {value : index for index, value in enumerate(inorder)}
build(0, n-1, 0 , n-1)
