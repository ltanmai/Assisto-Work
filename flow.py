from jina import Flow
from executor import StableLM
from text_to_image import TextToImage

flow = (
    Flow(port=12345)
    .add(uses=StableLM, timeout_ready=-1)
    .add(uses=TextToImage, timeout_ready=-1)
)

with flow:
    flow.block()