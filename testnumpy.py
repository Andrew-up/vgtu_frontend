import numpy as np

# Создаем массив
arr = np.random.rand(128, 128, 3)

# Находим максимальные значения по трем осям
max_values = np.amax(arr, axis=(0, 1, 2))

# Создаем новый массив, содержащий только максимальные значения
new_arr = np.full_like(arr, max_values)

print(new_arr.shape)