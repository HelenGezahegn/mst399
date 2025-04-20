import time

gesture_sequence = []
gesture_timeout = 1.0  # seconds
last_input_time = None

def add_key_to_gesture(key):
    global gesture_sequence, last_input_time
    current_time = time.time()
    if last_input_time and current_time - last_input_time > gesture_timeout:
        gesture_sequence = []
        print("⏱️ Gesture timed out. Resetting sequence.")
    gesture_sequence.append(key)
    last_input_time = current_time
    print(f"🧠 Sequence so far: {gesture_sequence}")
    check_for_gesture()

def check_for_gesture():
    global gesture_sequence
    sequence = "".join(gesture_sequence)
    if sequence == "ad":
        print("🎯 You did a left-right gesture!")
        gesture_sequence.clear()
    elif sequence == "aa":
        print("💥 Double-tapped left!")
        gesture_sequence.clear()
    elif sequence == "dd":
        print("💥 Double-tapped right!")
        gesture_sequence.clear()
