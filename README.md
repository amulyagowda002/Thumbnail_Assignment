Thumbnail Producer-Consumer
---------------------------
This is a minimal multiprocessing implementation that:
- Producer: reads images from `producer/`, creates thumbnails and pushes them into a multiprocessing Queue.
- Consumer: reads from the Queue and saves thumbnails into `consumer/` with names `<original>-thumbnail.jpg`.

Requirements:
- Python 3.8+
- Pillow (pip install pillow)

Run:
1. (Optional) Generate sample images:
   python generate_sample_images.py
2. Run producer/consumer:
   python producer.py

The script will print progress and save thumbnails into the consumer/ folder.

producer/README.md
consumer/README.md
This folder stores images processed by the producer.
This folder stores thumbnails saved by the consumer.
