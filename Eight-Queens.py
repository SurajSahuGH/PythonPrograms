def conflict(state, nextX):
# state = tuple of containing col as values
# and rows are the indices, nextX=col
    nextY = len(state)
    print(nextY)
    for i in range(nextY):
        print(i)
        print(f'{state[i]} - {nextX}')
        # i=row, state[i]=col
        print(f'(0, {nextY} - {i})')
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()): # num = n-queens, s = tuple
    for pos in range(num): # 0,1,2,3
        if not conflict(state, pos):# (1,3,0), 0-3
            if len(state) == num-1: # Last queen
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result
