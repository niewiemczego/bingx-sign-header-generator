# bingx-sign-header-generator

A Python implementation for generating secure sign header for the Bingx API. This project is based on reverse engineering efforts to understand and replicate the signing mechanism used by the official Bingx obfuscated JavaScript implementation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [How do I get request_payload values?](#how-do-i-get-request_payload-values)
    - [Understanding the Original JavaScript Implementation](#understanding-the-original-javascript-implementation)
- [Testing](#testing)
- [Contributing](#contributing)

## Disclaimer

This project is a reverse-engineered implementation based on analysis of the official Bingx JavaScript code responsible for generating sign header. Please be aware that this is not an officially endorsed or supported tool by Bingx. Users should exercise caution and be aware of the potential risks when using reverse-engineered solutions. **This project is intended for educational use only!**


## Features

- **Automatic Sign Header Generation:** Streamlines the process of creating secure sign header for the Bingx API.
- **Request Payload Sorting:** Ensures consistent signature generation by automatically sorting the request payload keys.
- **Simplified Configuration:**  Uses Python's dataclasses to manage configuration and initialization, offering flexibility with sensible defaults.
- **Testable Codebase:** Includes a comprehensive test suite to ensure reliability and correctness.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/niewiemczego/bingx-sign-header-generator.git
    cd bingx_sign_header_generator
    ```

2.  **Install the package using pip:**

    ```bash
    pip install -e .
    ```

    The `-e .` flag installs the package in editable mode, allowing you to modify the source code directly while testing and developing.

## Usage

Here's a simple example of how to use the `BingxSignHeader` class:

```python
from datetime import datetime
from uuid import uuid4
from bingx_sign_header_generator import BingxSignHeader

# Make sure to use the same values in headers
timestamp = int(datetime.now().timestamp() * 1000)
trace_id = str(uuid4())
device_id = str(uuid4())


# Initialize with required parameters
sign_header = BingxSignHeader(
    timestamp=timestamp,
    trace_id=trace_id,
    device_id=device_id,
    request_payload={
        "copyTradeLabelType": "2",
        "apiIdentity": "1347851488071426053",
        "pageId": "0",
        "uid": "1339191395874545671",
        "pageSize": "10",
    },
)

# Generate the sign header value
sign_value = sign_header.generate_sign_header_value()
print(f"Sign Header Value: {sign_value}")
```

### How do I get request_payload values?

The most crucial and dynamic values, especially the `request_payload`, often come directly from API requests made by the Bingx web client. Here’s how to obtain them:

1. **Open Developer Tools:**
   - Launch your browser and open the Bingx website.
   - Open the Developer Tools by pressing `F12` or right-clicking on the page and selecting "Inspect" or "Inspect Element."

2. **Navigate to the Network Tab:**
   - In the Developer Tools, click on the "Network" tab. This tab captures all network requests made by the webiste.

3. **Filter Requests:**
   - Use the filter to narrow down the requests to a specific API endpoint. For example, type `api/copy-trade-facade/v2/real/trader/positions` or `api/v3/trader/orders/v3` in the filter box.

4. **Inspect Request Details:**
   - Click on the specific request to view its details.

5. **Find Request Payload:**
   - Switch to the "Payload" tab to view the request payload. This is the `request_payload` dictionary that you'll use in your code.

  ![Developer Tools Example](https://github.com/user-attachments/assets/9bddc5db-d4e8-41e3-ad39-3a9bd7b10925)
  
7. **Copy and Use:**
   - Copy the values and use them in your Python code to generate the sign header.

### Understanding the Original JavaScript Implementation

The sign header generation logic is located within the JavaScript files loaded by the Bingx web client. Here's how to find and understood the relevant code:

1. Locating the Code: The sign generation logic can often be found in one of the initial JavaScript files loaded by the website. In many cases, the sixth loaded <script> is the one that contains the "encryptionContent" keyword, which is a key component used later in generating the sign.

   **If you're having trouble locating the correct script, here are some previously used URLs that might help:**
   - https://bin.bb-os.com/_nuxt/08f13682b3.modern.js
   - https://bin.bb-os.com/_nuxt/941f858513.modern.js
   - https://bin.bb-os.com/_nuxt/1491b29.js <-- the oldest one, used a few years ago

![Location JavaScript Sign Implementation](https://github.com/user-attachments/assets/c704e003-1254-402f-a796-52a3265e3470)

2. Analyzing the Code: Once you find the script file, search for the encryptionContent variable or the function responsible for generating the sign. By observing how this variable is constructed, you can understand the steps needed to replicate the signing process.

![JavaScript Sign Implementation](https://github.com/user-attachments/assets/178245ac-3b2d-45aa-83e1-ad04a714e151)

## Testing 

The project includes comprehensive tests using pytest. The tests ensure that the key functionalities work as expected, including the signing process and payload sorting.

To run the tests:

```bash
pytest -s
```

This command will execute all tests and show output from print statements if needed. A pytest.ini configuration file is included to manage test configurations.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Write tests for your changes.
4. Ensure all tests pass.
5. Submit a pull request with a clear description of your changes.

