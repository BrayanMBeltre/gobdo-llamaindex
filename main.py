from llama_index import SimpleDirectoryReader
from llama_index.llama_pack import download_llama_pack
from ollama_pack.base import OllamaQueryEnginePack

# load in some sample data

# data = requests.get("https://gob-do-api.www.gob.do/api/v2/portals/services", verify=False).json()
# JsonDataReader = download_loader("JsonDataReader")
# loader = JsonDataReader()
# documents = loader.load_data(data)

reader = SimpleDirectoryReader(input_files=["paul_graham_essay.txt"])
documents = reader.load_data()

# download and install dependencies
OllamaQueryEnginePack = download_llama_pack("OllamaQueryEnginePack", "./ollama_pack")

# You can use any llama-hub loader to get documents!
ollama_pack = OllamaQueryEnginePack(model="tinyllama", documents=documents)
response = ollama_pack.run("What did the author do growing up?")
print(str(response))