from jina import Flow

with Flow(port=1234, protocol='grpc') as f:
    f.block()