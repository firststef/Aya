import sys

import numpy
import numpy as np
import os
import time


def get_maze(x, y):
    return np.random.choice(2, size=(x, y), p=[0.6, 0.4])
    return [[1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]


class Maze:
    def __init__(self, x, y):
        self.maze = get_maze(x, y)
        self.x = x
        self.y = y
        self.initial_state = None
        self.final_state = None
        for i in range(x):
            for j in range(y):
                if self.maze[i][j] == 0:
                    self.initial_state = (i, j)
                    break
        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                if self.maze[i][j] == 0:
                    self.final_state = (i, j)
                    break
            if self.final_state is not None:
                break

    def is_final(self, state):
        return state == self.final_state

    def get_initial(self):
        return self.initial_state


class MazeSolver:
    def __init__(self, problem, a_solver):
        self.problem = problem
        self.solver = a_solver
        a_solver.set_problem(self.problem)

    def transition(self, state, transition):
        self.problem.maze[state] = 0
        self.problem.maze[transition] = 2
        return transition

    @staticmethod
    def transition_to_st(state, transition):
        for k, v in zip(['N', 'S', 'E', 'V'], [(0, -1), (0, 1), (-1, 0), (1, 0)]):
            if transition == k:
                return state[0] + v[0], state[1] + v[1]
        raise TypeError

    def validate(self, transition):
        try:
            return 0 <= transition[0] <= self.problem.x and 0 <= transition[1] <= self.problem.y and self.problem.maze[transition] == 0
        except:
            return False

    def strategy(self, state):
        self.problem.maze[self.problem.get_initial()] = 2
        print(self.problem.maze)
        while not self.problem.is_final(self):
            # with open('maze.txt', 'w+') as f:
            #     f.write(str(self.problem.maze))
            os.system('CLS')
            print(self.problem.maze)
            transition = self.solver.choose_next(state)
            if self.validate(transition):
                print("transition: " + str(state) + "->" + str(transition))
                state = self.transition(state, transition)
                time.sleep(1)


class NoOptionException(BaseException):
    pass


class RandomSolver:
    def __init__(self):
        self.direction = 0
        pass

    def set_problem(self, problem: Maze):
        pass

    def choose_next(self, state):
        self.direction = (self.direction + 1) % 4
        return ['N', 'S', 'E', 'V'][self.direction]


class BacktrackingSolver:
    def __init__(self):
        self.maze = None
        self.stack = []
        pass

    def set_problem(self, problem: Maze):
        self.maze = problem.maze.copy()

    def choose_next(self, state):
        if len(self.stack) > 0 and self.stack[-1][0] == state:
            if len(self.stack[-1][1]) == 0:
                self.stack.pop()
                if len(self.stack) > 0:
                    return self.stack[-1][1].pop()
                else:
                    raise NoOptionException
            else:
                return self.stack[-1][1].pop()
        elif self.maze[state] == 0:
            self.stack.append((state, [(state[0] + 1, state[1]), (state[0], state[1] - 1), (state[0] - 1, state[1]), (state[0], state[1] + 1)]))
            self.maze[state] = 3
            return self.stack[-1][1].pop()

        raise NoOptionException


class BFSSolver:
    def __init__(self):
        self.maze = None
        self.stack = []
        pass

    def set_problem(self, problem: Maze):
        self.maze = problem.maze.copy()

    def choose_next(self, state):
        if self.maze[state] == 0:
            self.stack += [(state[0] + 1, state[1]), (state[0], state[1] - 1), (state[0] - 1, state[1]), (state[0], state[1] + 1)]
            self.maze[state] = 3
            return self.stack.pop(0)
        else:
            if len(self.stack) > 0:
                st = self.stack.pop()
                return st
            else:
                raise NoOptionException


class HillClimbingSolver:
    def __init__(self):
        self.maze = None
        self.dist = 100000
        self.final = None
        pass

    def set_problem(self, problem: Maze):
        self.maze = problem.maze.copy()
        self.final = problem.final_state

    def choose_next(self, state):
        aaa = [(state[0] + 1, state[1]), (state[0], state[1] - 1), (state[0] - 1, state[1]), (state[0], state[1] + 1)]
        dist = [(i, numpy.linalg.norm((x[0] - self.final[0], x[1] - self.final[1]))) for i, x in enumerate([(state[0] + 1, state[1]), (state[0], state[1] - 1), (state[0] - 1, state[1]), (state[0], state[1] + 1)])]
        choose = None
        for i, d in dist:
            if d < self.dist:
                choose = i
                self.dist = d
        if choose is None:
            raise NoOptionException
        else:
            return aaa[choose]


if __name__ == "__main__":
    try:
        solver = MazeSolver(Maze(30, 30), BFSSolver())
        solver.strategy(solver.problem.get_initial())
    except NoOptionException:
        print('No option left')
