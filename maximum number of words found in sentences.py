test_string1 = "alice and bob love leetcode"
res = len(test_string1.split())
print ("The number of words in string1 : ",res)
test_string2 = "i think so too"
res =len(test_string2.split())
print ("the number of words in string2 :",res)
list=[len(test_string1.split()),len(test_string2.split())]
print( max(list))