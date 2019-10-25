"""
General workflow for importing a new session
"""
subject = 'P01' # TODO: change this for each subject
verbose = True  # change this for debugging

import matplotlib
# matplotlib inline

from deepthought.datasets.openmiir.preprocessing.pipeline import Pipeline
settings = dict(debug=False, mne_log_level='Info', sfreq=64) # optional pipeline settings
pipeline = Pipeline(subject, settings)

