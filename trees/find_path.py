# find_path.py

# Going through the tree from bottom to top comparing each two
# adjacent elements, finding the greater one and pushing the
# greater element higher on the tree

# I'm sorry in advance for the syntax I chose to use.
# Haven't find a way to access next/previous items in
# the list through python usual functions, so decided 
# to use indices

def read_tree(filename: str) -> list:
    '''
    Reads a tree from file
    '''
    with open(filename, 'rt') as f:
        tree = []

        for line in f:
            tree.append([int(element) for element in line.split(' ')])

    return tree

def tree_greatest_value(tree: list) -> int:
    '''
    Find the value of the greatest-value route in the tree
    '''
    tree.reverse() # Reverse the list
    indices = [] # Contains lists of higher-value integer indices in each tree-line

    # For every line in given tree (tree_index indicates the line in the tree)
    for tree_index in range(0, len(tree)):
        if indices != []:
            for line_index in range(0, len(tree[tree_index])):
                tree[tree_index][line_index] += tree[tree_index - 1][indices[tree_index - 1][line_index]]

        indices.append([])

        # For every integer in line (except the last one; line_index indicates integer in a given line)
        for line_index in range(0, len(tree[tree_index]) - 1):
            # Collect all the indices together
            if tree[tree_index][line_index] >= tree[tree_index][line_index + 1]:
                indices[tree_index].append(line_index)
            else:
                indices[tree_index].append(line_index + 1)

    return tree[len(tree) - 1][0]

# Change file path here
print('And the value is', tree_greatest_value(read_tree('tree2.txt')))
