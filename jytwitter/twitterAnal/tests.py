

# Create your tests here.

a = {
    '김밥' : 30,
    '초밥' : 25,
    '유부' : 58,
    '곤니찌와' : 100,
    '탕수' : 12
}

list_menu = list(a)
for i in range(len(list_menu)):
    for j in range(len(list_menu)):
        if a[list_menu[i]] > a[list_menu[j]]:
            tmp = list_menu[j]
            list_menu[j] = list_menu[i]
            list_menu[i] = tmp

for menu in list_menu:
    print(a[menu], menu)