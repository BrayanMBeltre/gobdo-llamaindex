import { MeiliSearch } from 'meilisearch'

// console.time('fetch')
// const documents = await fetch('https://gob-do-api.www.gob.do/api/v2/portals/services?perPage=10000000').then(response => response.json())
// console.timeEnd('fetch')


const client = new MeiliSearch({
  host: 'http://127.0.0.1:7700',
})


async function getMovies() {
    const response = await fetch("https://www.meilisearch.com/movies.json")
    const movies = await response.json()
    return movies
}

// A document identifier must be of type integer or string, composed only of alphanumeric characters (a-z A-Z 0-9), hyphens (-), and underscores (_).
function sanitizeIdentifier(id: string) {
    return id.replace(/[^a-zA-Z0-9-_]/g, '_');
}

async function getServices() {
    const response = await fetch('https://gob-do-api.www.gob.do/api/v2/portals/services?perPage=10000000')
    const data = await response.json();
  
    const services = data.data.map((item: any) => {
      return {
        name: item.service_name,
        description: item.service_name,
        slug: sanitizeIdentifier(item.slug),
        type: item.service_type,
        institutionName: item.institution_name,
        institutionPhone: item.institution_phone,
        institutionImage: item.institution_logo,
      }
    }
    );

    console.log({services})

    return services
}


// Function to add documents
async function addDocuments(indexName: string, documents: Array<object>, primaryKey: string = 'id') {
    const index = client.index(indexName)
    const response = await index.addDocuments(documents, { primaryKey })
    return response
}

// Function to update a document
async function updateDocument(indexName: string, id: string, document: object) {
    const index = client.index(indexName)
    const response = await index.updateDocuments([{ ...document, id: id }])
    return response
}

// Function to delete a document
async function deleteDocument(indexName: string, id: string) {
    const index = client.index(indexName)
    const response = await index.deleteDocument(id)
    return response
}

// Function to search documents
async function searchDocuments(indexName: string, query: string) {
    const index = client.index(indexName)
    const response = await index.search(query)
    return response
}

// Function to get a document by ID
async function getDocument(indexName: string, id: string) {
    const index = client.index(indexName)
    const document = await index.getDocument(id)
    return document
}

// console.log(await client.getTasks().then((task)=> task.results.map((task)=> task.error)))
// console.log(await addDocuments('services2', await getServices(), "slug"))