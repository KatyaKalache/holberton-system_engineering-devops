# Application server #0
![alt text](http://i.imgur.com/QbqjElZ.jpg)
## Description
You web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. And while a web server can also serve dynamic content, the task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.
## Tasks:
0. Let’s serve what you built for AirBnB clone - Web framework `on web01`.
1. Create an Upstart script that starts Gunicorn to serve web_flask/6-number_odd_or_even.py from your Airbnb clone. Setup Nginx so that the route /airbnb-dynamic/ points to `Gunicorn`. Nginx must serve this locally but also on its public IP on port `80`. Provide your Upstart config file, name it `1-pass_parameter-upstart_config`. Provide your Nginx config file, name it `1-pass_parameter-nginx_config`.

2. Let's do this for your API
Setup MySQL 5.7 and import your production data dump. Make sure to use the necessary environment variables for your Airbnb clone app. Create an Upstart script that starts Gunicorn to serve `api/v1/app.py` from your Airbnb clone.  Setup Nginx so that the route `/api/` points to Gunicorn. Nginx must serve this locally but also on its public IP on port `80`.

3. Serve your complete Airbnb clone.
### __Clone repository:__ https://github.com/KatyaKalache/holberton-system_engineering-devops

|What should I learn  |
| ---------------- |
|    `Application server vs web server`   |
|  `How To Serve a Flask Application with Gunicorn and Nginx on Ubuntu 14.04` |
|    `Running Gunicorn` |
|    `Be careful with the way Flask manages slash in route` |
|    `Upstart documentation`   |

## Authors

Ekaterina Kalache: [github account](https://github.com/KatyaKalache), [twitter](https://twitter.com/KatyaKalache)

## License
Public, no copyright protection# holberton-system_engineering-devops
