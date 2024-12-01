import pandas as pd

advent_df = pd.read_csv("./day1_input.tsv", sep="\t", header=None)

advent_df = advent_df[0].str.split(expand=True)

left = list(advent_df[0].sort_values())
right = list(advent_df[1].sort_values())

# For total difference
diff = list()
[diff.append(abs(int(x)-int(y))) for x, y in zip(right,left)]

total_diff = sum(diff)
print(f"The total difference between list 1 and two is `{total_diff}.`")
      
# For similarity score
similar = list()
[similar.append(int(x)*right.count(x)) for x in left]

total_similar = sum(similar)
print(f"The similarity score between left and right lists is `{total_similar}`.")