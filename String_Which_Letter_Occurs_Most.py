a = input("Enter your string : ")
conv_list = list(a)
first_char = conv_list[0]
count = 0
for i in range(0, len(conv_list)):
    for j in range(1+i, len(conv_list)):
        if conv_list[i] == conv_list[j]:
            print(conv_list[i])
            count = count + 1
print(count)

