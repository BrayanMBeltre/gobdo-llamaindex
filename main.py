from pathlib import Path
from llama_index import SimpleDirectoryReader, download_loader
from llama_index.llama_pack import download_llama_pack
from ollama_pack.base import OllamaQueryEnginePack

# load in some sample data

# data = requests.get("https://gob-do-api.www.gob.do/api/v2/portals/services").json()
# JsonDataReader = download_loader("JsonDataReader")
# loader = JsonDataReader()
# documents = loader.load_data(data)

# reader = SimpleDirectoryReader(input_files=["paul_graham_essay.txt"])
# documents = reader.load_data()

JSONReader = download_loader("JSONReader")
loader = JSONReader()
documents = loader.load_data(Path("./data.json"))

# download and install dependencies
ollamaQueryPack = download_llama_pack("OllamaQueryEnginePack", "./ollama_pack")

# You can use any llama-hub loader to get documents!
ollama_pack = ollamaQueryPack(model="mistral", documents=documents)
response = ollama_pack.run(
    "cual es el numero del Consejo Nacional de Zonas Francas de Exportación?"
)
print(str(response))
