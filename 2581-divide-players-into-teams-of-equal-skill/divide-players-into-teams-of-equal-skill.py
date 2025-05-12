class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        N=len(skill)
        target_skill= skill[0]+ skill[-1]
        total_chemistry=0
        for i in range(N//2):
            if skill[i]+skill[N-i-1]!=target_skill:
                return -1
            total_chemistry+=skill[i]*skill[N-i-1]
        return total_chemistry
        