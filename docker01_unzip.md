
```sql
vscode@441e368db4cd:/$ cd home/vscode/notebooks
vscode@441e368db4cd:~/notebooks$ ls
a.py  data.zip  test.ipynb
vscode@441e368db4cd:~/notebooks$ mkdir data
vscode@441e368db4cd:~/notebooks$ ls
a.py  data  data.zip  test.ipynb
vscode@441e368db4cd:~/notebooks$ mv data.zip ./data
vscode@441e368db4cd:~/notebooks$ cd data
vscode@441e368db4cd:~/notebooks/data$ ls
data.zip
vscode@441e368db4cd:~/notebooks/data$ unzip data.zip
Archive:  data.zip
  inflating: banklist.csv            
  inflating: billboard.csv           
  inflating: concat_1.csv            
  inflating: concat_2.csv            
  inflating: concat_3.csv            
  inflating: country_timeseries.csv  
  inflating: gapminder.tsv           
  inflating: pew.csv                 
  inflating: raw_data_urls.txt       
  inflating: scientists.csv          
  inflating: survey_person.csv       
  inflating: survey_site.csv         
  inflating: survey_survey.csv       
  inflating: survey_visited.csv      
  inflating: tesla_stock_quandl.csv  
  inflating: weather.csv             
vscode@441e368db4cd:~/notebooks/data$ 
```
