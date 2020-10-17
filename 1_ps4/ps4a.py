# Problem Set 4A
# Name: Gyalpo
# Collaborators: 
# Time Spent: 5:30
# Late Days Used: 0

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
treeA = [[14,19],[[3,5],0]]
treeB = [[9,3],6] # TODO: change this assignment
treeC = [[7],[16,4,2],[8]] # TODO: change this assignment


# Part A1: Multiplication on tree leaves

def add_tree(tree):
    """
    Recursively computes the sum of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the sum of all the leaves of the tree.

    """

    # TODO: Your code here
    if type(tree) == list:
        if len(tree) == 0:
            return 0
        else:
            sum_tree = 0
            for i in tree:
                sum_tree += add_tree(i)
                #use of recursion to add until it gets to a leaf
            return sum_tree
    elif type(tree) == int:
        #if we are in a leaf then the value of it will be returned
        return tree

# Part A2: Arbitrary operations on tree leaves

def sumem(a, b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b


def prod(a, b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b


def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """

    # TODO: Your code here
    if type(tree) == list:
        if len(tree) == 0:
            return base_case
        else:
            result = base_case
            for i in tree:
                result = op(result,op_tree(i,op,base_case))
                #use of recursion for the operator
            return result
    elif type(tree) == int:
        return tree
    
# Part A3: Searching a tree

def search_greater_ten(a, b):
    """
    Operator function that searches for greater-than-10 values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or > 10, and False otherwise
    """
    if type(a) == type(b):
        #in case both a and b are the same type
        if (a or b) > 10:
            return True
        elif (a or b) == True:
            return True
        else:
            return False
    else:
        #in case a and b aren't the same type either a is a bool and b and int
        #or viceversa
        if a == True or b > 10:
            return True
        elif a > 10 or b == True:
            return True
        else:
            return False           

# Part A4: Find the maximum element of a tree using op_tree and max() in the
# main function below (remembering to pass the function in without parenthesis)
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below.
    max_A = op_tree(treeA,max,0)
    #returns 19 which is the expected result for tree A
    print(max_A)
