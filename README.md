# Rasa Chatbot Project

This is a Rasa-powered chatbot designed to assist with GATE exam preparation. The chatbot offers tips, resources, and guidance to help users excel in their GATE exam.

## Features
- AI-powered chatbot using Rasa
- Provides personalized GATE exam tips
- User-friendly web interface with chat functionality

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Tejasri-123/Rasa_Chatbot.git
    ```

2. Navigate to the project folder:
    ```bash
    cd Rasa_Chatbot
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. Install the necessary dependencies:
    ```bash
    pip install rasa
    pip install flask
    pip install flask-cors
    requests
    ```

## Running the Application

1. Start the Rasa server:
    ```bash
    rasa run
    ```

2. Start the Rasa actions server (if applicable):
    ```bash
    rasa run actions
    ```

3. Start the web application using Flask:
    ```bash
    python app.py
    ```
