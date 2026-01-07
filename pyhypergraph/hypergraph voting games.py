
>>> class Hypergraph:
...     def __init__(self, vertices=None):
...         self.vertices = set()
...         if vertices is not None:
...             for v in vertices:
...                 self.vertices.add(v)
...         self.hyperedges = []
... 
...     def add_vertex(self, v):
...         self.vertices.add(v)
... 
...     def add_hyperedge(self, edge):
...         edge_set = set()
...         for v in edge:
...             edge_set.add(v)
... 
...         if not edge_set.issubset(self.vertices):
...             raise ValueError("Hyperedge contains unknown vertices")
... 
...         if edge_set:
...             self.hyperedges.append(edge_set)
... 
...     def all_coalitions(self):
...         vertices_list = []
...         for v in self.vertices:
...             vertices_list.append(v)
... 
...         coalitions = []
...         n = len(vertices_list)
... 
...         mask = 1
...         while mask < (2 ** n):
...             coalition = set()
...             i = 0
...             while i < n:
...                 if (mask >> i) & 1:
...                     coalition.add(vertices_list[i])
                i += 1
            coalitions.append(coalition)
            mask += 1

        return coalitions

class VotingRule:
    def is_winning(self, coalition, game):
        raise NotImplementedError


class QuotaRule(VotingRule):
    def __init__(self, quota):
        self.quota = quota

    def is_winning(self, coalition, game):
        return len(coalition) >= self.quota


class WeightedQuotaRule(VotingRule):
    def __init__(self, weights, quota):
        self.weights = weights
        self.quota = quota

    def is_winning(self, coalition, game):
        total = 0
        for v in coalition:
            total += self.weights[v]
        return total >= self.quota


class VotingGame:
    def __init__(self, hypergraph, rule):
        self.hypergraph = hypergraph
        self.rule = rule

    def winning_coalitions(self):
        winners = []
        for coalition in self.hypergraph.all_coalitions():
            if self.rule.is_winning(coalition, self):
                winners.append(coalition)
        return winners

    def is_minimal_winning(self, coalition):
        if not self.rule.is_winning(coalition, self):
            return False

        for v in coalition:
            reduced = set(coalition)
            reduced.remove(v)
            if self.rule.is_winning(reduced, self):
                return False

        return True


class PowerIndex:
    @staticmethod
    def banzhaf(game):
        power = {}
        for v in game.hypergraph.vertices:
            power[v] = 0

        for coalition in game.hypergraph.all_coalitions():
            if game.rule.is_winning(coalition, game):
                for v in coalition:
                    reduced = set(coalition)
                    reduced.remove(v)
                    if not game.rule.is_winning(reduced, game):
                        power[v] += 1

        return power
    


