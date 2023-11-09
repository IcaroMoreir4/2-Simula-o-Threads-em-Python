import threading

def thread_function_1():
    for i in range(10):
        print(f"Thread 1: {i}")

def thread_function_2():
    for c in range(10):
        print(f"Thread 2: {c}")

if __name__ == "__main__":
    t1 = threading.Thread(target=thread_function_1)
    t2 = threading.Thread(target=thread_function_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
