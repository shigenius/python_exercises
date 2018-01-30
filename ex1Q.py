"""
以下のcalcFrequencyOfText関数を完成させましょう．
mainに記述してあるassertionをすべてクリアし，"The local tests are done."が標準出力されれば完全クリアです．

calcFrequencyOfText関数の仕様:
* 関数の入力 : 英字と記号を含むテキスト(文字列)
* 関数の出力 : 入力テキストの中で，最も出現頻度の高い文字
 * 出力について，文字は"小文字"で返さなければいけません．
* テキストの検索(検査)中，大文字と小文字は区別しません。 "A" と "a"は同じものとしてカウントします．
* 記号．数字．空白はカウントしません．文字だけです．
* もし二文字以上が同じ頻度のときは，アルファベットの順番で一番若い文字を返します．例えば，"ONE"は"o", "n", "e"を各一個ずつ含んでいるので、その中で一番若い"e"が出力されます．

問題は以下のサイトから参考にしました．(丸パクリ)
https://py.checkio.org
"""

def calcFrequencyOfText(text):
    #replace this for solution

    print(text)
    hoge = 'a'

    return hoge


if __name__ == '__main__':
    assert calcFrequencyOfText("Hello World!") == "l", "Hello test"
    assert calcFrequencyOfText("How do you do?") == "o", "O is most wanted"
    assert calcFrequencyOfText("One") == "e", "All letter only once."
    assert calcFrequencyOfText("Oops!") == "o", "Don't forget about lower case."
    assert calcFrequencyOfText("AAaooo!!!!") == "a", "Only letters."
    assert calcFrequencyOfText("abe") == "a", "The First."
    print("Start the long test")
    assert calcFrequencyOfText("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

