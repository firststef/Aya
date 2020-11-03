from abc import abstractmethod
from typing import Generic, TypeVar, Dict, List, Set, Optional
from csp import ConstraintSatisfactionProblem, Constraint, V, D


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str):
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        if self.place1 not in assignment or self.place2 not in assignment:
            return True

        return assignment[self.place1] != assignment[self.place2]


class MapColoringProblem(ConstraintSatisfactionProblem[str, str]):
    def __init__(self, variables_and_domains: Dict[str, Set[str]]):
        super().__init__(variables_and_domains)
