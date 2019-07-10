"""Compute the following voxel measures:
DSC, wDSC, J, sensitivity, TP, FP, FN.
"""

import sys
import argparse
import nibabel as nib
import numpy as np
import csv
from dipy.tracking.vox2track import streamline_mapping


def compute_dsc_mask_tract(mask, true_tract):

    data = mask.get_data()
    affine = mask.affine
    voxel_list_estimated_tract = np.array(np.where(data)).T
    voxel_set_estimated_tract = set()
    for s in range(len(voxel_list_estimated_tract)):
        i,j,k = voxel_list_estimated_tract[s]
        voxel_set_estimated_tract.add((i,j,k))        
    voxel_list_true_tract = streamline_mapping(true_tract, affine=affine).keys()
    
    TP = len(voxel_set_estimated_tract.intersection(set(voxel_list_true_tract)))
    vol_A = len(voxel_set_estimated_tract)
    vol_B = len(set(voxel_list_true_tract))
	FP = vol_B-TP
    FN = vol_A-TP
    sensitivity = float(TP) / float(TP + FN) 
    DSC = 2.0 * float(TP) / float(vol_A + vol_B)
	wDSC = 0 #not possible to compute
	J = float(TP) / float(TP + FN + FP)
    
    return DSC, wDSC, J, sensitivity, TP, FP, FN


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-sub', nargs='?', const=1, default='',
	                    help='Subject ID')
	parser.add_argument('-dir_est', nargs='?',  const=1, default='',
	                    help='Directory of estimated masks')  
	parser.add_argument('-dir_true', nargs='?',  const=1, default='',
	                    help='Directory of ground truth tracts')                        
	args = parser.parse_args()

	#Write results on a file
	results = 'sub-%s_results.csv' %args.sub
	metrics = ['DSC', 'wDSC', 'J', 'sens', 'TP', 'FP', 'FN']
	with open(results, 'a') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(metrics)

	with open('tract_name_list.txt') as f:
		tract_name_list = f.read().splitlines()

	results_matrix = np.zeros((len(tract_name_list), len(metrics)))
	
	for t, tract_name in enumerate(tract_name_list):
		estimated_mask_filename = '%s/%s.nii.gz' %(args.dir_est, tract_name)
		estimated_mask = nib.load(estimated_mask_filename)
		true_tract_filename = '%s/%s_tract.trk' %(args.dir_true, tract_name)
		true_tract = nib.streamlines.load(true_tract_filename)
		true_tract = true_tract.streamlines
		DSC, wDSC, J, sensitivity, TP, FP, FN = compute_dsc_mask_tract(estimated_mask, true_tract)
		print("The DSC of the tract %s is %s" %(tract_name, DSC))
		results_matrix[t] = [DSC, wDSC, J, sensitivity, TP, FP, FN] 
		with open(results, "a") as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(np.float16(results_matrix[t]))
	
	np.save('sub-%s_results' %args.sub, results_matrix)
	sys.exit()    