#coding=utf-8
import zbar
from PIL import Image
import sys
import threading
import time
import os

reload(sys)
#设置系统默认编码方式，避免中文乱码
sys.setdefaultencoding('utf-8')
#创建MyThread线程类
class MyThread(threading.Thread):
	def __init__(self, func, args):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
	#改写run方法
	def run(self):
		#apply用于间接的调用func函数
		apply(self.func, self.args)
#二维码扫描类
def qr_scan(folder):
	#计算图片数量的全局变量
	global n
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')
	#遍历folder路径下的所有内容，walk返回3个值（路径，路径下的文件夹，路径下的文件）
	for root,dir,files in os.walk(folder):
		#遍历该文件夹下的所有文件
		for file in files:
			#挨个打开二维码图片
			img = Image.open(root+"/"+file).convert('L')
			w, h = img.size
			zimg = zbar.Image(w, h, 'Y800', img.tobytes())
			scanner.scan(zimg)
			n += 1
			for s in zimg:
				#如果不是二维码，这里给出提示
				if not s.data:
					print  "ERROR : "+str(file)+" is not QRcode!\n"
				#否则打印二维码的相关数据
				else:
					print str(file)+":"+s.data.decode('utf-8').encode('gbk')+"\n"

if __name__ == '__main__':
	#创建线程列表
	threads = []
	#创建二维码图片路径列表
	img_folder = []
	for i in range(1,4):
		tmp = raw_input("Please input three QR-image's path (input enter to default),"+str(i)+":")
		if tmp:
			img_folder.append(tmp)
	#如果3次都输入回车，则打开根目录下的文件夹
	if not img_folder:
		img_folder = [r".\half_qrimg",r".\is_qrimg",r".\not_qrimg"]
	
	thread_num = range(len(img_folder))
	#记录开始时间
	start = time.time()
	n = 0
	#创建多线程
	for f in img_folder:
		t = MyThread(qr_scan,(f,))
		threads.append(t)
	#运行线程
	for i in thread_num:
		threads[i].start()
	#阻塞进程直到线程执行完毕
	for i in thread_num:
		threads[i].join()
		
	spend = time.time() - start
	print "总耗时：" + str(spend) + "秒"
	print "共扫描" + str(n) + "张图片"
	os.system("pause")
		