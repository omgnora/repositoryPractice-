#algorithm for finding hamiltonain circuts
#recursive <3
#d is an adjacency dictionary already established, path is path

assert len(d) !=0

#base case, found a circut
if len(path) == len(d) and path[0] in d[path[-1]]:
    print(path + [path[0]])
    #return True

#case 1- path is empty. pick a vertix and start w that
if len(path)== 0:
    for v in d:
        #call findpath on a new path
        return findpath(d,path + [v])
    
#otherwise, find a not-already-visited vertex adjacent to end of path    
else:
    end = path[-1]
    for n in d[end]:
        if n not in path:
            if findpath(d,path + [n]):
                return true
            
    return False        