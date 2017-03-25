#coding=utf-8
import zbar
from PIL import Image
import sys
import threading
import time
import os

reload(sys)
#����ϵͳĬ�ϱ��뷽ʽ��������������
sys.setdefaultencoding('utf-8')
#����MyThread�߳���
class MyThread(threading.Thread):
	def __init__(self, func, args):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
	#��дrun����
	def run(self):
		#apply���ڼ�ӵĵ���func����
		apply(self.func, self.args)
#��ά��ɨ����
def qr_scan(folder):
	#����ͼƬ������ȫ�ֱ���
	global n
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')
	#����folder·���µ��������ݣ�walk����3��ֵ��·����·���µ��ļ��У�·���µ��ļ���
	for root,dir,files in os.walk(folder):
		#�������ļ����µ������ļ�
		for file in files:
			#�����򿪶�ά��ͼƬ
			img = Image.open(root+"/"+file).convert('L')
			w, h = img.size
			zimg = zbar.Image(w, h, 'Y800', img.tobytes())
			scanner.scan(zimg)
			n += 1
			for s in zimg:
				#������Ƕ�ά�룬���������ʾ
				if not s.data:
					print  "ERROR : "+str(file)+" is not QRcode!\n"
				#�����ӡ��ά����������
				else:
					print str(file)+":"+s.data.decode('utf-8').encode('gbk')+"\n"

if __name__ == '__main__':
	#�����߳��б�
	threads = []
	#������ά��ͼƬ·���б�
	img_folder = []
	for i in range(1,4):
		tmp = raw_input("Please input three QR-image's path (input enter to default),"+str(i)+":")
		if tmp:
			img_folder.append(tmp)
	#���3�ζ�����س�����򿪸�Ŀ¼�µ��ļ���
	if not img_folder:
		img_folder = [r".\half_qrimg",r".\is_qrimg",r".\not_qrimg"]
	
	thread_num = range(len(img_folder))
	#��¼��ʼʱ��
	start = time.time()
	n = 0
	#�������߳�
	for f in img_folder:
		t = MyThread(qr_scan,(f,))
		threads.append(t)
	#�����߳�
	for i in thread_num:
		threads[i].start()
	#��������ֱ���߳�ִ�����
	for i in thread_num:
		threads[i].join()
		
	spend = time.time() - start
	print "�ܺ�ʱ��" + str(spend) + "��"
	print "��ɨ��" + str(n) + "��ͼƬ"
	os.system("pause")
		