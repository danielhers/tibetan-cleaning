article1 = open(r'D:\Dev\tibetan-cleaning\Rong-zom_rawTexts_clean1\2-3.txt', 'r')
article2 = open(r'D:\Dev\tibetan-cleaning\Rong-zom_rawTexts_clean1\2-19.txt', 'r')
matches = open(r'D:\Dev\tibetan-cleaning\Test1.union.txt', 'r')
str_article1 = article1.read()
str_article2 = article2.read()

output_csv = open(r'D:\Dev\tibetan-cleaning\matches.csv', 'w')
output_csv.write('article1txt,article2txt,score,id\n')
count = 0
for line in matches:
    arr = line.split(',')
    output_csv.write(
        str_article1[int(arr[0]): int(arr[2])].replace(',', '_comma_') + ',' + str_article2[
                                                                               int(arr[1]): int(arr[3])].replace(',',
                                                                                                                 '_comma_') + ',' +
        arr[4] + ',' + str(count) + '\n')
    count += 1
output_csv.close()
