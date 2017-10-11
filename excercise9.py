# Problem 1
print('Problem 1:')
def arrayCheck(nums):
    if (1 in nums):
        if (2 in nums):
            if (3 in nums):
                return True
    return False

result = arrayCheck([1,2,3])
print(result)

# Problem 2
print('Problem 2:')
def stringBits(mystring):
    print(mystring[::2])

stringBits('hello')

# Problem 3
print('Problem 3:')
def end_other(a,b):
    first = a.lower()
    second = b.lower()
    if (first in second):
        print(True)
    elif (second in first):
        print(True)
    else:
        print(False)

end_other('tux','fgh')
end_other('abc','defabc')


# Problem 4
print('Problem 4:')
def doubleChar(str):
    c = 0
    f = ''
    while (c<len(str)):
        f= f+str[c]+str[c]
        c= c + 1
    print(f)
doubleChar('hey')

# Problem 5
print('Problem 5:')
def fix_teen(n):
  if (n in [13,14]) or (n in [17,18,19,20]):
      n=0
      return n
  else:
      return n

sum = 0
def no_teen_sum(a, b, c):
  A = fix_teen(a)
  B = fix_teen(b)
  C = fix_teen(c)
  sum = A + B + C
  print(sum)

no_teen_sum(1,15,8)

# Problem 6
print('Problem 6:')
mylist = [1,2,3,4,5,6,7,8,10,12,14]
def count_even(m):
    count=0
    for element in m:
        if element%2 == 0:
            count=count+1
    return count

evens = (count_even(mylist))
print(evens)
