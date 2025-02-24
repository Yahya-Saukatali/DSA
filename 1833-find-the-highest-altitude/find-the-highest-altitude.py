class Solution(object):
    def largestAltitude(self, gain):
        curr_altitude = 0
        max_altitude = 0
        for g in gain:
            curr_altitude += g
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude
