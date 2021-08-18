# Manish kushwah 1901CB23
# Tut-1 CS 384

def meraki_helper(n):
    """This will detect meraki numner"""


input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321] 

meraki_count=0 #for counting of total meraki no.
non_meraki_count=0 #for counting of total non- meraki no.

for x in range(len(input)):  # creating the separate string for each element
    Checker=0
    string_create = str(input[x])
    
    for i in range(len(string_create)-1):  # evaluating the no.
        if abs(int(string_create[i]) - int(string_create[i+1])) == 1:
            continue
       
        else:
            Checker=1
            print('No  - ', input[x], 'is not a Meraki number')
            non_meraki_count+=1
    if Checker==0 :
        print('Yes - ', input[x], 'is a Meraki number')
        meraki_count+=1

print('The input list cointains', meraki_count , 'meraki no. and' , non_meraki_count ,'non meraki numbers.')


