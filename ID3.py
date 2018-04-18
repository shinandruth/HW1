from node import Node
import math, copy

'''
Calculate the Information Gain of a specific attribute
'''
def infoGain(examples, a):
    

'''
Picks the best attribute to split on (i.e., highest information gain)
'''
def chooseAttribute(examples):
    max = -1
    attr = examples[0].keys()
    attr.remove("Class")

    #Calcuate the attr with highest info gain
    best = attr[0]
    for a in attr:
        curr = infoGain(examples, a)
        if curr > max:
            max = curr
            best = a
    return best



'''
Takes in an array of examples, and returns a tree (an instance of Node)
trained on the examples.  Each example is a dictionary of attribute:value pairs,
and the target class variable is a special attribute with the name "Class".
Any missing attributes are denoted with a value of "?"
'''
def ID3(examples, default):
    #print examples
    #Creating the new Node
    root = Node()
    root.dataset = copy.deepcopy(examples)
    #Default Case: Examples is Empty
    if examples == None:
        root.label = default
        return root
    #Calculate num of instances of each key/value combo
    attribute_dict = {}
    example_length = len(examples)
    for i in range(0, example_length):
        for key, value in examples[i].iteritems():
            if key not in attribute_dict:
                attribute_dict[key] = {}
            if value not in attribute_dict[key]:
                attribute_dict[key][value] = 1
            else:
                attribute_dict[key][value] += 1
    #Case 2: Examples all hae same classifcation
    if len(attribute_dict["Class"]) == 1:
        root.label = attribute_dict["Class"].keys()[0]
        return root
    #Case 3: Non-Trivial split is not possible. Find best att to split on
    single_att = True
    for key in attribute_dict:
        if key != "Class" and len(attribute_dict[key]) > 1:
            single_att = False
            break
    if single_att:
        tree.label = max(attribute_dict["Class"].values())
        return root
    best = chooseAttribute(examples)

    print best

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
