#libraries
import random
#map
m = [['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*']]
aim = [['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*']]
am = [['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*']]
aiam = [['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*'],['*','*','*','*','*','*','*','*','*','*']]

#ships
ships = ['==','===','===','====','====','=====']

aiships = ['==','===','===','====','====','=====']


#variables
sx = 0
sy = 0
sd = ''
sfc = False
t = 0
cc = ''
direction = ['N','S','W','E']
coinflip = [['h','Heads'],['t','Tails']]
ec = 0
ax = 0
ay = 0
aiax = 0
aiay = 0
nax = 0
nay = 0

#last hit? last coordinates?  target hit? last direction? found direction? next move?
hi = [[0,[0,0],0,'N',0,0]]

#rules
print('(*) means not occupied, (!) means failed attack, (=) means occupied by ship, (X) means occupied by a destroyed ship.')
print('')

#ships placing
#player
while ships != []:
  sfc = False
  
  #print defense map
  print('Defense map:')
  print(' ',end=' ')
  for z in range(0,10):
    print(z,end='')
  print('')
  for z in range(len(m)):
    print(z,end=' ')
    for y in m[z]:
      print(y,end='')
    print('')

  #print ships
  for x in range(0,len(ships)):
    print('('+str(x)+')',end='')
    print(ships[x],end=' ')
  print('')

  #placing ship
  print('What ship do you wish to place?')
  si = int(input('ship: '))
  if si == 10:
    break
  try:
    print(ships[si])
  except IndexError:
    print('This ship does not exist pls chose again.')
    continue
  except ValueError:
    print('This ship does not exist pls chose again.')
    continue
  print('How do you want to put your ship?')
  print('Coordinates:')
  sx = int(input('x: '))
  sy = int(input('y: '))
  
  #input check
  if sx > 9 or sx < 0 or sy > 4 or sy < 0:
      print('There is no such coordiates')
  sd = input('direction(N,S,E,W): ')
  if sd != 'N' and sd != 'S' and sd != 'W' and sd != 'E':
    print('There has been an error, please try again.')
    continue
  if sx > 9 or sy > 4:
    print('There has been an error, please try again.')
    continue

  #ship fit check
  for z in range(len(ships[si])):
    #north
    if sd == 'N':
      if len(ships[si]) > sy+1 or m[sy-z][sx] == '=':
        print('The ships does not fit, please try again.')
        sfc = True
        break
    #south
    if sd == 'S':
      if len(ships[si]) > len(m)-sy or m[sy+z][sx] == '=':
        print('The ships does not fit, please try again.')
        sfc = True
        break
    #west
    if sd == 'W':
      if len(ships[si]) > sx+1 or m[sy][sx-z] == '=':
        print('The ships does not fit, please try again.')
        sfc = True
        break
    #east
    if sd == 'E':
      if len(ships[si]) > len(m[sy])-sx or m[sy][sx+z] == '=':
        print('The ships does not fit, please try again.')
        sfc = True
        break
  if sfc:
    continue
  
  #map update
  for z in range(0, len(ships[si])):
    if sd == 'N':
      m[sy-z][sx] = '='
    if sd == 'S':
      m[sy+z][sx] = '='
    if sd == 'W':
      m[sy][sx-z] = '='
    if sd == 'E':
      m[sy][sx+z] = '='
    else:
      m[sy][sx] = '='
  ships.remove(ships[si])
  print('')

#print defense map
print('Defense map:')
print(' ',end=' ')
for z in range(0,10):
    print(z,end='')
print('')
for z in range(len(m)):
    print(z,end=' ')
    for y in m[z]:
        print(y,end='')
    print('')
print('')

#com
while aiships != []:
  sfc = False
  #print map
  #for z in aim:
    #for y in z:
      #print(y,end='')
    #print('')

  #print ships
  #for x in range(0,len(aiships)):
    #print('('+str(x)+')',end='')
    #print(aiships[x],end=' ')
  #print('')

  #placing ship
  #print('What ship do you wish to place?')
  si = random.randint(0,len(aiships)-1)
  #print('How do you want to put your ship?')
  sx = random.randint(0,9)
  sy = random.randint(0,4)
  sd = direction[random.randint(0,3)]

  #ship fit check
  for z in range(len(aiships[si])):
    #north
    if sd == 'N':
      if len(aiships[si]) > sy+1 or aim[sy-z][sx] == '=':
        #print('The ships does not fit, please try again.')
        sfc = True
        break
    #south
    if sd == 'S':
      if len(aiships[si]) > len(aim)-sy or aim[sy+z][sx] == '=':
        #print('The ships does not fit, please try again.')
        sfc = True
        break
    #west
    if sd == 'W':
      if len(aiships[si]) > sx+1 or aim[sy][sx-z] == '=':
        #print('The ships does not fit, please try again.')
        sfc = True
        break
    #east
    if sd == 'E':
      if len(aiships[si]) > len(aim[sy])-sx or aim[sy][sx+z] == '=':
        #print('The ships does not fit, please try again.')
        sfc = True
        break
  if sfc:
    continue
  
  #map update
  for z in range(0, len(aiships[si])):
    if sd == 'N':
      aim[sy-z][sx] = '='
    if sd == 'S':
      aim[sy+z][sx] = '='
    if sd == 'W':
      aim[sy][sx-z] = '='
    if sd == 'E':
      aim[sy][sx+z] = '='
  aiships.remove(aiships[si])
  #print('')

