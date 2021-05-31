# Scraper y Parser para datos de dolar histórico de ámbito financiero.

El diario ámbito financiero tiene una [página](https://www.ambito.com/contenidos/dolar-informal-historico.html) donde muestran información de la cotización histórica del dolar. Como no ofrecen una forma sencilla de descargar el dataset detrás de esa tabla, cree este script para poder levantar esos datos y pasarlos a un dataframe de pandas. El script está escrito de forma rápida y descuidada, pero si a alguien le sirve, adelante.

El código está presentado en dos 'versiones'

* El archivo `script.py`. Para usarlo hacen falta algunas cosas:
   * Descargar el webdriver necesario para el browser que tengan instalado. Como está escrito el script, se espera el chromedriver en la carpeta raiz. Se descarga    de [esta web](https://chromedriver.chromium.org/).
   * Instalar las librerías necesarias. Incluí dos archivos, uno para conda y otro para pip. 
    Para instalar utilizando el de conda, se puede utilizar el siguiente comando:
    ```bash
    conda env create -f scraper_env.yml

    ```
    Para instalar utilizando el de pip:
    ```bash
    pip install -r requirements_pip.txt
    ```
    Al correr el script se generará el archivo `ambito.csv` con los datos descargados.
    
* El archivo `notebooks\ambito.ipynb`. Se puede visualizar localmente con Jupyter notebooks/lab, o online en Google Colab con el link provisto. Tiene un par de grafiquitos que obviamente no pretenden ser ningun tipo de análisis, mi idea es poner algún gráfico interactivo en algún momento.


