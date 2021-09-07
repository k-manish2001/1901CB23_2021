from os import read


#Manish kushwah
#1901CB23

#Task-1 giving output by the subject
def output_by_subject():

    Read = open('regtable_old.csv', 'r') 
    #reading the giving file
    for items in Read:
        i = items.split(',')
        p = open(f"output_by_subject/{i[3]}.csv", "a")
        p.write(f"{i[0]}, ") #writing the rollno

        p.write(f"{i[1]}, ") #writing the register sem

        p.write(f"{i[3]}, ") #writing the schedule sem

        p.write(f"{i[8]}")   #writing the sub type
             
    return          
              

output_by_subject()

#Task-2 giving the output by roll no.
def output_individual_roll():

    p = open('regtable_old.csv', 'r') #reading data from file
    for data in p:
        x = data.split(',')
        y = open(f"output_by_subject/{x[0]}.csv", "a")

        #printing the data
        y.write(f"{x[0]}, ")
        y.write(f"{x[1]}, ")
        y.write(f"{x[3]}, ")
        y.write(f"{x[8]}")
             
    return                 

output_individual_roll()




