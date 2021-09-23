# Import and initiations:
import sys
import os
import pathlib
import csv
import json
import pickle

data_objects = []   # objects keeper
adjustment = ""     # temporary content of change
data_json = {}      # temporary data holder for .json file writing
data_pickle = []    # temporary data holder for .pkl file writing

# Checking source and parameters:
arguments_amount = len(sys.argv[::])  # minimum arguments
if arguments_amount < 3:
    print("There is no minimum number of assumptions: src and dst files.")
    exit()
changes_amount = arguments_amount - 3  # amount of required changes
src_file = sys.argv[1]
try:  # empty src file
    if not os.path.getsize(src_file) > 0:
        print("Src file is empty.")
        exit()
except:  # no src file
    if not os.path.exists(src_file):
        print("Src file does not exist.")
        exit()
imp_name = pathlib.Path(src_file)  # missed src file type
type_srcfile = imp_name.suffix
if type_srcfile != ".csv" and type_srcfile != ".json" and type_srcfile != ".pkl":
    print("Src file is not in required format.")
    exit()
dst_file = sys.argv[2]
exp_name = pathlib.Path(dst_file)  # missed dst file type
type_dstfile = exp_name.suffix
if type_dstfile != ".csv" and type_dstfile != ".json" and type_dstfile != ".pkl":
    print("Dst file is not in required format.")
    exit()

# Common:


class DataGeneral:
    def __init__(self, row, content):
        self.row = row
        self.content = content

    def printer(self):
        print("Content of initial database:")
        for object in data_objects:
            print((str(object.content).strip("[]")).replace("'", ""))

    def replacer(self):  # adjusts initial content following sys.argv
        rows_count = 0
        for object in data_objects:
            rows_count += 1
        request_number = 3
        while request_number < arguments_amount:
            called_adjustment = sys.argv[request_number]  # reading content
            called_elms = called_adjustment.split(',')
            row = int(called_elms[0])
            column = int(called_elms[1])
            combined = ""
            for element in called_elms[2:]:  # if nr of commas > 2
                combined += element + ","
            new_content = combined[:-1]     # last comma abandoned
            try:
                if row > rows_count:
                    print("Row out of range: {}, {}, {}".format(row, column,
                                                                new_content))
                    break
                for object in data_objects:
                    if object.row == row:
                        object.content[column] = new_content
                        print("Adjustment executed: {}, {}, {}"
                              .format(row, column, new_content))
            except IndexError:
                print("Column out of range: {}, {}, {}"
                      .format(row, column, new_content))
            request_number += 1
            continue

# Diversified:


class Readers(DataGeneral):
    def __init__(self, row, content):
        super().__init__(row, content)

    def csv_read(self):  # reading src file
        with open(src_file, "r", encoding="utf-8", newline="") \
                as sf:
            reader = csv.reader(sf)
            for line in reader:
                yield line

    def csv_rexecution(self):  # executing reading and replacing procedure
        Readers.csv_read(self)
        Readers.objects_maker(self)
        super().printer(self)
        super().replacer(self)  # calling adjustments maker

    def json_read(self):  # reading src file
        with open(src_file, "r", encoding="utf-8") as sf:
            reader = json.load(sf)
            for key, value in reader.items():
                yield value

    def json_rexecution(self):  # executing reading and replacing procedure
        Readers.json_read(self)
        Readers.objects_maker(self)
        super().printer(self)
        super().replacer(self)  # calling adjustments maker

    def pkl_read(self):  # reading src file
        with open(src_file, "br") as sf:
            reader = pickle.load(sf)
            for list in reader:
                yield list

    def pkl_rexecution(self):  # executing reading and replacing procedure
        Readers.pkl_read(self)
        Readers.objects_maker(self)
        super().printer(self)
        super().replacer(self)  # calling adjustments maker

    def objects_maker(self):  # creating objects
        if type_srcfile == ".csv":
            data_lines = Readers.csv_read(self)
        if type_srcfile == ".json":
            data_lines = Readers.json_read(self)
        if type_srcfile == ".pkl":
            data_lines = Readers.pkl_read(self)
        row = 0
        for item in data_lines:
            item = list(item)
            data_objects.append(DataGeneral(row, content=item))
            row += 1

if type_srcfile == ".csv":
    Readers.csv_rexecution(Readers)
if type_srcfile == ".json":
    Readers.json_rexecution(Readers)
if type_srcfile == ".pkl":
    Readers.pkl_rexecution(Readers)


class Writers(DataGeneral):

    def csv_write(self):  # creating dst file
        with open(dst_file, "w", encoding="utf-8", newline="") \
                as df:
            writer = csv.writer(df)
            for object in data_objects:
                writer.writerow(object.content)
        print("Data written to file: {}.".format(dst_file))

    def csv_wexecution(self):  # executing writing procedure
        Writers.csv_write(self)

    def json_write(self):  # creating dst file
        counter = 1
        for object in data_objects:
            data_json[counter] = object.content
            counter += 1
        with open(dst_file, "w", encoding="utf-8") \
                as filejson:
            json.dump(data_json, filejson)
            filejson.close()
        print("Data written to file: {}.".format(dst_file))

    def json_wexecution(self):  # executing writing procedure
        Writers.json_write(self)

    def pkl_write(self):  # creating dst file
        with open(dst_file, "bw") as df:
            for object in data_objects:
                data_pickle.append(object.content)
            pickle.dump(data_pickle, df)
        print("Data written to file: {}.".format(dst_file))

    def pkl_wexecution(self):  # executing writing procedure
        Writers.pkl_write(self)

if type_dstfile == ".csv":
    Writers.csv_write(Writers)
if type_dstfile == ".json":
    Writers.json_write(Writers)
if type_dstfile == ".pkl":
    Writers.pkl_write(Writers)
