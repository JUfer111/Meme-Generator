from PIL import Image, ImageDraw, ImageFont
from colorama import Fore,Style
print(f"{Fore.LIGHTGREEN_EX}Генератор мемов запущен!{Style.RESET_ALL}")
his_choice= int(input("Если хотите только верхний текст введите 1, если хотите только нижний введите 2, если хотите оба вида введите 3:"))
top_text= ""
bottom_text= ""
text_type= [1, 2, 3]
if his_choice == text_type[0]:
    top_text = input("Введите верхний текст: ")
elif his_choice == text_type[1]:
    bottom_text = input("Введите нижний текст: ")
elif his_choice == text_type[2]:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print(f"{Fore.RED}Введите 1,2 или 3{Style.RESET_ALL}")
    quit()
top_text = top_text.replace("Java", "Python")
bottom_text = bottom_text.replace("Java", "Python")
print(top_text, bottom_text)
pictures = ["глупый_кот.png", "милый_кот.jpg", "удивленный_кот.jpg", "Улыбающийся_кот.jpg"]
for i in range(4):
    print(Fore.CYAN,i,".",pictures[i],Style.RESET_ALL)
picture_answer = int(input("Выберете картинку:"))
if picture_answer not in [0, 1, 2, 3]:
    print(f"{Fore.RED}Такой картинки не найденно{Style.RESET_ALL}")
    quit()
image= Image.open(pictures[picture_answer])
w,h = image.size
if w > 2000: size= 225

else:
    size= 100

draw= ImageDraw.Draw(image)

font= ImageFont.truetype("arial.ttf",size=size)
text_high = draw.textbbox((0, 0), top_text, font)

text_low = draw.textbbox((0, 0), bottom_text, font)
draw.text(((w - text_high[2]) / 2, 10), top_text, font=font, fill="purple", stroke_width=4, stroke_fill="black")

draw.text(((w - text_low[2]) / 2, h - text_low[3] - 10), bottom_text, font=font, fill="purple", stroke_width=4, stroke_fill="black")

image.show()