import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { MINUTES_IN_A_DAY } from '../constants'

class TimeRange extends Component {
  render() {
    const onClick = (event) => {
      const rect = ReactDOM.findDOMNode(this)
      const width = rect.getBoundingClientRect().width
      const x = event.pageX - rect.getBoundingClientRect().x
      const minute = (MINUTES_IN_A_DAY * x / width).toFixed()
      this.props.onClick(minute)
      console.log('x', x)
    }
    console.log('this.props.actualMinute', this.props.actualMinute)
    const style = {
      left: (this.props.left || 200) + 'px',
    }
    return (
      <div id="t-r" className="time-range" onClick={onClick}>
        <span style={style} className="time-current"></span>
      </div>
    )
  }
}

export default TimeRange
