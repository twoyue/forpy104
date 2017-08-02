from sys import argv  #一个函数包#

script, filename = argv  #拆解定义函数包#

txt = open(filename)  #打开的文件定义为txt#

print "Here's your file %r:" % filename   #提示用户，“这是你的文件”#
print txt.read()  #阅读文件，显示文件内容#

print "Type the filename again:"  #再次输入文件名#
file_again = raw_input("> ")   #定义输入符号#

txt_again = open(file_again)   #文件定义为txt#

print txt_again.read()   #阅读文件，显示文件内容#
