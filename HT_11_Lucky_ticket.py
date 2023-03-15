import threading
from multiprocessing import Process
import datetime


def check_input(name: str):
    marker = True
    while marker is True:
        ticket = input(f'{name}')
        try:
            ticket_1 = int(ticket)
            marker = False
        except ValueError:
            print('Error! The ticket number must contains only digits.')
            continue
        if len(str(ticket)) == 6:
            return ticket
        else:
            print('Error! The lucky ticket number should has 6 digits.')
            print(len(str(ticket)))
            marker = True
            continue


def generate_tickets(start, end):
    tickets_list = []
    for ticket in range(start, end):
        tickets_list.append(ticket)
    return tickets_list


def format_tickets(pre_ticket):
    list_new_tickets = []
    for k in pre_ticket:
        if len(str(k)) != 6:
            len_num = len(str(k))
            k_new = str(0) * (6 - len_num) + str(k)
            list_new_tickets.append(k_new)
        else:
            list_new_tickets.append(str(k))
    return list_new_tickets


def calculation_lucky_tickets(list_tickets_par, calc):
    start = datetime.datetime.now()
    lucky_tickets_list = []
    count_tickets = 0
    for one_ticket in list_tickets_par:
        sum_num_1 = 0
        avg = len(str(one_ticket))/2
        for k1 in range(0, int(avg)):
            sum_num_1 += int(one_ticket[k1])
        sum_num_2 = 0
        for k2 in range(int(avg), int(len(str(one_ticket)))):
            sum_num_2 += int(one_ticket[k2])
        if sum_num_1 == sum_num_2:
            lucky_tickets_list.append(one_ticket)
            count_tickets += 1
    end = datetime.datetime.now()
    time_work = end - start
    print(f'''start {calc}: {start}, end: {end}, duration: {time_work}.
    The number of lucky tickets in the user-defined range: {count_tickets}\n''')


if __name__ == '__main__':
    start_range = check_input('Enter the lower limit of the lucky ticket range:')
    end_range = check_input('Enter the upper limit of the lucky ticket range:')
    list_tickets = generate_tickets(int(start_range), int(end_range))
    format_to_tickets = format_tickets(list_tickets)

    #MULTIPROCESSING
    process1 = Process(target=calculation_lucky_tickets, args=(format_to_tickets, 1))
    process2 = Process(target=calculation_lucky_tickets, args=(format_to_tickets, 2))
    process3 = Process(target=calculation_lucky_tickets, args=(format_to_tickets, 3))

    start_2 = datetime.datetime.now()
    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
    end_2 = datetime.datetime.now()
    time_work2 = end_2 - start_2
    print(f'time multiprocessing: {time_work2}')

    #THREADING
    thread1 = threading.Thread(target=calculation_lucky_tickets, args=(format_to_tickets, 1))
    thread2 = threading.Thread(target=calculation_lucky_tickets, args=(format_to_tickets, 2))
    thread3 = threading.Thread(target=calculation_lucky_tickets, args=(format_to_tickets, 3))

    start_1 = datetime.datetime.now()
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
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
