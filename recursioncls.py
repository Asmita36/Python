import sys
sys.setrecursionlimit(500)

'''print(sys.getrecursionlimit())'''

n=0   
def num():
    global n
    n+=1
    print("python",n)
    num()
num()
