def step(levels: list) -> bool:
    check = list()
    for i in range(0,len(levels)-1):
       check.append(4>abs(levels[i]-levels[i+1])>0)
    return all(check)


def safe(levels: list) -> bool:
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False

    return step(levels)

def skip(levels: list, skipped: int) -> list:
    return levels[:skipped] + levels[skipped+1:]

def dampened(levels:list) -> bool:
    tolerance = list()
    for i in range(0,len(levels)):
        tolerance.append(safe(skip(levels, skipped=i)))
        
    return any(tolerance)


with open('day2_input.tsv', 'r') as file:
    reports = list()
    magic = list()
    for line in file:
        levels = list(map(int, line.split()))
        result = safe(levels)
        reports.append(result)

        result = dampened(levels)
        magic.append(result)

    print(f"The number of safe reactor levels is {str(sum(reports))}.") 
    print(f"The number of safe reactor levels within tolerance is {str(sum(magic))}.")