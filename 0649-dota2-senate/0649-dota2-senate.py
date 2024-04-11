class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # keep track of 2 queues
        radiant = []
        dire = []
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            # Remove first occurent of R and D, add first to end of queue
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.pop(0)
            dire.pop(0)
        return 'Radiant' if radiant else 'Dire'