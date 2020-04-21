import sys

class Position:

	def __init__(self, transversable, food, ghost):
		self.transversable = transversable
		self.ghost = ghost
		self.food = food

class Maze:

	def __init__(self, num_rows, num_cols):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.grid = [[None for j in range(num_cols)] for i in range(num_rows)]

	def is_allowed(self, position):
		return position[0] >= 0 and position[0] < self.num_rows and position[1] >= 0 and position[1] < self.num_cols and self.grid[position[0]][position[1]].transversable

	def get_int_grid(self, initial_position, goal_position):
		#this method is necessary only for plots
		grid = []
		for i in range(0, self.num_rows):
			row = []
			for j in range(0, self.num_cols):
				if (i, j) == initial_position:
					row.append(0)
				elif (i, j) == goal_position:
					row.append(1)
				elif self.grid[i][j].food:
					row.append(2)
				elif self.grid[i][j].transversable:
					row.append(3)
				elif self.grid[i][j].ghost:
					row.append(4)
				else:
					row.append(5)
				grid.append(row)
		return grid

	def get_final_grid(self, initial_position, goal_position, path):
		#this method is necessary only for plots
		grid = []
		for i in range(0, self.num_rows):
			row = []
			for j in range(0, self.num_cols):
				if (i, j) == initial_position:
					row.append(0)
				elif (i, j) == goal_position:
					row.append(1)
				elif (i, j) in path:
					row.append(2)
				else:
					row.append(3)
				
				grid.append(row)

		return grid


def read_maze(maze_file, num_rows, num_cols):
	maze = Maze(num_rows, num_cols)
	initial_position = goal_position = (-1, -1)

	k = 0
	for i in range(0, maze.num_rows):
		for j in range(0, maze.num_cols):
			pos = maze_file[k]
			
			transversable = True
			food = False
			ghost = False
			
			if pos == '|':
				transversable = False
			elif pos == '.':
				food = True
			elif pos == 'o':
				ghost = True
				transversable = False
			elif pos == 'p':
				initial_position = (i, j)
			elif pos == 'g':
				goal_position = (i, j)
			
			maze.grid[i][j] = Position(transversable, food, ghost)

			k += 1
			
	return maze, initial_position, goal_position

def getMazeTest():
	maze_file = open("maze-test.txt","r").read()
	return read_maze(maze_file, num_rows = 31, num_cols = 29)

