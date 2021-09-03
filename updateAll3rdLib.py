import subprocess

# pip显示需要更新的python列表
com_list_o = 'pip list -o' 
# 执行命令并返回结果
p = subprocess.Popen(com_list_o, shell=True, stdout=subprocess.PIPE)
# 取命令返回结果，结果是一个二进制字符串，包含了我们上面执行pip list -o后展现的所有内容
out = p.communicate()[0]
# 二进制转utf-8字符串
out = str(out, 'utf-8')

# 切出待升级的包名, 并存入列表
need_update = []
for i in out.splitlines()[2:]:
    need_update.append(i.split(' ')[0])

# 执行升级命令，每次取一个包进行升级，pip只支持一个包一个包的升级
for nu in need_update:
    com_update = 'pip install -U {py}'.format(py=nu)
    print("执行命令:", com_update)
    subprocess.call(com_update)
    print("----------{com} 执行结束-----------\n".format(com=com_update))


print("检查更新情况:")
subprocess.call(com_list_o)