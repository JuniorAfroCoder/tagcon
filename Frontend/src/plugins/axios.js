import axios from 'axios'

function baseUrl() {
  let base_url = ""
  let base_host = window.location.host.split(":")[0]
  let locals = ["localhost", "127.0.0.1"]
  if (locals.includes(base_host)) {
    base_url = window.location.protocol + "//" + base_host + ":8000"
  }
  //return base_url+'/api'
  return "http://api.tagcon.bi/api"
}

const apiClient = axios.create({
  baseURL: baseUrl(),
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

let isRefreshing = false
let failedQueue = []

const processQueue = (error, token = null) => {
  failedQueue.forEach((prom) => {
    if (error) {
      prom.reject(error)
    } else {
      prom.resolve(token)
    }
  })
  failedQueue = []
}

// Request interceptor to attach token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Response interceptor to handle token refresh
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        })
          .then((token) => {
            originalRequest.headers.Authorization = `Bearer ${token}`
            return apiClient(originalRequest)
          })
          .catch((err) => Promise.reject(err))
      }

      isRefreshing = true

      const refreshToken = localStorage.getItem('refresh_token')

      try {
        const { data } = await axios.post(baseUrl() + '/refresh/', {
          refresh: refreshToken,
        })

        const newToken = data.access
        localStorage.setItem('access_token', newToken)
        apiClient.defaults.headers.Authorization = `Bearer ${newToken}`
        processQueue(null, newToken)

        originalRequest.headers.Authorization = `Bearer ${newToken}`
        return apiClient(originalRequest)
      } catch (err) {
        processQueue(err, null)
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        window.location.href = '/'
        return Promise.reject(err)
      } finally {
        isRefreshing = false
      }
    }

    return Promise.reject(error)
  },
)

export default apiClient
