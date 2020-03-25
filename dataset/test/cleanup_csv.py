import csv


def cleanup_csv(file_path):
    print(file_path)
    with open(file_path) as f:
        reader = csv.reader(f)
        with open('movies_director.csv', 'w', encoding='utf-8') as fp:
            writer111 = csv.writer(fp, delimiter=',')
            for row in reader:
                writer = row[4]
                a = writer.split("|")
                result = []
                for i in a:
                    strsplit = i.split(" (")
                    if strsplit[0] not in result:
                        result.append(strsplit[0])
                row[4] = '|'.join(result)
                writer111.writerow(row)



movies_file_path = "movies.csv"
cleanup_csv(movies_file_path)
