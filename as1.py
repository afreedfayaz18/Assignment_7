try:
	print("open a resource")
	a=5
	print("a=",a)
	b=0
	print("b=",b)
	c=a/b
	print(c)
	print("succesfull")
except Exception as e:
	print("zero division not possible",e)
finally:
	print("closed resource")