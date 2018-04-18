from node import Node
import math, copy

def H(pi):
    return float(-pi*math.log(pi,2))

'''
Calculates the entropy of example
'''
def entropy(examples):
    cl = {}
    l = len(examples)
    h = 0
    for i in range(0, l):
        if examples[i]["Class"] not in cl:
            cl[examples[i]["Class"]] = 1
        else:
            cl[examples[i]["Class"]] += 1
    for value in cl.values():
        h += H(float(value)/l)
    return h

'''
Calculate the Information Gain of a specific attribute
'''
def infoGain(examples, a):
    unknown = []
    sum = float(0)
    max = -1
    d = {}
    l = len(examples)
    new_gain = entropy(examples)
    for i in range(0, l):
        sum += 1
        if examples[i][a] == "?":
            unknown.append(examples[i])
        if examples[i][a] not in d:
            d[examples[i][a]] == examples[i]
        else:
            d[examples[i][a]].append(examples[i])
    for value in d.values():
        if value > max:
            max = value
    for value in d.values():
        if value == max:
            value += unknown
        new_gain -= (entropy(value)*(len(value)/sum))
    return new_gain

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
    # for i in range(0, len(examples)):
    #     print "MY TESTER: ", examples[i]["Class"]
    # print examples
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
    #Find the highest info gain attribute
    best = chooseAttribute(examples)
    root.label = best
'''
I STILL NEED TO FINISH THIS LAST PART!
'''
    for

    #print best

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
