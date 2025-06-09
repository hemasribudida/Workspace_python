def analyze_2d_array(arr):
    rows = len(arr)
    cols = len(arr[0])

   
    overall_min = float('inf')
    overall_max = float('-inf')

    for row in arr:
        for num in row:
            if num < overall_min:
                overall_min = num
            if num > overall_max:
                overall_max = num

    row_min = [min(row) for row in arr]
    row_max = [max(row) for row in arr]

    
    column_min = []
    column_max = []

    for col in range(cols):
        column = [arr[row][col] for row in range(rows)]
        column_min.append(min(column))
        column_max.append(max(column))

    print("IN")
    print("Max:", overall_max)
    print("Min:", overall_min)
    print("Col Wise Min:", column_min)
    print("Col Wise Max:", column_max)
    print("Row Wise Max:", row_max)
    print("Row Wise Min:", row_min)
 
arr = [ [1, 0, 1, 2], [3, 4, 5, 5],[6, 7, 8, 8],[9, 0, 1, 9]]


analyze_2d_array(arr)