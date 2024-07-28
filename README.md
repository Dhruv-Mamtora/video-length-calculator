# Video Length Calculator

This project calculates the total length of all video files in a given folder. It supports `.mkv`, `.mp4`, `.avi`, and `.mov` formats. The script also allows users to select specific videos from the folder to include in the length calculation.

## Features

- Calculate the total length of all videos in a folder.
- Select specific videos to include in the length calculation.
- Output the total length in seconds, minutes, hours, days, and in a formatted `days, hours, minutes, seconds` string.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

## Installation

1. Ensure you have Python 3.x installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/video-length-calculator.git
    ```

3. Navigate to the project directory:
    ```sh
    cd video-length-calculator
    ```

4. It’s recommended to use a virtual environment to manage dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

5. Install the required packages:
    ```sh
    pip install opencv-python
    ```

## Usage

1. Run the script:
    ```sh
    python video_length_calculator.py
    ```

2. Enter the folder path when prompted:
    ```sh
    Enter the folder path: /path/to/your/video/folder
    ```

3. Choose an option:
    - Calculate the total length of all videos in the folder
    - Select specific videos to calculate their total length

4. If selecting specific videos, enter the numbers of the videos to include (separated by spaces), or a range (e.g., `1-5`), or a combination of both (e.g., `1 2 3-5`).

## Example

```sh
Enter the folder path: /path/to/your/video/folder

Select an option:
1. Calculate total length of all videos in the folder
2. Select specific videos to calculate their total length
Enter your choice (1/2): 1

Total video length:
  * Seconds: 12345.67
  * Day, Hour, Minute, Second: 0 days, 3 hours, 25 minutes, 45 seconds
  * Minutes: 205.76
  * Hours: 3.43
  * Days: 0.14
