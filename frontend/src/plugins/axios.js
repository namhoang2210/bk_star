import axios from 'axios'

const bk_axios = axios.create({
  baseURL: 'http://localhost:8100' // baseURL = http://localhost:8100
})

export default bk_axios