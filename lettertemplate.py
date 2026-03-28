name = "Vishakha Patidar"
date = "6 March 2026"
letter = '''Dear <|NAME|>
you are selected for the position of Software Engineer at our company
Congratulations!
<|DATE|>'''

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)   
print(letter)