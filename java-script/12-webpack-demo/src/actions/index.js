import { API, SET_ARCHIVES, SET_INTERVALS } from '../constants'

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
    payload: data.archives
  }
}

const setIntervals = (intervals) => {
  return {
    type: SET_INTERVALS,
    payload: intervals
  }
}

export {
  fetchArchives,
  setArchives,
  setIntervals,
}
