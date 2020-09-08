import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract

# Initial Lists
skill_list = []
item_list = []
weapon = "Unsure"
weapon_max_val = 0.7
hero = "Unsure"
hero_ability = "Unsure"
hero_ability_max_val = 0.7

# End Screen Image
end_screen = cv2.imread(r"C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Kevin Dead Picture.png",0)
flamebreak_template = cv2.imread(r"C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\windowed_template.png", 0) # 1420x900, 1420x930
if cv2.minMaxLoc(cv2.matchTemplate(end_screen, flamebreak_template,method=5))[1] > 0.9:
    print("hi")
    top_left_loc = cv2.minMaxLoc(cv2.matchTemplate(end_screen, flamebreak_template,method=5))[3]
    left_coord = top_left_loc[0]
    up_coord = top_left_loc[1] + 30
    end_screen = end_screen[up_coord:up_coord+900, left_coord:left_coord+1420]
    plt.imshow(end_screen)
    plt.show()
end_screen = cv2.resize(end_screen, (round(end_screen.shape[1]*4/3), round(end_screen.shape[0]*4/3)))
end_screen2 = end_screen.copy()


def skill_check(skill_file_name):
    skill_name = skill_file_name[:-4].replace("_"," ")

    #  Upload Pics
    img = end_screen2.copy()
    img = img[950:,700:1200] # cropping to just the skill tab
    skill_pic = cv2.imread(os.path.join(r'C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\skill_icon', skill_file_name),0)
    skill_pic = cv2.resize(skill_pic, (80, 80))  # This is for 1080x1920 resoloution, may have to look into different sizes
    skill_pic = skill_pic[10:70, 10:70]  # Cropping out border

    # Apply template Matching
    res = cv2.matchTemplate(img, skill_pic,method=5)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.8:
        skill_list.append(skill_name)
        result = "MATCH: " + str(max_val)
    else:
        result = "NO MATCH: " + str(max_val)
    print(skill_file_name, result)

def weapon_check(weapon_file_name):
    if weapon_file_name == "musket2.png":
        weapon_name = weapon_file_name[:-5].replace("_", " ")
    else:
        weapon_name = weapon_file_name[:-4].replace("_"," ")

    #  Upload Pics
    img = end_screen2.copy()
    img = img[950:,750:900] # Cropped to just the weapon icon
    weapon_pic = cv2.imread(os.path.join(r'C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\weapon_icon', weapon_file_name),0)
    weapon_pic = cv2.resize(weapon_pic, (80, 80))  # This is for 1080x1920 resoloution, may have to look into different sizes
    weapon_pic = weapon_pic[10:70, 10:70]  # Cropping out border


    #  Apply Template Matching
    res = cv2.matchTemplate(img, weapon_pic, method = 5)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > weapon_max_val:
        result = "MATCH: " + str(max_val)
        print(weapon_file_name, result)
        return max_val, weapon_name
    else:
        result = "NO MATCH: " + str(max_val)
        print(weapon_file_name, result)
        return weapon_max_val, weapon

def item_check(item_file_name):
    result = "no match"
    item_name = item_file_name[:-4].replace("_"," ")

    #  Upload Pics
    img = end_screen2.copy()
    img = img[950:, 1500:]
    item_pic = cv2.imread(os.path.join(r'C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\item_icon', item_file_name),0)
    item_pic = cv2.resize(item_pic, (33, 33))  # This is for 1080x1920 resoloution, may have to look into different sizes

    # Apply template Matching
    res = cv2.matchTemplate(img, item_pic,method=5)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.98:
        item_list.append(item_name)
        result = "MATCH: " + str(max_val)
    else:
        result = "NO MATCH: " + str(max_val)
    print(item_file_name, result)

def hero_check(hero_ability_file_name):
    file_name_split = hero_ability_file_name[:-4].split("_")
    hero_name = file_name_split[0]
    ability_name = " ".join(file_name_split[1:])

    #  Upload Pics
    img = end_screen2.copy()
    img = img[950:,950:1150] # Cropped to just the ability in question tab
    hero_pic = cv2.imread(os.path.join(r'C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\hero_ability_icons', hero_ability_file_name),0)
    hero_pic = cv2.resize(hero_pic, (80, 80))  # This is for 1080x1920 resoloution, may have to look into different sizes
    hero_pic = hero_pic[10:70, 10:70] # Cropping out border

    #  Apply Template Matching
    res = cv2.matchTemplate(img, hero_pic, method = 5)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > hero_ability_max_val:
        result = "MATCH: " + str(max_val)
        print(hero_ability_file_name, result)
        return max_val, hero_name, ability_name
    else:
        result = "NO MATCH: " + str(max_val)
        print(hero_ability_file_name, result)
        return hero_ability_max_val, hero, hero_ability

# Skill List
print("SKILL CHECK")
print("")
for file in os.listdir(r"C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\skill_icon"):
    if file.endswith(".png"):
        skill_check(file)

#  Weapon Check
print("")
print("")
print("WEAPON CHECK")
print("")
for file in os.listdir(r"C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\weapon_icon"):
    if file.endswith(".png"):
        weapon_max_val, weapon = weapon_check(file)

# Item List
print("")
print("")
print("Item CHECK")
print("")
for file in os.listdir(r"C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\item_icon"):
    if file.endswith(".png"):
        item_check(file)

#  Hero Check
print("")
print("")
print("WEAPON CHECK")
print("")
for file in os.listdir(r"C:\Users\Adam PC\PycharmProjects\FlamebreakStatProgram\Icons\hero_ability_icons"):
    if file.endswith(".png"):
        hero_ability_max_val, hero, hero_ability = hero_check(file)

