food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        if(len(x)>=5):
		fifth.append(x[4])

    except IndexError:
        pass
    
print(fifth)
