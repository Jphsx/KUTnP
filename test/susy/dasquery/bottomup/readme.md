

this directory contains several scripts (cant be run in bash script) that must be run in sequence

input: some list of miniaod files in an input list directory
output: a file (uniqueaod.list) with the aod parents of the miniaod

the sequence goes as follows

python dasqueryparentsfromlist.py ./path/to/some/file.list

the file.list is coppy pasted content from CMS DAS browser page (from dataset files)

this produces the das queries to be run in temp.sh

to make the queries for the parents:

./temp.sh > tempaod.list

the output of temp.sh is tempaod.list

this first output list will contain all of the aod parents from the miniaod queries
the list of files may contain duplicates-- so they need to be removed

to remove duplicates run

python verifylistunique.py

the resulting list is the unique AOD parents of all miniaod files that can be copy pasted into a CMSSW cfg script

(NOTE) sometimes the DAS queries are slow -- also remember to setup cmsenv and set up grid

Example run for JPsi MC

python dasqueryparentsfromlist.py ../jpsi/inputlists/jfile.list
./temp.sh > tempaod.list
python verifylistunique.py


