import os

class Grid:
	def __init__(self, size):
		self.x = size[0]
		self.y = size[1]
	def set_grid(self):
		self.grid = []
		for y in range(self.y):
			self.grid.append([])
			for x in range(self.x):
				self.grid[y].append(0)

	def draw_grid(self):
		clear
		print("#"*(self.x + 2), end="\n")
		for y in range(self.y):
			print("#", end="")
			for x in range(self.x):
				if self.grid[y][x] == 0:
					print(" ", end="")
				elif self.grid[y][x] == 1:
					print("#", end="")
			print("#", end="\n")
		print("#"*(self.x + 2), end="\n")

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

				
g = Grid([100, 20])
g.set_grid()
g.draw_grid()