#定义函数 奶酪和小饼干#
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
	
#第一次赋值给函数#
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#先将数字赋值给变量，再赋值给函数#
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#将加法算式赋值给函数#
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#将数字和变量相加赋值给函数#
print  "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
