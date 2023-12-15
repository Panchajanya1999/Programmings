class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n = len(paths)
        
        # cover edge cases
        if n == 1:
            return paths[0][1]
        
        # create a dictionary to store the paths
        path_dict = {}
        for i in range(n):
            path_dict[paths[i][0]] = paths[i][1]
        print(path_dict)
        
        # find the destination city
        for key in path_dict.keys():
            if path_dict[key] not in path_dict.keys():
                return path_dict[key]
