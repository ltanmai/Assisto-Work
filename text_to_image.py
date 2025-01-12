import numpy as np
from jina import Executor, requests
from docarray import BaseDoc, DocList
from docarray.documents import ImageDoc


class Generation(BaseDoc):
    prompt: str
    text: str


class TextToImage(Executor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from diffusers import StableDiffusionPipeline
        import torch

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
        ).to("cuda")

    @requests
    def generate_image(self, docs: DocList[Generation], **kwargs) -> DocList[ImageDoc]:
        result = DocList[ImageDoc]()
        images = self.pipe(
            docs.text
        ).images  # image here is in [PIL format](https://pillow.readthedocs.io/en/stable/)
        result.tensor = np.array(images)
        return result