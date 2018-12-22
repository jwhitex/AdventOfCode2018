from collections import deque

def isspecial(m):
    return m % 23 == 0

def placemarble(circle, m):
    # item at index 0 in deque is cm
    if isspecial(m):
        # go 7 counter-clockwise and rm and add to score
        circle.rotate(7)
        l7marb = circle.popleft()
        score = m + l7marb
        return score
    # x -> cm, 1, x, 2
    circle.rotate(-2)
    circle.appendleft(m)
    return 0

# 439 players; last marble is worth 71307 points.
players_scores = [0]*439
# pt1 answer: 410375
# last_marble = 71307
# pt2 answer: 3314195047
last_marble = 71307*100

circle = deque([0])
for marble in range(1, last_marble+1):
    players_scores[marble % len(players_scores)] += placemarble(circle, marble)

print(max(players_scores))

