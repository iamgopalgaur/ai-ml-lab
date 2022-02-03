a = []
with open("ws.csv") as f:
    for x in f:
        a.append(x.strip().split(","))
num_att = len(a[0]) - 1
S = ["0"] * num_att
G = ["?"] * num_att
print("initial shypo",S)
print("initial ghypo",G)
temp = []
for i in range(0, num_att):
    S[i] = a[1][i]

print("-------------------")
for i in range(1, len(a)):
    if a[i][num_att] == "Yes":
        for j in range(0, num_att):
            if S[j] != a[i][j]:
                S[j] = "?"
        for j in range(0, len(temp)):
            for k in range(0, num_att):
                if temp[j][k] != S[k] and temp[j][k] != "?":
                    del temp[j]
    if a[i][num_att] == "No":
        for j in range(0, num_att):
            if a[i][j] != S[j] and S[j] != "?":
                G[j] = S[j]
                temp.append(G)
                G = ["?"] * num_att
    print(S)
    if len(temp) != 0:
        G=temp
    print(G)
    print("-------------------")
print('final s', S)
print('final g', G)