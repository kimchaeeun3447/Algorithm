from sys import stdin

for _ in range(int(stdin.readline().rstrip())):
    a = list(map(int, stdin.readline().rstrip()))
  
    for i in range(-1, -len(a), -1):
        if a[i-1] < a[i]:
            front = a[:i-1] 
            back = a[i-1:]
            back.sort() 
            break
    else:
        print("BIGGEST")
        continue
        
    for idx in range(len(back)) :
        if back[idx] > a[i-1]: 
            front.append(back.pop(idx)) 
            front.extend(back) 
            print(*front, sep = '') 
            break