# New Python Project

This project implements an Ethereum bridging solution using the Orbiter class. The Orbiter class allows users to bridge ETH from the Sepolia network to the Monad network, while managing gas fees and waiting for funds to arrive.

## Project Structure

```
new-python-project
├── src
│   ├── main.py                # Entry point of the application
│   └── model
│       └── orbiter
│           ├── __init__.py    # Marks the directory as a Python package
│           ├── instance.py     # Contains the Orbiter class
│           └── constants.py    # Contains constants used in the Orbiter module
├── requirements.txt           # Lists project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the `main.py` file. This file serves as the entry point and will create an instance of the `Orbiter` class, allowing you to utilize its functionality.

Example command to run the application:

```
python src/main.py
```

## Dependencies

This project requires the following Python libraries:

- `web3`
- `eth_account`
- `primp`
- `loguru`

Make sure to install these dependencies before running the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.