def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Entrada de datos
input_list = input("Enter numbers, separated by ',': ").split(',')
value_list = [int(x) for x in input_list]
array = value_list.copy()

# Ordenar el array
mergesort(array)

# Imprimir la salida esperada
print(f"Enter numbers, separated by ',': input_list: {input_list}")
print(f"value_list: {value_list}")
print(f"array: {array}")