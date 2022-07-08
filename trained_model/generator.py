import logging
from aitextgen import aitextgen

logging.basicConfig(
        format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO
    )



ai = aitextgen(model_folder="trained_model", to_gpu=True)
ai.generate(n=1,
            batch_size=50,
            max_length=256,
            temperature=1.0,
            top_p=0.9)
'''
num_files = 4

for _ in range(num_files):
  ai.generate_to_file(n=10000,
                     batch_size=50,
                     max_length=256,
                     temperature=1.0,
                     top_p=0.9)
'''