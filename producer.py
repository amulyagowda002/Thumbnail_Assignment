from multiprocessing import Process, Queue
from PIL import Image
import io, os, time

PRODUCER_DIR = 'producer'
CONSUMER_DIR = 'consumer'
THUMB_SIZE = (200, 200)

def producer(q: Queue):
    """Read images from PRODUCER_DIR, create thumbnails and put (name, bytes) into queue."""
    files = [f for f in os.listdir(PRODUCER_DIR) if f.lower().endswith(('.jpg','.jpeg','.png'))]
    for fname in files:
        path = os.path.join(PRODUCER_DIR, fname)
        try:
            with Image.open(path) as img:
                img.thumbnail(THUMB_SIZE)
                bio = io.BytesIO()
                img.convert('RGB').save(bio, format='JPEG')
                data = bio.getvalue()
                q.put((fname, data))
                print(f'[PRODUCER] Pushed thumbnail for {fname}')
        except Exception as e:
            print(f'[PRODUCER] Failed for {fname}:', e)
    # signal consumers by sending None
    q.put(None)
    print('[PRODUCER] Done producing.')

def consumer(q: Queue):
    os.makedirs(CONSUMER_DIR, exist_ok=True)
    while True:
        item = q.get()
        if item is None:
            # put back signal for other consumers (if any) and exit
            q.put(None)
            print('[CONSUMER] Received termination signal. Exiting.')
            break
        fname, data = item
        outname = os.path.splitext(fname)[0] + '-thumbnail.jpg'
        outpath = os.path.join(CONSUMER_DIR, outname)
        try:
            with open(outpath, 'wb') as f:
                f.write(data)
            print(f'[CONSUMER] Saved {outpath}')
        except Exception as e:
            print(f'[CONSUMER] Failed to save {outpath}:', e)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    c = Process(target=consumer, args=(q,))
    start = time.time()
    p.start()
    c.start()
    p.join()
    c.join()
    print('All done. Exiting.')