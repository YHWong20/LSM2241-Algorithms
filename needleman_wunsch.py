"""
Needleman-Wunsch Algorithm
 - Calculates the optimal pairwise alignment score of two given sequences
 - WIP: Returning the optimal sequences
"""

string_a = "SIMILAR"
string_b = "SIMMARE"

len_a = len(string_a)
len_b = len(string_b)

# Initialise matrix
# Column count = length of string A
# Row count = length of string B
matrix = [[0 for i in range(1 + len_a)] for j in range(1 + len_b)]

gap_penalty = -3
match = 5
mismatch = -5

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j > 0:
            matrix[i][j] = matrix[i][j-1] + gap_penalty
        elif i > 0 and j == 0:
            matrix[i][j] = matrix[i-1][j] + gap_penalty
        else:
            a_base = string_a[j-1]
            b_base = string_b[i-1]

            possible_val = [] # Array of possible values for the given grid (i,j)
        
            if a_base == b_base: # Letter match
                match_sum = matrix[i-1][j-1] + match
                possible_val.append(match_sum)
            elif a_base != b_base: # Letter mismatch
                mismatch_sum = matrix[i-1][j-1] + mismatch
                possible_val.append(mismatch_sum)
                
            gap_hori = matrix[i][j-1] + gap_penalty # Gap penalty applied horizontally
            possible_val.append(gap_hori)
            
            gap_verti = matrix[i-1][j] +  gap_penalty # Gap penalty applied vertically
            possible_val.append(gap_verti)
            
            matrix[i][j] = max(possible_val) # (i,j) takes the maximum value of the recurrence relation   
             

s = ""
for row in matrix:
    for val in row:
        s += f"{val}  "
    s += "\n"

print("Result matrix")
print(s)

score = matrix[-1][-1] # Score would be the very last element of the matrix
output_s = f"The alignment score is {score}."
print(output_s)
