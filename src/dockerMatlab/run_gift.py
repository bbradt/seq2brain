import os
import nipype.interfaces.gift as gift

# CONSTANTS
ICA_TYPES = ['spatial', 'temporal']
PCA_TYPES = ['subject specific', 'group grand mean']
BACK_RECON = ['regular', 'spatial-temporal regression',
              'gica3', 'gica', 'gig-ica']
PREPROC_TYPES = ['remove mean per timepoint', 'remove mean per voxel',
                 'intensity normalization', 'variance normalization']
SCALE_TYPE = ['No scaling', 'percent signal change', 'Z-scores']
WHICH_ANALYSIS = ['standard', 'ICASSO', 'MST']
ICA_ALGORITHMS = ['InfoMax', 'Fast ICA', 'Erica', 'Simbec', 'Evd', 'Jade Opac',
                  'Amuse', 'SDD ICA', 'Semi-blind Infomax', 'Constrained ICA (Spatial)', 'Radical ICA',
                  'Combi', 'ICA-EBM', 'ERBM', 'IVA-GL', 'GIG-ICA', 'IVA-L']

# SHARED DEFAULTS
matlab_cmd = 
DEFAULT_OUT_DIR = os.path.join('results')
DEFAULT_DISPLAY_RESULTS = 1
DEFAULT_NUM_COMPS = 100
DEFAULT_COMP_NETWORK_NAMES = {}
DEFAULT_TR = 2

# GICA DEFAULTS
DEFAULT_DIM = 53
DEFAULT_ALG = 16
DEFAULT_ICA_PARAM_FILE = ''
DEFAULT_REFS = os.path.join('data',
                            'NeuroMarkICNs.nii')
DEFAULT_RUN_NAME = 'test'
DEFAULT_GROUP_PCA_TYPE = 0
DEFAULT_BACK_RECON_TYPE = 5
DEFAULT_PREPROC_TYPE = 1
DEFAULT_NUM_REDUCTION_STEPS = 1
DEFAULT_SCALE_TYPE = 2
DEFAULT_GROUP_ICA_TYPE = 'spatial'
DEFAULT_WHICH_ANALYSIS = 1
DEFAULT_MASK = ''

# dFNC DEFAULTS
# populated into the dfnc_parameters dict
DEFAULT_TC_DETREND = 3,
DEFAULT_TC_DESPIKE = 'yes',
DEFAULT_TC_FILTER = 0.15,
DEFAULT_TC_COVARIATES_FILES_LIST = []
DEFAULT_TC_COVARIATES_FILE_NUMBERS = []
DEFAULT_METHOD = 'none'
DEFAULT_WSIZE = 30
DEFAULT_WINDOW_ALPHA = 3
DEFAULT_NUM_REPETITIONS = 10
# populated into the postprocessing dict
DEFAULT_NUM_CLUSTERS = 5
DEFAULT_ICA_ALGORITHM = 'infomax'
DEFAULT_ICA_NUM_ICA_RUNS = 5
DEFAULT_REGRESS_COV_FILE = ''
DEFAULT_KMEANS_MAX_ITER = 150
DEFAULT_DMETHOD = 'city'

