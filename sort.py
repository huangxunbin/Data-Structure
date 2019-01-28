#! usr/bin/env/python
# -*- coding: utf-8-*-
# hb: 2019-01-15 11:02
# @Author H
# @File .py



# Bubble sort

def bubbleSort(myList):
	n = len(myList) #
	if n <=1:
		return  myList
	for i in range(n):
		for j in range(1,n-i):
			print('i= %d,(j-1= %d : myList[j-1] = %d),(j =%d :myList[j] = %d)' % (i,j-1,myList[j-1],j,myList[j]))
			if myList[j-1]> myList[j]:
				myList[j],myList[j-1] = myList[j-1],myList[j]
				print('==数据交换==，交换后结果为：%s' % myList)
		continue
	print('排序结束')
	return myList





#insertSort

def insertSort(myList):
	#遍历列表的下标和对应的值:[6,4,2,1,3,5]  ===>  0,6;1,4....
	for i,item_i in enumerate(myList):
		index = i #遍历下标 i ===>0,1,2,3,4,5
		print('index: %d' % index)
		#i=0 时，index不大于0，不执行while语句
		#i=1时，index>0,myList[index-1]=myList[0]=6,item_i = myList[1]=4；myList[index] = myList[1]= 4,替换，[6，6，2，1，3，5]--- index -1,myList[0]=4 ----[4,6,2,1,3,5]
		while index >0 and myList[index -1]>item_i:
			print('index：%s, myList[index-1]: %s,item_i: %s ' % (index,myList[index-1],item_i))
			myList[index] = myList[index -1] #替换
			print(myList)
			index -=1
			myList[index] = item_i #
			print(myList)
	return myList






def shellSort(alist):
	sublistcount = len(alist)//2
	while sublistcount > 0:

		for startposition in range(sublistcount):
			gapInsertionSort(alist,startposition,sublistcount)

		print("After increments of size",sublistcount,"The list is",alist)

		sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
	for i in range(start+gap,len(alist),gap):

		currentvalue = alist[i]
		position = i

		while position>=gap and alist[position-gap]>currentvalue:
			alist[position]=alist[position-gap]
			position = position-gap

		alist[position]=currentvalue






def mergeSort(alist):
	print(' cut',alist)
	n = len(alist) // 2 #将列表dui
	if n >=1:
		leftPart = alist[:n]
		rightPart = alist[n:]
		#print('leftPart :%s,rightPart: %s' % (leftPart,rightPart))
		mergeSort(leftPart)
		mergeSort(rightPart)

		i= 0
		j= 0
		k= 0
		while i <len(leftPart) and j <len(rightPart):
			if leftPart[i] <rightPart[j]:
				alist[k] = leftPart[i]
				i +=1
			else:
				alist[k] = rightPart[j]
				j +=1
			k +=1
		while i <len(leftPart):
			alist[k] = leftPart[i]
			i +=1
			k +=1
		while j <len(rightPart):
			alist[k] = rightPart[j]
			j +=1
			k +=1
	print('merge',alist)






def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
	'''
	:param alist:需排序列表
	:param first: 列表切分点
	:param last:
	:return:
	'''
	pivotvalue = alist[first]

	leftmark = first+1
	rightmark = last

	done = False
	while not done:

		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1

			if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp


	return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)







if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	mergeSort(alist)

