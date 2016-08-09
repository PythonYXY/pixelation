# -*- coding:utf-8 -*-

from PIL import Image
from functools import reduce
import os

base_dir = os.path.abspath('.')
candidates_path = os.path.join(base_dir, 'candidates')
thumnail_path = os.path.join(base_dir, 'thumnail')
counter = 0

def cal_avg(im):
	global counter
	im = im.resize((15, 15), Image.ANTIALIAS).convert('L')
	im.save(os.path.join(thumnail_path, '%s.jpg' % counter) )
	counter += 1
	return int(reduce(lambda x, y: x + y, list(im.getdata()) ) / 225)


if __name__ == '__main__':
	if os.path.exists('thumnail_data.txt'):
			os.remove('thumnail_data.txt')
	for i in os.listdir(candidates_path):
		im = Image.open(os.path.join(candidates_path, i))
		with open('thumnail_data.txt', 'a') as f:
			f.write('%s\n' % cal_avg(im))
			print('%s complete!'% i)
