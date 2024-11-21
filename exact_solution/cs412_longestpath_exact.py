"""
    Name: Patrick Belbin
      Longest Path Exact Solution
"""
import itertools as it

""" Example input:
3 3
a b 3
b c 4
a c 5
as 
vertices edges
v1 v2 w
v1 v2 w
Example output:
9
a c b
as 
length
list of verticies on path
"""

def main():
  lenV = int(input())
  lenE = int(input())
  g = [input().split() for _ in range(lenE)] # list: {{u, v, w}, {u1, u2, uw}}
  graph = dict()
  for e in g: # use set to prevent duplicates
    graph[e[0]] = set()
    graph[e[1]] = set()
  for e in g: # dict: {u : (v, w)}, {u : (v, w)} ...
    graph[e[0]] = ((e[1], e[2]))
    graph[e[1]] = ((e[0], e[2]))



  return


if __name__ == "__main__":
  main()