import chardet

# File path
file_path = "dataset.csv"

# Read a portion of the file to detect encoding
with open(file_path, "rb") as f:
    raw_data = f.read(10000)  # Read first 10KB

# Detect encoding
encoding_info = chardet.detect(raw_data)
print(encoding_info)
 ##output:
 # {'encoding': None, 'confidence': 0.0, 'language': None} means the file might be binary or compressed instead of a regular csv file.