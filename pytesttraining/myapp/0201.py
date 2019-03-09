a=10
print(type(a))
var1="15"
print(type(var1))
var2 = int(var1)
print(type(var2))
a=[1,2,3]
b=tuple(a)
print(b)
c=(("name","lili"),("age","18"))
d=dict(c)
print(d)

#字符串拼接
str1 = "hello testing"
str2 = "home"
str3 = str1 + str2
print(str3)

#字符串复制
print("*"*10)

#字符串拆分，split
path = "C:\ProgramData\Oracle\Java\javapath;" \
       "%SystemRoot%\system32;" \
       "%SystemRoot%;" \
       "%SystemRoot%\System32\Wbem;" \
       "%SYSTEMROOT%\System32\WindowsPowerShell\\v1.0\;" \
       "%JAVA_HOME%\\bin;%JRE_HOME%\\bin;" \
       "D:\software\\android-sdk-windows\platform-tools;" \
       "D:\software\\android-sdk-windows\\tools;" \
       "C:\Program Files\\nodejs\;" \
       "D:\TortoiseGit\\bin;" \
       "D:\Git\cmd;%ANDROID_HOME%\\tools;%ANDROID_HOME%\platform-tools;" \
       "D:\software\\apache-ant-1.10.4-bin\\apache-ant-1.10.4\\bin;" \
       "D:\python3.7;" \
       "D:\python3.7\Scripts;" \
       "D:\software\\apache-maven-3.5.4\\bin;" \
       "%ANDROID_HOME%\\build-tools\\28.0.0;" \
       "D:\python3.7\Lib\site-packages\\allure\\allure-2.7.0\\bin;"
for item in path.split(";"):
    print(item)

#字符串拆分，split
str4 = "litter star testing home"
list = str4.split()
print(list[-2:])

#字符串替换，replace
str5 = "I love Python"
print(str5.replace("Python","Java"))

print(str5.lower())
print(str5.upper())