#print map
#for z in aim:
  #for y in z:
    #print(y,end='')
  #print('')
#print('')

#desicion who goes first
while 1:
  print('Now a coin flip to see who goes first...')
  cc = input('Call heads(h) or tails(t): ')
  cf = coinflip[random.randint(0,1)]
  if cc == 'h' or cc == 't':
    print('...',cf[1])
    if cc == cf[0]:
      print('You won!')
      print('You will start first.')
      t = 0
      break
    else:
      print('You lost!')
      print('The enemy will start first.')
      t = 1
      break
  else:
    print('Thats is not an option.')
    continue

#attacking
while 1:
  #game end check
  ec = 1
  for x in m:
    if '=' in x:
      ec = 0
  if ec == 1:
    print('The enemy has destroyed all your ships!')
    print('You Lose.')
    break

  ec = 1
  for x in aim:
    if '=' in x:
      ec = 0
  if ec == 1:
    print('You have destroyed all the enemies ships!')
    print('You Win.')
    break
    
  #Player
  if t == 0:

    #print defense map
    print('Defense map:')
    print(' ',end=' ')
    for z in range(0,10):
      print(z,end='')
    print('')
    for z in range(len(m)):
      print(z,end=' ')
      for y in m[z]:
        print(y,end='')
      print('')
      
    #print attack map
    print('Attack map:')
    print(' ',end=' ')
    for z in range(0,10):
      print(z,end='')
    print('')
    for z in range(len(am)):
      print(z,end=' ')
      for y in am[z]:
        print(y,end='')
      print('')

    #attacking
    print('Where do you want to attack.')
    print('Coordinates:')
    ax = int(input('x: '))
    ay = int(input('y: '))

    #attack check
    if am[ay][ax] == '!' or am[ay][ax] == 'X':
      print('This coordinates has already been attacked.')
      continue

    #map update
    if aim[ay][ax] == '*':
      print('You missed.')
      aim[ay][ax] = '!'
      am[ay][ax] = '!'
    if aim[ay][ax] == '=':
      print('You hit.')
      aim[ay][ax] = 'X'
      am[ay][ax] = 'X'

    #switch turn
    t = 1
  #com
  elif t == 1:
    #last hit? last coordinates?  target hit? last direction? found direction?
    nmi = [0,[0,0],0,'N',0]

    #info processing
    nmi[1][0] = aiax
    nmi[1][1] = aiay
    if aiam[aiay][aiax] == 'X':
        nmi[0] = 1
    elif aiam[aiay][aiax] == '!':
        nmi[0] = 0
    if hi[-1][2] == 0:
      if nmi[0] == 1:
        nmi[2] = 1
      if nmi[0] == 0:
        nmi[2] = 0
    if hi[-1][2] == 0:
      if hi[-1][4] == 1:
        if nmi[0] == 1:
          if hi[-1][3] == 'N':
            nax = nmi[1][0]
            nay = nmi[1][1]-1
          if hi[-1][3] == 'S':
            nax = nmi[1][0]
            nay = nmi[1][1]+1
          if hi[-1][3] == 'W':
            nax = nmi[1][0]-1
            nay = nmi[1][1]
          if hi[-1][3] == 'E':
            nax = nmi[1][0]+1
            nay = nmi[1][1]
        elif nmi[0] == 0:
          nmi[2] = 0
      else:
        if hi[-1][3] == 'N':
          if hi[-1][0] == 1:
            nmi[4] = 1
            nax = nmi[1][0]
            nay = nmi[1][1]-1
          elif hi[-1][0] == 0:
            nmi[4] = 0
            nax = nmi[1][0]
            nay = nmi[1][1]+1
        if hi[-1][3] == 'S':
          if hi[-1][0] == 1:
            nmi[4] = 1
            nax = nmi[1][0]
            nay = nmi[1][1]+1
          elif hi[-1][0] == 0:
            nmi[4] = 0
            nax = nmi[1][0]-1
            nay = nmi[1][1]
        if hi[-1][3] == 'W':
          if hi[-1][0] == 1:
            nmi[4] = 1
            nax = nmi[1][0]-1
            nay = nmi[1][1]
          elif hi[-1][0] == 0:
            nmi[4] = 0
            nax = nmi[1][0]+1
            nay = nmi[1][1]
        if hi[-1][3] == 'E':
          if hi[-1][0] == 1:
            nmi[4] = 1
          elif hi[-1][0] == 0:
            nmi[4] = 0
          nax = nmi[1][0]+1
          nay = nmi[1][1]  
    hi.append(nmi)
    #attack
    if hi[-1][2] == 0:
      aiax = random.randint(0,4)*2
      aiay = random.randint(0,4)
      aiax += aiay%2
    if hi[-1][2] == 1:
      aiax = nax
      aiay = nay

    #attack check
    if aiam[aiay][aiax] == '!' or aiam[aiay][aiax] == 'X':
      continue

    #map update
    if m[aiay][aiax] == '*':
      #print('You missed.')
      m[aiay][aiax] = '!'
      aiam[aiay][aiax] = '!'
      h = 0
    elif m[aiay][aiax] == '=':
      #print('You hit.')
      m[aiay][aiax] = 'X'
      aiam[aiay][aiax] = 'X'
      h = 1
    t = 0