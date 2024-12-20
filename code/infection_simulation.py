# -*- coding: utf-8 -*-
"""Infection_simulation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LNJYjXAdBWJIE9UOVJJBTjYFqtJhNh_G
"""

import math
num_trials = 1000
ir_75 = [78.90360585, 76.56321092, 74.11374744, 72.66377158, 72.00116013]
ir_90 = [77.8842118, 74.99884289, 73.08418985, 71.23686197, 70.69809562]

# 평균 계산 (%)
average_ir_75 = [round(value * 0.05 / num_trials, 5) * 100 for value in ir_75]
average_ir_90 = [round(value * 0.05 / num_trials, 5) * 100 for value in ir_90]

# 직장인 비율 75%
base_ir = average_ir_75[0]
reduced_ir_75 = [average_ir_75[i]/base_ir for i in range(len(average_ir_75))]
reduced_ir_75

base_R = 2.68
reduced_R = [(1-1*(1-i))*base_R for i in reduced_ir_75]
reduced_R

import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_infected = 1 # 초기
total_population = 1000000 # max
observation_period = 30  # 1달 관찰
infection_period = 7  # 감염지속기간 7일
R_values = [2.68, 2.598582278481013, 2.517164556962025, 2.462886075949367, 2.44253164556962] # 감소된 R값 by 재택근무+오피스근무

Des_R = {2.68 : 15,
 2.598582278481013 : 25,
 2.517164556962025 : 35,
 2.462886075949367 : 45,
 2.44253164556962 : 55}


time_steps = np.arange(0, observation_period + 1)
results = {}  # R 값별 누적 감염자 데이터
for R in R_values:
    infected = [initial_infected]  # 초기 누적 감염자 수를 리스트에 저장
    for day in time_steps[1:]:

        # 새로 감염된 사람의 수를 계산
        new_infections = infected[-1] * R / infection_period

        # 누적 감염자 수를 업데이트
        infected.append(infected[-1] + new_infections)

    # 누적데이터 저장
    results[R] = infected


# Plot results
plt.figure(figsize=(10, 6))
for R, infected in results.items():
    plt.plot(time_steps, infected, label=f'Remote Work Ratio = {Des_R[R]:.0f}%')
plt.title('Infection Spread for Decreasing R Values')
plt.xlabel('Days')
plt.ylabel('Cumulative Number of Infected')
plt.legend()
plt.grid(True)
plt.show()

cnt_30_R = [results[i][-1] for i in reduced_R]
base_cnt = cnt_30_R[0]
Reduced_cnt = [100-(i/base_cnt)*100 for i in cnt_30_R]
Reduced_cnt

import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_infected = 1 # 초기
total_population = 1000000 # max
observation_period = 60  # 1달 관찰
infection_period = 7  # 감염지속기간 7일
R_values = [2.68, 2.598582278481013, 2.517164556962025, 2.462886075949367, 2.44253164556962] # 감소된 R값 by 재택근무+오피스근무

Des_R = {2.68 : 15,
 2.598582278481013 : 25,
 2.517164556962025 : 35,
 2.462886075949367 : 45,
 2.44253164556962 : 55}


time_steps = np.arange(0, observation_period + 1)
results = {}  # R 값별 누적 감염자 데이터
for R in R_values:
    infected = [initial_infected]  # 초기 누적 감염자 수를 리스트에 저장
    for day in time_steps[1:]:

        # 새로 감염된 사람의 수를 계산
        new_infections = infected[-1] * R / infection_period

        # 누적 감염자 수를 업데이트
        infected.append(infected[-1] + new_infections)

    # 누적데이터 저장
    results[R] = infected


# Plot results
plt.figure(figsize=(10, 6))
for R, infected in results.items():
    plt.plot(time_steps, infected, label=f'Remote Work Ratio = {Des_R[R]:.0f}%')
plt.title('Infection Spread for Decreasing R Values')
plt.xlabel('Days')
plt.ylabel('Cumulative Number of Infected')
plt.legend()
plt.grid(True)
plt.show()

