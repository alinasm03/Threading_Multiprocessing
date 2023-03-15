import datetime
import threading
from multiprocessing import Process

file = 'Terminal_22_reading.csv'
with open(file, 'r') as f:
    data = f.read()


def write_to_file(calc):
    start = datetime.datetime.now()
    file2 = f'Terminal_22_writing.csv'
    with open(file2, 'w') as f:
        f.write(data)
    end = datetime.datetime.now()
    time_work = end - start
    print(f'start {calc}: {start}, end {calc}: {end}, duration: {calc}: {time_work}\n')


if __name__ == '__main__':
    # Multiprocessing
    process1 = Process(target=write_to_file, args=(1,))
    process2 = Process(target=write_to_file, args=(2,))
    process3 = Process(target=write_to_file, args=(3,))
    process4 = Process(target=write_to_file, args=(4,))
    process5 = Process(target=write_to_file, args=(5,))
    process6 = Process(target=write_to_file, args=(6,))

    start_2 = datetime.datetime.now()
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()

    end_2 = datetime.datetime.now()
    time_work2 = end_2 - start_2
    print(f'time multiprocessing: {time_work2}')
    # THREAD
    thread1 = threading.Thread(target=write_to_file, args=(1,))
    thread2 = threading.Thread(target=write_to_file, args=(2,))
    thread3 = threading.Thread(target=write_to_file, args=(3,))
    thread4 = threading.Thread(target=write_to_file, args=(4,))
    thread5 = threading.Thread(target=write_to_file, args=(5,))
    thread6 = threading.Thread(target=write_to_file, args=(6,))

    start_1 = datetime.datetime.now()
    thread1.start()
    thread2.start()
    thread5.start()
    thread6.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread5.join()
    thread6.join()
    thread3.join()
    thread4.join()

    end_1 = datetime.datetime.now()
    time_work1 = end_1 - start_1
    print(f'time threading: {time_work1}')

    if time_work1 < time_work2:
        print(f'''\nThreading faster than multiprocessing in this case: 
        diff: {time_work2-time_work1} ({time_work1} < {time_work2})''')
    elif time_work1 > time_work2:
        print(f'''\nMultiprocessing faster than threading in this case: 
        diff: {time_work1-time_work2} ({time_work1} > {time_work2})''')
    else:
        print(f'''\nMultiprocessing and threading in this case have the same time: 
        {time_work1} = {time_work2}''')
