# Url Shortner

URL shortening is a technique on the World Wide Web that enables the Uniform Resource Locator to be made considerably shorter and still direct to the desired page. This is done by using a redirect path to a web page that has a long URL.

The project is developed using Django for backend and HTML and CSS for frontend. 

## Installation

In order to run the program, you need Python and Django. Take the instructions below to successfully execute the program.

1) Create a virtual environment;
Create a virtual environment to install the dependent packages. You can use whatever method you like to create your own environment.

2) Install the packages using ```requirements.txt```. You can type ```pip install -r requirements.txt``` after activating your virtual environment. 

3) Open the terminal in the directory where the file ```manage.py``` is stored.
    1)  Type ```python manage.py makemigrations``` and press enter.
    2)  Then type ```python manage.py migrate``` and press enter.
    3)  Finally, ```python manage.py runserver``` and press enter to run the server.

4) Open the link which will flash while the server is running. 

## Usage
When the user enters the link, a short link will appear. Use clipboard emote to copy the link. The link will redirect you to the original link. 

This is only going to work locally. You can deploy it in order to access the link globally. 

## Screenshots

1) Home Page rendered after opening the link from the terminal
![Screenshot (6)](https://user-images.githubusercontent.com/54246710/109489089-63aa4980-7aac-11eb-938e-3a079b3334c6.png)

2) Entered the link in the text field and clicked submit
![Screenshot (7)](https://user-images.githubusercontent.com/54246710/109489097-660ca380-7aac-11eb-9b2c-23cfd1800efd.png)

3) A short link is given in a read-only field. Copied the link using the clipboard.
![Screenshot (8)](https://user-images.githubusercontent.com/54246710/109489106-673dd080-7aac-11eb-9817-6de8ca5c4ed6.png)

4) Opened a new tab and pasted the link and pressed enter
![Screenshot (9)](https://user-images.githubusercontent.com/54246710/109489115-6b69ee00-7aac-11eb-8432-176b9c591133.png)

5) It redirected to the original link
![Screenshot (10)](https://user-images.githubusercontent.com/54246710/109489121-6c9b1b00-7aac-11eb-8404-9ffbeb864c1c.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
