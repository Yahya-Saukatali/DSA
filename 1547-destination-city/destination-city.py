class Solution(object):
    def destCity(self, paths):
        start_cities={path[0] for path in paths}
        for path in paths:
            if path[1]  not in start_cities:
                return path[1]