import csv

def cleanup_csv(file_path):
    print(file_path)
    with open(file_path) as f:
        reader = csv.reader(f)
        with open('xxxxx.csv', 'w', encoding='utf-8') as fp:
            writer111 = csv.writer(fp, delimiter=',')
            for row in reader:
                print("ssss")
                print(row)
                result = []
                for i in row:
                    a = i.split("|")[:2]
                    print("1111")
                    print(a)
                    xxx = "|".join(a)
                    result.append(xxx)

                writer111.writerow(result)

movies_file_path = "movies_director.csv"
cleanup_csv(movies_file_path)