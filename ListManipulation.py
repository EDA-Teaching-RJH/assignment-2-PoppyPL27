### Part Three -- your code goes here. 
##base list
List = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

##sort in ascending order
List.sort()

##Removes all occurrences of the number 1
ListNoOnes = []
for r in List:
    if (List[r]!=1):
        ListNoOnes.append(r)
List = ListNoOnes

##add the numbers 7 and 8 to the end of the list
extension = [7,8]
List.extend(extension)

print(str(List))
