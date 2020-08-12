#coding:utf-8
import pyperclip
title = '廉政追缉令'
result = '#### '+title+'\r\n'
p=1
for n in range(7,21):
    result = result+'- [ ] '+str(p)+'. 【 】【'+str(n)+'-1】\r\n'
    result = result+'- [ ] '+str(p+1)+'. 【 】【'+str(n)+'-2】\r\n'
    result = result+'- [ ] '+str(p+2)+'. 【 】【'+str(n)+'-3】\r\n'
    print(result)
    p = p+3
    pyperclip.copy(result)