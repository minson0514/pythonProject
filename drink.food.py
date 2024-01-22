'''
import random
drinks_food = {"위스키": "초콜릿", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}
#drink = input(drinks_food.keys())
drinks_food_keys = list(drinks_food)
#print(drinks_food_keys)
#print(random.choice(drinks_food_keys)) #key 중에서 random하게 choice
while True:
    menu = input(f'다음 술 중에 고르세요.\n1. {drinks_food_keys[0]}\n2. {drinks_food_keys[1]}\n3. {drinks_food_keys[2]}\n4. {drinks_food_keys[3]}\n5. 종료\nenter here: ')
    menu = input(f'다음 술 중에 고르세요.\n1. {drinks_food_keys[0]}\n2. {drinks_food_keys[1]}\n3. {drinks_food_keys[2]}\n4. {drinks_food_keys[3]}\n5. 랜덤 추천\n6. 종료\nenter here: ')
    if menu == '1':
        print(f'{drinks_food_keys[0]}에 어울리는 안주는 {drinks_food[drinks_food_keys[0]]} 입니다.')
    elif menu == '2':
@@ -12,6 +16,60 @@
        print(f'{drinks_food_keys[2]}에 어울리는 안주는 {drinks_food[drinks_food_keys[2]]} 입니다.')
    elif menu == '4':
        print(f'{drinks_food_keys[3]}에 어울리는 안주는 {drinks_food[drinks_food_keys[3]]} 입니다.')
    elif menu == '5':
        random_drink = random.choice(drinks_food_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_food[random_drink]} 입니다.')
    else:
        print(f'다음에 또 오세요')
        break
'''

#combine dictionaries with {**a, **b}
#-> shallow copies(mutable list를 쉐어받음 -> origin & main 다 바뀜)
#combine dictionaries with update


import random
drinks_food = {"위스키": "초콜릿", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}

'''
print(drinks_food)
print(drinks_food.pop("고량주"))
print(drinks_food)
'''

#del drinks_food["위스키"] #위스키 지우면 3번방이 비었다는 에러 생김 IndexError: list index out of range -> [3]을 지우거나 변경해야함
#drinks_food["사케"] = "고등어봉초밥"
#drink = input(drinks_food.keys())
japan_drinks_foods = {"사케" : "광어회", "위스키": "낙곱새"}
drinks_food.update(japan_drinks_foods) #update 했기 때문에 초콜릿이 아니라 낙곱새가 나옴

drinks_food_keys = list(drinks_food)
'''
print(drinks_food_keys)
print(drinks_food.remove("위스키")) #AttributeError: 'dict' object has no attribute 'remove'
print(drinks_food_keys)
'''

#print(drinks_food_keys)
#print(random.choice(drinks_food_keys)) #key 중에서 random하게 choice

while True:
    menu = input(f'다음 술 중에 고르세요.\n1. {drinks_food_keys[0]}\n2. {drinks_food_keys[1]}\n3. {drinks_food_keys[2]}\n'
                 f'4. {drinks_food_keys[3]}\n5. {drinks_food_keys[4]}\n6. 랜덤 추천\n7. 종료\nenter here: ')
    if menu == '1':
        print(f'{drinks_food_keys[0]}에 어울리는 안주는 {drinks_food[drinks_food_keys[0]]} 입니다.')
    elif menu == '2':
        print(f'{drinks_food_keys[1]}에 어울리는 안주는 {drinks_food[drinks_food_keys[1]]} 입니다.')
    elif menu == '3':
        print(f'{drinks_food_keys[2]}에 어울리는 안주는 {drinks_food[drinks_food_keys[2]]} 입니다.')
    elif menu == '4':
        print(f'{drinks_food_keys[3]}에 어울리는 안주는 {drinks_food[drinks_food_keys[3]]} 입니다.')
    elif menu == '5':
        print(f'{drinks_food_keys[4]}에 어울리는 안주는 {drinks_food[drinks_food_keys[4]]} 입니다.')
    elif menu == '6':
        random_drink = random.choice(drinks_food_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_food[random_drink]} 입니다.')
    else:
        print(f'다음에 또 오세요')
        break