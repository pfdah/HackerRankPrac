# Let's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by on a 3D grid where the sum of is not equal to . Here,

# Input Format

# Four integers
# and

# each on four separate lines, respectively.

# Constraints

# Print the list in lexicographic increasing order.


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
    lst_fil = []
    for i in lst:
        if sum(i) != n:
            lst_fil.append(i)
    

    print(lst_fil)
