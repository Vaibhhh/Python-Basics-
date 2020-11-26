friends = ["Kevin","Karen","Jim","Oscar","Toby","Jim","Jim"]
print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:])
friends[2] = "Mike"

#List Functions

lucky_numbers = [4,8,15,16,23,42]
friends.append("Creed")
friends.insert(1,"Kelly")
friends.remove("Toby")
friends.extend(lucky_numbers)
friends.pop()
print(friends)
print(friends.index("Oscar"))
print(friends.count("Jim"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
