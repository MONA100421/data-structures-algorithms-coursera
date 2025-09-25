# python3

EPS = 1e-6

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    n = len(a)
    for col in range(n):
        if used_columns[col]:
            continue
        for row in range(n):
            if not used_rows[row] and abs(a[row][col]) > EPS:
                return Position(col, row)
    return None

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot_element):
    n = len(a)
    row = pivot_element.row
    col = pivot_element.column
    div = a[row][col]
    for j in range(col, n):
        a[row][j] /= div
    b[row] /= div
    for i in range(n):
        if i != row:
            factor = a[i][col]
            for j in range(col, n):
                a[i][j] -= factor * a[row][j]
            b[i] -= factor * b[row]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if pivot_element is None:
            break
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b

def PrintColumn(column):
    for x in column:
        print("%.20lf" % x)

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
