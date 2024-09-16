import numpy as np
from pathlib import Path
import os
import re
import time

folder_path = Path(__file__).parent / "bad_apple_frames(60fps)"
folder = []
strings = ['.', '~', '=', '+', '*', ';', '/', 'k', '!', 'f', 'J', '#', '%', '$', '&', '0']

os.system('cls' if os.name == 'nt' else 'clear')

# 收集所有 .npz 文件
for file in os.listdir(folder_path):
    if file.endswith(".npz"):
        folder.append(file)

# 定義一個函數來提取檔案名中的數字部分並轉換為整數
def extract_number(file_name):
    match = re.search(r'\d+', file_name)
    return int(match.group()) if match else -1

# 根據提取的數字對文件名進行排序
folder.sort(key=extract_number)

# 按照排序後的順序處理文件
for file in folder:
    npz_file = np.load(folder_path / file)
    frames = npz_file['frames']

    for frame in frames:
        s = ''
        t = time.time()

        for row in frame:
            for pixel in row:
                s += strings[pixel // 16]

            s += '\n'

        print(f"\033[H{s.strip()}", end='', flush=True)

        while time.time() - t < 1/60:
            pass