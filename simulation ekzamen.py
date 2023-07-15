# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:04:51 2023

@author: miku_
"""

import random

gen_tickets = []  #список, содержащий билеты
for i in range(1,31):
    gen_tickets.append(i)
print(gen_tickets)

def pulls(x):
    tick_pulls = 0
    while tick_pulls < 25: #тянем билет n человеком в очереди, к этому времени осталось 30-n билетов
        a = random.randrange(1, len(x))
        x.pop(a)
        tick_pulls += 1
    return x

good = 0
bad = 0
sim_nums = 10000 #количество симуляций события

for i in range(sim_nums):
    f = pulls(gen_tickets.copy())
    f.sort()
    #print(f)
    my_pull = random.randrange(1, len(f))
    my_ticket_num = f.pop(my_pull)
    if my_ticket_num % 2 == 0:
        good += 1
    else:
        bad += 1

summary_good = (good/sim_nums)
summary_bad = (bad/sim_nums)

print('количество симуляицй =', sim_nums)
print('количество хороших исходов =', good)
print('количество плохих исходов =', bad)
print('вероятность хорошего исхода =',summary_good,'\n'
      'вероятность плохого исхода =', summary_bad)



