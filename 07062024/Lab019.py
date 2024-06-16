#string
#inbult functions
#function --- Repeat a task - you can use function
#print() Input() type() format()

#string

name="Vijay" # 0 to 4

# 0,1,2,3,4
# V,i,j,a,y

print(name)
print(type(name))
print(id(name))   # id-----.> Memory address where it is stored 1928424133888
print(len(name))  # Lenght of string . Lenth is always starts with 1

name=name.upper()
print(name)

name=name.lower()
print(name)
a=name.count('v')
print(a)

#python - immutable
name[0]='p' #  'str' object does not support item assignment