i=0
while read p; 
do
   echo $p $i
   aws batch submit-job --job-name freading-1-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in_aws":"openneuro.org","in_files":"'${p}'", "out_dir":"/out/'${p}'", "out_aws":"seq2brain-text"}' 
   i=$((i+1))
done <reading1.txt