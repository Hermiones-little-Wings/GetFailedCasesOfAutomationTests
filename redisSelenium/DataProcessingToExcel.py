import pandas as pd

def DataProcessingToExcel():
    #打开并读取文件
    with open('test_results.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    #删除换行
    data = [line.strip() for line in data]

    for i in data:
        print(i)
    #创建数据库
    df = pd.DataFrame(data, columns=["Test Cases"])

    #存储到excel
    df.to_excel('test_results.xlsx', index=False)
    
    print("保存成功！文件为test_results.xlsx")
