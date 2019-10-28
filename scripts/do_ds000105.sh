i=0
while read p; 
do
   echo $p $i
   aws batch submit-job --job-name ds000105-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"openneuro.org","in_files":"'${p}'", "out_dir":"/out/'${p}'", "out-aws":"seq2brain-text"}' 
   i=$((i+1))
done <ds000105.txt