def merge_sort(array):
    print(f"array: {array}")
    if len(array) > 1:
        m = len(array) // 2
        print(f"m: {m}")
        left_half = array[:m]
        right_half = array[m:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        print("Merging...")
        print(f"left: {left_half}")
        print(f"right: {right_half}")

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

        print(f"merged: {array}")

# ✅ Esto es lo que cambiamos: quitamos el end=' ' para que coincida con el formato esperado
print("Enter numbers, separated by ','")
input_str = input()
input_list = input_str.split(',')
print(f"input_list: {input_list}")
value_list = list(map(int, input_list))
print(f"value_list: {value_list}")

merge_sort(value_list)
print(value_list)