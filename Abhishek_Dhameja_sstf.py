#sstf
import sys
f=open('C:\\Users\\dhame\\Downloads\\testcases&answers\\test2.txt','r')
#f=open(sys.argv[1],'r')
line1=f.readline().rstrip("\n")
curr_position=int(line1)
line2=f.readline().rstrip('\n')
requests=[int(i) for i in line2.split(",")]
result=[]
cost=0
print 'current position:',curr_position
print 'Request:',requests

while(len(requests)!=0):
    for i in requests:
        print "i is:",i
        if(i == requests[0]):
            mindist = abs(curr_position - i)
            #print "mindist is",mindist
            next_position=i
            continue
        else:
            if(mindist>abs(curr_position-i)):
                mindist=abs(curr_position-i)
                #print "mindist is", mindist
                next_position=i
            elif (mindist==abs(curr_position-i)):
                if(next_position>i):
                    next_position = i
    #print "Mind dist is", mindist
    cost+=mindist
    #print "next position", next_position
    result.append(next_position)
    curr_position = next_position
    requests.remove(next_position)

print str(result)[1:-1]
print cost
print result[len(result)-1],',',cost