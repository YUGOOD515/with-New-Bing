# 导入 tkinter 库
import tkinter as tk
# 导入 random 库
import random

# 定义一些常量
SIZE = 4 # 网格的大小
SIDE = 100 # 方块的边长
MARGIN = 10 # 网格的边距
FONT = ("Verdana", 40, "bold") # 方块的字体
BACKGROUND_COLOR = "#92877d" # 背景颜色
EMPTY_COLOR = "#9e948a" # 空方块的颜色
COLORS = { # 不同数字方块的颜色
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}

# 定义一个函数，用于创建一个空的网格
def create_grid():
    grid = []
    for i in range(SIZE):
        row = [0] * SIZE
        grid.append(row)
    return grid

# 定义一个函数，用于在网格中随机添加一个数字（2 或者 4）
def add_number(grid):
    empty_cells = [] # 存储空方块的位置
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
    if empty_cells: # 如果有空方块
        i, j = random.choice(empty_cells) # 随机选择一个位置
        grid[i][j] = random.choice([2, 4]) # 随机选择一个数字

# 定义一个函数，用于判断网格是否已满（没有空方块）
def is_full(grid):
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == 0:
                return False
    return True

# 定义一个函数，用于判断网格是否可以移动（有相邻的相同数字）
def can_move(grid):
    for i in range(SIZE):
        for j in range(SIZE - 1):
            if grid[i][j] == grid[i][j + 1]: # 水平方向有相同数字
                return True
            if grid[j][i] == grid[j + 1][i]: # 垂直方向有相同数字
                return True
    return False

# 定义一个函数，用于移动网格（根据方向键）
def move_grid(grid, direction):
    moved = False # 记录是否移动过
    merged = [] # 记录哪些位置已经合并过

    if direction == "Up": # 向上移动
        for j in range(SIZE): # 对每一列进行操作
            for i in range(1, SIZE): # 对每一行进行操作，从第二行开始
                if grid[i][j] != 0: # 如果当前方块不为空
                    k = i - 1 # 找到上面的方块位置
                    while k >= 0 and grid
                        [k][j] == 0: # 如果上面的方块为空
                        k -= 1 # 继续向上找
                    if k == -1: # 如果到了最上面
                        grid[0][j] = grid[i][j] # 把当前方块移到最上面
                        grid[i][j] = 0 # 把当前方块置空
                        moved = True # 标记为移动过
                    elif grid[k][j] == grid[i][j] and (k, j) not in merged: # 如果上面的方块和当前方块相同，并且没有合并过
                        grid[k][j] *= 2 # 把上面的方块乘以 2
                        grid[i][j] = 0 # 把当前方块置空
                        merged.append((k, j)) # 把上面的方块位置加入到合并过的列表中
                        moved = True # 标记为移动过
                    elif k + 1 != i: # 如果上面的方块和当前方块不同，并且中间有空隙
                        grid[k + 1][j] = grid[i][j] # 把当前方块移到上面的空隙处
                        grid[i][j] = 0 # 把当前方块置空
                        moved = True # 标记为移动过

    elif direction == "Down": # 向下移动，逻辑类似，不再赘述
        for j in range(SIZE):
            for i in range(SIZE - 2, -1, -1):
                if grid[i][j] != 0:
                    k = i + 1
                    while k < SIZE and grid[k][j] == 0:
                        k += 1
                    if k == SIZE:
                        grid[SIZE - 1][j] = grid[i][j]
                        grid[i][j] = 0
                        moved = True
                    elif grid[k][j] == grid[i][j] and (k, j) not in merged:
                        grid[k][j] *= 2
                        grid[i][j] = 0
                        merged.append((k, j))
                        moved = True
                    elif k - 1 != i:
                        grid[k - 1][j] = grid[i][j]
                        grid[i][j] = 0
                        moved = True

    elif direction == "Left": # 向左移动，逻辑类似，不再赘述
        for i in range(SIZE):
            for j in range(1, SIZE):
                if grid[i][j] != 0:
                    k = j - 1
                    while k >= 0 and grid[i][k] == 0:
                        k -= 1
                    if k == -1:
                        grid[i][0] = grid[i][j]
                        grid[i][j] = 0
                        moved = True
                    elif grid[i][k] == grid[i][j] and (i, k) not in merged:
                        grid[i][k] *= 2
                        grid[i][j] = 0
                        merged.append((i, k))
                        moved = True
                    elif k + 1 != j:
                        grid[i][k + 1] = grid[i][j]
                        grid[i][j] = 0
                        moved = True

    elif direction == "Right": # 向右移动，逻辑类似，不再赘述
        for i in range(SIZE):
            for j in range(SIZE - 2, -1, -1):
                if grid[i][j] != 0:
                    k = j + 1
                    while k < SIZE and grid[i][k] == 0:
                        k += 1
                    if k == SIZE:
                        grid[i][SIZE - 1] = grid[i][j]
                        grid[i][j] = 0
                        moved = True
                    elif grid[i][k] == grid[i][j] and (i, k) not in merged:
                        grid[i][k] *= 2
                        grid[i][j] = 0
                        merged.append((i, k))
                        moved = True
                    elif k - 1 != j:
                        grid[i][k - 1] = grid[i][j]
                        grid[i][j] = 0
                        moved = True

    return grid, moved # 返回移动后的网格和是否移动过的标志

