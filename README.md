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

| Parameter  | Description                                                       | Example                                |
|------------|------------------------------------------------------------------|----------------------------------------|
| CLIENT_ID  | The Client ID of your service account                            | acme-integration@acme-svc.example      |
| SECRET_KEY | The Secret Key issued for your service account (keep it secret)  | secret                                 |
| SERVER_URL | Dedicated server that you want to access                         | https://not-gonna-tell-you.example.com |




## Examples

Most examples are small, single-purpose scripts that can also be imported as helper functions
(their demo runs only under `if __name__ == "__main__":`). They all use the shared
[auth.py](python_examples/auth.py) helper for authentication.

### Marketing assets from a spreadsheet

[marketing_asset_from_spreadsheet.py](python_examples/marketing_asset_from_spreadsheet.py) is a
wrapper that reads a spreadsheet and, for each row, creates a parent marketing asset plus up to
three scenarios. It composes the smaller examples:
[find_library_record.py](python_examples/find_library_record.py),
[find_prompt_template.py](python_examples/find_prompt_template.py),
[upload_file.py](python_examples/upload_file.py),
[create_marketing_asset.py](python_examples/create_marketing_asset.py),
[create_scenario.py](python_examples/create_scenario.py), and
[get_workflow.py](python_examples/get_workflow.py).

The spreadsheet must have a header row with these columns:

| Column      | Description                                                                |
|-------------|----------------------------------------------------------------------------|
| fieldA      | Customer-specific custom field set on the marketing asset (per environment)|
| fieldB      | Customer-specific custom field set on the marketing asset (per environment)|
| Model       | Name of a `base_model` record in the `supporting_assets` library           |
| Footwear    | Name of a `supporting_product` record in the `supporting_assets` library   |
| Detail path | Folder containing the row's detail images (named with `_1`, `_2`, … suffix) |

A ready-to-run sample is included: [marketing_assets.xlsx](python_examples/marketing_assets.xlsx)
(two rows) together with a [sample_details](python_examples/sample_details) folder of detail
images. A relative `Detail path` in the spreadsheet is resolved against the spreadsheet's own
folder (override with the `DETAIL_BASE_DIR` environment variable), and the bundled sample
spreadsheet is found relative to the script, so the example runs from any working directory.

Configure the run by editing the constants at the top of the script — the workflow name (its
model is used for every scenario), the per-scenario prompt template names (each scenario's
prompt is taken from the named prompt template's `prompt_text`), the library key, and the image
`WIDTH` / `HEIGHT` / `NUM_IMAGES`. The spreadsheet path can be set with the `SPREADSHEET_PATH`
environment variable (it defaults to the bundled `marketing_assets.xlsx`). The service account
needs the `marketing_asset:create` role and read access to the `supporting_assets` library.


## API Documentation

The APIs are available in yaml format.  You can review the APIs in your preferred tool or import directly to the online swagger tool at https://editor.swagger.io/