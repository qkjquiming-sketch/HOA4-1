import time

# pause()
def pause():
    for i in range(10,0,-1):
        print(f"The program will end in {i}..")
        time.sleep(1)

pause()

# print(current_time())
def current_time():
    t = time.strftime("%I:%M %p")
    return t

print(current_time())

# print(current_date())
def current_date():
    d = time.strftime("%b %d %Y")
    return d

print(current_date())

