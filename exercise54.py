# This is where Exercise 5.4 goes
# Name: Jackie Gushue

def is_triangle(l1, l2, l3):
    """Determines whether or not a triangle can
        be made with three possible side lengths."""
    if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
        print "No"
    else:
        print "Yes"

def user_triangle():
    """User is prompted to input three triangle side
        lengths and whether or not a triangle can be
        formed is determined."""
    len_list = []
    for i in range(3):
        len_list.append(int(raw_input("Enter length " + str(i+1) + " of triangle: ")))
    is_triangle(len_list[0], len_list[1], len_list[2])

user_triangle()