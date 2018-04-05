#scan
import sys
#f=open('C:\\Users\\dhame\\Desktop\\USC\\Sem 1\\INF 551\\Assignments\\HW1\\testCases\\testCases\\test7.txt','r')
f=open(sys.argv[1],'r')
line1=f.readline().rstrip("\n")
curr_position=int(line1)
line2=f.readline().rstrip('\n')
requests=[int(i) for i in line2.split(",")]
requests.sort()
left=[x for x in requests if x < curr_position]
left.reverse()
right=[x for x in requests if x > curr_position]
#print left
#print right
result=[]
cost=0
#print curr_position

def movesInwards(next_position,curr_position):
    if (next_position > curr_position):
        return 0
    else:
        return 1

while(curr_position in requests):
    result.append(curr_position)
    requests.remove(curr_position)
#print 'result:',result

for i in requests:
    last=i
    if(i == requests[0]):
        mindist = abs(curr_position - i)
        next_position=i
        inwards = movesInwards(next_position, curr_position)
        continue
    else:
        if(mindist>abs(curr_position-i)):
            mindist=abs(curr_position-i)
            next_position=i
            inwards = movesInwards(next_position, curr_position)
        elif (mindist==abs(curr_position-i)):
            if(next_position>i):
                next_position = i
            inwards = movesInwards(next_position, curr_position)

if(inwards==1):
    for x in left:
        cost+= curr_position-x
        curr_position=x
        requests.remove(x)
        result.append(curr_position)
    if(len(right)!=0):
        cost+=curr_position
        curr_position=0
        for x in right:
            cost += abs(curr_position - x)
            curr_position = x
            requests.remove(x)
            result.append(curr_position)
else:
    for x in right:
        cost+= abs(curr_position-x)
        curr_position=x
        requests.remove(x)
        result.append(curr_position)
    if(len(left)!=0):
        cost+=199-curr_position
        curr_position=199
        for x in left:
            cost += curr_position - x
            curr_position = x
            requests.remove(x)
            result.append(curr_position)

print str(result)[1:-1]
print cost
print result[len(result)-1],",",cost