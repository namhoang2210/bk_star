import axios from 'axios'

const bk_axios = axios.create({
  baseURL: process.env.VUE_APP_API_URL
})

export default bk_axios