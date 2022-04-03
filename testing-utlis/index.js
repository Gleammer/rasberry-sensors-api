const axios = require('axios')
const baseUrl = 'http://localhost'
const PORT = 5000

async function makeRequest(value) {
  let reqUrl = `${baseUrl}:${PORT}/todo/api/v1.0/tasks`
  reqUrl += value ? `/${value}` : ''

  try {
    const response = await axios.get(reqUrl);
    return response.data;
  } catch (err) {
    console.log(err);
  }
}

const main = async () => {
  const res = await makeRequest(0)
  console.log(res)
}

main()