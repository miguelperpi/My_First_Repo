def merge_sort(array):
    if len(array) > 1:
        m = len(array) // 2
        left = array[:m]
        right = array[m:]

        print(f"array: {array}")  # <-- Muestra el array actual
        print(f"m: {m}")          # <-- Muestra el punto de división

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        print(f"Merging...")      # <-- Muestra que se está fusionando
        print(f"left: {left}")   # <-- Muestra la parte izquierda
        print(f"right: {right}") # <-- Muestra la parte derecha
        print(f"merged: {array}") # <-- Muestra el array fusionado

if __name__ == "__main__":
    input_list = input("Enter numbers, separated by ',': ").split(',')
    value_list = [int(x) for x in input_list]
    merge_sort(value_list)
    print(value_list)
