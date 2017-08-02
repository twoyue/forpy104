from sys import argv
#定义函数#

script,filename = argv
#函数包含两个变量#
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#清除同名文件中的内容#
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#正在打开文件#
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#三行信息分别输入#
print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#输入三行文件（还有回车）#
print"And finally, we close it."
target.close()
