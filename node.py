# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - a list of 2 nodes if numeric, and a dictionary (key=attribute value, value=node) if nominal.
#            For numeric, the 0 index holds examples < the splitting_value, the
#            index holds examples >= the splitting value
#
# label - is the output label (0 or 1 for
#	the homework data set) if there are no other attributes
#       to split on or the data is homogenous
#	if there is a decision attribute, your implementation can choose set label to None
#	or to the class mode of the examples
#
# decision_attribute - the index of the decision attribute being split on
#
# is_nominal - is the decision attribute nominal
#
# value - Ignore (not used, output class if any goes in label)
#
# splitting_value - if numeric, where to split
#
# name - name of the attribute being split on
class Node:
  def __init__(self):
    self.children = {}
    self.label = None
    self.examples = []
    self.pruned = False
    self.value = -1000

	# you may want to add additional fields here...
