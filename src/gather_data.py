import scipy.io as sio
import glob
import os
import numpy as np
import argparse
from multiprocessing import Pool

DATA_DIR = '/data'
DATASET = 'ds001980'

def load_one_dfnc(result_tuple):
    result_file = result_tuple[0]
    data_dir = result_tuple[1]
    print("DOING %s" % result_file)
    task =  os.path.abspath(os.path.join(result_file ,"../.."))
    df = sio.loadmat(result_file)
    clusterInfo = df['clusterInfo']
    clusters = clusterInfo[0,0]['Call']
    states = clusterInfo[0,0]['states']
    df = sio.loadmat(os.path.join(task, 'gica_cmd_ica_br1.mat'))
    tc = df['compSet'][0,0]['tc']
    if 'run-' in task or not 'ds' in data_dir:
        out_dir = os.path.join('/data/dfnc/%s/%s' % (data_dir,os.path.basename(task).replace('bold.nii.gz','')))
        os.makedirs(out_dir, exist_ok=True)
        np.save(os.path.join(out_dir, 'clusters'), clusters)
        np.save(os.path.join(out_dir, 'states'),states)
        states = states.flatten()
        np.save(os.path.join(out_dir, 'tc'),tc)
        if 'ds' in data_dir:
            run_num = int(task[(task.index('run-')+4):(task.index('run-')+5)])
            np.save(os.path.join(out_dir, 'label'), run_num)

def load_dfncs(data_dir=DATA_DIR, dataset=DATASET, ingore=[], procs=64):
    search_dir = os.path.join(data_dir, dataset)
    search_str = os.path.join(search_dir, '**', 'gica_cmd_dfnc_post_process.mat')
    result_files = glob.iglob(search_str, recursive=True)    
    p = Pool(procs)
    p.map(load_one_dfnc, [(r,dataset) for r in result_files])
    for state_file in glob.iglob('/data/dfnc/%s/**/states*' % dataset):
        states = np.load(state_file)
        states = states.flatten()
        states = [str(i) for i in states]
        print(os.path.join(search_dir,'labels.txt'))
        with open(os.path.join(search_dir,'labels.txt'), 'a') as file:
            file.write(' '.join(list(states))+'\n')
        if 'ds' in dataset:
            label = np.load(state_file.replace('states','label'))
            with open(os.path.join(search_dir, str(label) + '.txt'), 'r') as file:
                real_label = file.read()
            with open(os.path.join(search_dir,'inputs.txt'), 'a') as file:
                file.write(real_label.replace('\n','').strip()+'\n')
    if 'ds' in dataset:
        cross_validate(os.path.join(search_dir,'inputs.txt'), os.path.join(search_dir,'labels.txt'), 5)
def cross_validate(input, labels, folds):
    data_files = []
    label_files = []
    
    with open(input, 'r') as file:
        for line in file:
            data_files.append(line.strip().replace("\n",''))
    with open(labels, 'r') as file:
        for line in file:
            label_files.append(line.strip().replace('\n',''))
    r = list(range(len(data_files)))
    if len(data_files) % folds != 0:
        raise ValueError(
            "invalid number of folds ({}) for the number of "
            "documents ({})".format(folds, len(data_files))
        )
    fold_size = len(data_files) // folds
    i = 1
    for split_index in range(0, len(data_files), fold_size):
        training = data_files[split_index:split_index + fold_size]
        testing = data_files[:split_index] + data_files[split_index + fold_size:]
        with open('train_data_fold%d.txt' % i,'w') as file:
            for line in training:
                file.write(line+'\n')
        with open('test_data_fold%d.txt' % i,'w') as file:
            for line in testing:
                file.write(line+'\n')
        training = label_files[split_index:split_index + fold_size]
        testing = label_files[:split_index] + data_files[split_index + fold_size:]

        with open('train_label_fold%d.txt' % i,'w') as file:
            for line in training:
                file.write(line+'\n')
        with open('test_label_fold%d.txt' % i,'w') as file:
            for line in testing:
                file.write(line+'\n')
        i += 1



if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dataset', default=DATASET, help='old foo help')
    parser.add_argument('-i', '--data_dir', default=DATA_DIR, help='old foo help')
    args = parser.parse_args()
    load_dfncs(data_dir=args.data_dir, dataset=args.dataset)


