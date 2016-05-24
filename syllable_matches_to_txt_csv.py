import sort_match_results as sorter
import convert_syllable_to_char_matches as syl_to_char
import matches_to_txt_csv as matches_to_txt

# todo: call syllable_to_txt
syllable_matches_filename = r'C:\Results\Tibet\1.txt'
article1_filename = r'C:\DataSets\Tibet\Kangyur_Tenjur-CLEAN\stem\Kangyur_Lhasa\001\acip-k_lha_sa-001-001.txt'
article2_filename = r'C:\DataSets\Tibet\Kangyur_Tenjur-CLEAN\stem\TENGYUR_ACIP\01_BSTOD_TSOGS\001_KA\TD1110E.txt'
char_matches_filename = syllable_matches_filename + r'_chars'

syl_to_char.convert_matches(syllable_matches_filename, [article1_filename , article2_filename ], char_matches_filename)

# TODO: call sort match
sorter.sort_matches(char_matches_filename)

# todo: call matches_to_txt
txt_matches_filename = syllable_matches_filename + '_text.csv'

matches_to_txt.convert_matches_to_txt(article1_filename,article2_filename,char_matches_filename,txt_matches_filename)
