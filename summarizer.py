import re
from collections import Counter
import nltk 
from nltk.corpus import stopwords

# for open ar read chat.txt file 
# used try, except .... for prevent crashes, Debugging and more 
try: 
    with open("chat.txt", "r", encoding="utf-8") as t:
        lines = t.readlines()

#shows when txt file not found or identify 
except FileNotFoundError:   
     print("chat.txt file not found.")
     exit()


user_messages = [] #blank list for user 
ai_messages = [] #blank list for AI

current_speaker = None # for remember whose msz is currently store 
current_message_parts = [] #to store if has mutile lines  

for line in lines:
    stripped_line = line.strip()   #remove whitespace 
    if not stripped_line:
        continue

#condition wise matching 
    match = re.match(r"^(User|AI):\s*(.*)", stripped_line, re.IGNORECASE)
    if match:
        if current_speaker == "user" and current_message_parts:
            user_messages.append(" ".join(current_message_parts))
        elif current_speaker == "ai" and current_message_parts:
            ai_messages.append(" ".join(current_message_parts))

        current_speaker = match.group(1).lower()
        message_content = match.group(2).strip()

        current_message_parts = [message_content]  #

    else:
        if current_speaker:
            current_message_parts.append(stripped_line)

if current_speaker == "user" and current_message_parts:
    user_messages.append(" ".join(current_message_parts))
elif current_speaker == "ai" and current_message_parts:
    ai_messages.append(" ".join(current_message_parts))


print("\n--- Parsing Result ---")
print("User Messages:")
if user_messages:
    for i, msg in enumerate(user_messages):
        print(f"  User {i+1}: {msg}")
else:
    print("  No user messages found.")

print("\nAI Messages:")
if ai_messages:
    for i, msg in enumerate(ai_messages): # enumerate for indexing 
        print(f"  AI {i+1}: {msg}")
else:
    print("  No AI messages found.")

#  Message Statistics 
#  mainly doing somg string operation 

print ("\n Message Statistics :")

# user msz count 
total_user_messages = len(user_messages)
print(f"Total User of Messages: {total_user_messages}")

#ai msz count
total_ai_messages = len(ai_messages)
print(f"Total AI Messages: {total_ai_messages}")

#all msz count 
total_exchanges = total_user_messages + total_ai_messages
print(f"Total Chat Exchanges: {total_exchanges}")

    

    

