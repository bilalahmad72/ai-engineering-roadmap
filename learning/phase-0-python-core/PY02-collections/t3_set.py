keyword_results = ["chunk_1", "chunk_4", "chunk_7", "chunk_1", "chunk_9"]
vector_results = ["chunk_4", "chunk_2", "chunk_7", "chunk_4", "chunk_5"]

print(f"unique keyword: {len(set(keyword_results))}")

common_chunks = set(keyword_results) & set(vector_results)

print(f"both found: {common_chunks}")

keyword_set = set(keyword_results)
vector_set = set(vector_results)

all_chunks = keyword_set | vector_set

print(f"total unique: {len(all_chunks)}")

vector_chunks_giving = vector_set - keyword_set

print(f"only vector: {vector_chunks_giving}")