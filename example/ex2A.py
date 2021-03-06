"""
classの概念の理解，また使い方について学びましょう．
以下に定義してあるclass SampleClass と関数main()はサンプルコードです．コメントを入れていますので参考にしてください．

問題:
* 名簿を表現するclassを作成しましょう．
* 名簿クラスの仕様:
  * 出席番号と生徒の名前をペアにした配列をメンバ変数として持つ．(配列表現は何を使ってもok)
  * 名簿に生徒を追加，削除，指定した出席版号の生徒の名前を出力する，名簿に記載してある生徒をすべて出力する，すべての要素を削除するといった機能をそれぞれ持つ．

* 作成したクラスは関数mainB()でインスタンス化して，各機能がきちんと動くかどうか確認しましょう．
"""

class SampleClass:
    def __init__(self, v=0): # コンストラクタ(イニシャライザ) : インスタンスが作られる際に呼ばれる関数．
        self.v = v 
        # メンバ変数v. 
        # selfはpython独自の書き方で，自分自身のオブジェクトを表す．
        # つまり"self.v"は"SampleClass"型オブジェクト(≒インスタンス)が持つ"v"というメンバ変数を表す．

    def setVariable(self, v): # メンバ関数
        self.v = v

    def getVariable(self):
        return self.v

def main():
    a = SampleClass() # インスタンス化 :
    # "SampleClass"型のオブジェクトが生成される(メモリ領域が確保される)．
    # 同時に生成されたインスタンスは左辺値"a"に紐付けられる．
    # "a"はポインタである．"a"は紐付けられているインスタンスのメモリ領域を参照しているに過ぎないが，pythonにおいてはGCが言語仕様として設計されているため，感覚的には"a"はポインタではなく実インスタンスとして使用することができる．(たぶん)
    a.setVariable(1) # メンバ関数の呼び出し
    print("a.getVariable():", a.getVariable())


    b = SampleClass(5) # aとは別のインスタンスをつくってみよう
    b.setVariable(2)
    print("b.getVariable():", b.getVariable()) # aとbでそれぞれ固有のメンバ変数(v)が保持されている．

    c = a # cはaと同じオブジェクトを参照する．

    print("c.getVariable():", c.getVariable())
    c.setVariable(3)
    print("c.getVariable():", c.getVariable())
    print("a.getVariable():", a.getVariable())

    print("a:", a) # オブジェクトの型が出力される
    print("c:", c) # aと同じアドレスを指している

    del c
    del a
    # オブジェクトを参照するポインタがすべて削除された時(明示的に削除を宣言(pythonであればdel構文)しなくても変数のスコープなどによって削除される)，参照先のオブジェクトのメモリ領域も解放される．

class StudentDict:
    def __init__(self):
        self.dict = {}

    def add(self, input):
        self.dict.update(input)

    def delete(self, id):
        self.dict.pop(id)

    def getStudentName(self, id):
        return self.dict[id]

    def getAllStudentInfo(self):
        return self.dict

    def clear(self):
        self.dict.clear()

def mainB():
    l = StudentDict()
    l.add({1:"shige", 2:"hoge", 3:"fuga"})
    l.add({4:"puri"})
    print(l.getAllStudentInfo())
    print(l.getStudentName(1))
    print(l.getAllStudentInfo())

    l.delete(1)
    print(l.getAllStudentInfo())

    l.clear()
    print(l.getAllStudentInfo())


# pythonインタプリタからこのファイルを実行した時に一番初めに以下が実行される．
if __name__ == '__main__':
    #main()
    mainB()