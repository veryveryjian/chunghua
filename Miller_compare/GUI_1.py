import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # Tk 창을 숨깁니다.
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    return file_path

def main():
    inv_file_path = select_file()  # INVOICE 파일 선택
    ir_file_path = select_file()  # IR 파일 선택
    # 여기서 파일 경로를 사용하여 필요한 작업을 수행합니다.
    # 예: 파일 읽기, 데이터 처리 등

if __name__ == "__main__":
    main()
