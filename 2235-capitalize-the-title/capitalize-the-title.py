class Solution(object):
    def capitalizeTitle(self, title):
        title = title.lower()
        words = title.split()
        for i in range(len(words)):
            if len(words[i]) >= 3:
                words[i] = words[i].capitalize()
        return ' '.join(words)

