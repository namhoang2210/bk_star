import axios from 'axios'

const bk_axios = axios.create({
  baseURL: process.env.VUE_APP_API_URL // baseURL = http://localhost:8100
})

export default bk_axios