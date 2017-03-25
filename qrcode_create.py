#coding=utf-8
import qrcode
import sys
import os

reload(sys)
#设置系统默认编码方式，避免中文乱码
sys.setdefaultencoding('utf-8')
#二维码创建
class QrCreate:
	#参数说明：data为需要转换成二维码的数据，img_name为生成的二维码的保存路径（若只有图片名，则默认保存在根目录下）
	def __init__(self,data, img_name):
		self.data = data
		self.img_name = img_name
		
	def create(self):
		#生成的二维码参数设置
		qr = qrcode.QRCode(
			version = 2,	#表示生成二维码的尺寸大小[1,40]
			error_correction = qrcode.constants.ERROR_CORRECT_L,#制定二维码的容错系统L,M,Q,H
			box_size = 5,	#表示每个格子的像素大小
			border = 1	#表示边框的格子厚度是多少（默认为4）
			)
		qr.add_data(self.data)
		qr.make(fit=True)
		img = qr.make_image()
		img.save(self.img_name)
		
if __name__ == '__main__':
	data = raw_input("Please input your QRCode data:").decode('gbk')
	img_name = raw_input("Please input QRCode name:")+".png"
	qr = QrCreate(data, img_name)
	qr.create()
	print "QRCode created successfully!"
	os.system("pause")