cnt_30_R = [results[i][-1] for i in reduced_R]
base_cnt = cnt_30_R[0]
Reduced_cnt = [100-(i/base_cnt)*100 for i in cnt_30_R]
Reduced_cnt

"""# 아래는 직장인 비율 90%"""

# 직장인 비율 90%
base_ir = average_ir_90[0]
reduced_ir_90 = [average_ir_90[i]/base_ir for i in range(len(average_ir_90))]
reduced_ir_90

base_R = 2.68
reduced_R = [(1-1*(1-i))*base_R for i in reduced_ir_90]
reduced_R

import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_infected = 1 # 초기
total_population = 1000000 # max
observation_period = 30  # 1달 관찰
infection_period = 7  # 감염지속기간 7일
R_values = [2.68,
 2.5835475578406175,
 2.514652956298201,
 2.452647814910026,
 2.4319794344473014] # 감소된 R값 by 재택근무+오피스근무

Des_R = {2.68 : 15,
 2.5835475578406175 : 25,
 2.514652956298201 : 35,
 2.452647814910026 : 45,
 2.4319794344473014 : 55}


time_steps = np.arange(0, observation_period + 1)
results = {}  # R 값별 누적 감염자 데이터
for R in R_values:
    infected = [initial_infected]  # 초기 누적 감염자 수를 리스트에 저장
    for day in time_steps[1:]:

        # 새로 감염된 사람의 수를 계산
        new_infections = infected[-1] * R / infection_period

        # 누적 감염자 수를 업데이트
        infected.append(infected[-1] + new_infections)

    # 누적데이터 저장
    results[R] = infected


# Plot results
plt.figure(figsize=(10, 6))
for R, infected in results.items():
    plt.plot(time_steps, infected, label=f'Remote Work Ratio = {Des_R[R]:.0f}%')
plt.title('Infection Spread for Decreasing R Values')
plt.xlabel('Days')
plt.ylabel('Cumulative Number of Infected')
plt.legend()
plt.grid(True)
plt.show()

cnt_30_R = [results[i][-1] for i in reduced_R]
base_cnt = cnt_30_R[0]
Reduced_cnt = [100-(i/base_cnt)*100 for i in cnt_30_R]
Reduced_cnt

import numpy as np
import matplotlib.pyplot as plt

# Parameters
initial_infected = 1 # 초기
total_population = 1000000 # max
observation_period = 60  # 1달 관찰
infection_period = 7  # 감염지속기간 7일
R_values = [2.68,
 2.5835475578406175,
 2.514652956298201,
 2.452647814910026,
 2.4319794344473014] # 감소된 R값 by 재택근무+오피스근무

Des_R = {2.68 : 15,
 2.5835475578406175 : 25,
 2.514652956298201 : 35,
 2.452647814910026 : 45,
 2.4319794344473014 : 55}


time_steps = np.arange(0, observation_period + 1)
results = {}  # R 값별 누적 감염자 데이터
for R in R_values:
    infected = [initial_infected]  # 초기 누적 감염자 수를 리스트에 저장
    for day in time_steps[1:]:

        # 새로 감염된 사람의 수를 계산
        new_infections = infected[-1] * R / infection_period

        # 누적 감염자 수를 업데이트
        infected.append(infected[-1] + new_infections)

    # 누적데이터 저장
    results[R] = infected


# Plot results
plt.figure(figsize=(10, 6))
for R, infected in results.items():
    plt.plot(time_steps, infected, label=f'Remote Work Ratio = {Des_R[R]:.0f}%')
plt.title('Infection Spread for Decreasing R Values')
plt.xlabel('Days')
plt.ylabel('Cumulative Number of Infected')
plt.legend()
plt.grid(True)
plt.show()

cnt_30_R = [results[i][-1] for i in reduced_R]
base_cnt = cnt_30_R[0]
Reduced_cnt = [100-(i/base_cnt)*100 for i in cnt_30_R]
Reduced_cnt

