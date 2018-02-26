PKU体系实习LAB3.2

姓名：张煌昭
学号：1400017707
院系：元培学院
邮箱：zhang_hz@pku.edu.cn

本次LAB3.2，仅与小组内成员讨论思路，其余所有工作均由本人独立完成。

本目录下包括：
	code源代码及可执行文件目录
	report实验报告及数据目录
	reference参考文献
	README文档

Cache-sim运行方法：
	进入code目录，解压cache.zip压缩包

	启动qtcreator，载入cache/cache-sim/cache-sim.pro项目，编译后于build-cache-sim-Desktop_Qt_5_9_2_GCC_64bit-Debug目录下运行；
	或直接进入cache\build-cache-sim-Desktop_Qt_5_9_2_GCC_64bit-Debug目录运行，其中已有编译好的可执行文件。
	命令行输入"./cache-sim"启动并运行程序。

	命令行参数：
		-trace=，指定trace文件路径
		-iter=，指定trace运行的轮数
		-defaultconfig，使用未经优化的默认配置的Cache，不设置该选项则默认使用优化过的Cache

	示例：
		"./cache-sim -trace=./1.trace -iter=100 -defaultconfig"
		"./cache-sim -trace=./2.trace -iter=100"