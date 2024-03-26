import tkinter as tk
from tkinter import filedialog


def select_file():
    root = tk.Tk()
    root.withdraw()  # 기본 Tk 창을 숨김
    file_path = filedialog.askopenfilename()  # 파일 선택 대화 상자 열기
    print("Selected file:", file_path)
    return file_path


def main():
    print("Select INVOICE file")
    inv_file_path = select_file()  # INVOICE 파일 선택

    print("Select IR file")
    ir_file_path = select_file()  # IR 파일 선택

    # 선택된 파일 경로를 사용하여 작업 수행
    # 예: 파일 처리, 데이터 분석 등


if __name__ == "__main__":
    main()
