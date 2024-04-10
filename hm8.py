print("Hello,how are you?")
user_mood= input()
print(f"Great,that you are {user_mood}! What is your name?")
user_name= input()
print(f"Hello,{user_name}! How old are you?")
user_age = int(input())
birth_year_guees = 2009 - user_age

print(f"I see, you were born in year {birth_year_guees}? Let me know if is True or False?")
birth_year_guees = input()

if birth_year_guees.lower()=="true":
    print(f"Great,then {birth_year_guees} is your birth year!")
else:
    print("Double-chek your information.")
         
    
