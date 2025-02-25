class Solution(object):
    def defangIPaddr(self, address):
        adddress=list(address)
        for i in range(len(adddress)):
            if adddress[i]=='.':
                adddress[i]='[.]'
        return ''.join(adddress)