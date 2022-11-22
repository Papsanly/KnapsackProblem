from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from knapsack_problem import KnapsackProblem


def get_optimal_solution(problem: KnapsackProblem) -> int:

    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get('https://augustineaykara.github.io/Knapsack-Calculator/')

    capacity_input = driver.find_element(By.XPATH, '//*[@id="capacity"]')
    items_count_input = driver.find_element(By.XPATH, '//*[@id="rows"]')
    generate_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/button')
    capacity_input.send_keys('250')
    items_count_input.send_keys('100')
    generate_button.click()

    for i, item in enumerate(problem.items):
        cost_input = driver.find_element(By.XPATH, f'//*[@id="table"]/tbody[{2 + i}]/tr/td[2]/input')
        weight_input = driver.find_element(By.XPATH, f'//*[@id="table"]/tbody[{2 + i}]/tr/td[3]/input')
        cost_input.send_keys(f'{item.cost}')
        weight_input.send_keys(f'{item.weight}')

    calculate_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/button')
    calculate_button.click()

    solution = driver.find_element(By.XPATH, '//*[@id="kp01ResultantProfit"]').text
    driver.close()
    return int(solution)
