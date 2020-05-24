# Web Scraper

Web Scraping on [barchat.com](https://www.barchart.com/stocks/quotes/GOOG/competitors)

## Clone Repository
```git clone https://github.com/codestromer/web-scrapper.git```

## Dependencies
### Step-1:
Install all required libraries using following command.<br/>
For python2<br/>
```pip install -r requirements.txt```<br/>
For python3<br/>
```pip3 install -r requirements.txt```<br/>

### Step-2:
Download chrome-driver v83 from [here](https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/)<br/>
(Although chrome-driver is already is in a repository(For Linux))

If you are using windows to perform the task.<br/>
After downloading chrome-driver paste it to drive folder and go-to scrapper.py add .exe extention in path. Like,

```python
chromedriver_path = '/driver/chromedriver.exe'
```

## Usage
### Using shell script
If you are using python2 then change shell.sh file as below.
```bash
 python scrapper.py -i $1
```
All set! Good to Go!!<br/>
Now give shell script permission for execute<br/>
```bash
 akshit@akshit:~$chmod +x shell.sh
```
And then to scrap the data provid input file(Having symbols AAPL, GOOG, MSFT on new line) as command line argument.<br/>
For ex:-
```bash
 akshit@akshit:~$./shell.sh input.txt
```

### Without Using shell script
To scrap the data provid input file(Having symbols AAPL, GOOG, MSFT on new line) as command line argument.<br/>
For ex:-
For python2
```bash
 python scrapper.py -i input.txt
```
For python3
```bash
 python3 scrapper.py -i input.txt
```

## Output
You will get json.data file and json formated data on CLI too.

## Screenshots
<img src="https://github.com/codestromer/web-scrapper/blob/master/Screenshot/1.jpg" width="400">

<img src="https://github.com/codestromer/web-scrapper/blob/master/Screenshot/2.jpg" width="400">

<img src="https://github.com/codestromer/web-scrapper/blob/master/Screenshot/3.jpg" width="400">

<img src="https://github.com/codestromer/web-scrapper/blob/master/Screenshot/4.jpg" width="400">

<img src="https://github.com/codestromer/web-scrapper/blob/master/Screenshot/5.jpg" width="400">
