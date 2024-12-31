# Image Processing Project

This project involves applying filters to images using both sequential and parallel processing techniques. It demonstrates the performance differences between these two approaches.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- Required Python packages (see below for installation)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Umeradhiaa/image-processing-project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-processing-project
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Update the `IMAGE_PATH` in `main.py` to the directory containing the images you want to process. For example:

   ```python
   IMAGE_PATH = r"data\natural_images\person"
   ```

   **Note**: Replace the above path with the actual path on your system.

2. Run the script:

   ```bash
   python main.py
   ```

   The script will:
   - Apply filters to the images sequentially and measure the time taken.
   - Apply filters to the images in parallel and measure the time taken.

3. Outputs will be saved in the following directories:
   - Sequential processing output: `data/natural_images/person/output_sequential`
   - Parallel processing output: `data/natural_images/person/output_parallel`

   Update these paths in the code if necessary to match your system setup.

## Project Structure

```
image-processing-project/
├── main.py                 # Main script to run the project
├── processors/
│   ├── sequential.py       # Sequential image processing logic
│   ├── parallel.py         # Parallel image processing logic
├── data/
│   └── natural_images/     # Directory containing the images
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
```

## Example Output

When you run the script, you will see outputs like this in the terminal:

```
Starting sequential processing...
Sequential processing completed. Time taken: 12 minutes

Starting parallel processing...
Parallel processing completed. Time taken: 2 minutes
```

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. We welcome bug fixes, feature additions, and documentation improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Inspired by the need for efficient image processing techniques.
- Thanks to the open-source community for providing helpful tools and libraries.

