import csv

#开文件
with open('老师.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([
        '魏叔叔', 'Python3'
    ])
    writer.writerow([
        '超叔叔', 'Spider'
    ])
