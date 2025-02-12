from prettytable import PrettyTable, HRuleStyle

table = PrettyTable()
table.add_column('Pokemon Name', ['Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie',
                                  'Frogadier', ])
table.add_column('Type', ['Grass', 'Grass', 'Grass', 'Fire', 'Fire', 'Fire', 'Water', 'Water', ])
table.border = False
table.header = True
# table.HRuleStyle = ALL # why doesn't this work?
table.align = "l"
print(table)
