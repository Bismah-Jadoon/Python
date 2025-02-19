# Replace Name with name and Date with date
letter = '''Dear <|Name|>,
                 you are selected!
                 <|Date|>'''

print(letter.replace("<|Name|>", "Shine").replace("<|Date|>","18 Feb 2025")) #chaining of .replace function
