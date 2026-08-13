class Solution(object):
    def destCity(self, paths):
        source_set = set()
        destination_set = set()

        for path in paths:
            source_set.add(path[0])
            destination_set.add(path[1])

        final_destination = destination_set.difference(source_set)
        if final_destination:
            return final_destination.pop()
        else:
            return ""