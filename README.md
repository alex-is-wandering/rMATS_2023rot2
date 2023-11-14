# rMATS_2023rot2
JCEC outputs of rMATS -> python filtering by 5% FDR and sorting by absolute value of inclusion level differences between groups

example run: 
python rMATS_2023rot2/sort_csv.py MXE.MATS.JCEC.txt tab IncLevelDifference

Sort by the absolute value of the IncLevelDifference column after filtering by false discovery rate <=0.05
Also works on .JC.txt file outputs, which also have FDR and IncLevelDifference columns
