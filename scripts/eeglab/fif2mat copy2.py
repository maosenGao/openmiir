#!/usr/bin/env python
__author__ = 'sstober'

'''
Created on Jun 16, 2015
@author: sstober
'''

# 'fif_filepath'='E:\OpenMIIR-RawEEG_v1\OpenMIIR\eeg\mne'

if __name__ == '__main__':

    import argparse
    # The parameters of the argparse is a comprehensive processing library.
    # Argparse module is mainly used to for the script command parameter function, make them more flexible.
    import mne
    import numpy as np
    from scipy import io

    #  1  the establishment of the parser

    parser = argparse.ArgumentParser(
                                     prog='fif2mat',
                                     description='converts raw EEG data in FIF format into MAT format;'
                                                 'events are stored in an extra file in EEGLab format.'
                                    )

    parser.add_argument('fif_filepath',
                        help='path to the input FIF file')

    parser.add_argument('eeg_filepath',
                        help='path to the output MAT file for the raw EEG data')

    parser.add_argument('events_filepath',
                        help='path to the output MAT file for the events')

    # get parameters
    args = parser.parse_args()

    print('loading raw data from ',
          args.fif_filepath)

    raw = mne.io.Raw(args.fif_filepath,
                     preload=True,
                     verbose=True)
    data, time = raw[:, :]

    print('saving raw data to',
           args.eeg_filepath)

    io.savemat(args.eeg_filepath,
               dict(data=data),
               oned_as='row')

    events = mne.find_events(raw,
                             stim_channel='STI 014',
                             shortest_event=0)

    # EEGLab event structure: type, latency, urevent
    # Event latencies are stored in units of data sample points relative to (0) 
    # the beginning of the continuous data matrix (EEG.data).
    
    eeglab_events = [[event[2], event[0], 0] for event in events]

    eeglab_events = np.asarray(eeglab_events,
                               dtype=int)
    
    print('saving events to',
           args.events_filepath)

    io.savemat(args.events_filepath,
               dict(data=eeglab_events),
               oned_as='row')


