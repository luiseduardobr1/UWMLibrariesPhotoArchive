# UWMLibrariesPhotoArchive
Automatically download all historical digital photos from UWM Libraries - AGSL Digital Photo Archive with maximum quality resolution. 

# Requirements
* [Selenium](https://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Chromedriver](https://chromedriver.chromium.org/downloads)

# How to use
Just change the link address in code:
```python
...
link='https://collections.lib.uwm.edu/digital/collection/ags_south/search/searchterm/Cear%C3%A1%20(state)/field/statep/mode/exact/conn/and/page/'+str(page)
...
```
**Important**: maintain the same pattern. 

After that, all photos from "UWM Libraries - AGSL Digital Photo Archive" link will be downloaded and saved in *PhotosFolder*. 

# Possible Problems
1) It's possible that could be necessary to change the code line:
```Python
...
for line in soup.findAll(class_="SearchResult-container shared-search-box shared-box row SearchResult cdm-item-card null"):
...
```
to
```Python
...
for line in soup.findAll(class_="SearchResult-container shared-search-box shared-box row SearchResult cdm-item-card"):
...
```
(just remove the *null* if the code is not working properly, more problems send me a message)

# Screenshot
![fotos-ouput](https://user-images.githubusercontent.com/56649205/73384650-684d6e80-42aa-11ea-8e0a-5bc40473c6ff.PNG)

