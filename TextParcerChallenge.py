text = input("Insert an article please: ")
L1 = input("Give me the first letter: ")
L2 = input("Give me the second letter: ")
L3 = input("Give me the third letter: ")

text = str(text.lower())
query1 = text.count(L1)
query2 = text.count(L2)
query3 = text.count(L3)
request = text.split()

print("\n")
print(f"How much your letters appears in the article \nL1 {query1} times \nL2 {query2} times \nL3 {query3} times")

print("\n")
print(f"There are {len(request)} words in your article.")

print("\n")
print("The first letter in the article is: ")
Ftext = text[0]
print(Ftext)

print("\n")
print("The last letter in the article is: ")
Ltext = text[-1]
print(Ltext)

print("\n")
print("This is the inverted text")
request.reverse()
inverted_text = ' '.join(request)
print(f"If we order the text in reverse '{inverted_text}'")

print("\n")
is_python = 'python' in text
dic = {True: 'was', False: 'was not'}
print(f"the word 'python' {dic[is_python]} found in the text")