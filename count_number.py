import tkinter as tk

root = tk.Tk()
root.title("カウンター")
root.geometry("450x200")

# カウント数を表示するテキストボックス
countTextBox = tk.Entry(width=10)
countTextBox.insert(tk.END, "0")
countTextBox.place(x=140, y=30)
# countTextBox.pack()

# 分数表示用のラベル
slashLabel = tk.Label(text="/")
slashLabel.place(x=220, y=30)

# 総数を表示するテキストボックス
totalTextBox = tk.Entry(width=10)
totalTextBox.place(x=250, y=30)

# 正解数をカウントする処理
def CountNumber():
    currentNumber = int(countTextBox.get()) + 1
    countTextBox.delete(0, tk.END)
    countTextBox.insert(tk.END, currentNumber)

# 正解数をカウントするボタン
countButton = tk.Button(text="カウント", bg="#55c500", fg="white", width=40, height=3, command=CountNumber)
countButton.place(x=80, y=70)

# 正答率を表示するテキストボックス
answerRateTextBox = tk.Entry(width=10)
answerRateTextBox.place(x=220, y=155)

# 正答率を表示する処理
def CalcNumber():
    currentNumber = int(countTextBox.get())
    totalNumber = int(totalTextBox.get())
    answerRate = currentNumber / totalNumber * 100
    answerRateTextBox.delete(0, tk.END)
    answerRateTextBox.insert(tk.END, answerRate)

# 正答率を表示するボタン
calcButton = tk.Button(text="正答率を表示する", width=20, command=CalcNumber)
calcButton.place(x=50, y=150)

# リセットする処理
def Reset():
    countTextBox.delete(0, tk.END)
    totalTextBox.delete(0, tk.END)
    answerRateTextBox.delete(0, tk.END)

# リセットするボタン
resetButton = tk.Button(text="リセット", width=10, command=Reset)
resetButton.place(x=300, y=150)

root.mainloop() 