age=1
while(age<7):
    print("只有",age,"岁，还不能上学")
    age = age+1
print("可以上学")

companys=["google","baidu","ali","sina"]
# for company in companys:
#     print(company)
#     if company == "google":
#         print("google chrome")
#     elif company == "baidu":
#         print("baidu搜索")
#     else:
#         print("非搜索公司")

for index in range(len(companys)):
    print(companys[index])
    if companys[index] == "google":
        print("google chrome")
    elif companys[index] == "baidu":
        print("baidu搜索")
    else:
        print("非搜索公司")

for i in range(1,10):
    print(i)

for first_number in range(1,10):
    for second_number in range(1,first_number+1):
        print(first_number,"*",second_number,"=",first_number*second_number,end=" ")
    print("\n")
