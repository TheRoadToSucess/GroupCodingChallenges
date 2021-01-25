# Given two integers x, and y return the number of positions
# where their values differ in their binary representations as a 32-bit integer.

# wanna alternate languages on the next questtion
# which lang?
# javascript
# im not that familiar with it , but we can do it in javascript k

# lets do this in python we can also alternate leads and try different approaches should be good practice in terms switching between languages


# oki do u understand this question tho?nvm jot got it, had to read the example
# do you understand what they mean by indices in this case I know in genearl
# it would be a index in arry
# yeah so the total of how many indexes are not the sameoh just got it
#  ok so it proably similar to one the last probleems we did last time where we compare
# values of the index and return the times they dont match also we proably have
#  to find a way to convert the numbers the binary

count = 0
x = 9
y = 5
     # since, the numbers are less than 2^31
     # run the loop from '0' to '31' only
for i in range(0, 32):

        # right shift both the numbers by 'i' and
        # check if the bit at the 0th position is different
    if (((x >> i) & 1) != ((y >> i) & 1)):
        count = count+1
print (count)

# quick question does vscode let you stay in whatever file you want if seems like it is switching
# just wondering what is the value of i