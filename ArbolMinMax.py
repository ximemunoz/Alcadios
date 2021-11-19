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