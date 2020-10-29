# WebScraping

<p align="center">
┏┓┏┓┏┓━━━━┏┓━━┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━━━━
┃┃┃┃┃┃━━━━┃┃━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━━━━━━━
┃┃┃┃┃┃┏━━┓┃┗━┓┃┗━━┓┏━━┓┏━┓┏━━┓━┏━━┓┏┓┏━┓━┏━━┓
┃┗┛┗┛┃┃┏┓┃┃┏┓┃┗━━┓┃┃┏━┛┃┏┛┗━┓┃━┃┏┓┃┣┫┃┏┓┓┃┏┓┃
┗┓┏┓┏┛┃┃━┫┃┗┛┃┃┗━┛┃┃┗━┓┃┃━┃┗┛┗┓┃┗┛┃┃┃┃┃┃┃┃┗┛┃
━┗┛┗┛━┗━━┛┗━━┛┗━━━┛┗━━┛┗┛━┗━━━┛┃┏━┛┗┛┗┛┗┛┗━┓┃
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━━━━━━━┏━┛┃
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗┛━━━━━━━━┗━━┛
</p>

<p align="center">
Herramienta hecha en Python para realizar webscraping.
</p>

## Instalación
```bash
git clone https://github.com/m4lal0/webScraping
cd webScraping
pip3 install -r requirements.txt
```

## Uso

Para usar el script:
```bash
python3 webScraping.py
```

<p align="center">
<img src="Images/portada.png"
	alt="Portada"
	style="float: left; margin-right: 10px;" />
</p>

El script cuenta con menú de 3 opciones para realizar webscraping.

#### Opción 1
+ La cual puedes realizar webscraping a cualquier sitio, ya que solo tienes que colocar dos datos:
	* URL del sitio web.
	* Selector de lo requieres scrapear.

#### Opción 2
+ Realizá webscraping a Youtube, en el cual podras obtener todos los subtitulos de un video en particular, el script solicita un dato:
	* ID del video.

#### Opción 3
+ Realizará busquedas en el sitio de la seccionamarilla.com.mx, el cual solo solicitará el siguiente dato:
	* Nombre de la persona o empresa a buscar.