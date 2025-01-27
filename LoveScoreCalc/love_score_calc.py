def calculate_love_score(name1:str,name2:str) -> str:
    true = 0
    love = 0
    combined = (name1+name2).upper()
    for letter in 'TRUE':
        true += combined.count(letter)
    for letters in 'LOVE':
        love += combined.count(letters)
    print(f"{true}{love}")

calculate_love_score("Abisheek","Sainath")