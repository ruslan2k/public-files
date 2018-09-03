import { API, SET_ARCHIVES } from '../constants'

const fetchArchives = () => {
  return {
    type: API,
    payload: {
      url: '/json',
      onSuccess: setArchives
    }
  }
}

const setArchives = (data) => {
  return {
    type: SET_ARCHIVES,
    payload: data
  }
}

export {
  fetchArchives,
  setArchives
}
