import time
from processors.sequential import apply_filter_sequential
from processors.parallel import apply_filter_parallel

if __name__ == "__main__":
    IMAGE_PATH = r"data\natural_images\person"

    # Sequential Processing
    print("Starting sequential processing...")
    start_time = time.time()
    apply_filter_sequential(IMAGE_PATH)
    end_time = time.time()
    print(f"Sequential processing completed. Time taken: {end_time - start_time:.2f} seconds\n")

    # Parallel Processing
    print("Starting parallel processing...")
    start_time = time.time()
    apply_filter_parallel(IMAGE_PATH)
    end_time = time.time()
    print(f"Parallel processing completed. Time taken: {end_time - start_time:.2f} seconds\n")

