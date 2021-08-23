def get_memory_score(input_nums):  # main function
     a=[] #array-1
     b=[] #array-2
     score=0
     check=False

     # checking the input

     for i in range(len(input_nums)):
          if type(input_nums[i])!= int:
               a.append(input_nums[i])
               check=True
          else:
               continue
     if check:
          print('Please enter a valid input list. Invalid inputs are', a)  
          return
     else: 
          #driving function
          for i in range(len(input_nums)): 
               if input_nums[i] in b:
                    score+=1
               else:
                    if len(b)<5:
                         b.append(input_nums[i])     
                    else:
                         del b[0]
                         b.append(input_nums[i])

     return score   
input_nums = [1, 2, 2, 2, 2, 3, 1, 1, 8, 2] #input 
print('1. Score:', get_memory_score(input_nums))