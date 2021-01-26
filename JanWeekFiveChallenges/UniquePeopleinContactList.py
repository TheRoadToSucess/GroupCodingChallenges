# You are given a two-dimensional list of strings contacts. Each element contacts[i] represents the list of emails for contact i. 
# Contact i is considered a duplicate if there's a j < i such that contact j shares a common email with i. Return the number of 
# unique people in contacts.


contacts = [
    ["elon@tesla.com", "elon@paypal.com"],
    ["elon@tesla.com", "elon@spacex.com"],
    ["tim@apple.com"]
]

seen = set()
ret = 0
for contact_list in contacts:
    ret += all([contact not in seen for contact in contact_list])
    seen |= set(contact_list)
print(ret)