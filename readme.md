*	#qrcode_creare.py
	这是一个二维码生成程序，用户通过输入字符串（支持中英文，数字，符号）
	和图片的路径（包括图片名称），即可实现在相应的路径下生成对应的二维码
	如果第二次输入的是图片的名字，则会在根目录下生成改二维码图片
	
*	#qrcode_scan.py
	这个一个二维码扫描程序，直接输入需要扫描的二维码的路径（包括二维码名
	称）就可以扫描出该二维码的数据。
	如果输入的是二维码图片的名字，则要求改二维码必须和程序处于同一目录下
	
*	#mutithread_qrcode_scanner.py
	这是一个多线程（默认为3个）的二维码扫描程序，可实现同时扫描多个个文件夹内的二
	维码图片数据。
	'half_qrimg','is_qrimg','not_qrimg'这三个是默认扫描的文件夹