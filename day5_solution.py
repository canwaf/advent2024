rules = dict()
print_jobs = list()

with open('day5_input.txt', 'r') as f:
    for line in f:
        if "|" in line:
            before = int(line.split("|")[0])
            after = int(line.split("|")[1])
            
            if before not in rules:
                rules[before] = [after]
            else:
                rules[before].append(after)

        elif "," in line:
            print_jobs.append([int(x) for x in line.split(",")])
        else:
            continue

mid_total = 0
to_sort = list()

for job in print_jobs:
    valid = True
    for i in range(0, len(job)-1):
        next_value = job[i+1]
        current_value = job[i]
        if next_value in rules[current_value]:
            valid = True
        else:
            valid = False
            break
    if valid:
        mid_total += job[len(job) // 2]
    else:
        to_sort.append(job)

print(f"Mid total: {mid_total}")

to_sort_mid_total = 0
sorted = list()

for job in to_sort:
    sorted = list()
    i = 0
    while sum(sorted) != len(job):
        
        for j in range(0, len(job)-1):

            if job[j+1] not in rules[job[j]]:
                current_value = job.pop(j)
                job.append(current_value)
                i=0
                sorted.clear()
                break

        i += 1
        sorted.append(True)

    to_sort_mid_total += job[len(job) // 2]

print(f"To sort mid total: {to_sort_mid_total}")