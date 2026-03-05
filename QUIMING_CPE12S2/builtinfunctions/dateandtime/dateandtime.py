import time

def pause():
    for i in range(10,0,-1):
        print(f"The program will end in {i}..")
        time.sleep(1)

def current_time():
    return time.strftime("%I:%M %p")

def current_date():
    return time.strftime("%b %d %Y")

if __name__ == "__main__":
    pause()
    print(current_time())
    print(current_date())