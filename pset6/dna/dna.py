# program for dna profiling:::
from csv import DictReader, reader
from sys import argv

# cchecking command line arguments:
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit()
# getting cml arguments:
db_path = argv[1]
seq_path = argv[2]

# open csv file
with open(db_path, "r") as db_csv:
    db_reader = DictReader(db_csv)
    db_list = list(db_reader)

# oopen sequences file as string
with open(seq_path) as seq_text:
    seq_list = seq_text.read()

max_counts = []

for i in range(1, len(db_reader.fieldnames)):
    STR = db_reader.fieldnames[i]
    max_counts.append(0)
# Loopo through sequence to find STR
    for j in range(len(seq_list)):
        STR_count = 0
        # if match found start counting repeats
        if seq_list[j:(j + len(STR))] == STR:
            k = 0
            while seq_list[(j + k):(j + k + len(STR))] == STR:
                STR_count += 1
                k += len(STR)
            # If new maximum of repeats, update max_counts
            if STR_count > max_counts[i - 1]:
                max_counts[i - 1] = STR_count
# comapre with database:
for i in range(len(db_list)):
    matches = 0
    for j in range(1, len(db_reader.fieldnames)):
        if int(max_counts[j - 1]) == int(db_list[i][db_reader.fieldnames[j]]):
            matches += 1
        if matches == (len(db_reader.fieldnames) - 1):
            print(db_list[i]['name'])
            exit()
print("No match")

