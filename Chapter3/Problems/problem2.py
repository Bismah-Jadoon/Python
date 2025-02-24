letter = '''Dear <|Name|>,
                 you are selected!
                 <|Date|>'''

print(letter.replace("<|Name|>", "Bismah").replace("<|Date|>","18 Feb 2025")) #chaining of .replace function