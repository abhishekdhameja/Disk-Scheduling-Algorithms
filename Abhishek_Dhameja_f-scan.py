import sys
#f=open('C:\\Users\\dhame\\Desktop\\USC\\Sem 1\\INF 551\\Assignments\\HW1\\testCases\\testCases\\test7.txt','r')
f=open(sys.argv[1],'r')
line1=f.readline().rstrip("\n")
curr_position=int(line1)
line2=f.readline().rstrip('\n')
requests=[int(i) for i in line2.split(",")]
result=[]
cost=0
inwards=0
requestlists = [requests[x:x+10] for x in xrange(0, len(requests), 10)]

def movesInwards(next_position,curr_position):
    if (next_position > curr_position):
        return 0
    else:
        return 1

def scan(requestlist,head,time):
    #print 'list:',requestlist
    #print 'head at',head
    #print 'previous time is',time
    requestlist.sort()
    left = [x for x in requestlist if x < head]
    left.reverse()
    right = [x for x in requestlist if x > head]

    while (head in requestlist):
        result.append(head)
        requestlist.remove(head)
        requests.remove(head)

    for i in requestlist:
        if (i == requestlist[0]):
            mindist = abs(head - i)
            next_position = i
            inwards = movesInwards(next_position, head)
            continue
        else:
            if (mindist > abs(head - i)):
                mindist = abs(head - i)
                next_position = i
                inwards = movesInwards(next_position, head)
            elif (mindist == abs(head - i)):
                if (next_position > i):
                    next_position = i
                inwards = movesInwards(next_position, head)
    #print 'next position:',next_position
    #print 'inwards:',inwards

    if (inwards == 1):
        for x in left:
            time += head - x
            head = x
            requests.remove(x)
            result.append(head)
        if (len(right) != 0):
            time += head
            head = 0
            for x in right:
                time += abs(head - x)
                head = x
                requests.remove(x)
                result.append(head)
    else:
        for x in right:
            time += abs(head - x)
            head = x
            requests.remove(x)
            result.append(head)
        if (len(left) != 0):
            time += 199 - head
            head = 199
            for x in left:
                time += head - x
                head = x
                requests.remove(x)
                result.append(head)

    return head,time

for x in requestlists:
    curr_position,cost=scan(x,curr_position,cost)
    #print 'head after iteration at:',curr_position
    #print 'cost after iteration',cost

print str(result)[1:-1]
print cost
print result[len(result)-1],",",cost

