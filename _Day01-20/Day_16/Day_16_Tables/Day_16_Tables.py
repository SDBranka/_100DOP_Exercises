# # creating a table with ascii
# print("| Pokemon Name | Type |")
# print("| ------------ | ---- |")

# creating table with PrettyTable
from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
print(table)

# changing the column alignment
table.align["Pokemon Name"] = "l"
print(table)

# change table alignment
table.align = "r"
print(table)