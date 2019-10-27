# docker container run -v /home/bbradt/projects/seq2brain/data/fbirn:/data/fbirn -v /home/bbradt/projects/seq2brain/data/results:/out giftdocker python /app/run_gift.py gica '{"in_files":["/data/fbirn/vsdwa_000360276455_0002.nii"]}'
# docker container run giftdocker python /app/run_gift.py eval '{"in-aws": "seq2brain-finetune", "in_files":["pixar/derivatives/fmriprep/sub-pixar001/sub-pixar001_task-pixar_run-001_swrf_bold.nii.gz"], "out_dir":"/out/pixar-sub001", "out-aws":"seq2brain-results"}'
# for i in {0..9}
# do
# aws batch submit-job --job-name pixar${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"pixar/derivatives/fmriprep/sub-pixar00'${i}'/sub-pixar00'${i}'_task-pixar_run-001_swrf_bold.nii.gz", "out_dir":"/out/pixar-sub00'${i}'", "out-aws":"seq2brain-results"}'
# done

# for i in {10..99}
# do
# aws batch submit-job --job-name pixar${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"pixar/derivatives/fmriprep/sub-pixar0'${i}'/sub-pixar0'${i}'_task-pixar_run-001_swrf_bold.nii.gz", "out_dir":"/out/pixar-sub0'${i}'", "out-aws":"seq2brain-results"}'
# done

# for i in {100..155}
# do
# aws batch submit-job --job-name pixar${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"pixar/derivatives/fmriprep/sub-pixar'${i}'/sub-pixar'${i}'_task-pixar_run-001_swrf_bold.nii.gz", "out_dir":"/out/pixar-sub'${i}'", "out-aws":"seq2brain-results"}'
# done

for i in {1..9}
do
aws batch submit-job --job-name twilight-0${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"twilight/sub-0'${i}'/func/sub-0'${i}'_task-watchmovie_bold.nii.gz", "out_dir":"/out/twilight-sub0'${i}'", "out-aws":"seq2brain-results"}'
done

for i in {10..24}
do
aws batch submit-job --job-name twilight-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"twilight/sub-'${i}'/func/sub-'${i}'_task-watchmovie_bold.nii.gz", "out_dir":"/out/twilight-sub'${i}'", "out-aws":"seq2brain-results"}'
done

for i in {1..9}
do
aws batch submit-job --job-name affective-0${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"affective/sub-0'${i}'/func/sub-0'${i}'_task-view_run-01.nii.gz", "out_dir":"/out/affective-sub0'${i}'", "out-aws":"seq2brain-results"}'
done

for i in {10..11}
do
aws batch submit-job --job-name affective-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"affective/sub-'${i}'/func/sub-'${i}'_task-view_run-01.nii.gz", "out_dir":"/out/affective-sub'${i}'", "out-aws":"seq2brain-results"}'
done

for i in {1..9}
do
aws batch submit-job --job-name sherlock-0${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"sherlock/sub-0'${i}'/func/sub-0'${i}'_task-SherlockMovie_bold.nii.gz", "out_dir":"/out/sherlock-sub0'${i}'", "out-aws":"seq2brain-results"}'
done

for i in {10..37}
do
aws batch submit-job --job-name sherlock-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-finetune","in_files":"sherlock/sub-'${i}'/func/sub-'${i}'_task-SherlockMovie_bold.nii.gz", "out_dir":"/out/sherlock-sub'${i}'", "out-aws":"seq2brain-results"}'
done

# for i in {1..9}
# do
# aws batch submit-job --job-name ds000243-00${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-pretrain","in_files":"ds000243/sub-00'${i}'/func/sub-00'${i}'_task-rest_run-1_bold.nii.gz", "out_dir":"/out/ds000243-sub00'${i}'", "out-aws":"seq2brain-results"}'
# done

# for i in {10..99}
# do
# aws batch submit-job --job-name ds000243-0${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-pretrain","in_files":"ds000243/sub-0'${i}'/func/sub-0'${i}'_task-rest_run-1_bold.nii.gz", "out_dir":"/out/ds000243-sub0'${i}'", "out-aws":"seq2brain-results"}'
# done

# for i in {100..120}
# do
# aws batch submit-job --job-name ds000243-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-pretrain","in_files":"ds000243/sub-'${i}'/func/sub-'${i}'_task-rest_run-1_bold.nii.gz", "out_dir":"/out/ds000243-sub'${i}'", "out-aws":"seq2brain-results"}'
# done

for i in {1..9}
do
aws batch submit-job --job-name ds000240-0${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-pretrain","in_files":"ds000240/sub-0'${i}'/func/sub-0'${i}'_task-restEyesOpen_asl.nii.gz", "out_dir":"/out/ds000240-sub0'${i}'", "out-aws":"seq2brain-results"}'
done

for i in {10..63}
do
aws batch submit-job --job-name ds000240-${i} --job-queue giftcomp-1000 --job-definition giftdocker-run:13 --parameters '{"in-aws":"seq2brain-pretrain","in_files":"ds000240/sub-'${i}'/func/sub-'${i}'_task-restEyesOpen_asl.nii.gz", "out_dir":"/out/ds000240-sub'${i}'", "out-aws":"seq2brain-results"}'
done