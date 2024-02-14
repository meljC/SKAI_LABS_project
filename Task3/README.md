
# Job Interview Scheduler API

## Description

This repository contains a Flask application that serves a RESTful API for scheduling job interviews. The API accepts start and end times for multiple job interviews and calculates the maximum number of non-overlapping interviews a person can attend. This tool is designed to help job seekers optimize their interview schedules.

## Features

- RESTful API endpoint accepting JSON input.
- Calculates the maximum number of non-overlapping interviews.
- Simple and efficient algorithm implementation.
- Easy to deploy and use with `curl` or any HTTP client.

## Getting Started

### Prerequisites

Before running this application, you need to have Python and Flask installed on your system. If you don't have Flask installed, you can install it using pip:

```bash
pip install Flask
```

### Running the Application

1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Run the application using Python:

```bash
python app.py
```

This command starts the Flask server, typically available at `http://127.0.0.1:5000/`.

### Sending a Request

#### Using `curl`

To send a request to the API, you can use the `curl` command from your terminal. Here's an example command that sends a POST request to the `/schedule` endpoint:

```bash
curl -X POST http://127.0.0.1:5000/schedule \
-H "Content-Type: application/json" \
-d @data.json
```

This command assumes that you have a file named `data.json` in the current directory containing the JSON-formatted start and end times of the interviews.

#### Example `data.json` File

Create a file named `data.json` with the following content:

```json
{
  "start_times": [10, 20, 30, 40, 50, 60],
  "end_times": [15, 25, 35, 45, 55, 65]
}
```

This file represents a sample request where the start times and end times of six interviews are specified.

### Expected Response

The API will return a JSON object with the maximum number of non-overlapping interviews that can be attended. For the provided example, the response would be:

```json
{
  "max_interviews": 6
}
```

## Error Handling

The API includes basic error handling for invalid requests, such as mismatched lengths of `start_times` and `end_times`. In such cases, it will return an appropriate error message and HTTP status code.

## Contact

For any queries or feedback regarding this project, please open an issue on GitHub.
