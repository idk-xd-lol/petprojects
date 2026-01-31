import os
import time

#main class
class Grid:
	def __init__(self, size):
		"""initializatin"""
		self.x = size[0]
		self.y = size[1]
		self.active_cells = []

	def set_grid(self):
		"""creating grid"""
		self.grid = []
		for y in range(self.y):
			self.grid.append([])
			for x in range(self.x):
				self.grid[y].append(0)

	def draw_grid(self):
		"""drawing grid"""
		clear()
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

	def add_cell(self, position):
		"""adding cell"""
		cell_x = position[0]
		cell_y = position[1]
		self.grid[cell_y][cell_x] = 1
		self.active_cells.append(position)

	def delete_cell(self, position):
		"""removing cell"""
		cell_x = position[0]
		cell_y = position[1]
		self.grid[cell_y][cell_x] = 0
		self.active_cells.remove(position)
	def update(self):
		self.check_cells = []
		self.cells_to_delete = []
		self.cells_to_add = []
		for i in self.active_cells:
			neighbours = []
			for x in range (-1, 2):
				for y in range(-1, 2):
					neighbours.append([i[0]+x, i[1]+y])
			neighbours.remove(i)
			neighbours_active = 0
			for n in neighbours:
				n_x = n[0]
				n_y = n[1]
				if self.grid[n_y][n_x]:
					neighbours_active += 1
				self.check_cells.append(n)
			if not neighbours_active in [2, 3]:
				self.cells_to_delete.append(i)

		for i in self.check_cells:
			neighbours = []
			for x in range (-1, 2):
				for y in range(-1, 2):
					neighbours.append([i[0]+x, i[1]+y])
			neighbours.remove(i)
			neighbours_active = 0
			for n in neighbours:
				n_x = n[0]
				n_y = n[1]
				if self.grid[n_y][n_x]:
					neighbours_active += 1
			if neighbours_active == 3:
				self.cells_to_add.append(i)
		for i in self.cells_to_delete:
			self.delete_cell(i)
		for i in self.cells_to_add:
			self.add_cell(i)


def clear(): #clear screen
    os.system('cls' if os.name=='nt' else 'clear')

				
g = Grid([100, 30])
g.set_grid()
g.add_cell([50, 15])
g.add_cell([51, 16])
g.add_cell([52, 14])
g.add_cell([52, 15])
g.add_cell([52, 16])


while True:
	g.draw_grid()
	g.update()