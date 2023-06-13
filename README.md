# AInytime (ChatGPT Offline)

 AInytime is built using `py2app`, `rumps`, and `gpt4all`. It provides a dropdown menu in the taskbar, allowing users to query a local version of ChatGPT-like model without requiring an internet connection.

## Features

- Access a local version of ChatGPT directly from the taskbar.
- Query the model using text input and receive responses in real-time.
- No internet connection required.

## Prerequisites

- Python 3.x
- `py2app` library
- `rumps` library
- `gpt4all` library
- Pretrained ChatGPT model weights (`.pt` file)

## Installation

1. Clone the repository: 
   ```
   git clone https://github.com/justdanzer/AInytime
   ```

2. Navigate to the project directory:
   ```
   cd AInytime
   ```

3. Create and activate a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```
   pip3 install -r requirements.txt
   ```

## Usage

1. Run the `app.py` .

2. 



## Customization

- To customize the app's appearance or behavior, you can modify the `Info.plist` file in the `setup.py` script.
- You can also make changes to the `main.py` file to enhance the functionality or add additional features to the app.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The developers of `py2app`, `rumps`, and `gpt4all` for their fantastic libraries.
- The creators of GPT4All for their remarkable work.

## Disclaimer

Please note that this local version of GPT may not have the same capabilities or performance as the cloud-based version. The pretrained model used in this application has limitations and may produce incorrect or inappropriate responses in certain cases. Use this application responsibly and exercise caution when interacting with the model.