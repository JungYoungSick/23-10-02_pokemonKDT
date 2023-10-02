# 2. '_pokemon' 배열의 마지막 포켓몬을 방출해주세요. 이를 위해 배열의 마지막 원소를 제거하고, 그 원소의 이름을 출력하세요.
pokemon = [
  "이상해씨", "이상해풀", "이상해꽃", "파이리", "꼬부기", "라이츄"]

for i in range(len(pokemon)):
  if i == len(pokemon)-1:
    pokemon[i] = "영식몬"
    print(i)

print(pokemon)