class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        moves=list(moves)
        count_l = moves.count('L')
        count_r = moves.count('R')
        count_underscore = moves.count('_')
        return abs(count_r-count_l)+count_underscore