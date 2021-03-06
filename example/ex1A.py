# aim :リストオブジェクトの扱いといった基本的なpython文法の習得，文字列操作，アルゴリズムの想像，テスト

def calcFrequencyOfText(text):

    #replace this for solution
    
    lowerd_text = text.lower()

    #chara_dict = {chara:lowerd_text.count(chara) for chara in lowerd_text if chara.isalpha()}
    # {c: text.count(c) for c in set(text)}
    # {c: sum(1 for x in lowerd_text if x == c) for c in set(lowerd_text)} # 頻度

    # another solution
    chara_dict = {}
    for chara in text.lower():
        if chara.isalpha():
            chara_dict[chara] = chara_dict[chara]+1 if chara in chara_dict else 1
    
    print(chara_dict)
    
    # get max value and key
    max_val = max(chara_dict.values())
    keys_of_max_val = [key for key in chara_dict if chara_dict[key] == max_val]
    print(keys_of_max_val)
    
    return sorted(keys_of_max_val)[0]

            
        

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

