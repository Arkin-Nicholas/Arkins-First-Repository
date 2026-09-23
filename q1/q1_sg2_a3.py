irth_Year = int(input("Enter your birthyear (Should not be earlier than 1900): "))

if birth_Year >= 1900:
    zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
    sign = zodiac[(birth_Year - 4) % 12]
    print(f"\nYour chinese zodiac sign is, {sign} ")
    
elif birth_Year < 1900:
    print("\nInvalid Year, it should not be earlier than 1900.")

else:
    print("That is not an applicable year. Enter a valid year next time.")
