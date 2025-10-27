with open('test_file/task1_data.txt', mode='r', encoding='utf-8') as f:
    content = f.read()

    for i in content:
        if i.isdigit():
            content = content.replace(i,'')

with open('test_file/task1_answer.txt', mode='w', encoding='utf-8') as f2:
    f2.write(content)
