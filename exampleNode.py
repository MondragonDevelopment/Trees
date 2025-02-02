from BSTNode import *

if __name__ == '__main__':
    v1 = [50, 30, 20, 40, 70, 60, 80]
    r = construct(v1)
    
    inOrder(r)
    print('')

    v2 = [10,5,2,1,5,15,13,14,22]
    r2 = construct(v2)
    inOrder(r2)
    #print(f"\n{r2.right.left.right.val}")

    print(f'\n{search(r2, 12)}')
