import axios from 'axios'
import { DEF_DOMAIN } from './config'
import { API } from './constants'

const apiMiddleware = ({ dispatch }) => next => action => {
  next(action)
  if (action.type !== API) {
    return
  }
  const { url, onSuccess } = action.payload
  axios.get(`${DEF_DOMAIN}${url}`)
    .then(({ data }) => dispatch(onSuccess(data)))
    .catch(error => console.log(error))
}

export { apiMiddleware }
