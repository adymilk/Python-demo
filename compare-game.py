#!/user/bin/python3

#————————————————————————————————————————————————————————————————————————
# 知识点：
#	1、随机数
#	2、字符比较
#————————————————————————————————————————————————————————————————————————

import time
import random
import datetime

print('\n\n\n')
print('--------------------------游戏提示----------------------------------\n')

print("这是一个猜数字大小的游戏。\n游戏规则是系统中随机选取一个整数，\n用户通过输入一个数字后，系统会给出一个数字范围，每次用户在系统提示的数字范围内再\n次选取一个数字进行猜测，进而猜中最终的那个数字！\n")
print('--------------------------游戏提示-----------------------------------\n')

ready = input('开始游戏请输入\'yes\' 退出游戏请按任意键：')
if ready == 'yes':
	print('——————————————————————————————————————————————————————————————————————游戏已经开始—————————————————————————————————————————————————————————————————————————\n')
	
	# 获取一个随机整数
	random_num = random.randint(0,100)
	# 记录当前的时间
	start_time = time.time();
	key_status = 0
	count = 0
	max = 100
	min = 0 
	print('请输入一个 0-100 的整数')
	while (key_status == 0):
		print('\n\n')
		user_input = input('请输入：')
		print('\n')
		if (user_input.isdigit() and int(user_input) >= 0 and int(user_input) <= 100):

			if (int(user_input) != random_num):
				if (int(user_input) < random_num):
					print('很遗憾，没猜对哦！给你个提示：' + str(user_input) + ' —— ' + str(max))
					min = int(user_input)					
				else:
					print('很遗憾，没猜对哦！给你个提示：' + str(min) + ' —— ' + str(user_input))
					max = int(user_input)
				print('————————————再试一次———————————————')
				key_status = 0
				count = count + 1
			else:
				print('————————————————————————————————————————猜对啦！———————————————————————————————————————————————————————\n\n')

				print('！！！恭喜你猜中了！！！快去买彩票吧！\n\n')

				print('————————————————————————————————————————猜对啦！———————————————————————————————————————————————————————\n\n')
				end_time = time.time()
				print('游戏总共耗时：',int(end_time - start_time),'秒')
				if int(end_time - start_time) < 8:
					print('游戏总共有效尝试次数：',count + 1,' 次，','击败了全国 95% 的选手')
				elif int(end_time - start_time) >8 and int(end_time - start_time) < 15:
					print('游戏总共有效尝试次数：',count + 1,' 次，','击败了全国 85% 的选手')
				else:
					print('游戏总共有效尝试次数：',count + 1,' 次，','击败了全国 60% 的选手')

				key_status = 1
				print('\n\n游戏结束！')
		else:
			print('输入的数据不合法！请输入一个 0 —— 100 的整数')
else:
	print('您没有输入yes,游戏已经结束！')


