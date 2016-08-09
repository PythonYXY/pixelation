# -*- coding:utf-8 -*-

from PIL import Image
from functools import reduce
import os

INF = 100000
thumnail_height = 15
main_pic_length = 2520
main_pic_height = 3510
num_i = int(main_pic_length / thumnail_height)
num_j = int(main_pic_height / thumnail_height)
main_val = dict()
which_pic = dict()
base_dir = os.path.abspath('.')

def cal_main_pic_val(l, im):
	global main_val
	for i in range(1, num_i + 1):
		for j in range(1, num_j + 1):
			longt = thumnail_height * (j - 1)

			total_val = 0
			for k in range(longt, longt + thumnail_height):
				lat = k * main_pic_length + (i - 1) * thumnail_height
				for v in range(lat, lat + thumnail_height):
					total_val += l[v]

			main_val[(i, j)] = int(total_val / (thumnail_height * thumnail_height))


def Search(val, temp_list):
	dis = INF
	res = -1
	for i in range(len(temp_list)):
		if abs(val - temp_list[i]) < dis:
			res = i
			dis = abs(val - temp_list[i])

	return res

def choose_pic():
	temp_list = []
	with open('thumnail_data.txt', 'r') as f:
		for item in f.readlines():
			temp_list.append(int(item))

	for i in range(1, num_i + 1):
		for j in range(1, num_j + 1):
			val = main_val[(i, j)]
			which_pic[(i, j)] = Search(val, temp_list)


if __name__ == '__main__':
	im = Image.open('main_pic.jpg').convert('L')
	l = list(im.getdata())
	print('List generated!')
	for i in range(10):
		l.append(0)

	cal_main_pic_val(l, im)
	choose_pic()
	
	toImage = Image.new('RGBA', (main_pic_length, main_pic_height))
	for i in range(1, num_i + 1):
		for j in range(1, num_j + 1):
			thumnail_dir = os.path.join(base_dir, 'thumnail')
			fname = '%s.jpg' % which_pic[(i, j)]
			fpath = os.path.join(thumnail_dir, fname)
			fromImage = Image.open(fpath)
			toImage.paste(fromImage, ((i - 1) * thumnail_height, (j - 1) * thumnail_height))

	toImage.save('result.jpg')