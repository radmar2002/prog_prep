###  Raymond Hettingers permutations based solution

from itertools import permutations
import time



n = 4 # number of queens; n must be greater than 4.
columns = range(n)

def board(perm):
    print ("\n".join('_|' * i + 'Q|' + '_|' * (n-i-1) for i in perm) + "\n\n===\n")


start = time.time()

solutions = []

# for perm in permutations(columns):

#     if n == len(set(perm[i]+i for i in columns)) \
#          == len(set(perm[i]-i for i in columns)):

#         print(perm,"\n")
#         board(perm)



for perm in permutations(columns):
    
    print(set(perm[i]-i + n - 1 for i in columns))


end = time.time()
print(end - start)