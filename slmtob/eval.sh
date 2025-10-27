python calculate_metrics.py ../euan-projects/slmtob/lse_gold.txt -f ../euan-projects/slmtob/lse_zero.txt
python chrF++.py -R ../euan-projects/slmtob/lse_gold.txt -H ../euan-projects/slmtob/lse_zero.txt -s

python calculate_metrics.py ../euan-projects/slmtob/en_gold.txt -f ../euan-projects/slmtob/en_zero.txt
python chrF++.py -R ../euan-projects/slmtob/en_gold.txt -H ../euan-projects/slmtob/en_zero.txt

python intersection_gloss.py ~/Documents/git/euan-projects/slmtob/gold_all isignos_all.txt 