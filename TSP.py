import sys
n = 5
dist = [[0,12,10,19,8],[12,0,3,7,6],[10,3,0,2,20],[19,7,2,0,4],[8,6,20,4,0]]

completed_visit = (1<<5) -1 #Representing all cities as 11111
dp = [[-1 for _ in range(n)] for _ in range(2**n)] #Initialize dp table with -1
#Memonization table with dimension (2^n)xn
#d[i][j] stores the min cost for visiting city i with current city j

def tsp(mark,pos):
    if mark == completed_visit:
        return dist[pos][0] #cost to returning to starting ity when all cities are visited
    if dp[mark][pos]!=-1:
        return dp[mark][pos]
   
    ans = sys.maxsize # initializing to a large value
    
    for city in range(n):
        if mark & (1<<city) ==0: #If City  is not visited
            new_ans=dist[pos][city] + tsp(mark | (1<<city),city) #calculate cost of visiting it
            ans = min(new_ans,ans) 
    dp[mark][pos]=ans #memoize the result
    return ans
    
for i in range(1<<n):
    for j in range(n):
        dp[i][j]=-1
        
print("Result: ",tsp(1,0)) #Initial state as starting city
