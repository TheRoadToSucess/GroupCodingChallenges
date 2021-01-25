# Give a list of numbers nums, 
# return the number of elements that 
# are in the correct indices, if the list were to be sorted.
# something like this 

nums = [1, 7, 3, 4, 10]
sorted_list = sorted(nums)
count = 0
for i in range(len(nums)):
    if sorted_list[i] == nums[i]:
        count +=1
print( count)

# why is there a error in the return 
# if we do it here we need to use print not return bv its not a funcion ok is see wanna try another one
# yeah alan is also in the room as well 

# also you should checkout this extension is vscode tabnine
# https://www.tabnine.com 
# what is it about? is it the autocomple ?

# Tabnine is a powerful Artificial Intelligence assistant designed to help you code faster, reduce mistakes, and discover best coding practices - without ever leaving the comfort of VSCode.​

# Tabnine studies publicly shared code and use A.I deep learning algorithms that provide us with the ability to predict your next coding needs and suggest one-click code completion.​
#  i added it. btw we should be done with this prob 
#
# the semi colon is ternary operator right or is it some thing else
# so we add that when we do the for loop or function i think it needs to end with : 
# so in java it similar to {} oh ok

# so return the index of the
# no i think to return how many numbers are in the correct order after we sort the list so the
#  ans is 2 bc 3 and 4 are correct


# so we should sort the array then redeclare the array in its original order and compare the indexes againts each other
# to see how many match

# so this sorts the list, should we have a count? and then save whtv is in the correct position yeah that sounds about right also 1 and 10 are proably what match
