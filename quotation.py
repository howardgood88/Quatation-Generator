from numbers_parser import Document

doc = Document("test(0.75).numbers")
sheets = doc.sheets
tables = sheets[0].tables
table = tables[0]
for row in table.iter_rows(values_only = True):
    print(row)
table.write("B8", "Fuck you")
table.write("C9", "bitch")
print()
for row in table.iter_rows(values_only = True):
    print(row)
doc.save("test_new.numbers")