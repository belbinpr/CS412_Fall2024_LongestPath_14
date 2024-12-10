from itertools import permutations

def longest_path(adj, vertNums):

    dist = 0
    path = []
    vertices = list(range(len(adj)))

    # creates and checks every permutation of verticies, and 
    for perm in permutations(vertices):
        currDist = 0
        isPath = True

        for i in range(len(perm) - 1):
            u, v = perm[i], perm[i + 1]
            edge = None
            # goes through verticies connected to u, and checks if it
            # connects to the next vertex in the perm
            for other, weight in adj[u]:
               if other == v:
                  edge = weight
                  break
            # if valid path, add the edge weight to it
            if edge is not None:
                currDist += edge
            else:
                isPath = False
                break
        # if the path is bigger make it the return path
        if isPath and currDist > dist:
            dist = currDist
            path = perm

    return dist, path

def main():
  lenV, lenE = input().split()
  lenV, lenE = int(lenV), int(lenE)
  g = [input().split() for _ in range(lenE)]

  # convert vertices to vertex index
  vertNums = dict()
  adj = {i: [] for i in range(lenV)} #edges
  i = 0
  for v in g:
    if v[0] not in vertNums:
      vertNums[v[0]] = i
      i += 1
    if v[1] not in vertNums:
      vertNums[v[1]] = i
      i += 1
  for v in g:
    adj[vertNums[v[0]]].append((vertNums[v[1]], int(v[2])))
    adj[vertNums[v[1]]].append((vertNums[v[0]], int(v[2])))

  dist, path = longest_path(adj, vertNums)

  # get the names back
  vertNames = {v: k for k, v in vertNums.items()}
  path = [vertNames[v] for v in path]

  print(dist)
  print(" ".join(path))
  return dist, path


if __name__ == "__main__":
    main()
