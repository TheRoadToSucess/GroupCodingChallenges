# Given a string s containing balanced parentheses "(" and ")", split them into the maximum number of balanced groups.
s = "()()(()())"

# anhy idea?
# we might want to add "" to certain parts of the string then split or what ever method at the qoutes to get the perenticies were we want in the array.
# how does that sound 
# i guess im nor sure how to do it tho how do we start it ? do you see my data structure folder 
# the arrays.js? yeah it seem like the potential solution might be in there let me check my other file quick 


# so we would definitely use spilt in this situation or what ever python eqivalent is 
# before that we would have to figur out hotw to add the qoutes to certain parts of the

# unless there is a better approach 
# im looking the question online and o found a solution but idk 
# it makes sense but im still a litle confused how the answer is returned 
# https://
# www.tutorialspoint.com/program-to-find-maximum-number-of-balanced-groups-of-parentheses-in-python

# the solution in this site seems different because it looks like they have more parentheses or there order different
# i tested it and it works on the problem oh wow lol
# this was another solution I can read this better 
counter = 0
paranthes = ""
lst = []
for i in s:
    if i == "(":
        counter += 1
        paranthes += i
    elif i == ")":
        counter -= 1
        paranthes += i
    if counter == 0:
        lst.append(paranthes)
        paranthes = ""
print(lst)
        

# does it run here? and nope weird now it does ran it in terminal
# yeah it works in the room seems like my intial approach was good 
# yeah now its just a matter of coding more with this different syntax to get a better feel
# yeah we need to practice a little more Anyweway  hvae to go now. we s houkld do this tomorrow too k night ill add to github
# goodnight 