# Created by pren1 at 5/24/2019

import pdb
import numpy as np

# Deal with the strings within txt, count the string frequency
class txt_processor:
	def __init__(self, path_to_txt, target_danmaku_list = []):
		self.path = path_to_txt
		self.target_danmaku_list = target_danmaku_list
		self.txt_list = []

	def read_target_txt(self):
		# Read in target txt into a string list
		if not self.path.endswith('.txt'):
			assert(1==0), file+" extension is not txt"
		with open(self.path, "r") as txtfile:
			data = txtfile.readlines()
		# Remove '\n'
		self.txt_list = [string.rstrip('\n') for string in data]
		# process the readin list with format: [Time, UID, Message]
		self.txt_list = self.preprocess_readin_list()
		# Turn to numpy array...
		self.txt_list = np.asarray(self.txt_list)
		return self.txt_list
	
	def preprocess_readin_list(self):
		# Remove the SPEAKERNUM, and append Time stamp to each message
		new_list = []
		# Avoid bug
		current_time_stamp = 0
		for single_string in self.txt_list:
			if single_string[:4] == 'TIME':
				current_time_stamp = self.Time_to_stamp_number(single_string)
			elif single_string[:10] == 'SPEAKERNUM':
				continue
			else:
				# Find the first occurance of ':'
				sign_pos = single_string.find(':')
				if sign_pos == -1:
					# Assign a fake UID
					UID = 114514
					message = single_string
				else:
					# assert single_string[:sign_pos].isdigit() == True
					if single_string[:sign_pos].isdigit() != True:
						# Assign a fake UID, in this condition, the string itself contains ':', and no UID is provided here
						UID = 114514
						message = single_string
					else:
						UID = int(single_string[:sign_pos])
						message = single_string[sign_pos + 1:]
				new_list.append([current_time_stamp, UID, message])
		return new_list

	def Time_to_stamp_number(self, time_string):
		assert time_string[:4] == 'TIME'
		# First, remove the first four characters: 'TIME'
		time_string = time_string[4:]
		# Then, find the position of the string 'ONLINE'
		end_pos = time_string.find('ONLINE')
		# After that, get the time string we need:
		time_string = time_string[:end_pos].split(':')
		assert len(time_string) == 2
		hour = int(time_string[0])
		minute = int(time_string[1])
		fin_time = hour * 60 + minute
		return fin_time









