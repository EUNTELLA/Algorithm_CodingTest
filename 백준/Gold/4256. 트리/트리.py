import sys
input = sys.stdin.readline

t = int(input())



def post(pos_start, in_start, in_end):
    if in_start > in_end:
        return
    root = preorder[pos_start]
    in_root_idx = inorder.index(root)
    left_size = in_root_idx - in_start
    
    post(pos_start+1 , in_start, in_root_idx -1)
    
    post(pos_start +1 + left_size, in_root_idx+1, in_end)
    
    print(root,end=" ")
    
    
for _ in range(t):
    n = int(input())  

    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    # print("Preorder:", preorder)
    # print("Inorder:", inorder)

    post(0,0,n-1)
    print()