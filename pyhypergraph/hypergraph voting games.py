#define class as hypergraph it defines what data an object has and what actions it can perform
>>> class Hypergraph:
  #constructor set up object internal data ,give it an initial valid statement
...     def __init__(self, vertices=None):
  #creates an empty set to store vertices in that case voters
...         self.vertices = set()
#check if user passed initial vertices
...         if vertices is not None:
#ensure that only voters exist and input order does not matter
...             for v in vertices:
...                 self.vertices.add(v)
#creates an empty list to store hyperedgess
...         self.hyperedges = []
#add single voter to the hypergraph
... 
...     def add_vertex(self, v):
...         self.vertices.add(v)
defines method to add a coalition
... 
...     def add_hyperedge(self, edge):
  #create a new empty set to store the hyperedge
...         edge_set = set()
#add every vert fro edges into set
...         for v in edge:
...             edge_set.add(v)
#ensure all vertice in the coalition already exist in th ehypergraph and prevent illegal coalition
... 
...         if not edge_set.issubset(self.vertices):
...             raise ValueError("Hyperedge contains unknown vertices")
#only add non empty hyperedges an dapped coalition to the list of hyperedges
... 
...         if edge_set:
...             self.hyperedges.append(edge_set)
generates every possible coalition of voters
... 
...     def all_coalitions(self):
  #convert the set of the vertice into a list
...         vertices_list = []
...         for v in self.vertices:
...             vertices_list.append(v)
#store all coalition
... 
...         coalitions = []
# numbers of voters
...         n = len(vertices_list)
#mask start at 1 to exclude empty coalion, mask tell which elemet to keep and ignore
... 
...         mask = 1
#loop over all binary number from1 to 2**n-1
...         while mask < (2 ** n):
  #create a empty coalition and a index counter
...             coalition = set()
...             i = 0
#decode binary mask check if i egale 1 and if yes include that voter
...             while i < n:
...                 if (mask >> i) & 1:
#add the coalition to the list and moves to the next mask
...                     coalition.add(vertices_list[i])
                i += 1
            coalitions.append(coalition)
            mask += 1

        return coalitions
#define voting ruke

class VotingRule:
  #force subclasses to define their own winning logic
    def is_winning(self, coalition, game):
        raise NotImplementedError

#coalition wins if as at lest quota member
class QuotaRule(VotingRule):
  store the quota
    def __init__(self, quota):
        self.quota = quota
      #check if coalition sixe meet the quota

    def is_winning(self, coalition, game):
        return len(coalition) >= self.quota

#weigthed voting system
class WeightedQuotaRule(VotingRule):
    def __init__(self, weights, quota):
        self.weights = weights
        self.quota = quota
#initializes the total weight
    def is_winning(self, coalition, game):
        total = 0
        for v in coalition:
            total += self.weights[v]
          #coalition wins if total weight meet quota
        return total >= self.quota

#combines hypergraph and voring rule represente the full voting game
class VotingGame:
  #stores both cmponent
    def __init__(self, hypergraph, rule):
        self.hypergraph = hypergraph
        self.rule = rule
#create an empty list for winning coalition
    def winning_coalitions(self):
        winners = []
      #itirates through all coalition
        for coalition in self.hypergraph.all_coalitions():
          #keep only those that satisfy the voting rule
            if self.rule.is_winning(coalition, self):
                winners.append(coalition)
        return winners
#check if coalition is minimal winning
    def is_minimal_winning(self, coalition):
    
        if not self.rule.is_winning(coalition, self):
            return False
#removes one voter at a tinme
        for v in coalition:
            reduced = set(coalition)
            reduced.remove(v)
          #if remains win is not minimal
            if self.rule.is_winning(reduced, self):
                return False

        return True

#utility class for power measurement
class PowerIndex:
  #define banzhaf power inder
    @staticmethod
    def banzhaf(game):
      #dictionary to sotre power values
        power = {}
      #initialize power score of each voter to zero
        for v in game.hypergraph.vertices:
            power[v] = 0
#check every coalition
        for coalition in game.hypergraph.all_coalitions():
          #only winning coalition matter
            if game.rule.is_winning(coalition, game):
              #test if voter v is critival
                for v in coalition:
                    reduced = set(coalition)
                    reduced.remove(v)
                  #if removing v turn wining into losing v pivotal increase banzhaf score
                    if not game.rule.is_winning(reduced, game):
                        power[v] += 1

        return power
    



