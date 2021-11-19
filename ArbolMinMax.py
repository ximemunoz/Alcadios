from sys import maxsize
class Node(object):
  def __init__ (self,i_depth, i_playerNum, i_beansRemain, i_value = 0):
    self.i_depth = i_depth
    self.i_playerNum = i_playerNum
    self.i_beansRemain = i_beansRemain
    self.i_value = i_value
    self.children = []
    self.CreateChildren()

    def CreateChildren(self):
      if self.i_depth >= 0:
        for i in range (1,4):
          v = self.i_stickRemaining = i
          self.children.append( Node( self.i_depth - 1, -self.i_playerNum, v, self.RealVal(v)))
    
    def RealVal (self, value):
      if (value==0):
        return maxsize * self.i_playerNum
      elif (value < 0):
        return maxsize * -self.i_playerNum
      return 0

def MinMax(node, i_depth, i_playerNum):
    if (i_depth == 0) or (abs(node.i_value) == maxsize):
        return node.i_value
    i_bestValue = maxsize * -i_playerNum

    for i in range(len(node.children)):
        child = node.children[i]
        i_val = MinMax(child, i_depth-1, -i_playerNum)
        if (abs(maxsize*i_playerNum-i_val)<abs(maxsize*i_playerNum - i_bestValue)):
            i_bestValue = i_val
    return i_bestValue

def WinCheck(i_beans, i_playerNum):
    
