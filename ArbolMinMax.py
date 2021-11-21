from sys import maxsize
class Node(object):
  def __init__ (self,i_depth, i_playerNum, i_beansRemain, i_value = 0):
    self.i_depth = i_depth #Con cada iteración la profundidad disminuye
    self.i_playerNum = i_playerNum # Valor + o -
    self.i_beansRemain = i_beansRemain #Beans restantes después de la elección
    self.i_value = i_value #Valor del nodo, gamesate, +infinito, 0, o -infinito 
    self.children = [] #Lista de nodos hijos
    self.CreateChildren() #Función que crea los hijos

  def CreateChildren(self):
    if self.i_depth >= 0: #Checamos si hemos pasado la profundidad 0
      for i in range (1,3): #Vamos a elegr entre 1-3 beans
        v = self.i_beansRemaining = i #Guarda el valor de cuantos beans quedan
        self.children.append( Node( self.i_depth - 1, -self.i_playerNum, v, self.RealVal(v))) #Se crea y agrega el nodo a la lista de hijos
  
  def RealVal (self, value): #Detecta quién va ganando (jugador positivo o jugador negativo)
    if (value==0): 
      return maxsize * self.i_playerNum
    elif (value < 0):
      return maxsize * -self.i_playerNum
    return 0

#ALGORITMO MIN MAX
def MinMax(node, i_depth, i_playerNum):
    if (i_depth == 0) or (abs(node.i_value) == maxsize): #Checamos si alcanzamos la profundidad 0 o si nos encontramos en una condicion de gana-pierde
        return node.i_value #Pasamos la mejor opción al padre.
    i_bestValue = maxsize * -i_playerNum

    for child in node.children:
        i_val = MinMax(child, i_depth-1, -i_playerNum)
        if (abs(maxsize*i_playerNum-i_val)<abs(maxsize*i_playerNum - i_bestValue)):
            i_bestValue = i_val
    return i_bestValue
    
def WinCheck(i_beans, i_playerNum):
  if i_beans < 0:
    print("*"*30)
    if i_playerNum > 0:
      if i_beans == 0:
        print("\tYou WIN!!!")
      else:
        print("\tToo many, you lose")
    else:
      if i_beans == 0:
        print("\tComputer wins, better luck next time")
      else:
        print("\tComp Error!")
    print("*"*30)
    return 0
  return 1

if __name__ == '__main__':
  i_beansTotal = 11
  i_depth = 4
  i_curPlayer = 1
  print("INSTRUCCIONES: Si eres el último en tomar frijoles cuando se acaben pierdes. Cada ronda deberás tomar entre 1-3 frijoles")
  while (i_beansTotal>0):
    print("\n%d Frijoles restantes. ¿Cuántos frijoles desea tomar?" %i_beansTotal)
    i_choice = input("\n1, 2 or 3:")
    i_beansTotal -= int(float(i_choice))
    if WinCheck(i_beansTotal,i_curPlayer):
      i_curPlayer *= -1 
      node = Node(i_depth,i_curPlayer, i_beansTotal)
      bestChoice = -100
      i_bestValue = i_curPlayer * maxsize
      #DETERMINAR EL NÚMERO DE FRIJOLES A QUITAR
      for i in range(len(node.children)):
        n_child = node.children[i]
        i_val = MinMax(n_child, i_depth,  -i_curPlayer)
        if(abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer*maxsize - i_bestValue)):
          i_bestValue = i_val
          bestChoice = i
      bestChoice +=1
      print("Comp chooses:" + str(bestChoice) + "\tBased on value: " + str(i_bestValue))
      i_beansTotal -= bestChoice
      WinCheck(i_beansTotal, i_curPlayer)
      i_curPlayer *= -1