def gift_gica(
    in_files, dim=DEFAULT_DIM, algoType=DEFAULT_ALG, refFiles=DEFAULT_REFS,
    run_name=DEFAULT_RUN_NAME, out_dir=DEFAULT_OUT_DIR, group_pca_type=DEFAULT_GROUP_PCA_TYPE,
    backReconType=DEFAULT_BACK_RECON_TYPE, preproc_type=DEFAULT_PREPROC_TYPE,
    numReductionSteps=DEFAULT_NUM_REDUCTION_STEPS, scaleType=DEFAULT_SCALE_TYPE,
    group_ica_type=DEFAULT_GROUP_ICA_TYPE, display_results=DEFAULT_DISPLAY_RESULTS,
    which_analysis=DEFAULT_WHICH_ANALYSIS, mask=DEFAULT_MASK
):
    """
    Wrapper for initializing GIFT nipype interface to run Group ICA.

    Args:
        in_files            (List [Str])    :   Input file names (either single file name or a list)
        dim                 (Int)           :   Dimensionality reduction into #num dimensions
        algoType            (Int)           :   options are 1 - Infomax, 2 - Fast ica , ...
        refFiles            (List [Str])    :   file names for reference templates (either single file name or a list)
        run_name            (Str)           :   Name of the analysis run
        out_dir             (Str)           :   Full file path of the results directory
        group_pca_type      (Str)           :   options are 'subject specific' and 'grand mean'
        backReconType       (Int)           :   options are 1 - regular, 2 - spatial-temporal regression, 3 - gica3, 4 - gica, 5 - gig-ica
        preproc_type        (Int)           :   options are 1 - remove mean per timepoint, 2 - remove mean per voxel, 3 - intensity norm, 4 - variance norm
        numReductionSteps   (Int)           :   Number of reduction steps used in the first pca step
        scaleType           (Int)           :   options are 0 - No scaling, 1 - percent signal change, 2 - Z-scores
        group_ica_type      (Str)           :   1 - Spatial ica, 2 - Temporal ica.
        display_results     (Int)           :   0 - No display, 1 - HTML report, 2 - PDF
        which_analysis      (Int)           :   Options are 1, 2, and 3. 1 - standard group ica, 2 - ICASSO and 3 - MST.
        mask                (Str)           :   Enter file names using full path of the mask. If you wish to use default mask leave it empty

        algoType full options:
        1           2           3       4           5       6
        'Infomax'   'Fast ICA'  'Erica' 'Simbec'    'Evd'   'Jade Opac',
        7           8           9                   10 
        'Amuse'     'SDD ICA'   'Semi-blind'        'Constrained ICA (Spatial)' 
        11              12      13          14      15          16          17
        'Radical ICA'   'Combi' 'ICA-EBM'   'ERBM'  'IVA-GL'    'GIG-ICA'   'IVA-L'

    Args (not supported here, but available for nipype):
        perfType            (Int)           :   Options are 1, 2, and 3. 1 - maximize performance, 2 - less memory usage  and 3 - user specified settings.
        prefix              (Str)           :   Enter prefix to be appended with the output files
        dummy_scans         (Int)           :   enter dummy scans
        numWorkers          (Int)           :   Number of parallel workers    
        doEstimation        (Int)           :   options are 0 and 1 


    """
    gift.GICACommand.set_mlab_paths(matlab_cmd=matlab_cmd)

    gc = gift.GICACommand()
    gc.inputs.in_files = in_files
    gc.inputs.algoType = algoType
    gc.inputs.group_pca_type = group_pca_type
    gc.inputs.backReconType = backReconType
    gc.inputs.preproc_type = preproc_type
    gc.inputs.numReductionSteps = numReductionSteps
    gc.inputs.scaleType = scaleType
    gc.inputs.group_ica_type = group_ica_type
    gc.inputs.which_analysis = which_analysis
    gc.inputs.refFiles = refFiles
    gc.inputs.display_results = display_results

    if dim > 0:
        gc.inputs.dim = dim

    gc.inputs.out_dir = out_dir

    return gc.run()

