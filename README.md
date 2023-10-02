# Обнаружение нарушений сердечного ритма по ЭКГ


## Описание

Модель нейронной сети с архитектурой [ResNet34](https://neurohive.io/ru/vidy-nejrosetej/resnet-34-50-101/) обучается на открытом датасете [PTB_XL](https://physionet.org/content/ptb-xl/1.0.3/)


## Подготовка данных для обучения модели
### 1.  **Скачайте репозиторий с [GitHub](https://github.com/MaratNaz12/ECG)**    
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=MaratNaz12&repo=ECG)](https://github.com/anuraghazra/github-readme-stats)

        git clone https://github.com/MaratNaz12/ECG

---
###    2. Перейдите в репозиторий ECG и [настройте виртуальное окружение](https://docs.python.org/3/library/venv.html#:~:text=Python%20-m%20venv%20%2Fpath%2Fto%2Fnew%2Fvirtual%2Fenvironment.%20Running,the%20target%20directory%20is%20.venv)
        python3 -m venv venv
---
        . venv/bin/activate
---
        pip install -r requirements.txt
---
  
### 3. **Запустите файл data_ready.py, указав место для загрузки данных ключом -pd**  
    
        python3 data_ready.py -pd <destination path>
        
### Вы запустите три этапа:
1.   Скачивание zip файла 
2.   Распаковку zip файла
3.   Конвертацию данных
#### Если у вас уже есть скачанный датасет ptbxl, и вам нужен только 3-ий этап, то вы можете указать путь к источнику с помощью ключа ps. Ключ k позволяет сохранить необработанные данные.

        python3 data_ready.py -ps <source path> -pd <destination path> -k 

#### По умолчанию данные будут загружены в директорию ECG/data
---
### 4.Запустите обучение модели настроив [конфигурацию](https://hydra.cc/docs/intro/)

        python3 main.py dataset.path_for_sigs = <path to data>   dataset.path_for_datamap = <path to ptbxl_database.csv> 
---


___конфигурационные файлы находятся в ECG/ptbxl_model/conf___


Резултаты обучения и тестирования сохраняются в папке outputs

Удачи!




