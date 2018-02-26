PKU体系实习LAB4.1

姓名：张煌昭
学号：1400017707
院系：元培学院
邮箱：zhang_hz@pku.edu.cn

本次LAB4.1，仅与小组内成员讨论思路，其余所有工作均由本人独立完成。

本目录下包括：
	code源代码及可执行文件目录
	report实验报告及数据目录
	README文档

yuv_conv运行方法：
	进入code目录，解压YUV.zip压缩包

	启动qtcreator，载入YUV/yuv_conv/yuv_conv.pro项目，编译后于build-yuv_conv-Desktop_Qt_5_9_2_GCC_64bit-Debug目录下运行；
	或直接进入YUV\build-yuv_conv-Desktop_Qt_5_9_2_GCC_64bit-Debug目录运行，其中已有编译好的可执行文件。
	命令行输入"./yuv_conv"启动并运行程序。

	./yuv_conv <yuv path 1> <yuv path 2> <fade path 1> <fade path 2> <merge path> <SIMD option>

	命令行参数：
		<yuv path 1>，第一个参数，指定第一个YUV420格式图像的路径
		<yuv path 2>，第二个参数，指定第二个YUV420格式图像的路径
		<fade path 1>，第三个参数，指定第一个YUV420图像进行淡入淡出处理后的YUV420格式视频存储的路径
		<fade path 2>，第四个参数，指定第二个YUV420图像进行淡入淡出处理后的YUV420格式视频存储的路径
		<merge path>，第五个参数，指定两个YUV420图像进行重叠渐变处理后的YUV420格式视频存储的路径
		<SIMD option>，第六个参数，指定使用的SIMD选项，“-no”不使用SIMD扩展指令，“-mmx”使用MMX扩展指令，“-sse”使用SSE2扩展指令，“-avx”使用AVX2扩展指令，不进行设置则默认使用-no选项。

	示例：
		"./yuv_conv ./dem1.yuv ./dem2.yuv ./res1.yuv ./res2.yuv ./res.yuv -avx"
		"./yuv_conv ./dem1.yuv ./dem2.yuv ./res1.yuv ./res2.yuv ./res.yuv"