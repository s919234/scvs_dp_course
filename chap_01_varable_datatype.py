"""
 變數及資料型別
 by 耀民 2020.9
"""
# 變數不用宣告即可使用
# 語法：  變數名稱 = 變數值

c_name ="耀民"   # 字串

ch_score,eng_score = 90,80    # 國文、英文 分別為  90 80   整數
# ch_score = eng_score = 90   # 國文、英文   皆為  90      整數
math_score=80.5  # 小數 、浮點數
score =ch_score+eng_score + math_score     # 數數 + 小數 = 小數
print(score)

del score  # 刪除變數以節省記憶體


# 資料型別：整數、浮點數 均為數值資料，整數不含小數、浮點數含小數
# 浮點數只需加入小數點即可為浮點數
data_type_float = 1.1
data_type_integer =2
# 字串使用 雙引號 或單引號  ，要包含其中一種雙引號或單引號，可在其外包住即可
data_type_string1 = "I'm fine"
data_type_string2 = '小民說"我很好"'
data_type_boolean  = True  # True or False
print(data_type_string1)
print(data_type_string2)

# 觀看其資料型為何
print("float",type(data_type_float))
print("integer",type(data_type_integer))
print("string",type(data_type_string1))
print("boolean",type(data_type_boolean))



""" 常用特殊字元輸入   反斜線+字元
 \' 單引號  \" 雙引號  \\ 反斜線  \n 換行  \t  Tab鍵
"""
escape_character = "大家好！\n歡迎光臨！"    # 歡迎光臨在第2行
print(escape_character)



