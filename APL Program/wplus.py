with open('adarsh.txt', 'w+') as file:
    file.write('Hello, world')
    file.seek(0)
    content = file.read()

