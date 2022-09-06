from numbers_parser import Document

doc = Document("test.numbers")
sheets = doc.sheets
tables = sheets[0].tables
table = tables[0]
for row in table.iter_rows():
    print(row.value)