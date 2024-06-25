from maze import *


class CreateMaze:
    def __init__(self, size, maze_file_name, solution_file_name, scale=30):
        self.size = size
        self.file_name = maze_file_name
        self.solution_name = solution_file_name
        self.scale = scale

    def make_maze(self):
        mazeing = Maze()
        mazeing.create(self.size, self.size, Maze.Create.BACKTRACKING)
        mazeing.solve((0, 0), (self.size - 1, self.size - 1), Maze.Solve.DEPTH)
        mazeing.save_maze(file_name=f"maze_qus/{str(self.file_name)}.png", scale=self.scale)
        mazeing.save_solution(file_name=f"maze_ans/{str(self.solution_name)}.png", scale=self.scale)


def make_this_many_mazes(how_many, size=25):
    for i in range(how_many):
        new_maze = CreateMaze(size, f"maze{i+1}", f"solution{i+1}")
        new_maze.make_maze()
        print(f"Done Making {i + 1}")


if __name__ == '__main__':
    make_this_many_mazes(1)

