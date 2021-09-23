# Initiations:
import sys
import os
from accountant import mng

# Starting procedures:
if not os.path.isfile("input.txt"):         #sprawdzanie pliku z danymi
    print("Nie znaleziono pliku wejściowego.")
    exit()
outputfile = open("output.txt", "w")        #czyszczenie pliku output
outputfile.close()

# Data entry from import file:
import_file = open("input.txt", "r", encoding="utf-8")
for line in import_file:
    transaction = line.replace("\n", "").split(" ")
    mng.log.append(transaction)
    procedure = transaction[0]
    trans_args = transaction[1:]
    mng.callbacks[procedure](trans_args)

# Data entry from .args:
if len(sys.argv[::]) > 1:
    procedure = ('magazyn')
    trans_args = sys.argv[1:]
    mng.callbacks[procedure](trans_args)

# Data output:
with open("output.txt", "a", encoding="utf-8") as export_file:
    for item in mng.log:
        export_file.write("\n".join(item) + "\n")
    export_file.write("Wykaz stanów magazynowych: \n")
    for list in mng.stocks:
        export_file.write(str(list) + "\n")

