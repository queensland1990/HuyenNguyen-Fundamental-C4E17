teen_code={
    "eny": "Em nguoi yeu",
    "any": "Anh nguoi yeu",
}
while True:
    code=input("enter a key: ")
    if code in teen_code:
        print(teen_code[code])
        break
    # else:
    #     print(code, "is not in teen_code")
    else:
        user_choice=input("wish to contribute ? ")
        if user_choice=="Y" or user_choice=="y":
            translation=input("enter the translation: ")
            teen_code[code]=translation
            print(teen_code)
