i=0
while read p; 
do
   echo $p $i
   aws batch submit-job --job-name forrest-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"'${p}'", "out_dir":"/out/'${p}'", "out-aws":"seq2brain-results"}' 
   i=$((i+1))
done <forrest.txt