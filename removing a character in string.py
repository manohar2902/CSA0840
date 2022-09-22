
def removeChar(s, c):
    counts = s.count(c)
    s = list(s)
    while counts:
        s.remove(c)
        counts -= 1
    s = ''.join(s)
    print(s)
if __name__ == '__main__':
    s=input("Enter the string: ")
    remove=input("Enter character: ")
    removeChar(s, remove)

