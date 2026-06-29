# ai-integration-examples

This repository provides examples on how to integrate with the Straight Lines Creative Design Platform.  

Prerequisites:

- obtain a license to the Straight Lines Creative Design Platform
- request a service account (Client ID + Secret Key) from the Straight Lines Support Team
- install Python virtual environment and desired IDE


## How to use

### 1. Get your Client ID and Secret Key

In order to access the Straight Lines Platform, contact the Straight Lines Support Team and obtain a dedicated service account. You will be given two values:

- a **Client ID** — identifies your service account
- a **Secret Key** — shown only once, when the account is created or its key is rotated; store it securely

These credentials are exchanged at runtime for a short-lived access token (a JWT) via `POST /signin/token`, which is then sent as a `Bearer` token on every API request. The shared [auth.py](python_examples/auth.py) helper handles this token exchange — and refreshes the token automatically when it expires — so the individual examples can focus on the API calls.

### 2. Install Python Requirements

Install the required python libraries as necessary for the available examples.  To install all requirements automatically, you can use the following pip command:

``pip install -r requirements.txt``

### 3. Set Environment Variables

The following environment variables must be set to run the examples:

| Parameter  | Description                                                       | Example                                  |
|------------|------------------------------------------------------------------|------------------------------------------|
| CLIENT_ID  | The Client ID of your service account                            | acme-integration@acme-svc.example        |
| SECRET_KEY | The Secret Key issued for your service account (keep it secret)  | secret                                   |
| SERVER_URL | Dedicated server that you want to access                         | https://not-gonna-tell-you.str8lines.com |




## API Documentation

The APIs are available in yaml format.  You can review the APIs in your preferred tool or import directly to the online swagger tool at https://editor.swagger.io/