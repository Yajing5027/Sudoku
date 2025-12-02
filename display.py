# display.py: 负责显示数独板和保存结果，不依赖外部模块

class Sudoku:
    # Sudoku类：负责显示板和保存结果
    def __init__(self):
        # 初始化Sudoku实例（目前无需额外设置）
        pass

    def display_board(self, board, original_board=None):
        # 显示数独板：打印行号、列号，用户输入用[ ]包围（如果original_board提供）
        size = len(board)  # 获取板的大小
        print("   " + " ".join("C" + str(i+1) for i in range(size)))  # 打印列标题
        for i in range(size):
            row_str = "R" + str(i+1) + " "  # 构建行字符串
            for j in range(size):
                value = board[i][j]
                if value == 0:
                    row_str += "_  "  # 空位显示_
                else:
                    if original_board and original_board[i][j] == 0:
                        row_str += "[" + str(value) + "] "  # 用户输入用[ ]
                    else:
                        row_str += str(value) + "  "  # 原始数字正常显示
            print(row_str)  # 打印整行

    def save_to_file(self, board, filename):
        # 保存板到文件：每行一个CSV格式的行
        with open(filename, 'w') as f:
            for row in board:
                f.write(','.join(map(str, row)) + '\n')  # 将行转换为逗号分隔字符串
