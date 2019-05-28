import re

html = '''
    <div><p>九霄龙吟惊天变</p></div>
    <div><p>风云际会浅水游</p></div>
    <div><p>金陵岂是池中物</p></div>
    <div><p>一遇风云变化龙</p></div>
'''
pattern = re.compile('<div><p>(.*?)</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)
