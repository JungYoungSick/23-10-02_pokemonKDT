pokemon = [
  "이상해씨", "이상해풀", "이상해꽃", "파이리", "꼬부기", "라이츄"]

# 리스트의 길이를 구합니다.
pokemon_length = len(pokemon)

# 리스트의 각 요소를 순회하며 마지막 요소를 확인합니다.
for i in range(len(pokemon)):
  if i == len(pokemon)-1:
    pokemon[i] = "영식몬"
    print(i)

print(pokemon)