# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. 
# You are given scores. Store them in a list and find the score of the runner-up. 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = list(arr)
    
    maxel = max(lst)
    cnt = lst.count(maxel)

    for i in range(cnt):
        lst.remove(maxel)
    print(max(lst))