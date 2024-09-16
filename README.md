# Bad Apple Terminal Animation

This project displays the "Bad Apple" animation in the terminal using preprocessed frame data stored in `.npz` files.

## Prerequisites

- Python 3.x
- NumPy

## Setup

1. Clone the repository and navigate to the project directory.
2. Ensure you have the required dependencies installed:
    ```sh
    pip install numpy
    ```

## Usage

1. Place your `.npz` files containing the frames in the `bad_apple_frames(60fps)` directory.
2. Run the script:
    ```sh
    python format_terminal.py
    ```

## How It Works

- The script loads all `.npz` files from the `bad_apple_frames(60fps)` directory.
- Each `.npz` file contains frames of the animation.
- Frames are displayed in the terminal at 60 frames per second using ASCII characters.

## Customization

- You can modify the `strings` list in `format_terminal.py` to change the characters used for rendering the frames.