
def convert_matches_to_txt(article1_file,article2_file,matches_file,output_file):

    article1 = open(article1_file, 'r')
    article2 = open(article2_file, 'r')
    matches = open(matches_file, 'r')
    str_article1 = article1.read()
    str_article2 = article2.read()

    output_csv = open(output_file, 'w')
    output_csv.write('article1txt,article2txt,score,id\n')
    count = 0
    for line in matches:
        arr = line.split(',')
        output_csv.write(
            str_article1[int(arr[0]): int(arr[2])].replace(',', '_comma_') + ',' + str_article2[
                                                                                   int(arr[1]): int(arr[3])].replace(',',
                                                                                                                     '_comma_') + ',' +
            arr[4].split()[0] + ',' + str(count) + '\n')
        count += 1
    output_csv.close()


if __name__ == '__main__':
    article1_filename = r'C:\DataSets\Tibet\Kangyur_Tenjur-CLEAN\stem\Kangyur_Lhasa\001\acip-k_lha_sa-001-001.txt', 'r'
    article2_filename = r'C:\DataSets\Tibet\Kangyur_Tenjur-CLEAN\stem\TENGYUR_ACIP\01_BSTOD_TSOGS\001_KA\TD1110E.txt', 'r'
    matches_filename = r'C:\Results\Tibet\test_enum_stem_chars', 'r'
    output_filename = r'C:\Results\Tibet\test_enum_stem_chars_text.csv'
    convert_matches_to_txt(article1_filename,article2_filename,matches_filename,output_filename)
