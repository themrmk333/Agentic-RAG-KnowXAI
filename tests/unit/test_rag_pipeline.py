import io
import zipfile

from rag.chunking.text_chunker import chunk_text
from rag.embeddings.openai_embeddings import OpenAIEmbeddingService
from rag.loaders.company_zip import iter_company_documents
from rag.retrieval.pgvector_retriever import PGVectorRetriever


def test_chunk_text_always_finishes_and_overlaps() -> None:
    chunks = chunk_text("one two three four five six", chunk_size=12, overlap=3)
    assert chunks
    assert all(chunks)
    assert len(" ".join(chunks)) > len("one two three four five six")


def test_company_zip_loader_reads_json_csv_markdown(tmp_path) -> None:
    archive_path = tmp_path / "company.zip"
    with zipfile.ZipFile(archive_path, "w") as archive:
        archive.writestr("MK_InfinitAI_Dataset/company/item.json", '{"name": "Example"}')
        archive.writestr("MK_InfinitAI_Dataset/helpdesk/tickets.csv", "id,title\n1,Login issue\n")
        archive.writestr("MK_InfinitAI_Dataset/documents/readme.md", "Company policy")
        archive.writestr("MK_InfinitAI_Dataset/evaluation/questions.json", "[1, 2]")

    documents = list(iter_company_documents(str(archive_path)))

    assert len(documents) == 3
    assert {document.content_type for document in documents} == {"application/json", "text/csv", "text/markdown"}
    assert all("Example" not in document.source_path or document.text for document in documents)


def test_embedding_service_rejects_wrong_dimension() -> None:
    service = object.__new__(OpenAIEmbeddingService)
    service.dimensions = 3
    service.model = "test-model"
    service._client = type("Client", (), {"embeddings": type("Embeddings", (), {"create": lambda *_args, **_kwargs: type("Result", (), {"data": [type("Item", (), {"embedding": [1.0, 2.0]})()]})()})()})()

    try:
        service.embed(["test"])
    except ValueError as error:
        assert "dimension" in str(error)
    else:
        raise AssertionError("wrong embedding dimension was accepted")


def test_pgvector_retriever_delegates_embedding_and_search() -> None:
    embedding_service = type("Embedding", (), {"embed_query": lambda self, query: [0.1, 0.2]})()
    chunk = type("Chunk", (), {"content": "grounded context"})()
    vector_store = type("Store", (), {"similarity_search": lambda self, vector, limit: [chunk]})()

    retriever = PGVectorRetriever(embedding_service, vector_store)

    assert retriever.retrieve("company question", top_k=1) == ["grounded context"]
    assert retriever.retrieve("", top_k=1) == []
