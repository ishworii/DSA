def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				

if __name__ == "__main__":
	arr = [23,-7,4,56,21]
	print(f"The array before sorting {arr}")
	bubble_sort(arr)
	print(f"The array after sortin {arr}")
