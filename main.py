from socket import timeout
import time
from llama_index.llms import Ollama
from pathlib import Path
import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    download_loader,
)
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
import torch


def main():
    start_time = time.time()

    # JSONReader = download_loader("JSONReader")
    # loader = JSONReader()
    # documents = loader.load_data(Path("./data.json"))

    client = qdrant_client.QdrantClient(path="./qdrant_data")
    vector_store = QdrantVectorStore(client=client, collection_name="services")
    # storage_context = StorageContext.from_defaults(vector_store=vector_store)

    llm = Ollama(model="llama2")
    service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store, service_context=service_context
    )
    query_engine = index.as_query_engine(similarity_top_k=20, streaming=True)
    streaming_response = query_engine.query(
        "A cual institucion pertenece el numero 8096868077",
    )

    streaming_response.print_response_stream()

    end_time = time.time()
    processing_time = end_time - start_time
    print(f"Processing time: {processing_time} seconds")


if __name__ == "__main__":
    main()
