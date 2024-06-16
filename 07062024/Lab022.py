#List - Shopping List

#m milk,bread,butter,poha

shopping_list = ["Milk","bread","butter","phoa"]
print(shopping_list)
print(len(shopping_list))
print((shopping_list[0]))
print((shopping_list[-1]))
print(type(shopping_list))

shopping_list.append("Curd") # Append -----> Add iterm in the end
print(shopping_list)

shopping_list.insert(1,"jam")
print(shopping_list)

shopping_list.extend(["chips","salt"])  # Add multiple items in the end
print(shopping_list)

shopping_list.remove("bread")  # remove item
print(shopping_list)

print(shopping_list.pop())
print(shopping_list)

print(shopping_list.index("butter"))
print(shopping_list)

print(shopping_list.reverse())
print(shopping_list)

shopping_list.sort()
print(shopping_list)