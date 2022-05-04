import  time

N=12
tab = [-1 for p in range(0, N)]
solutions = []

print(tab)

test = [3, 3, 1, 0]

def absentSurLigne(list, col, k):
   for i in range(0, col):
      if k == list[i]:
         return False
   return True

def absentSurDiagonale(list, col, k):
   for i in range(0, col):
      if abs(k-list[i]) == abs(i-col):
         return False
   return True

def estValide(list, col):
   if col == N:
      global solutions
      solutions.append(list)
      # print(list)
   for k in range(0, N):
      if absentSurLigne(list, col, k) & absentSurDiagonale(list, col, k):
         list[col] = k
         estValide(list, col+1)







if __name__ == '__main__':
   t1 = time.time()
   estValide(tab, 0)
   t2 = time.time()

   print("%d trouvées en %f secondes." %(len(solutions),t2 - t1))


