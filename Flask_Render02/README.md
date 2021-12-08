# Flask Render
Note, to render CSS...[see here](https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python)

- folder structure needs to be this

```
/app
    - app_runner.py
    /services
        - app.py
    /templates
        - mainpage.html
    /static
        /styles
            - mainpage.css
```

- then do this

```html
<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/index.css') }}">
```