def gift_dfnc(
    ica_param_file=DEFAULT_ICA_PARAM_FILE,
    out_dir=DEFAULT_OUT_DIR,
    run_name=DEFAULT_RUN_NAME,
    comp_network_names=DEFAULT_COMP_NETWORK_NAMES,
    TR=DEFAULT_TR,
    tc_detrend=DEFAULT_TC_DETREND,
    tc_despike=DEFAULT_TC_DESPIKE,
    tc_filter=DEFAULT_TC_FILTER,
    tc_covariates_filesList=DEFAULT_TC_COVARIATES_FILES_LIST,
    tc_covariates_file_numbers=DEFAULT_TC_COVARIATES_FILE_NUMBERS,
    method=DEFAULT_METHOD,
    wsize=DEFAULT_WSIZE,
    window_alpha=DEFAULT_WINDOW_ALPHA,
    num_repetitions=DEFAULT_NUM_REPETITIONS,
    num_clusters=DEFAULT_NUM_CLUSTERS,
    ica_num_comps=DEFAULT_NUM_COMPS,
    ica_algorithm=DEFAULT_ICA_ALGORITHM,
    ica_num_ica_runs=DEFAULT_ICA_NUM_ICA_RUNS,
    regressCovFile=DEFAULT_REGRESS_COV_FILE,
    kmeans_max_iter=DEFAULT_KMEANS_MAX_ITER,
    dmethod=DEFAULT_DMETHOD,
    display_results=DEFAULT_DISPLAY_RESULTS,
):
    '''
    Wrapper for initializing GIFT nipype interface to run dynamic FNC.

    Args:
        ica_param_file      (Str)   :   Enter fullfile path of the ICA parameter file
        out_dir             (Str)   :   Enter fullfile path of the results directory
        run_name            (Str)   :   Name of the analysis run
        comp_network_names  (Dict)  :   dictionary containing network names and network values
        TR                  (Float) :   Enter experimental TR in seconds
        tc_detrend          (Int)   :   Detrend number used to remove the trends in timecourses. Options are 0, 1, 2 and 3.
        tc_despike          (Str)   :   Remove spikes from the timecourses. Options are 'yes' and 'no'.
        tc_filter           (Float) :   High frequency cutoff
        tc_covariates_filesList (List)  :   List of covariate files to include. Leave empty if you want to select all.
        tc_covariates_file_numbers (List)  :   Enter scan numbers to include. Leave empty if you want to select all.
        wsize               (Int)   :   Window size (number of scans)
        window_alpha        (Float) :   Gaussian Window alpha value.
        num_repetitions     (Int)   :   No. of repetitions (L1 regularisation).
        num_clusters        (Int)   :   Number of KMeans clusters to use for dFNC
        ica_num_comps       (Int)   :   Number of ICA components
        ica_algorithm       (Int)   :   ICA Algorithm used in ICA estimation
        ica_num_ica_runs    (Int)   :   Number of ICA runs to perform
        regressCovFile      (Str)   :   'yes' or 'no' to regress out covariates
        kmeans_max_iter     (Int)   :   Maximum number of KMeans iterations
        dmethod             (Str)   :   Distance Method ('city', 'sqEuclid',...)
        display_results     (Int)   :   0 - No display, 1 - HTML report, 2 - PDF

    Args (not supported here, but available for nipype):
        Regularisation      (Str)   :   Options are 'none' and 'L1'. 
    '''
    out_dir = os.path.join(out_dir, run_name)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    gift.DFNCCommand.set_mlab_paths(matlab_cmd=matlab_cmd)

    gc = gift.DFNCCommand()
    gc.inputs.ica_param_file = ica_param_file
    gc.inputs.out_dir = out_dir
    gc.inputs.comp_network_names = resolve_comp_network_names(ica_num_comps, comp_network_names)
    gc.inputs.TR = TR
    dfnc_params = dict(
        tc_detrend=tc_detrend,
        tc_covariates=dict(file_numbers=tc_covariates_file_numbers,
                           filesList=tc_covariates_filesList),
        tc_despike=tc_despike,
        tc_filter=tc_filter,
        method=method,
        wsize=wsize,
        window_alpha=window_alpha,
        num_repetitions=num_repetitions,
    )
    postprocess = dict(
        num_clusters=num_clusters,
        ica=dict(algorithm=ica_algorithm,
                 num_comps=ica_num_comps,
                 num_ica_runs=ica_num_ica_runs),
        regressCovFile=regressCovFile,
        kmeans_max_iter=kmeans_max_iter,
        dmethod=dmethod,
        display_results=display_results,
    )
    gc.inputs.dfnc_params = dfnc_params
    gc.inputs.postprocess = postprocess

    return gc.run()