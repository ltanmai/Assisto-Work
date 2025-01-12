from jina import Deployment
from executor import StableLM

dep = Deployment(uses=StableLM, timeout_ready=-1, port=1234)

with dep:
    dep.block()