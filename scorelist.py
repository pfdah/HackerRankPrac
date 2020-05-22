# Given the names and grades for each student in
#  a Physics class of

# students, store them in a nested list and print t
# he name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the 
# same grade, order their names alphabetically and print 
# each name on a new line.
if __name__ == '__main__':
    lst = []
    sclst = []
    for _ in range(int(input())):
        tlst = []
        name = input()
        score = float(input())
        tlst.append(name)
        tlst.append(score)
        sclst.append(score)
        lst.append(tlst)
    l = sclst.count(min(sclst))
    for i in range(l):
        sclst.remove(min(sclst))
    name = []
    for i in lst:
        if i[1] == min(sclst):
            name.append(i[0])
    name.sort()
    for n in name:
        print(n)
