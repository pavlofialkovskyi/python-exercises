def count_levels(lines):

    line = lines.copy()

    d = {}

    for i in range(len(line)):
        phrazes = line[i].split()
        if len(phrazes) != 0:  # can also slicing if phraze[:1]: that returns True 
            if (phrazes[0] in d):     # build a dictionary with keys as Error Codes
                        d[phrazes[0]] += 1
            else: 
                        d[phrazes[0]] = 1          

    return d





for text in (["ERROR disk full", "INFO started", "ERROR timeout"], ["INFO a", "INFO b", "INFO c"], [], ["", "   ", "WARN low memory"], ["  ERROR   spaced out  "], ["INFO x", "info y"],["ERROR"]):
    print(count_levels(text))
        








 

