import re

s = '''<div class="animal">
        <p class="name">
            <a title="Tiger"></a>
        </p>
        <p class="content">
            Two tigers two tigers run fast
        </p>
    </div>
    <div class="animal">
        <p class="name">
            <a title="Rabbit"></a>
        </p>
        <p class="content">
            Two Rabbits two Rabbits run fast
        </p>
    </div>
    
'''

pattern = re.compile('<div class="animal">.*?title="(.*?)".*?content">(.*?)</p>', re.S)
res = pattern.findall(s)
print(res)
for r in res:
    print(r[0].strip(), r[1].strip())

#
# #首先去除空白
#
