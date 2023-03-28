import numpy as np
import json


def main():
    months_names = [
                    'january', 
                    'february', 
                    'march', 
                    'april', 
                    'may', 
                    'june', 
                    'july', 
                    'august', 
                    'september', 
                    'october', 
                    'november', 
                    'december'
                   ]
    
    months_temperatures = []

    for i in range(12):
        with open('months/' + months_names[i] + '.json', 'r') as f:
            # В json файле температуры хранятся в всиде строк, поэтому приводим всё к float
            temps = list(map(float, json.load(f).values()))
            # Потом преабразуем это в np.array и добавляем его в список температур по месяцам
            months_temperatures.append(np.array(temps, dtype=np.float32))
            # Чтобы добить количество температур в месяце до 31 без особого изменения данных - добовляем медианы недостоющее количество раз
            months_temperatures[i] = np.append(months_temperatures[i], [months_temperatures[i].mean() for _ in range(31-len(months_temperatures[i]))])

    # после того как у нас получился список из 12 массивов температур по 31 значению в каждом, мы можем преобразовать его в np.array 12x31
    months_temperatures = np.array(months_temperatures, dtype=np.float32)
    # теперь мы можем использовать методы numpy чтобы получать нужные нам значения за весь год
    print('min', months_temperatures.min())
    print('max', months_temperatures.max())
    print('mean', months_temperatures.mean())
    print('dispersion', months_temperatures.std())
    # и за отдельный месяц
    month = int(input('enter number of month: ')) - 1
    print(f'min of {months_names[month]}', months_temperatures[month].min())
    print(f'max of {months_names[month]}', months_temperatures[month].max())
    print(f'mean of {months_names[month]}', months_temperatures[month].mean())
    print(f'dispersion of {months_names[month]}', months_temperatures[month].std())
    
if __name__ == '__main__':
    main()
