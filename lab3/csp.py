from functools import reduce
from typing import Generic, TypeVar, Dict, List, Set, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        pass


class ConstraintSatisfactionProblem(Generic[V, D], ABC):
    def __init__(self, variables_and_domains: Dict[V, Set[D]]) -> None:
        self.variables_and_domains: Dict[V, Set[D]] = variables_and_domains # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        self._arc_consistency_variables_and_domains = self.variables_and_domains
        self._arc_queue = [c.variables for c in self.constraints]
        for variable in self.variables_and_domains:
            self.constraints[variable] = []

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables_and_domains:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False

        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)

        if len(assignment) == len(self.variables_and_domains):
            return assignment
        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables_and_domains if v not in assignment]
        # get the every possible domain value of the first unassigned variable

        first: V = unassigned[0]
        for value in self.variables_and_domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # if we're still consistent, we recurse (continue)

            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking

                if result is not None:
                    return result
        return None

    def _remove_from_domain(self, var_1, var_2):
        removed = False
        to_remove = []
        for x in self._arc_consistency_variables_and_domains[var_1]:
            diff = False
            for y in self._arc_consistency_variables_and_domains[var_2]:
                if x != y:
                    diff = True
            if not diff:
                to_remove.append(x)
                removed = True
        for x in to_remove:
            self._arc_consistency_variables_and_domains[var_1].remove(x)
        return removed

    def arc_consistency(self):
        self._arc_consistency_variables_and_domains = self.variables_and_domains
        self._arc_queue = reduce(lambda aa, bb: aa + bb, [[c.variables for c in l] for l in self.constraints.values()])

        while len(self._arc_queue) > 0:
            rule = self._arc_queue.pop()
            values = {v: self._arc_consistency_variables_and_domains[v] for v in rule}

            for var_1 in values:
                for var_2 in values:
                    if var_1 != var_2:
                        if all([len(val) == 1 for val in self._arc_consistency_variables_and_domains.values()]):
                            return self._arc_consistency_variables_and_domains
                        if any([len(val) == 0 for val in self._arc_consistency_variables_and_domains.values()]):
                            return None

                        if self._remove_from_domain(var_1, var_2):
                            for c in self.constraints[var_1]:
                                self._arc_queue.append(c.variables)
