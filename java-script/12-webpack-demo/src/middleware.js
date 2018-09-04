import axios from 'axios'
import { DEF_DOMAIN } from './config'
import { API, SET_ARCHIVES } from './constants'
import { setIntervals } from './actions'

const MINUTES_IN_DAY = 1440
//   var blockWidth = $('.time-range').width()
//   var minutesInPixel = MIN_IN_DAY / blockWidth

const createIntervals = (archives) => {
  var intervals = []
  var l = archives.length
  for (var i = 0, j = 0; i < l; i ++) {
    var archive = archives[i]
    var interval = {archives: []}
    console.log(archive)
    if (! intervals[j]) {
      interval.start = archive.start_dt
      interval.stop = archive.stop_dt
      interval.archives.push(archive)
      intervals[j] = interval
      continue
    }
    var stopTime = new Date(intervals[j].stop)
    var startTime = new Date(archive.start_dt)
    if (Math.abs(startTime - stopTime) > 60000) {
      j += 1
      interval.start = archive.start_dt
      interval.stop = archive.stop_dt
      interval.archives.push(archive)
      intervals[j] = interval
      continue
    }
    intervals[j].stop = archive.stop_dt
    intervals[j].archives.push(archive)
  }
  return intervals
}


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

const timelineMiddleware = ({ dispatch }) => next => action => {
  next(action)
  if (action.type !== SET_ARCHIVES) {
    return
  }
  dispatch(setIntervals([1, 2, 3]))
}

const logger = store => next => action => {
  console.log('action.type', action.type)
  next(action)
  console.log('store.getState', store.getState())
}

export {
  apiMiddleware,
  timelineMiddleware,
  logger
}
