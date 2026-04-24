# Weather Web App

A simple Flask-based web application that fetches current weather data from the OpenWeatherMap API and displays it in the browser.

## Features

- Search weather by city name
- Default city fallback to `Kampala` when the search field is empty
- Displays temperature, feels-like temperature, and weather description
- Shows a friendly "city not found" page for invalid city names
- Uses Flask templates for rendering dynamic pages
- Uses `waitress` to serve the app in production mode

## Tech Stack

- Python
- Flask
- Waitress
- Requests
- python-dotenv
- OpenWeatherMap API

## Project Structure

- `server.py` - Flask application and route handlers
- `weather.py` - OpenWeatherMap API client logic
- `templates/` - HTML templates for the application pages
  - `index.html` - main search page
  - `weather.html` - weather result page
  - `city-not-found.html` - error page for unknown cities
- `static/styles/style.css` - basic styling for the pages
- `requirements.txt` - Python dependency list
- `.env` - local environment variables (not included in version control)
- `first.py` - learning script placeholder
- `tempCodeRunnerFile.py` - temporary VS Code execution file


## Usage

 Enter a city name and submit the form
- The app shows current weather data for the entered city
- If the search value is empty, the app defaults to `Kampala`
- If the city is not found, a `City not found` page is shown

## Notes

The app uses the OpenWeatherMap current weather endpoint with metric units.
server.py uses waitress.serve when run directly, which is suitable for production deployment.
