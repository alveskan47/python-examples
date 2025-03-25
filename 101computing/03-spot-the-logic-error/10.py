def printGrid(grid):
   print(" |---+---+---|")
   line = ""
   for i in range(0,3):
      line = ""
      for j in range(0,3):
         line = line + " | " + tictactoe[i][j]
      print(line + " |")
      print(" |---+---+---|")
tictactoe = [["X","O","X"],["O","X","O"],["X","X","O"]]
printGrid(tictactoe)