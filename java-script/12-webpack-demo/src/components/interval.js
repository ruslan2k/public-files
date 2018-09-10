import React from 'react'
import { MINUTES_IN_A_DAY } from '../constants'

const Interval = (props) => {
  const { start, stop, parentWidth } = props
  const pixelsPerMinute = parentWidth / MINUTES_IN_A_DAY
  const startDate = new Date(start)
  const stopDate = new Date(stop)
  const startOffset = startDate.getHours() * 60 + startDate.getMinutes()
  const stopOffset = stopDate.getHours() * 60 + stopDate.getMinutes()
  const widthMinute = stopOffset - startOffset
  const width = Math.round(widthMinute * pixelsPerMinute)
  const left = Math.round(startOffset * pixelsPerMinute)
  const style = {
    position: 'absolute',
    left: `${left}px`,
    width: `${width}px`
  }
  return <span className='time-selection' style={style} />
}

export default Interval
