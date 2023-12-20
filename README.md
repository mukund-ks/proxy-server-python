# Python Proxy Server with WebSocket and HTTP Support

This Python script demonstrates a simple proxy server with support for both WebSocket and HTTP traffic. It uses the `http.server` module for handling HTTP requests and the `SimpleWebSocketServer` library for WebSocket communication.

## Features

- Proxies HTTP requests to a specified target URL.
- Proxies WebSocket messages to a specified WebSocket server.
- Dynamic target URL configuration.
- Basic error handling.

## Prerequisites

- Python 3.x

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mukund-ks/proxy-server-python.git
    cd proxy-server-python
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the proxy server with a target URL:**

    ```bash
    python main.py ws://echo.websocket.org
    ```

    ```bash
    python main.py https://example.com
    ```

    Replace `ws://echo.websocket.org`, `ws://echo.websocket.org` with your desired WebSocket, HTTP target URL.

2. **Access the HTTP proxy at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and WebSocket at [ws://127.0.0.1:9000/](ws://127.0.0.1:9000/).**

## Testing

- Test the HTTP proxy using a web browser, cURL, or a custom HTTP client.
- Test the WebSocket proxy using a WebSocket client, a web browser, or a custom WebSocket client.
