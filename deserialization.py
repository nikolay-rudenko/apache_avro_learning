from avro.datafile import DataFileReader
from avro.io import DatumReader

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
# the schema is embedded in the data file
for user in reader:
    print (user)

reader.close()