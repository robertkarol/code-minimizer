def delete_line_by_index(lines, lineIdx):
    i = lineIdx
    lines = lines.copy()
    deleted = lines.pop(i)
    if deleted.strip().endswith(":"):
        s = ""
        while len(s) < len(deleted) and deleted[len(s)] == " ":
            s += deleted[len(s)]
        while i < len(lines) and len(s) < len(lines[i]) and lines[i][len(s)] == " ":
            lines[i] = lines[i][4:]
            i += 1
    return lines

def delete_lines_by_index(lines, lineIdxList):
    i = 0
    for lineIdx in lineIdxList:
        lines = delete_line_by_index(lines, lineIdx - i)
        i += 1
    return lines

def delete_lines(lines, keepOrNotList):
   lineIdxList = [idx for idx in range(len(keepOrNotList)) if keepOrNotList[idx] == 0]
   return delete_lines_by_index(lines, lineIdxList) 

def get_lines(filename):
    with open(filename, "r") as f:
        return f.readlines()

def write_lines(filename, lines):
    with open(filename, "w") as f:
        return f.write("".join(lines))

def get_test_module_name(filename):
    return f"{filename.split('.')[0]}_test"