# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:38:02 2019

@author: S.S.HARI
"""
import os
import argparse
import sys
from crop import crop_image
from saliency_create import saliency

saliency_folder = "./saliency_output"
cropped_folder = "./cropped_output"

def main(args):
    
    if not os.path.exists(cropped_folder):
        os.mkdir(cropped_folder)
	
    if not os.path.exists(saliency_folder):
        os.mkdir(saliency_folder)	
        
    if args.rgb_folder:
        rgb_pths = os.listdir(args.rgb_folder)
        for rgb_pth in rgb_pths:
            saliency(args.rgb_folder,rgb_pth)
            crop_image(args.rgb_folder,rgb_pth)
			#print(os.path.join(args.rgb_folder,rgb_pth))

    else:
        saliency(None,args.rgb)
        crop_image(None,args.rgb)
        #print(args.rgb)

def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--rgb', type=str,
		help='input rgb',default = None)
	parser.add_argument('--rgb_folder', type=str,
		help='input rgb',default = None)
	parser.add_argument('--gpu_fraction', type=float,
		help='how much gpu is needed, usually 4G is enough',default = 1.0)
	return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
