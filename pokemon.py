import random
import time
import sys

class Pokemon:
    def __init__(self, name, type, hp):
        self.name = name
        self.type = type
        self.attack_power = hp

    def attack(self, target):
        #print(f"{self.name} attacked {target.name} using {damage} skill")
        while self.attack_power > 0 and target.attack_power > 0:
            print(f"SYSTEM >>> Choose how to attack {target.name}.")
            time.sleep(1)
            print(f"<{self.name}'s available way to attack>")
            print("==========\n1)'Quick Attack'\n2) 'Strong Attack'\n3) 'Run'\n==========")
            fight = int(input(f"Look at the options above\nchoose a way to attack {target.name} >>> "))
            if fight == 1:
                target.attack_power = target.attack_power - 5
                self.attack_power = self.attack_power -2
                print(f"{self.name} quicly attacked {target.name}")
                print(f"{self.name}'s hp: {self.attack_power}\n{target.name}'s hp: {target.attack_power}")
            elif fight == 2:
                target.attack_power = target.attack_power - 10
                self.attack_power = self.attack_power -5
                print(f"{self.name} strongly attacked {target.name}")
                print(f"{self.name}'s hp: {self.attack_power}\n{target.name}'s hp: {target.attack_power}")
            elif fight == 3:
                target.attack_power= target.attack_power + 2
                self.attack_power = self.attack_power
                print(f"{self.name} has escaped ! ! !")
                print(f"{self.name}'s hp: {self.attack_power}\n{target.name}'s hp: {target.attack_power}")
                break
            else:
                print("Please enter right number.")
                target.attack_power =target.attack_power
                self.attack_power = self.attack_power
        if self.attack_power <=0:
            time.sleep(1)
            print(f"\nYour {self.name} is fainted ! Wild {target.name} wins !\n")
        elif target.attack_power <= 0:
            time.sleep(1)
            print(f"\nWild {target.name} is fainted ! Your {self.name} wins !\n")
        time.sleep(1)
        print("dr.Ma) 'Good job !'\n")
        time.sleep(1)
        print("SYSTEM >>> Q U I T T H I S G A M E")
        sys.exit()





class Pokemon_list: #Pokemon_list 라는 이름을 가지는 클래스
    def __init__(self): #Pokemon_list 클래스 안의 객체 초기화 메서드
        self.pokemon_list = [ #self.pokemon_list라는 속성 초기화
            # Pokemon클래스의 객체들이 리스트로 지정되어 있음
            Pokemon("'피카츄'", "electric", 20), #name과 type을 가지는 포켓몬 객체 생성
            Pokemon("'꼬부기'", "water", 18),
            Pokemon("'파이리'", "fire", 22),
            Pokemon("'이상해씨'", "grass", 25),
            Pokemon("'꼬마돌'", "rock", 30)
        ]

    def display_pokemon_list(self):
        print(f"\n<Available Pokemon List To Fight>")
        for i, pokemon in enumerate(self.pokemon_list,1):
        #enumerate함수는 리스트의 원소에 순서값을 부여해주는 함수
        #enumerate(sequence, start) start의 default value는 0
        #range 함수는 지정한 범위의 숫자 리스트를 생성
        #enumerate함수는 리스트의 인덱스와 값을 동시에 순회할 수 있도록 해줌
            print(f"{i}. {pokemon.name}")
    def choose_pokemon(self, index):
        if 1 <= index <= len(self.pokemon_list):
            return self.pokemon_list[index - 1]
        else:
            print("SYSTEM >>> ERR>> !You entered a number outside of the range.!")
            return None

#메인함수
#프로그램 실행 안내문
def main():
    print(". . . P O K E M O N I S L O A D I N G . . .")
    time.sleep(1)
    user_name = input("SYSTEM >>> Enter your name: ")
    print(f"\ndr.MA) 'HI Mr./Mrs. {user_name}, Welcome to Pokemon world.'\n")
    time.sleep(1)
    print(f"dr.MA) 'I am dr.Ma'\n")
    time.sleep(1)
    print(f"dr.Ma) 'Mr./Mrs.{user_name}, choose your Pokemon.'")
    time.sleep(1)

    pokemon_list = Pokemon_list() #객체 생성

    while True:
        try:
            pokemon_list.display_pokemon_list()  # pokemon_list라는 객체가 display_pokemon_list 함수 호출
            choice = int(input("\nSYSTEM >>> Enter Your Choice(1-5) >>> "))
            selected_pokemon = pokemon_list.choose_pokemon(choice) #pokemon_list라는 객체가 choose_pokemon() 이라는 함수 호출
            if selected_pokemon:
                time.sleep(1)
                print(f"dr.Ma) 'You choose {selected_pokemon.name}.'\n")
                time.sleep(1)
                print(f"dr.Ma) 'It is {selected_pokemon.type} type Pokemon.'\n")
                time.sleep(1)
                print(f"dr.Ma) 'You will fight with opponets'\n")
                time.sleep(1)
                print(f"dr Ma) 'GOOD LUCK'\n")
                time.sleep(1)
                print(f"\n L O A D I N G  . . .")
                time.sleep(2)
                computer_pokemon = random.choice(pokemon_list.pokemon_list)
                print(f"SYSTEM >>> Wild {computer_pokemon.name} has appeared ! ! !\n")
                time.sleep(1)
                selected_pokemon.attack(computer_pokemon)
            else:
                print(f"SYSTEM >>> Please enter right number.\n")
        except ValueError:
            print(f"SYSTEM >>> Please enter right number.\n")

#실행
main()