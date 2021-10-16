import tkinter as tk

class Application(tk.Frame):
    def checkButtonWidget(self, event):
        txt = str(event.widget)
        if txt == '.!frame.!button':
            print('huga')
        elif txt == '.!frame.!button2':
            print('hoge')
        elif txt == '.!frame.!button3':
            print('piyo')

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        AButton = tk.Button(frame, text='A')
        # イベントと関数の実行を紐づける。
        # 第一引数 : イベント内容。button Widgetがクリックされた場合
        # 第二引数 : 第一引数が実行された場合に、呼び出す関数。self.checkButtonWidgetとする。
        # bind関数について : https://kuroro.blog/python/eI5ApJE1wkU7bHsuwk0H/
        AButton.bind("<ButtonPress>", self.checkButtonWidget)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        BButton = tk.Button(frame, text='A')
        # イベントと関数の実行を紐づける。
        # 第一引数 : イベント内容。button Widgetがクリックされた場合
        # 第二引数 : 第一引数が実行された場合に、呼び出す関数。self.checkButtonWidgetとする。
        # bind関数について : https://kuroro.blog/python/eI5ApJE1wkU7bHsuwk0H/
        BButton.bind("<ButtonPress>", self.checkButtonWidget)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        CButton = tk.Button(frame, text='A')
        # イベントと関数の実行を紐づける。
        # 第一引数 : イベント内容。button Widgetがクリックされた場合
        # 第二引数 : 第一引数が実行された場合に、呼び出す関数。self.checkButtonWidgetとする。
        # bind関数について : https://kuroro.blog/python/eI5ApJE1wkU7bHsuwk0H/
        CButton.bind("<ButtonPress>", self.checkButtonWidget)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        AButton.pack()
        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        BButton.pack()
        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        CButton.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
