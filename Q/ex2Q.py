# classについて
# 定義の仕方, メンバとコンストラクタ(デストラクタ)，インスタンス，インスタンス化
# binding
# 継承 ポリモーフィズム?

# 定義の仕方など最初は理解が難しいのでかんたんなサンプルを与える．
# 自分で調べさせるところとのバランス
# 変数のスコープ，保守性などについて

# ちょっと詳細に書きすぎてるかも

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
    instanceA = SampleClass() # インスタンス化 :
    # "SampleClass"型のオブジェクトが生成される(メモリ領域が確保される)．
    # 同時に生成されたインスタンスは左辺値"instanceA"に紐付けられる．
    # "instanceA"はポインタである．"instanceA"は紐付けられているインスタンスのメモリ領域を参照しているに過ぎないが，pythonにおいてはGCが言語仕様として設計されているため，感覚的には"instanceA"はポインタではなく実インスタンスとして使用することができる．(たぶん)
    instanceA.setVariable(1) # メンバ関数の呼び出し
    print(instanceA.getVariable())


    instanceB = SampleClass(5) # Aとは別のインスタンスをつくってみよう
    instanceB.setVariable(2)
    print(instanceB.getVariable()) # AとBでそれぞれ固有のメンバ変数(v)が保持されている．


    print(instanceA) # オブジェクトの型が出力される


# pythonインタプリタからこのファイルを実行した時に一番初めに以下が実行される．
if __name__ == '__main__':
    main()
