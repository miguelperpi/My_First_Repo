def mergesort(arr, depth=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Mensajes de depuración (como en el ejemplo)
        print(f"{'  ' * depth}m: {mid}")
        print(f"{'  ' * depth}array: {left}")
        mergesort(left, depth + 1)
        print(f"{'  ' * depth}array: {right}")
        mergesort(right, depth + 1)

        i = j = k = 0

        # Proceso de mezcla
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

        # Mensaje de mezcla
        print(f"{'  ' * depth}Merging...")
        print(f"{'  ' * depth}left: {left}")
        print(f"{'  ' * depth}right: {right}")
        print(f"{'  ' * depth}merged: {arr}")

# Entrada de datos
input_str = input("Enter numbers, separated by ',': ")
input_list = [x.strip() for x in input_str.split(',')]
value_list = [int(x) for x in input_list]
array = value_list.copy()

# Imprimir información inicial (como en el ejemplo)
print(f"Enter numbers, separated by ',': input_list: {input_list}")
print(f"value_list: {value_list}")
print(f"array: {array}")

# Llamar a mergesort
mergesort(array)

# Imprimir resultado final
print(array)
