def main(file):
    import csv
    result = {}
    with open(file) as text:
        reader = csv.reader(text)
        for item in reader:
            if reader.line_num == 1:
                continue
            result[item[0]] = item[1]
    
    return result
    
