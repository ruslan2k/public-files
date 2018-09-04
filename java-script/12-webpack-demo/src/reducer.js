import { SET_ARCHIVES, SET_INTERVALS } from './constants'

const reducer = (state={intervals:[]}, action) => {
  switch (action.type) {
    case SET_ARCHIVES:
      return Object.assign({}, state, {archives: action.payload})
    case SET_INTERVALS:
      return Object.assign({}, state, {intervals: action.payload})
    default:
      return state
  }
}

export default reducer
