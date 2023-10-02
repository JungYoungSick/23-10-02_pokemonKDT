# 1. 포켓몬스터 배열 '_pokemon'에 새로운 포켓몬을 추가해주세요. if나 for문을 사용하여 _pokemon 배열의 마지막에 새로운 포켓몬 이름을 추가하세요.

pokemon = [
  "이상해씨", "이상해풀", "이상해꽃", "파이리", "꼬부기", "라이츄"]

for i in range(len(pokemon)+1):
  if i == len(pokemon):
    pokemon.insert(i, "영식몬")
    print(i)
print(pokemon)