# 定义一个类，用于创建游戏界面
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self) # 调用父类的构造函数
        self.grid() # 设置网格布局
        self.master.title("2048") # 设置窗口标题
        self.master.bind("<Key>", self.key_press) # 绑定按键事件
        self.commands = { # 定义方向键对应的命令
            "Up": "Up",
            "Down": "Down",
            "Left": "Left",
            "Right": "Right"
        }
        self.grid_cells = [] # 存储方块的标签
        self.init_grid() # 初始化网格
        self.init_matrix() # 初始化矩阵
        self.update_grid_cells() # 更新方块的显示
        self.mainloop() # 进入主循环

    def init_grid(self):
        # 创建一个背景框架，设置大小和颜色
        background = tk.Frame(self, bg=BACKGROUND_COLOR, width=SIZE * SIDE + 2 * MARGIN, height=SIZE * SIDE + 2 * MARGIN)
        background.grid()
        for i in range(SIZE): # 对每一行进行操作
            row = [] # 存储当前行的方块标签
            for j in range(SIZE): # 对每一列进行操作
                # 创建一个方块标签，设置大小、颜色、字体和居中对齐
                cell = tk.Label(background, bg=EMPTY_COLOR, justify=tk.CENTER, font=FONT, width=4, height=2)
                # 设置方块标签在背景框架中的位置和边距
                cell.grid(row=i, column=j, padx=MARGIN / 2, pady=MARGIN / 2)
                row.append(cell) # 把方块标签加入到当前行中
            self.grid_cells.append(row) # 把当前行加入到网格中

    def init_matrix(self):
        # 创建一个空的矩阵，用于存储数字
        self.matrix = create_grid()
        # 在矩阵中随机添加两个数字（2 或者 4）
        add_number(self.matrix)
        add_number(self.matrix)

    def update_grid_cells(self):
        for i in range(SIZE): # 对每一行进行操作
            for j in range(SIZE): # 对每一列进行操作
                if self.matrix[i][j] == 0: # 如果当前位置是空的
                    self.grid_cells[i][j].configure(text="", bg=EMPTY_COLOR) # 设置方块标签为空白和空颜色
                else: # 如果当前位置不是空的
                    number = self.matrix[i][j] # 获取当前位置的数字
                    color = COLORS[number] if number in COLORS else "#ff0000" # 获取当前数字对应的颜色，如果没有则用红色表示
                    self.grid_cells[i][j].configure(text=str(number), bg=color) # 设置方块标签为数字和颜色

    def key_press(self, event):
        key = event.keysym # 获取按键的符号
        if key in self.commands: # 如果按键是方向键之一
            direction = self.commands[key] # 获取对应的命令
            self.matrix, moved = move_grid(self.matrix, direction) # 移动矩阵，并获取是否移动过的标志
            if moved: # 如果移动过了
                add_number(self.matrix) # 在矩阵中随机添加一个数字（2 或者 4）
                self.update_grid_cells() # 更新方块的显示
                if is_full(self.matrix) and not can_move(self.matrix): # 如果矩阵已