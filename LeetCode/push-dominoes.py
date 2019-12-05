def pushDom(dominoes):
    N = len(dominoes)
    # zero list with the size of N 
    force = [0] * N
    f = 0 
    for i in range(N):
        if dominoes[i] == 'R':
            f = N
        elif dominoes[i] == 'L':
            f = 0
        force += f
    
    for i in range(N-1, -1, -1):
        if dominoes[i] == 'L':
          f = N
        elif dominoes[i] == 'R':
          f = 0
        force -= f 
        
    for i in range(N):
      if force[i] == 0:
        force[i] = '.'
      elif force[i] > 0:
        force[i] = 'R'
      else:
        force[i] = 'L'
    return "".join(force)