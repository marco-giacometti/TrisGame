
class Tris ():
  def __init__(self) -> None:
    self.pO = []
    self.pX = []
    self.available_pos = list(range(9))
    
    self.win_combo = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]  # All the possible win combos
    
  def play_game(self):
    
    print('Game starting...')
    self.print_pos()
    
    while True:
      print('Player X turn... ', end='')
      self.get_move('X')
      
      self.print_pos()
      
      if self.check_win('X'):
        print('Player X WON!!! GODO')
        break
        
      print('Player O turn... ', end='')
      self.get_move('O')
      
      self.print_pos()
      
      if self.check_win('O'):
        print('Player O WON!!! GODO')
        break
        
      
  def get_move(self, player):
    while True:
      pos = input(f'Insert position of {player}:')
      
      try:
        pos = int(pos)
        if pos in self.pX:
          raise ValueError()
        elif pos in self.pO:
          raise ValueError()
        break
      except ValueError:
        print(f'Yo bro ther available positions are: {self.available_pos}...')
        print(f'{pos} is not valid! Try again!')
      
    
    if player == 'X':
      self.pX.append(pos)
    elif player == 'O':
      self.pO.append(pos)
    
    self.available_pos.remove(pos)
    pass
  
  
  def check_win(self, player):
    if player == 'X':
      for a,b,c in self.win_combo:
        if a in self.pX and b in self.pX and c in self.pX:
          return True
      return False
    
    if player == 'O':
      for a,b,c in self.win_combo:
        if a in self.pO and b in self.pO and c in self.pO:
          return True
      return False
    
  def print_pos(self):
    print('|', end='')
    for i in range(9):
      if i == 3 or i == 6:
        print('\n|', end='')
      if i in self.available_pos:
        print(' |', end='')
      elif i in self.pX:
        print('X|', end='')
      elif i in self.pO:
        print('O|', end='')
      else:
        raise RuntimeError('DKN BRO WTF')
    print()
    pass
  
if __name__ == '__main__':
  
  game = Tris()
  
  game.play_game()
  