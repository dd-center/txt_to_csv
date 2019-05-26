# Turn txt danmaku files to csv...
# Created by pren1 5/26/2019

import pdb
import time
import numpy as np
from File_scan import File_scan
from txt_processor import txt_processor
import pandas as pd
import os

def Generate_csv_save_path(single_file_path, output_folder):
	# Generate the output path of csv
	split_list = single_file_path.split('/')
	csv_file_name = os.path.splitext(split_list[2])[0] + ".csv"
	folder_path = output_folder + split_list[1] + "/"
	create_folders(folder_path)
	fin_res = folder_path + csv_file_name
	return fin_res

def create_folders(directory):
	# Create a folder if it does not exist
	if not os.path.exists(directory):
		os.makedirs(directory)

if __name__ == '__main__':
	input_path = "bilibili-vtuber-danmaku-master/"
	output_folder = "bilibili-vtuber-danmaku-CSV/"
	file_scan = File_scan(input_path)
	all_file_paths = file_scan.path_gen()
	Fashion_message_list = []
	for (process_index, single_file_path) in zip(range(len(all_file_paths)), all_file_paths):
		start_time = time.time()
		processor = txt_processor(single_file_path)
		processed_danmaku = processor.read_target_txt()
		target_path = Generate_csv_save_path(single_file_path, output_folder)
		if len(processed_danmaku) == 0:
			continue
		df = pd.DataFrame(processed_danmaku)
		df.columns = ["Time","Uid","danmaku"]
		df.to_csv(target_path)
		print("data {} processed in {}".format(target_path, "--- %s seconds ---" % (time.time() - start_time)))
