print("Touch left or right hand! (a = left click, d = right click, q = quit)")

while True:
    key = input("Touch: ").strip().lower()

    if key == 'q':
        print("👋 Exiting!")
        break
    elif key == 'a':
        print("🖱️ Left click detected!")
    elif key == 'd':
        print("🖱️ Right click detected!")
    else:
        print("❌ Unknown input. Try 'a' or 'd'.")
