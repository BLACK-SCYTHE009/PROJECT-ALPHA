# LIFE SYSTEM

#importing libraries


import json
import os
#file path 
DATA_FILE="data.json"

# Check if file exists (returning user)
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        NAME = data["username"]
        stat = data["stat"]
        xp   =data["xpp"]
      
    print("WELCOME BACK", NAME + "!")
else:
    # First time run
    NAME = input("ENTER YOUR USERNAME: ")
    print("SYSTEM WELCOME", NAME + "!")


    
stat={
"Strength":1,
"Stamina":1,
"Endurance":1,
"flexiblity":1,
"Charisma":1,
"Mind":1,
"Looks":1,
"skills":{
    "combat":1,
    "programming":1
}



}
print(stat)
# xp section
xp={
"st":0,
"sta":0,
"end":0,
"flex":0,
"char":0,
"mi":0,
"lo":0,
"com":0,
"pro":0
}
print("AVALABLE TAKSKS FOR YOU  1)w.s \n 2)app dev \n 3)look maxing \n 4)combo practice ")
task=input("ENTER THE TASK U COMPLETED")
#  the tasks 1)w.s 2)app dev 3)look maxing 4)combo practice 

if task in ["w.s" , "ws" ,  "workoutscedule"]:
  xp["st"]+=1
elif task=="app dev":
 xp["pro"]+=1
elif task in ["look max" , "look maxing"  ]:
  xp["lo"]+=1
elif task in ["combo" , "combo practice" , "boxing"  ]:
  xp["com"]+=1










# stats level
if xp["st"]==100 :
  stat["Strength"]+=1
  print("Congratulations now your Strength "  +"has Reached level " , stat["Strength"] ) 
  xp["st"]=0

if xp["sta"]==100 :
  stat["Stamina"]+=1
  print("Congratulations now your Stamina "  +"has Reached level " , stat["Stamina"] ) 
  xp["sta"]=0



if xp["end"]==100 :
  stat["Endurance"]+=1
  print("Congratulations now your Endurance "  +"has Reached level " , stat["Endurance"] ) 
  xp["end"]=0


if xp["flex"]==100:
  stat["flexiblity"]+=1
  print("Congratulations now your Flexiblity "  +"has Reached level " , stat["flexiblity"] ) 
  xp["flex"]=0

if xp["char"]==100:
  stat["Charisma"]+=1
  print("Congratulations now your Charisma "  +"has Reached level " , stat["Charisma"] ) 
  xp["char"]=0

if xp["mi"]==100:
  stat["Mind"]+=1
  print("Congratulations now your Mind "  +"has Reached level " , stat["Mind"] ) 
  xp["mi"]=0

if xp["lo"]==100:
  stat["Looks"]+=1
  print("Congratulations now your Looks"  +"has Reached level " , stat["Looks"] ) 
  xp["lo"]=0

if xp["com"]==100:
  stat["skills"]["combat"]+=1
  print("Congratulations now your Combat"  +"has Reached level " , stat["skills"]["combat"] ) 
  xp["com"]=0

if xp["pro"]==100:
  stat["skills"]["programming"] +=1
  print("Congratulations now your Programming "  +"has Reached level " , stat["skills"]["programming"] ) 
  xp["pro"]=0

  print("Updated stats:", stat)

  #UpDATED XP CAP
  for b, vlauea in xp.items():
   print(f"{b}:{vlauea}") 



#UPDATED stats

for i, vlaue in stat.items():
  print(f"{i}:{vlaue}") 




# Save everything
with open(DATA_FILE, "w") as f:
    json.dump({
        "username": NAME,
        "stat": stat,
        "xpp":xp,
       
    }, f)
    print(f"\n✅ Progress saved to {DATA_FILE}")