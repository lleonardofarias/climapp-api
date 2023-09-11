# Climapp-api

## Overview

The Climapp-api is a simple and powerful tool that provides essential parameters for your UI. This API fetches real-time weather data and the current time for a specified city. It's designed to be straightforward to set up using Docker and customizable according to your needs.

## Features

- Obtain weather information for any city
- Choose between metric, imperial, or standard units
- Retrieve accurate local time for the requested location

## Getting Started

Follow these steps to set up the Climapp-api API:

### Prerequisites

Before you begin, you'll need the following:

- Docker installed on your system.

### Configuration

1. Clone this repository to your local machine.

2. Open the `views.py` file and locate the following lines:

```ini
api_key = "your api key"
base_url = "your weather api url"
```

3. Now replace the "your api key" and "your weather api url" for your api key nad your weather api url

## What is an API Key?

An API key is a unique identifier that grants access to a specific API. It serves as a security measure to control who can use the API and helps the provider track usage. When you request data from an API, you typically include your API key in the request, allowing the provider to associate your requests with your account and provide you with the data you need.

## What is an API URL?

An API URL (Uniform Resource Locator) is the web address that you use to access a specific API. It includes the base URL for the API and additional parameters that specify the type of data you want to retrieve and any customization options. These URLs are used in your code to make requests to the API and receive responses.

## Example of Free Weather APIs and How to Get API Keys

### 1. OpenWeatherMap

- **API Base URL:** https://api.openweathermap.org/data/2.5/weather

- **API Key Registration:**

   1. Go to the OpenWeatherMap website at [https://openweathermap.org/](https://openweathermap.org/).

   2. Sign up for an account or log in if you already have one.

   3. After logging in, go to the "API Keys" section in your account dashboard.

   4. Generate a new API key, and it will be provided to you.

### Usage

Start the API using Docker by running the following command in the project directory:

```ini
docker-compose up
```

This will launch the API locally on port that you choose on the Docker.

Access the API by making HTTP GET requests to:

```ini
http://localhost:/api/weather/?city=CITY_NAME&unit=UNIT&timezone=TIMEZONE
```
- Replace CITY_NAME with the name of the city you want weather information for.
- Choose UNIT to specify the desired unit system (metric, imperial).
- Set TIMEZONE to the desired timezone (default is UTC).
- Receive a JSON response containing weather and time data.

### Next Steps

This API is the first step in building a complete weather and time application. To create a user-friendly UI utilizing this API, check out the climapp-ui repository.
Feel free to explore, customize, and build upon this API to suit your project's requirements.




